
# -*- coding: utf-8 -*-
"""
বোম্ব ও আইইডি সনাক্তকরণ সিস্টেম (BIIDS)
Bomb & IED Identification and Disposal System
Bangladesh Armed Forces
"""

import os
import json
import base64
import hashlib
import secrets
from datetime import datetime
from functools import wraps
from flask import (Flask, render_template, request, redirect, url_for,
                   session, flash, jsonify, send_from_directory)
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import anthropic
import markdown as md_lib

from translations import TRANSLATIONS, get_translation, t
from explosive_data import (get_all_explosives, get_explosive_by_id,
                             search_explosives, get_explosives_by_category,
                             find_by_image_keywords)
from bomb_ied_knowledge import get_knowledge, get_chapter

# ─── App Configuration ────────────────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

# Secret key - use env var in production for session stability
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))

# Database - use creator function to bypass URL parsing (handles special chars in password)
_db_host = os.environ.get('DB_HOST', '')
_db_user = os.environ.get('DB_USER', '')
_db_pass = os.environ.get('DB_PASS', '')

if _db_host and _db_user and _db_pass:
    import psycopg2 as _psycopg2
    def _pg_creator():
        return _psycopg2.connect(
            host=_db_host, port=5432, dbname='postgres',
            user=_db_user, password=_db_pass, sslmode='require'
        )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'creator': _pg_creator, 'pool_pre_ping': True, 'pool_recycle': 300
    }
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "biids.db")}'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_pre_ping': True, 'pool_recycle': 300}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Custom Jinja2 filters
@app.template_filter('enumerate')
def jinja_enumerate(iterable, start=0):
    return enumerate(iterable, start)

@app.template_filter('markdown')
def render_markdown(text):
    if not text:
        return ''
    return md_lib.markdown(str(text), extensions=['tables', 'fenced_code', 'nl2br'])

app.jinja_env.globals['enumerate'] = enumerate

# ─── Database Models ──────────────────────────────────────────────────────────

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    personal_number = db.Column(db.String(50), unique=True, nullable=False)
    number_type = db.Column(db.String(30), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    rank = db.Column(db.String(50), nullable=True)
    mobile = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    unit = db.Column(db.String(150), nullable=False)
    organization = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    language = db.Column(db.String(5), default='bn')
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)
    scans = db.relationship('ScanHistory', backref='user', lazy=True)


class ScanHistory(db.Model):
    __tablename__ = 'scan_history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    identified_item = db.Column(db.String(200))
    threat_level = db.Column(db.String(20))
    scan_result_json = db.Column(db.Text)
    image_filename = db.Column(db.String(200), nullable=True)
    scanned_at = db.Column(db.DateTime, default=datetime.utcnow)


# ─── Helper Functions ─────────────────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


def get_lang():
    return session.get('lang', 'bn')


def tr(key):
    lang = get_lang()
    trans = TRANSLATIONS.get(lang, TRANSLATIONS['bn'])
    return trans.get(key, key)


def get_current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None


def analyze_image_with_claude(image_data_b64, lang='bn'):
    """Use Claude Vision API to identify explosives in image"""
    try:
        api_key = os.environ.get('ANTHROPIC_API_KEY', '')
        if not api_key:
            return get_demo_result(lang)

        client = anthropic.Anthropic(api_key=api_key)

        if lang == 'bn':
            prompt = """আপনি একজন বিশেষজ্ঞ EOD (Explosive Ordnance Disposal) অফিসার।
এই ছবিটি বিশ্লেষণ করুন এবং যদি কোনো বোম্ব, আইইডি, বিস্ফোরক বা বিস্ফোরক সামগ্রী দেখতে পান, তাহলে নিচের JSON ফর্ম্যাটে উত্তর দিন:

{
    "identified": true/false,
    "item_name": "সনাক্তকৃত বস্তুর নাম",
    "category": "ied/conventional/mines/aerial/naval/cbrn/unknown",
    "threat_level": "high/medium/low/none",
    "confidence": "high/medium/low",
    "description": "বিস্তারিত বিবরণ",
    "immediate_actions": ["পদক্ষেপ ১", "পদক্ষেপ ২"],
    "disposal_steps": ["ধাপ ১", "ধাপ ২"],
    "safety_precautions": ["সতর্কতা ১", "সতর্কতা ২"],
    "technical_details": "প্রযুক্তিগত বিশ্লেষণ",
    "similar_items": ["মিলসম বস্তু ১", "মিলসম বস্তু ২"]
}

যদি কোনো বোম্ব বা বিস্ফোরক না থাকে তাহলে identified: false দিন।
শুধু JSON উত্তর দিন, অন্য কিছু নয়।"""
        else:
            prompt = """You are an expert EOD (Explosive Ordnance Disposal) officer.
Analyze this image and if you see any bomb, IED, explosive, or explosive material, respond in the following JSON format:

{
    "identified": true/false,
    "item_name": "Name of identified item",
    "category": "ied/conventional/mines/aerial/naval/cbrn/unknown",
    "threat_level": "high/medium/low/none",
    "confidence": "high/medium/low",
    "description": "Detailed description",
    "immediate_actions": ["Step 1", "Step 2"],
    "disposal_steps": ["Step 1", "Step 2"],
    "safety_precautions": ["Precaution 1", "Precaution 2"],
    "technical_details": "Technical analysis",
    "similar_items": ["Similar item 1", "Similar item 2"]
}

If there is no bomb or explosive, set identified: false.
Respond with JSON only, nothing else."""

        message = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": image_data_b64,
                            },
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ],
                }
            ],
        )

        response_text = message.content[0].text.strip()
        # Extract JSON from response
        if '```json' in response_text:
            response_text = response_text.split('```json')[1].split('```')[0]
        elif '```' in response_text:
            response_text = response_text.split('```')[1].split('```')[0]

        result = json.loads(response_text)
        return result

    except Exception as e:
        app.logger.error(f"Claude API error: {e}")
        return get_demo_result(lang)


def get_demo_result(lang='bn'):
    """Demo result when API key is not configured"""
    if lang == 'bn':
        return {
            "identified": True,
            "item_name": "সন্দেহজনক বস্তু সনাক্ত (ডেমো মোড)",
            "category": "ied",
            "threat_level": "high",
            "confidence": "medium",
            "description": "এটি একটি ডেমো ফলাফল। সম্পূর্ণ বিশ্লেষণের জন্য ANTHROPIC_API_KEY সেট করুন।\n\nছবিতে সন্দেহজনক বস্তু শনাক্ত হয়েছে।",
            "immediate_actions": [
                "১. তাৎক্ষণিকভাবে এলাকা খালি করুন",
                "২. বোম্ব স্কোয়াডকে সূচিত করুন: ০১৭৬৯-৬০০-৯৯৯",
                "৩. কমপক্ষে ৩০০ মিটার দূরে থাকুন",
                "৪. মোবাইল ফোন বন্ধ করুন",
            ],
            "disposal_steps": [
                "পদক্ষেপ ১: এলাকা পরিষ্কার করুন",
                "পদক্ষেপ ২: EOD বিশেষজ্ঞ দলের জন্য অপেক্ষা করুন",
                "পদক্ষেপ ৩: রোবোটিক্স দিয়ে পরীক্ষা করুন",
                "পদক্ষেপ ৪: বিশেষজ্ঞ দল নিষ্ক্রিয় করবে",
            ],
            "safety_precautions": [
                "কখনো নিজে নিষ্ক্রিয় করার চেষ্টা করবেন না",
                "EOD প্রোটোকল মেনে চলুন",
                "নিরাপদ দূরত্ব বজায় রাখুন",
            ],
            "technical_details": "API কী সেট না থাকায় ডেমো মোডে চলছে। পূর্ণ বিশ্লেষণের জন্য ANTHROPIC_API_KEY সেট করুন।",
            "similar_items": ["হোমমেড আইইডি", "সার্কিট বোম্ব"],
            "api_mode": "demo"
        }
    else:
        return {
            "identified": True,
            "item_name": "Suspicious Object Detected (Demo Mode)",
            "category": "ied",
            "threat_level": "high",
            "confidence": "medium",
            "description": "This is a demo result. Set ANTHROPIC_API_KEY for full analysis.\n\nSuspicious object detected in image.",
            "immediate_actions": [
                "1. Immediately evacuate the area",
                "2. Notify bomb squad: 01769-600-999",
                "3. Stay at least 300 meters away",
                "4. Turn off mobile phones",
            ],
            "disposal_steps": [
                "Step 1: Clear the area",
                "Step 2: Wait for EOD specialist team",
                "Step 3: Examine with robotics",
                "Step 4: Specialist team will neutralize",
            ],
            "safety_precautions": [
                "Never try to neutralize yourself",
                "Follow EOD protocol",
                "Maintain safe distance",
            ],
            "technical_details": "Running in demo mode because API key not set. Set ANTHROPIC_API_KEY for full analysis.",
            "similar_items": ["Homemade IED", "Circuit Bomb"],
            "api_mode": "demo"
        }


def enrich_result_with_db(result, lang='bn'):
    """Enrich AI result with database information"""
    if not result.get('identified'):
        return result
    keywords = []
    item_name = result.get('item_name', '').lower()
    keywords.extend(item_name.split())
    keywords.append(result.get('category', ''))
    db_matches = find_by_image_keywords(keywords, lang)
    if db_matches:
        db_item = db_matches[0]
        if not result.get('disposal_steps') or len(result.get('disposal_steps', [])) < 2:
            result['disposal_steps'] = db_item.get('disposal_steps', result.get('disposal_steps', []))
        if not result.get('safety_precautions'):
            result['safety_precautions'] = db_item.get('safety_precautions', [])
        result['db_match'] = {
            'id': db_item['id'],
            'name': db_item['name'],
        }
    return result


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/sw.js')
def service_worker():
    resp = send_from_directory(os.path.join(app.root_path, 'static', 'js'), 'sw.js')
    resp.headers['Content-Type'] = 'application/javascript'
    resp.headers['Service-Worker-Allowed'] = '/'
    return resp

@app.route('/manifest.json')
def manifest():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'manifest.json',
                               mimetype='application/manifest+json')

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['bn', 'en']:
        session['lang'] = lang
        if 'user_id' in session:
            user = get_current_user()
            if user:
                user.language = lang
                db.session.commit()
    return redirect(request.referrer or url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    lang = get_lang()
    if request.method == 'POST':
        personal_number = request.form.get('personal_number', '').strip().upper()
        password = request.form.get('password', '')
        user = User.query.filter_by(personal_number=personal_number).first()
        if user and user.is_active and bcrypt.check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['lang'] = user.language
            user.last_login = datetime.utcnow()
            db.session.commit()
            flash(tr('login_success'), 'success')
            return redirect(url_for('dashboard'))
        else:
            flash(tr('invalid_credentials'), 'danger')
    return render_template('login.html', lang=lang, tr=tr, TRANSLATIONS=TRANSLATIONS)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    lang = get_lang()
    if request.method == 'POST':
        personal_number = request.form.get('personal_number', '').strip().upper()
        number_type = request.form.get('number_type', '').strip()
        full_name = request.form.get('full_name', '').strip()
        rank = request.form.get('rank', '').strip()
        mobile = request.form.get('mobile', '').strip()
        email = request.form.get('email', '').strip()
        unit = request.form.get('unit', '').strip()
        organization = request.form.get('organization', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        reg_lang = request.form.get('language', 'bn')

        if not all([personal_number, number_type, full_name, mobile, unit, organization, password]):
            flash(tr('required_field'), 'danger')
            return render_template('register.html', lang=lang, tr=tr, TRANSLATIONS=TRANSLATIONS)

        if password != confirm_password:
            flash(tr('password_mismatch'), 'danger')
            return render_template('register.html', lang=lang, tr=tr, TRANSLATIONS=TRANSLATIONS)

        if User.query.filter_by(personal_number=personal_number).first():
            flash(tr('number_exists'), 'danger')
            return render_template('register.html', lang=lang, tr=tr, TRANSLATIONS=TRANSLATIONS)

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(
            personal_number=personal_number,
            number_type=number_type,
            full_name=full_name,
            rank=rank,
            mobile=mobile,
            email=email,
            unit=unit,
            organization=organization,
            password_hash=password_hash,
            language=reg_lang,
        )
        db.session.add(new_user)
        db.session.commit()
        flash(tr('account_created'), 'success')
        return redirect(url_for('login'))

    return render_template('register.html', lang=lang, tr=tr, TRANSLATIONS=TRANSLATIONS)


@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash(t('logout_success', 'bn'), 'success')
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    lang = get_lang()
    user = get_current_user()
    recent_scans = ScanHistory.query.filter_by(user_id=user.id)\
        .order_by(ScanHistory.scanned_at.desc()).limit(5).all()
    return render_template('dashboard.html', lang=lang, tr=tr, user=user,
                           recent_scans=recent_scans, TRANSLATIONS=TRANSLATIONS)


@app.route('/scanner')
@login_required
def scanner():
    lang = get_lang()
    user = get_current_user()
    return render_template('scanner.html', lang=lang, tr=tr, user=user,
                           TRANSLATIONS=TRANSLATIONS)


@app.route('/api/scan', methods=['POST'])
@login_required
def api_scan():
    lang = get_lang()
    user = get_current_user()

    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data received'}), 400

        image_data = data.get('image', '')
        if not image_data:
            return jsonify({'error': 'No image data'}), 400

        # Remove data URL prefix
        if ',' in image_data:
            image_data = image_data.split(',')[1]

        # Analyze with Claude
        result = analyze_image_with_claude(image_data, lang)
        result = enrich_result_with_db(result, lang)

        # Save to history
        if result.get('identified'):
            scan = ScanHistory(
                user_id=user.id,
                identified_item=result.get('item_name', 'Unknown'),
                threat_level=result.get('threat_level', 'unknown'),
                scan_result_json=json.dumps(result, ensure_ascii=False),
            )
            db.session.add(scan)
            db.session.commit()
            result['scan_id'] = scan.id

        return jsonify(result)

    except Exception as e:
        app.logger.error(f"Scan error: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/scan/result/<int:scan_id>')
@login_required
def scan_result(scan_id):
    lang = get_lang()
    user = get_current_user()
    scan = ScanHistory.query.get_or_404(scan_id)
    if scan.user_id != user.id:
        flash(tr('access_denied'), 'danger')
        return redirect(url_for('dashboard'))
    result = json.loads(scan.scan_result_json) if scan.scan_result_json else {}
    return render_template('scan_result.html', lang=lang, tr=tr, user=user,
                           scan=scan, result=result, TRANSLATIONS=TRANSLATIONS)


@app.route('/knowledge')
@login_required
def knowledge_base():
    lang = get_lang()
    user = get_current_user()
    category = request.args.get('category', 'all')
    query = request.args.get('q', '')

    if query:
        explosives = search_explosives(query, lang)
    elif category != 'all':
        explosives = get_explosives_by_category(category, lang)
    else:
        explosives = get_all_explosives(lang)

    # Sort by priority (Bangladesh first)
    explosives.sort(key=lambda x: (x.get('origin') != 'bangladesh', x.get('priority', 99)))

    categories = ['all', 'ied', 'conventional', 'mines', 'aerial', 'naval', 'cbrn', 'eod_equipment']
    return render_template('knowledge_base.html', lang=lang, tr=tr, user=user,
                           explosives=explosives, category=category, query=query,
                           categories=categories, TRANSLATIONS=TRANSLATIONS)


@app.route('/knowledge/<explosive_id>')
@login_required
def explosive_detail(explosive_id):
    lang = get_lang()
    user = get_current_user()
    explosive = get_explosive_by_id(explosive_id, lang)
    if not explosive:
        flash(tr('no_results'), 'warning')
        return redirect(url_for('knowledge_base'))
    return render_template('explosive_detail.html', lang=lang, tr=tr, user=user,
                           explosive=explosive, TRANSLATIONS=TRANSLATIONS)


@app.route('/bomb-ied')
@login_required
def bomb_ied_page():
    lang = get_lang()
    user = get_current_user()
    chapter_id = request.args.get('chapter', None)
    knowledge = get_knowledge(lang)
    chapters = knowledge.get('chapters', [])
    current_chapter = None
    if chapter_id:
        current_chapter = get_chapter(chapter_id, lang)
    elif chapters:
        current_chapter = chapters[0]
    return render_template('bomb_ied_page.html', lang=lang, tr=tr, user=user,
                           chapters=chapters, current_chapter=current_chapter,
                           TRANSLATIONS=TRANSLATIONS)


@app.route('/history')
@login_required
def scan_history():
    lang = get_lang()
    user = get_current_user()
    page = request.args.get('page', 1, type=int)
    scans = ScanHistory.query.filter_by(user_id=user.id)\
        .order_by(ScanHistory.scanned_at.desc())\
        .paginate(page=page, per_page=10)
    return render_template('scan_history.html', lang=lang, tr=tr, user=user,
                           scans=scans, TRANSLATIONS=TRANSLATIONS)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    lang = get_lang()
    user = get_current_user()
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'change_password':
            current_pw = request.form.get('current_password', '')
            new_pw = request.form.get('new_password', '')
            confirm_pw = request.form.get('confirm_password', '')
            if not bcrypt.check_password_hash(user.password_hash, current_pw):
                flash(tr('invalid_credentials'), 'danger')
            elif new_pw != confirm_pw:
                flash(tr('password_mismatch'), 'danger')
            else:
                user.password_hash = bcrypt.generate_password_hash(new_pw).decode('utf-8')
                db.session.commit()
                flash(tr('success'), 'success')
    return render_template('profile.html', lang=lang, tr=tr, user=user,
                           TRANSLATIONS=TRANSLATIONS)


@app.route('/emergency')
@login_required
def emergency():
    lang = get_lang()
    user = get_current_user()
    return render_template('emergency.html', lang=lang, tr=tr, user=user,
                           TRANSLATIONS=TRANSLATIONS)


# ─── Initialize Database ──────────────────────────────────────────────────────

def init_db():
    try:
        with app.app_context():
            db.create_all()
            if User.query.count() == 0:
                demo_user = User(
                    personal_number='DEMO001',
                    number_type='army_number',
                    full_name='Demo User',
                    rank='Captain',
                    mobile='01700000000',
                    email='demo@army.mil.bd',
                    unit='EOD Unit, Dhaka',
                    organization='Bangladesh Army',
                    password_hash=bcrypt.generate_password_hash('demo123').decode('utf-8'),
                    language='bn',
                )
                db.session.add(demo_user)
                db.session.commit()
                print("Demo user created: DEMO001 / demo123")
    except Exception as e:
        print(f"DB init warning: {e}")


# Always run init_db — works for both `python app.py` and gunicorn
init_db()

if __name__ == '__main__':
    print("=" * 60)
    print("বোম্ব ও আইইডি সনাক্তকরণ সিস্টেম চালু হচ্ছে...")
    print("Bomb & IED Identification System Starting...")
    print("=" * 60)
    print(f"URL: http://localhost:5000")
    print(f"Demo Login: DEMO001 / demo123")
    print(f"API Key: {'Set ✓' if os.environ.get('ANTHROPIC_API_KEY') else 'Not Set (Demo Mode)'}")
    print("=" * 60)
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
