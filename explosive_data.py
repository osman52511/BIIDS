
# -*- coding: utf-8 -*-
"""
Comprehensive Explosives & IED Database
Source: Bangladesh Army BIDC Book 2023 + IED & CBRN Book + International References
"""

EXPLOSIVES_DATABASE = {
    'bn': [
        # ===== বাংলাদেশ প্রসঙ্গ - BANGLADESH SPECIFIC IEDs =====
        {
            'id': 'bd_ied_001',
            'name': 'সাধারণ আইইডি (হোমমেড)',
            'english_name': 'Homemade IED - Bangladesh Type',
            'category': 'ied',
            'origin': 'bangladesh',
            'priority': 1,
            'threat_level': 'high',
            'description': 'বাংলাদেশে সন্ত্রাসীদের দ্বারা সাধারণত ব্যবহৃত ঘরে তৈরি বিস্ফোরক ডিভাইস। সহজলভ্য উপাদান ব্যবহার করে তৈরি করা হয়।',
            'components': ['মূল চার্জ (বিস্ফোরক)', 'ডেটোনেটর', 'ফায়ারিং সুইচ', 'ব্যাটারি/পাওয়ার সোর্স', 'কন্টেইনার'],
            'types': ['টাইমড আইইডি', 'কমান্ড আইইডি', 'ভিকটিম অপারেটেড', 'রেডিও কন্ট্রোলড'],
            'indicators': ['অস্বাভাবিক তার বা ক্যাবেল', 'অপরিচিত প্যাকেজ বা পার্সেল', 'অস্বাভাবিক গন্ধ', 'খোলা তার'],
            'immediate_actions': [
                '১. নিজে ও অন্যদের তাৎক্ষণিকভাবে নিরাপদ দূরত্বে সরিয়ে নিন (কমপক্ষে ৩০০ মিটার)',
                '২. অবিলম্বে কর্তৃপক্ষকে সূচিত করুন (বোম্ব স্কোয়াড: ০১৭৬৯-৬০০-৯৯৯)',
                '৩. এলাকা সিল করুন এবং সাধারণ জনগণকে দূরে রাখুন',
                '৪. ডিভাইসে কোনো কিছু স্পর্শ করবেন না',
                '৫. মোবাইল ফোন বন্ধ রাখুন (RCIED সক্রিয় হতে পারে)',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: এলাকা পরিষ্কার করুন - সকল অসামরিক ব্যক্তিকে ৩০০মি+ দূরে সরান',
                'পদক্ষেপ ২: বিশেষজ্ঞ দলের জন্য অপেক্ষা করুন - নিজে নিষ্ক্রিয় করার চেষ্টা করবেন না',
                'পদক্ষেপ ৩: EOD দলকে নিরাপদ প্রবেশ পথ নিশ্চিত করুন',
                'পদক্ষেপ ৪: ডকুমেন্টেশন - ছবি তুলুন (নিরাপদ দূরত্ব থেকে)',
                'পদক্ষেপ ৫: EOD টিম ডিসরাপ্টার/রোবট ব্যবহার করে নিষ্ক্রিয় করবে',
            ],
            'safety_precautions': [
                'কখনো একা কাজ করবেন না',
                'প্রাইমারি ও সেকেন্ডারি ডিভাইসের সম্ভাবনা বিবেচনা করুন',
                'ইলেকট্রনিক জ্যামার ব্যবহার করুন (যদি উপলব্ধ)',
                'সর্বদা EOD প্রোটোকল মেনে চলুন',
            ],
            'image_keywords': ['wire', 'battery', 'package', 'ied', 'bomb', 'device', 'explosive'],
        },
        {
            'id': 'bd_ied_002',
            'name': 'ভিবিআইইডি (গাড়ি বোম্ব)',
            'english_name': 'VBIED - Vehicle Borne IED',
            'category': 'ied',
            'origin': 'bangladesh',
            'priority': 1,
            'threat_level': 'high',
            'description': 'যানবাহনে স্থাপিত আইইডি। বাংলাদেশে বিভিন্ন সন্ত্রাসী হামলায় ব্যবহৃত হয়েছে। অত্যন্ত উচ্চ বিপদজনক।',
            'components': ['বড় মূল চার্জ (সাধারণত ৫-৫০ কেজি)', 'ডেটোনেটিং সিস্টেম', 'শ্রাপনেল উপাদান', 'ট্রিগার মেকানিজম'],
            'types': ['SVBIED (সুইসাইড)', 'RVBIED (রিমোট)', 'টাইমড VBIED'],
            'indicators': ['সন্দেহজনক পার্কিং', 'অস্বাভাবিক ভারী যানবাহন', 'অপরিচিত চালক', 'ঝুলন্ত তার'],
            'immediate_actions': [
                '১. তাৎক্ষণিকভাবে ৫০০ মিটার দূরে যান',
                '২. নিকটবর্তী ভবন থেকে দূরে থাকুন (ধ্বংসাবশেষ থেকে সুরক্ষা)',
                '৩. বোম্ব স্কোয়াড ও পুলিশকে অবহিত করুন',
                '৪. ট্রাফিক এবং জনগণকে এলাকা থেকে সরান',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: ৫০০মি+ কর্ডন স্থাপন করুন',
                'পদক্ষেপ ২: রোবোটিক্স ব্যবহার করে গাড়ি পরীক্ষা করুন',
                'পদক্ষেপ ৩: X-ray স্ক্যানিং সম্পন্ন করুন',
                'পদক্ষেপ ৪: নিয়ন্ত্রিত বিস্ফোরণ বা EOD টিম দ্বারা নিষ্ক্রিয়করণ',
            ],
            'safety_precautions': [
                'কখনো যানবাহনের কাছে যাবেন না',
                'রেডিও ব্যবহারে সতর্ক থাকুন',
                'সকল যোগাযোগ সতর্কতার সাথে করুন',
            ],
            'image_keywords': ['car', 'vehicle', 'truck', 'van', 'bomb', 'vbied'],
        },
        {
            'id': 'bd_ied_003',
            'name': 'পার্সেল/লেটার বোম্ব',
            'english_name': 'Parcel/Letter Bomb',
            'category': 'ied',
            'origin': 'bangladesh',
            'priority': 1,
            'threat_level': 'high',
            'description': 'চিঠি বা পার্সেলে লুকানো বিস্ফোরক ডিভাইস। বাংলাদেশে রাজনৈতিক হত্যাকাণ্ডে ব্যবহৃত হয়েছে।',
            'components': ['ছোট মূল চার্জ', 'ডেটোনেটর', 'স্প্রিং/প্রেশার ট্রিগার', 'কাগজ/প্যাকেজিং'],
            'types': ['প্রেশার প্লেট', 'পুল সুইচ', 'টিল্ট সুইচ'],
            'indicators': ['অস্বাভাবিক ওজন', 'তৈলাক্ত দাগ', 'অস্বাভাবিক গন্ধ', 'অপরিচিত প্রেরক', 'অতিরিক্ত টেপ'],
            'immediate_actions': [
                '১. খোলার চেষ্টা করবেন না',
                '২. নিরাপদ স্থানে রাখুন',
                '৩. ঘর থেকে সকলকে বের করুন',
                '৪. পুলিশ ও বোম্ব স্কোয়াডকে অবহিত করুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: স্পর্শ না করে নিরাপদ স্থানে রেখে দিন',
                'পদক্ষেপ ২: EOD টিম আসা পর্যন্ত অপেক্ষা করুন',
                'পদক্ষেপ ৩: X-ray বা স্ক্যানিং মেশিন দিয়ে পরীক্ষা',
                'পদক্ষেপ ৪: বিশেষজ্ঞ দ্বারা নিষ্ক্রিয়করণ',
            ],
            'safety_precautions': ['কখনো নিজে খোলার চেষ্টা করবেন না', 'তাপমাত্রা পরিবর্তন এড়িয়ে চলুন'],
            'image_keywords': ['package', 'letter', 'parcel', 'envelope', 'box'],
        },

        # ===== উচ্চ বিস্ফোরক (HIGH EXPLOSIVES) =====
        {
            'id': 'he_001',
            'name': 'টিএনটি (ট্রাইনাইট্রোটলুইন)',
            'english_name': 'TNT - Trinitrotoluene',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'সবচেয়ে পরিচিত সামরিক বিস্ফোরক। হলুদ বা বাদামী রঙের কঠিন পদার্থ। বিস্ফোরণ শক্তির পরিমাপের মানদণ্ড হিসেবে ব্যবহৃত হয়।',
            'physical_properties': {
                'রং': 'হলুদ/বাদামী',
                'অবস্থা': 'কঠিন',
                'গলনাঙ্ক': '৮০.৯° সেলসিয়াস',
                'ঘনত্ব': '১.৬৫ গ্রাম/সিসি',
                'বিস্ফোরণ গতি': '৬,৯০০ মি/সেকেন্ড',
            },
            'components': ['C₇H₅N₃O₆'],
            'uses': ['সামরিক চার্জ', 'খনিতে ব্যবহার', 'নির্মাণ কাজে'],
            'immediate_actions': [
                '১. এলাকা খালি করুন (৩০০ মিটার)',
                '২. EOD টিমকে ডাকুন',
                '৩. কোনো তাপ বা ঘর্ষণ এড়িয়ে চলুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: নিরাপদ কর্ডন স্থাপন',
                'পদক্ষেপ ২: অগ্নিনির্বাপক প্রস্তুত রাখুন',
                'পদক্ষেপ ৩: নিয়ন্ত্রিত বিস্ফোরণ বা পানিতে নিষ্ক্রিয়করণ',
                'পদক্ষেপ ৪: EOD বিশেষজ্ঞ দ্বারা অপসারণ',
            ],
            'safety_precautions': ['তাপ থেকে দূরে রাখুন', 'ঘর্ষণ এড়িয়ে চলুন', 'প্রত্যক্ষ আঘাত এড়িয়ে চলুন'],
            'image_keywords': ['tnt', 'yellow', 'block', 'explosive', 'military charge'],
        },
        {
            'id': 'he_002',
            'name': 'পিই (প্লাস্টিক বিস্ফোরক) ৮০৮, ৮৫১, ৮৫২',
            'english_name': 'PE (Plastic Explosive) - 808, 851, 852',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'প্লাস্টিক বিস্ফোরক - হাতে আকৃতি দেওয়া যায়। বাংলাদেশ সেনাবাহিনীতে ব্যাপকভাবে ব্যবহৃত। ডেমোলিশন কাজে আদর্শ।',
            'physical_properties': {
                'রং': 'সাদা/ক্রিম/বাদামী',
                'অবস্থা': 'নরম কঠিন (প্লাস্টিক)',
                'বিশেষত্ব': 'হাতে যেকোনো আকৃতি দেওয়া যায়',
            },
            'components': ['RDX/PETN', 'প্লাস্টিফায়ার'],
            'immediate_actions': [
                '১. স্পর্শ করবেন না',
                '২. তাপ বা আঘাত থেকে দূরে রাখুন',
                '৩. EOD কর্তৃপক্ষকে জানান',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: নিরাপদ দূরত্বে থাকুন',
                'পদক্ষেপ ২: EOD টিম বিশেষ সরঞ্জাম ব্যবহার করে অপসারণ করবে',
                'পদক্ষেপ ৩: নিয়ন্ত্রিত বিস্ফোরণ বা ডেটোনেশন',
            ],
            'safety_precautions': ['আগুনের কাছে নিয়ে যাবেন না', 'তীক্ষ্ণ বস্তু দিয়ে খোঁচা দেবেন না'],
            'image_keywords': ['plastic explosive', 'pe4', 'c4', 'semtex', 'white putty'],
        },
        {
            'id': 'he_003',
            'name': 'হেক্সোজেন (RDX)',
            'english_name': 'Hexogen / RDX',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'সামরিক বাহিনীতে সর্বাধিক ব্যবহৃত শক্তিশালী বিস্ফোরক। TNT এর চেয়ে ১.৫ গুণ বেশি শক্তিশালী।',
            'physical_properties': {
                'রং': 'সাদা',
                'অবস্থা': 'কঠিন পাউডার',
                'বিস্ফোরণ গতি': '৮,৭৫০ মি/সেকেন্ড',
                'রাসায়নিক সূত্র': 'C₃H₆N₆O₆',
            },
            'immediate_actions': [
                '১. তাৎক্ষণিকভাবে এলাকা খালি করুন',
                '২. EOD টিমকে সূচিত করুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: বিশেষজ্ঞ EOD টিম আনুন',
                'পদক্ষেপ ২: নিয়ন্ত্রিত বিস্ফোরণ',
            ],
            'safety_precautions': ['অত্যন্ত সংবেদনশীল - সামান্য আঘাতে বিস্ফোরিত হতে পারে'],
            'image_keywords': ['rdx', 'hexogen', 'white powder', 'military explosive'],
        },
        {
            'id': 'he_004',
            'name': 'নাইট্রোগ্লিসারিন',
            'english_name': 'Nitroglycerin',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'তরল বিস্ফোরক। অত্যন্ত সংবেদনশীল - সামান্য কম্পনে বিস্ফোরিত হতে পারে। ডিনামাইট তৈরিতে ব্যবহৃত।',
            'physical_properties': {
                'রং': 'বর্ণহীন/হালকা হলুদ',
                'অবস্থা': 'তরল',
                'বিপদ': 'অত্যন্ত সংবেদনশীল',
            },
            'immediate_actions': [
                '১. কোনো কম্পন বা আঘাত দেবেন না',
                '২. তাৎক্ষণিকভাবে সরে যান',
                '৩. EOD টিমকে ডাকুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: সর্বোচ্চ সতর্কতার সাথে পরিচালনা করুন',
                'পদক্ষেপ ২: বিশেষজ্ঞ টিম নিউট্রালাইজিং রাসায়নিক ব্যবহার করবে',
            ],
            'safety_precautions': ['কখনো নাড়াবেন না', 'তাপ থেকে দূরে রাখুন', 'বিশেষজ্ঞ ছাড়া স্পর্শ করবেন না'],
            'image_keywords': ['liquid explosive', 'nitroglycerin', 'clear liquid'],
        },
        {
            'id': 'he_005',
            'name': 'ANFO (অ্যামোনিয়াম নাইট্রেট/ফুয়েল অয়েল)',
            'english_name': 'ANFO - Ammonium Nitrate Fuel Oil',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'সবচেয়ে সস্তা ও সহজলভ্য বিস্ফোরক মিশ্রণ। সার থেকে তৈরি করা যায়। ১৯৯৫ ওকলাহোমা সিটি বোম্বিং এ ব্যবহৃত।',
            'components': ['অ্যামোনিয়াম নাইট্রেট (৯৪%)', 'ডিজেল তেল (৬%)'],
            'immediate_actions': [
                '১. এলাকা খালি করুন',
                '২. অগ্নিনির্বাপক টিম প্রস্তুত রাখুন',
                '৩. EOD কর্তৃপক্ষকে সূচিত করুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: পানি দিয়ে ভিজিয়ে নিষ্ক্রিয় করুন',
                'পদক্ষেপ ২: বিশেষজ্ঞ দল দ্বারা অপসারণ',
            ],
            'safety_precautions': ['আগুন থেকে দূরে রাখুন', 'আর্দ্র পরিবেশ এড়িয়ে চলুন'],
            'image_keywords': ['anfo', 'fertilizer bomb', 'white granules', 'ammonium nitrate'],
        },

        # ===== ডেটোনেটর ও ফিউজ =====
        {
            'id': 'det_001',
            'name': 'ডেটোনেটর নং ৬, ৮, ২৭',
            'english_name': 'Detonator No. 6, 8, 27',
            'category': 'detonator',
            'origin': 'bangladesh',
            'priority': 1,
            'threat_level': 'high',
            'description': 'বাংলাদেশ সেনাবাহিনীতে ব্যবহৃত ইলেকট্রিক ও নন-ইলেকট্রিক ডেটোনেটর। ডেমোলিশন ও মাইন ক্লিয়ারেন্সে ব্যবহৃত।',
            'types': ['ইলেকট্রিক ডেটোনেটর', 'নন-ইলেকট্রিক ডেটোনেটর', 'ডিলে ডেটোনেটর'],
            'immediate_actions': [
                '১. স্পর্শ করবেন না',
                '২. তাপ বা বিদ্যুৎ থেকে দূরে রাখুন',
                '৩. EOD টিমকে সূচিত করুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: সাবধানে শনাক্ত করুন',
                'পদক্ষেপ ২: বিশেষজ্ঞ দ্বারা অপসারণ',
                'পদক্ষেপ ৩: নিয়ন্ত্রিত বিস্ফোরণ',
            ],
            'safety_precautions': ['কখনো হাতুড়ি দিয়ে আঘাত করবেন না', 'বৈদ্যুতিক ক্ষেত্র থেকে দূরে রাখুন'],
            'image_keywords': ['detonator', 'blasting cap', 'electric detonator'],
        },

        # ===== মাইন (MINES) =====
        {
            'id': 'mine_001',
            'name': 'এন্টি-পার্সোনেল মাইন',
            'english_name': 'Anti-Personnel Mine',
            'category': 'mines',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'high',
            'description': 'মানুষকে আঘাত করার জন্য ডিজাইন করা ভূমি মাইন। মাটিতে বা মাটির কাছে স্থাপিত। পদচাপে বিস্ফোরিত হয়।',
            'types': ['ব্লাস্ট মাইন', 'ফ্র্যাগমেন্টেশন মাইন', 'বাউন্ডিং মাইন'],
            'examples': ['PMN-2', 'TM-62', 'M14', 'VS-50'],
            'indicators': ['অস্বাভাবিকভাবে মসৃণ মাটি', 'তারের চিহ্ন', 'বিঘ্নিত মাটি'],
            'immediate_actions': [
                '১. থামুন এবং নড়াচড়া করবেন না',
                '২. আস্তে আস্তে পিছনে সরে যান (আসার পথে)',
                '৩. অন্যদের সতর্ক করুন',
                '৪. মাইন ক্লিয়ারেন্স বিশেষজ্ঞ ডাকুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: এলাকা চিহ্নিত ও বন্ধ করুন',
                'পদক্ষেপ ২: EOD বা মাইন ক্লিয়ারেন্স টিম আনুন',
                'পদক্ষেপ ৩: প্রড ও মেটাল ডিটেক্টর দিয়ে সার্ভে',
                'পদক্ষেপ ৪: নিয়ন্ত্রিত বিস্ফোরণ বা নিউট্রালাইজেশন',
            ],
            'safety_precautions': ['কখনো একা মাইনফিল্ডে প্রবেশ করবেন না', 'প্রশিক্ষিত EOD ছাড়া মাইন অপসারণ করবেন না'],
            'image_keywords': ['landmine', 'mine', 'anti-personnel', 'ground mine'],
        },
        {
            'id': 'mine_002',
            'name': 'সামুদ্রিক মাইন',
            'english_name': 'Sea Mine / Naval Mine',
            'category': 'naval',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'সমুদ্রে বা নদীতে স্থাপিত বিস্ফোরক ডিভাইস। জাহাজ ও নৌকাকে ধ্বংস করতে ব্যবহৃত।',
            'types': ['মুড়িং মাইন', 'বটম মাইন', 'ড্রিফটিং মাইন', 'লিমপেট মাইন'],
            'immediate_actions': [
                '১. নৌযান থামান এবং সরিয়ে নিন',
                '২. নৌবাহিনীর EOD টিমকে সূচিত করুন',
                '৩. এলাকা চিহ্নিত করুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: নৌবাহিনী EOD ডাইভার টিম পাঠান',
                'পদক্ষেপ ২: MCM (Mine Counter Measure) অপারেশন পরিচালনা',
                'পদক্ষেপ ৩: নিয়ন্ত্রিত বিস্ফোরণ',
            ],
            'safety_precautions': ['সকল নৌযান দূরে রাখুন', 'শুধুমাত্র প্রশিক্ষিত ডাইভার'],
            'image_keywords': ['sea mine', 'naval mine', 'water mine', 'floating mine'],
        },

        # ===== বিমান বোম্ব =====
        {
            'id': 'aerial_001',
            'name': 'বিমান বোম্ব (জেনারেল পারপাস)',
            'english_name': 'Aircraft Bomb - General Purpose',
            'category': 'aerial',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'বিমান থেকে নিক্ষিপ্ত সাধারণ উদ্দেশ্যের বোম্ব। বিভিন্ন ওজনে পাওয়া যায় - ২৫০ লব্স থেকে ২০০০ লব্স।',
            'types': ['GP Bomb', 'SAP Bomb', 'AP Bomb', 'Incendiary Bomb'],
            'components': ['মূল বিস্ফোরক চার্জ', 'নোজ ফিউজ', 'টেইল ফিউজ', 'ফিন অ্যাসেম্বলি'],
            'immediate_actions': [
                '১. অবিলম্বে ১০০০ মিটার দূরে সরে যান',
                '২. সামরিক কর্তৃপক্ষকে সূচিত করুন',
                '৩. স্থান চিহ্নিত করুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: বিশাল কর্ডন স্থাপন করুন',
                'পদক্ষেপ ২: সামরিক EOD বিশেষজ্ঞ ডাকুন',
                'পদক্ষেপ ৩: রোবোটিক্স দিয়ে পরীক্ষা',
                'পদক্ষেপ ৪: নিয়ন্ত্রিত বিস্ফোরণ বা ফিউজ নিউট্রালাইজেশন',
            ],
            'safety_precautions': ['কখনো ফিউজ স্পর্শ করবেন না', 'বিমান বোম্বে UXO ট্যাগ লাগান'],
            'image_keywords': ['aerial bomb', 'aircraft bomb', 'drop bomb', 'fin bomb'],
        },

        # ===== CBRN =====
        {
            'id': 'cbrn_001',
            'name': 'রাসায়নিক অস্ত্র/বিস্ফোরক',
            'english_name': 'Chemical Weapon/Explosive',
            'category': 'cbrn',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'high',
            'description': 'রাসায়নিক পদার্থ দিয়ে তৈরি অস্ত্র। নার্ভ এজেন্ট, ব্লিস্টারিং এজেন্ট, চকিং এজেন্ট ইত্যাদি থাকতে পারে।',
            'types': ['নার্ভ এজেন্ট (সারিন, ভিএক্স)', 'ব্লিস্টার এজেন্ট (মাস্টার্ড গ্যাস)', 'চকিং এজেন্ট (ক্লোরিন)', 'রক্ত এজেন্ট (সায়ানাইড)'],
            'indicators': ['অপ্রত্যাশিত গন্ধ', 'মানুষ বা প্রাণীর হঠাৎ অসুস্থতা', 'অস্বাভাবিক মৃত্যু', 'তরল বা বাষ্প নির্গমন'],
            'immediate_actions': [
                '১. তাৎক্ষণিকভাবে বাতাসের উলটো দিকে সরে যান',
                '২. MOPP গিয়ার পরুন (যদি থাকে)',
                '৩. CBRN প্রতিক্রিয়া দল ডাকুন',
                '৪. আক্রান্তদের ডিকন্টামিনেট করুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: নিরাপদ পরিধি স্থাপন করুন',
                'পদক্ষেপ ২: CBRN বিশেষজ্ঞ দল আনুন',
                'পদক্ষেপ ৩: ডিকন্টামিনেশন অপারেশন',
                'পদক্ষেপ ৪: বিশেষ পদ্ধতিতে নিউট্রালাইজেশন',
            ],
            'safety_precautions': ['CBRN গিয়ার ছাড়া প্রবেশ নিষেধ', 'আক্রান্তদের স্পর্শ করার আগে নিজেকে সুরক্ষিত করুন'],
            'image_keywords': ['chemical weapon', 'gas canister', 'cbrn', 'yellow cross', 'nerve agent'],
        },
        {
            'id': 'cbrn_002',
            'name': 'পারমাণবিক/রেডিওলজিক্যাল ডিভাইস',
            'english_name': 'Nuclear/Radiological Device (Dirty Bomb)',
            'category': 'cbrn',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'high',
            'description': '"ডার্টি বোম্ব" - রেডিওঅ্যাকটিভ উপাদান ছড়িয়ে দেওয়ার জন্য প্রচলিত বিস্ফোরক ব্যবহার করে। সরাসরি পারমাণবিক নয়।',
            'indicators': ['গিগার কাউন্টারে উচ্চ রিডিং', 'অস্বাভাবিক রোগের লক্ষণ', 'সন্দেহজনক ধাতব কন্টেইনার'],
            'immediate_actions': [
                '১. তাৎক্ষণিকভাবে ৩০০+ মিটার দূরে যান',
                '২. বায়ু সংস্পর্শ এড়িয়ে চলুন',
                '৩. সামরিক CBRN টিম ডাকুন',
                '৪. আক্রান্তদের চিকিৎসা দিন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: রেডিওলজিক্যাল কর্ডন স্থাপন',
                'পদক্ষেপ ২: CBRN বিশেষজ্ঞ ও পারমাণবিক বিশেষজ্ঞ ডাকুন',
                'পদক্ষেপ ৩: রেডিওলজিক্যাল সার্ভে',
                'পদক্ষেপ ৪: বিশেষ পদ্ধতিতে নিষ্ক্রিয়করণ',
            ],
            'safety_precautions': ['শুধুমাত্র CBRN-প্রশিক্ষিত কর্মী', 'রেডিওলজিক্যাল মনিটরিং করুন'],
            'image_keywords': ['dirty bomb', 'radiation', 'nuclear device', 'radiological', 'geiger'],
        },

        # ===== সুইচ ও সার্কিট =====
        {
            'id': 'switch_001',
            'name': 'রেডিও কন্ট্রোলড আইইডি (RCIED)',
            'english_name': 'Radio Controlled IED - RCIED',
            'category': 'ied',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'high',
            'description': 'রেডিও সংকেত দিয়ে দূর থেকে নিয়ন্ত্রিত আইইডি। মোবাইল ফোন, রিমোট কন্ট্রোল, ওয়াকিটকি দিয়ে সক্রিয় করা যায়।',
            'components': ['রিসিভার', 'ট্রান্সমিটার', 'ফায়ারিং সার্কিট', 'মূল চার্জ', 'ব্যাটারি'],
            'indicators': ['অ্যান্টেনা দৃশ্যমান', 'রেডিও ডিভাইস', 'অস্বাভাবিক ইলেকট্রনিক উপাদান'],
            'immediate_actions': [
                '১. সকল মোবাইল ও রেডিও যন্ত্রপাতি বন্ধ করুন',
                '২. এলাকা থেকে সরে যান',
                '৩. ইলেকট্রনিক জ্যামার ব্যবহার করুন',
                '৪. EOD টিমকে সূচিত করুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: ইলেকট্রনিক জ্যামিং শুরু করুন',
                'পদক্ষেপ ২: EOD টিম রোবোটিক্স পাঠাবে',
                'পদক্ষেপ ৩: ডিসরাপ্টার দিয়ে পাওয়ার সাপ্লাই কাট',
                'পদক্ষেপ ৪: বিশেষজ্ঞ দ্বারা পূর্ণ নিষ্ক্রিয়করণ',
            ],
            'safety_precautions': ['মোবাইল ব্যবহার করবেন না', 'রেডিও ট্রান্সমিশন বন্ধ করুন'],
            'image_keywords': ['rcied', 'radio controlled', 'remote controlled bomb', 'mobile phone ied'],
        },
        {
            'id': 'switch_002',
            'name': 'সুইসাইড বোম্ব/পিবিআইইডি',
            'english_name': 'Suicide Bomb / PBIED - Person Borne IED',
            'category': 'ied',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'high',
            'description': 'ব্যক্তি কর্তৃক বহন করা আইইডি। ভেস্ট বা বেল্টে পরিধান করা হয়। সবচেয়ে বিপজ্জনক ধরন।',
            'indicators': ['অস্বাভাবিক মোটা বা ভারী পোশাক', 'ঘামাচ্ছে কিন্তু ঠান্ডা আবহাওয়া', 'অস্বাভাবিক হাঁটাচলা', 'হাত পকেটে রাখছে', 'অস্বাভাবিক উত্তেজনা'],
            'immediate_actions': [
                '১. তাৎক্ষণিকভাবে এলাকা খালি করুন',
                '২. ব্যক্তির সাথে সরাসরি কথা বলুন বা বাধা দিন',
                '৩. নিরাপত্তা বাহিনীকে সতর্ক করুন',
                '৪. নিজেকে ঢেকে রাখুন',
            ],
            'disposal_steps': [
                'পদক্ষেপ ১: আলোচনা বা বাধা প্রদানের মাধ্যমে বিলম্ব করুন',
                'পদক্ষেপ ২: EOD নেগোশিয়েটর আনুন',
                'পদক্ষেপ ৩: সুরক্ষিত স্থান থেকে EOD অপারেশন',
            ],
            'safety_precautions': ['কখনো একা মোকাবেলা করবেন না', 'ব্যক্তি থেকে দূরত্ব বজায় রাখুন'],
            'image_keywords': ['suicide bomber', 'vest bomb', 'pbied', 'body worn', 'explosive vest'],
        },

        # ===== EOD সরঞ্জাম (EOD EQUIPMENT) =====
        {
            'id': 'eod_001',
            'name': 'ইওডি সুরক্ষা পোশাক (বোম্ব স্যুট)',
            'english_name': 'EOD Protective Suit (Bomb Suit)',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'বিস্ফোরক নিষ্ক্রিয়করণে ব্যবহৃত বিশেষ সুরক্ষা পোশাক। ব্লাস্ট প্রেশার, ফ্র্যাগমেন্টেশন ও তাপ থেকে সুরক্ষা দেয়। ওজন প্রায় ৩৫-৮০ কেজি।',
            'components': ['ব্লাস্ট-প্রতিরোধী জ্যাকেট', 'সুরক্ষা হেলমেট ও ভাইজার', 'গ্লাভস', 'ট্রাউজার্স', 'বুট', 'কুলিং ভেস্ট'],
            'types': ['হেভি EOD স্যুট (Mk5/Mk6)', 'লাইটওয়েট সার্চ স্যুট', 'CBRN স্যুট'],
            'image_keywords': ['eod suit', 'bomb suit', 'protective suit', 'disposal suit'],
        },
        {
            'id': 'eod_002',
            'name': 'ইওডি রোবট',
            'english_name': 'EOD Robot / Remote Controlled Vehicle',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'দূর থেকে নিয়ন্ত্রিত রোবট যা IED পরীক্ষা ও নিষ্ক্রিয়করণে ব্যবহৃত হয়। অপারেটরকে সরাসরি বিপদ থেকে রক্ষা করে। ক্যামেরা, রোবোটিক আর্ম এবং ডিসরাপ্টার মাউন্ট থাকে।',
            'components': ['রোবোটিক আর্ম (মাল্টি-জয়েন্ট)', 'HD ক্যামেরা সিস্টেম (ফ্রন্ট/রিয়ার)', 'রিমোট কন্ট্রোল কনসোল', 'ডিসরাপ্টার মাউন্ট', 'ট্র্যাক/হুইল ড্রাইভ', 'লাইটিং সিস্টেম'],
            'types': ['iRobot PackBot 510', 'QinetiQ Talon', 'Dragon Runner', 'Telemax Pro'],
            'image_keywords': ['eod robot', 'bomb robot', 'remote vehicle', 'disposal robot', 'packbot'],
        },
        {
            'id': 'eod_003',
            'name': 'ডিসরাপ্টার (PAN Disruptor)',
            'english_name': 'Disruptor / PAN Disruptor Mk5',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'উচ্চ-চাপের পানি বা প্রজেক্টাইল দিয়ে IED-এর সার্কিট বা পাওয়ার সাপ্লাই বিচ্ছিন্ন করে। নিরাপদ ও কার্যকর নিষ্ক্রিয়করণ পদ্ধতি। সাধারণত রোবটে মাউন্ট করা হয়।',
            'components': ['হাই-প্রেশার ওয়াটার/স্লাগ গান', 'ফায়ারিং মেকানিজম', 'মাউন্টিং ব্র্যাকেট', 'রিমোট ফায়ারিং কেবল', 'প্রজেক্টাইল চার্জ'],
            'types': ['PAN Disruptor Mk5', 'Piglet', 'REMO Disruptor', 'Water Disruptor'],
            'image_keywords': ['disruptor', 'pan disruptor', 'water disruptor', 'eod tool', 'mk5'],
        },
        {
            'id': 'eod_004',
            'name': 'মেটাল ডিটেক্টর ও সার্চ কিট',
            'english_name': 'Metal Detector & Mine Search Kit',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'মাটিতে বা বস্তুর ভেতরে ধাতব বস্তু শনাক্তকরণে ব্যবহৃত। মাইন ও IED সার্চে অপরিহার্য সরঞ্জাম। বাংলাদেশ সেনাবাহিনীতে ব্যাপকভাবে ব্যবহৃত।',
            'components': ['মেটাল ডিটেক্টর হেড', 'কন্ট্রোল বক্স', 'প্রড (তদন্ত কাঠি)', 'হেডফোন', 'মার্কিং পেগ ও টেপ'],
            'types': ['Vallon VMH3CS', 'CEIA CMD', 'Minelab F3', 'Ebinger UPEX 740'],
            'image_keywords': ['metal detector', 'mine detector', 'search kit', 'eod search', 'vallon'],
        },
        {
            'id': 'eod_005',
            'name': 'হুক ও লাইন কিট',
            'english_name': 'Hook & Line Kit (Manual Disruptor)',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'নিরাপদ দূরত্ব থেকে সন্দেহজনক বস্তু সরানো বা টেনে আনার জন্য ব্যবহৃত হয়। প্রথম পর্যায়ের EOD কার্যক্রমে সবচেয়ে মৌলিক সরঞ্জাম।',
            'components': ['স্টিল গ্র্যাপনেল হুক', 'নাইলন রোপ (১০০ মিটার+)', 'পুলি সিস্টেম', 'কার্বাইনার ক্লিপ', 'স্টোরেজ ব্যাগ'],
            'types': ['সিঙ্গেল হুক ও লাইন', 'ট্রিপল হুক', 'গ্র্যাপনেল হুক', 'টেলিস্কোপিক হুক'],
            'image_keywords': ['hook and line', 'rope kit', 'eod hook', 'drag kit', 'grapnel'],
        },
        {
            'id': 'eod_006',
            'name': 'পোর্টেবল X-রে স্ক্যানিং সিস্টেম',
            'english_name': 'Portable X-Ray Scanning System',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'পোর্টেবল X-রে সিস্টেম যা IED, পার্সেল বোম্ব বা সন্দেহজনক বস্তুর ভেতরের কাঠামো পরীক্ষায় ব্যবহৃত হয়। বিস্ফোরণ ছাড়াই আভ্যন্তরীণ কাঠামো দেখা সম্ভব।',
            'components': ['X-রে জেনারেটর হেড', 'ডিজিটাল ডিটেক্টর প্যানেল', 'ল্যাপটপ/ট্যাবলেট ভিউয়ার', 'রিমোট ফায়ারিং কেবল', 'কোলিমেটর'],
            'types': ['Scanna SC12C', 'Golden Engineering XRIS50', 'Vidisco Fox-RAPISCAN', 'Logos Imaging'],
            'image_keywords': ['xray', 'x-ray scanner', 'portable xray', 'eod xray', 'scanna'],
        },
    ],

    'en': [
        # ===== BANGLADESH SPECIFIC IEDs =====
        {
            'id': 'bd_ied_001',
            'name': 'Homemade IED (Bangladesh Type)',
            'bengali_name': 'সাধারণ আইইডি (হোমমেড)',
            'category': 'ied',
            'origin': 'bangladesh',
            'priority': 1,
            'threat_level': 'high',
            'description': 'Improvised explosive device commonly used by terrorists in Bangladesh. Made using easily available materials from local markets.',
            'components': ['Main Charge (Explosive)', 'Detonator', 'Firing Switch', 'Battery/Power Source', 'Container'],
            'types': ['Timed IED', 'Command IED', 'Victim Operated', 'Radio Controlled'],
            'indicators': ['Unusual wires or cables', 'Unknown packages or parcels', 'Unusual smell', 'Exposed wiring'],
            'immediate_actions': [
                '1. Immediately evacuate yourself and others to safe distance (minimum 300 meters)',
                '2. Immediately notify authorities (Bomb Squad: 01769-600-999)',
                '3. Seal the area and keep civilians away',
                '4. Do not touch anything on the device',
                '5. Turn off mobile phones (RCIED may be active)',
            ],
            'disposal_steps': [
                'Step 1: Clear the area - move all civilians 300m+ away',
                'Step 2: Wait for specialist team - do not attempt to neutralize yourself',
                'Step 3: Ensure safe approach route for EOD team',
                'Step 4: Documentation - photograph (from safe distance)',
                'Step 5: EOD team will neutralize using disruptor/robot',
            ],
            'safety_precautions': [
                'Never work alone',
                'Consider possibility of primary and secondary devices',
                'Use electronic jammers (if available)',
                'Always follow EOD protocol',
            ],
            'image_keywords': ['wire', 'battery', 'package', 'ied', 'bomb', 'device', 'explosive'],
        },
        {
            'id': 'bd_ied_002',
            'name': 'VBIED - Vehicle Borne IED (Car Bomb)',
            'bengali_name': 'ভিবিআইইডি (গাড়ি বোম্ব)',
            'category': 'ied',
            'origin': 'bangladesh',
            'priority': 1,
            'threat_level': 'high',
            'description': 'IED placed in a vehicle. Used in various terrorist attacks in Bangladesh. Extremely dangerous due to large explosive payload.',
            'components': ['Large Main Charge (usually 5-50 kg)', 'Detonating System', 'Shrapnel Material', 'Trigger Mechanism'],
            'types': ['SVBIED (Suicide)', 'RVBIED (Remote)', 'Timed VBIED'],
            'indicators': ['Suspicious parking', 'Unusually heavy vehicle', 'Unknown driver', 'Hanging wires'],
            'immediate_actions': [
                '1. Immediately move 500 meters away',
                '2. Stay away from nearby buildings (protection from debris)',
                '3. Notify bomb squad and police',
                '4. Clear traffic and civilians from area',
            ],
            'disposal_steps': [
                'Step 1: Establish 500m+ cordon',
                'Step 2: Examine vehicle using robotics',
                'Step 3: Complete X-ray scanning',
                'Step 4: Controlled detonation or EOD team neutralization',
            ],
            'safety_precautions': [
                'Never approach the vehicle',
                'Be cautious with radio use',
                'Handle all communications carefully',
            ],
            'image_keywords': ['car', 'vehicle', 'truck', 'van', 'bomb', 'vbied'],
        },

        # ===== HIGH EXPLOSIVES =====
        {
            'id': 'he_001',
            'name': 'TNT - Trinitrotoluene',
            'bengali_name': 'টিএনটি',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'The most well-known military explosive. Yellow or brown solid substance. Used as the standard for measuring explosive power (equivalent).',
            'physical_properties': {
                'Color': 'Yellow/Brown',
                'State': 'Solid',
                'Melting Point': '80.9°C',
                'Density': '1.65 g/cc',
                'Detonation Velocity': '6,900 m/s',
            },
            'components': ['C₇H₅N₃O₆'],
            'uses': ['Military charges', 'Mining', 'Construction demolition'],
            'immediate_actions': [
                '1. Clear area (300 meters)',
                '2. Call EOD team',
                '3. Avoid any heat or friction',
            ],
            'disposal_steps': [
                'Step 1: Establish safe cordon',
                'Step 2: Keep fire extinguisher ready',
                'Step 3: Controlled detonation or water neutralization',
                'Step 4: Removal by EOD expert',
            ],
            'safety_precautions': ['Keep away from heat', 'Avoid friction', 'Avoid direct impact'],
            'image_keywords': ['tnt', 'yellow', 'block', 'explosive', 'military charge'],
        },
        {
            'id': 'he_002',
            'name': 'PE (Plastic Explosive) - 808, 851, 852',
            'bengali_name': 'পিই (প্লাস্টিক বিস্ফোরক)',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'Plastic explosive - can be molded by hand. Widely used in Bangladesh Army. Ideal for demolition work.',
            'physical_properties': {
                'Color': 'White/Cream/Brown',
                'State': 'Soft solid (plastic)',
                'Special': 'Can be shaped by hand',
            },
            'components': ['RDX/PETN', 'Plasticizer'],
            'immediate_actions': [
                '1. Do not touch',
                '2. Keep away from heat or impact',
                '3. Notify EOD authority',
            ],
            'disposal_steps': [
                'Step 1: Maintain safe distance',
                'Step 2: EOD team removes using special equipment',
                'Step 3: Controlled detonation or deflagration',
            ],
            'safety_precautions': ['Do not bring near fire', 'Do not pierce with sharp objects'],
            'image_keywords': ['plastic explosive', 'pe4', 'c4', 'semtex', 'white putty'],
        },
        {
            'id': 'he_003',
            'name': 'RDX / Hexogen',
            'bengali_name': 'হেক্সোজেন (RDX)',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'The most commonly used powerful explosive in military forces. 1.5 times more powerful than TNT.',
            'physical_properties': {
                'Color': 'White',
                'State': 'Solid powder',
                'Detonation Velocity': '8,750 m/s',
                'Chemical Formula': 'C₃H₆N₆O₆',
            },
            'immediate_actions': [
                '1. Immediately clear area',
                '2. Notify EOD team',
            ],
            'disposal_steps': [
                'Step 1: Bring specialist EOD team',
                'Step 2: Controlled detonation',
            ],
            'safety_precautions': ['Extremely sensitive - may explode with slight impact'],
            'image_keywords': ['rdx', 'hexogen', 'white powder', 'military explosive'],
        },
        {
            'id': 'he_004',
            'name': 'Nitroglycerin',
            'bengali_name': 'নাইট্রোগ্লিসারিন',
            'category': 'conventional',
            'origin': 'international',
            'priority': 2,
            'threat_level': 'high',
            'description': 'Liquid explosive. Extremely sensitive - can detonate with slight vibration. Used in dynamite manufacture.',
            'physical_properties': {
                'Color': 'Colorless/Light yellow',
                'State': 'Liquid',
                'Danger': 'Extremely sensitive',
            },
            'immediate_actions': [
                '1. Do not cause any vibration or impact',
                '2. Immediately move away',
                '3. Call EOD team',
            ],
            'disposal_steps': [
                'Step 1: Handle with extreme caution',
                'Step 2: Specialist team uses neutralizing chemicals',
            ],
            'safety_precautions': ['Never shake', 'Keep away from heat', 'Do not touch without expertise'],
            'image_keywords': ['liquid explosive', 'nitroglycerin', 'clear liquid'],
        },
        {
            'id': 'mine_001',
            'name': 'Anti-Personnel Mine',
            'bengali_name': 'এন্টি-পার্সোনেল মাইন',
            'category': 'mines',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'high',
            'description': 'Landmine designed to injure or kill personnel. Placed in or near the ground. Detonates under foot pressure.',
            'types': ['Blast Mine', 'Fragmentation Mine', 'Bounding Mine'],
            'examples': ['PMN-2', 'TM-62', 'M14', 'VS-50'],
            'indicators': ['Unusually smooth ground', 'Wire marks', 'Disturbed soil'],
            'immediate_actions': [
                '1. Stop and do not move',
                '2. Slowly back away (same path you came)',
                '3. Warn others',
                '4. Call mine clearance specialist',
            ],
            'disposal_steps': [
                'Step 1: Mark and seal the area',
                'Step 2: Bring EOD or mine clearance team',
                'Step 3: Survey with prod and metal detector',
                'Step 4: Controlled detonation or neutralization',
            ],
            'safety_precautions': ['Never enter minefield alone', 'Do not remove mines without trained EOD'],
            'image_keywords': ['landmine', 'mine', 'anti-personnel', 'ground mine'],
        },
        {
            'id': 'switch_001',
            'name': 'RCIED - Radio Controlled IED',
            'bengali_name': 'রেডিও কন্ট্রোলড আইইডি',
            'category': 'ied',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'high',
            'description': 'IED controlled from a distance using radio signals. Can be activated by mobile phone, remote control, or walkie-talkie.',
            'components': ['Receiver', 'Transmitter', 'Firing Circuit', 'Main Charge', 'Battery'],
            'indicators': ['Visible antenna', 'Radio device', 'Unusual electronic components'],
            'immediate_actions': [
                '1. Turn off all mobile and radio equipment',
                '2. Move away from area',
                '3. Use electronic jammers',
                '4. Notify EOD team',
            ],
            'disposal_steps': [
                'Step 1: Start electronic jamming',
                'Step 2: EOD team will send robotics',
                'Step 3: Cut power supply with disruptor',
                'Step 4: Full neutralization by specialist',
            ],
            'safety_precautions': ['Do not use mobile phones', 'Stop radio transmission'],
            'image_keywords': ['rcied', 'radio controlled', 'remote controlled bomb', 'mobile phone ied'],
        },
        {
            'id': 'cbrn_001',
            'name': 'Chemical Weapon/Explosive',
            'bengali_name': 'রাসায়নিক অস্ত্র/বিস্ফোরক',
            'category': 'cbrn',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'high',
            'description': 'Weapons made with chemical substances. May contain nerve agents, blisering agents, choking agents, etc.',
            'types': ['Nerve Agents (Sarin, VX)', 'Blister Agents (Mustard Gas)', 'Choking Agents (Chlorine)', 'Blood Agents (Cyanide)'],
            'indicators': ['Unexpected smell', 'Sudden human/animal illness', 'Unexplained deaths', 'Liquid or vapor emission'],
            'immediate_actions': [
                '1. Immediately move upwind',
                '2. Put on MOPP gear (if available)',
                '3. Call CBRN response team',
                '4. Decontaminate affected persons',
            ],
            'disposal_steps': [
                'Step 1: Establish safe perimeter',
                'Step 2: Bring CBRN specialist team',
                'Step 3: Decontamination operation',
                'Step 4: Neutralization using special methods',
            ],
            'safety_precautions': ['No entry without CBRN gear', 'Protect yourself before touching victims'],
            'image_keywords': ['chemical weapon', 'gas canister', 'cbrn', 'yellow cross', 'nerve agent'],
        },

        # ===== EOD EQUIPMENT =====
        {
            'id': 'eod_001',
            'name': 'EOD Protective Suit (Bomb Suit)',
            'bengali_name': 'ইওডি সুরক্ষা পোশাক',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'Specialized protective suit used in explosive ordnance disposal. Protects against blast pressure, fragmentation, and heat. Weighs approximately 35-80 kg.',
            'components': ['Blast-resistant jacket', 'Protective helmet & visor', 'Gloves', 'Trousers', 'Boots', 'Cooling vest'],
            'types': ['Heavy EOD Suit (Mk5/Mk6)', 'Lightweight Search Suit', 'CBRN Suit'],
            'image_keywords': ['eod suit', 'bomb suit', 'protective suit', 'disposal suit'],
        },
        {
            'id': 'eod_002',
            'name': 'EOD Robot / Remote Controlled Vehicle',
            'bengali_name': 'ইওডি রোবট',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'Remotely controlled robot used for IED inspection and neutralization. Protects operators from direct danger. Equipped with camera system, robotic arm, and disruptor mount.',
            'components': ['Multi-joint robotic arm', 'HD camera system (front/rear)', 'Remote control console', 'Disruptor mount', 'Track/wheel drive', 'Lighting system'],
            'types': ['iRobot PackBot 510', 'QinetiQ Talon', 'Dragon Runner', 'Telemax Pro'],
            'image_keywords': ['eod robot', 'bomb robot', 'remote vehicle', 'disposal robot', 'packbot'],
        },
        {
            'id': 'eod_003',
            'name': 'Disruptor / PAN Disruptor Mk5',
            'bengali_name': 'ডিসরাপ্টার (PAN Disruptor)',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'Disrupts IED circuitry or power supply using high-pressure water or projectile. Safe and effective neutralization method. Typically mounted on EOD robot.',
            'components': ['High-pressure water/slug gun', 'Firing mechanism', 'Mounting bracket', 'Remote firing cable', 'Projectile charge'],
            'types': ['PAN Disruptor Mk5', 'Piglet', 'REMO Disruptor', 'Water Disruptor'],
            'image_keywords': ['disruptor', 'pan disruptor', 'water disruptor', 'eod tool', 'mk5'],
        },
        {
            'id': 'eod_004',
            'name': 'Metal Detector & Mine Search Kit',
            'bengali_name': 'মেটাল ডিটেক্টর ও সার্চ কিট',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'Used to detect metallic objects in ground or within objects. Essential tool for mine and IED search operations. Widely used in Bangladesh Army.',
            'components': ['Metal detector head', 'Control box', 'Prod (probe rod)', 'Headphones', 'Marking pegs & tape'],
            'types': ['Vallon VMH3CS', 'CEIA CMD', 'Minelab F3', 'Ebinger UPEX 740'],
            'image_keywords': ['metal detector', 'mine detector', 'search kit', 'eod search', 'vallon'],
        },
        {
            'id': 'eod_005',
            'name': 'Hook & Line Kit (Manual Disruptor)',
            'bengali_name': 'হুক ও লাইন কিট',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'Used to move or drag suspicious objects from a safe distance. The most basic EOD tool used in initial response. Keeps operator at safe distance.',
            'components': ['Steel grapnel hook', 'Nylon rope (100m+)', 'Pulley system', 'Carabiner clips', 'Storage bag'],
            'types': ['Single Hook & Line', 'Triple Hook', 'Grapnel Hook', 'Telescopic Hook'],
            'image_keywords': ['hook and line', 'rope kit', 'eod hook', 'drag kit', 'grapnel'],
        },
        {
            'id': 'eod_006',
            'name': 'Portable X-Ray Scanning System',
            'bengali_name': 'পোর্টেবল X-রে স্ক্যানিং সিস্টেম',
            'category': 'eod_equipment',
            'origin': 'international',
            'priority': 1,
            'threat_level': 'safe',
            'description': 'Portable X-ray system used to examine internal structure of IEDs, parcel bombs, or suspicious objects without detonation.',
            'components': ['X-ray generator head', 'Digital detector panel', 'Laptop/tablet viewer', 'Remote firing cable', 'Collimator'],
            'types': ['Scanna SC12C', 'Golden Engineering XRIS50', 'Vidisco Fox-RAPISCAN', 'Logos Imaging'],
            'image_keywords': ['xray', 'x-ray scanner', 'portable xray', 'eod xray', 'scanna'],
        },
    ]
}


_T = 'https://upload.wikimedia.org/wikipedia/commons/thumb/'

# Verified real image URLs (Wikimedia Commons public domain / CC)
_IED  = _T + 'a/a5/IED_Baghdad_from_munitions.jpg/480px-IED_Baghdad_from_munitions.jpg'
_VBIED= _T + '5/5d/Car_bomb_in_Iraq.jpg/480px-Car_bomb_in_Iraq.jpg'
_TNT  = _T + '0/05/Tools_of_the_Trade%2C_Motor_Transport_Marines_Learn_Explosive_Ordnance_Fundamentals_100820-m-1394j-007.jpg/480px-Tools_of_the_Trade%2C_Motor_Transport_Marines_Learn_Explosive_Ordnance_Fundamentals_100820-m-1394j-007.jpg'
_C4   = _T + '2/2e/C4_plastic_explosive.jpg/480px-C4_plastic_explosive.jpg'
_RDX  = _T + '9/93/RDX_crystal.jpg/480px-RDX_crystal.jpg'
_NITRO= _T + '6/64/Nitro.JPG/400px-Nitro.JPG'
_ANFO = _T + 'f/f8/Ammonium_nitrate-fuel_oil_%28ANFO%29_explosive.jpg/480px-Ammonium_nitrate-fuel_oil_%28ANFO%29_explosive.jpg'
_DET  = _T + '2/2c/Detonator.jpg/480px-Detonator.jpg'
_PMN  = _T + '3/31/PMN_%28rechts%29_und_PMN_2.jpeg/480px-PMN_%28rechts%29_und_PMN_2.jpeg'
_PMN2 = _T + 'b/bd/PMN_anti-personnel_landmine_%28DOSAAF_Museum_in_Minsk%29.jpg/480px-PMN_anti-personnel_landmine_%28DOSAAF_Museum_in_Minsk%29.jpg'
_CLAY = _T + 'c/c1/US_M18a1_claymore_mine.jpg/480px-US_M18a1_claymore_mine.jpg'
_NVAL = _T + '8/82/Moored_contact_mine_Mk6.jpg/480px-Moored_contact_mine_Mk6.jpg'
_MK82 = _T + 'e/e2/US_Navy_030529-N-0295M-007_Aviation_Ordnanceman_3rd_Class_Aaron_Harris_checks_a_MK-82_500lb._General_purpose_bomb.jpg/480px-US_Navy_030529-N-0295M-007_Aviation_Ordnanceman_3rd_Class_Aaron_Harris_checks_a_MK-82_500lb._General_purpose_bomb.jpg'
_GAS  = _T + 'd/d9/Gas_mask_MUA_IMGP0157.jpg/480px-Gas_mask_MUA_IMGP0157.jpg'
_GAS2 = _T + 'a/ae/Swiss_Army_gas_mask_model_90-IMG_7567.jpg/480px-Swiss_Army_gas_mask_model_90-IMG_7567.jpg'
_GEIG = _T + '4/40/Geiger_counter.jpg/480px-Geiger_counter.jpg'
_SUIT = _T + 'b/b5/British_army_officer_pays_tribute_in_an_EOD_bomb_suit_130303-A-RW508-001.jpg/480px-British_army_officer_pays_tribute_in_an_EOD_bomb_suit_130303-A-RW508-001.jpg'
_ROBT = _T + '2/28/Explosive_ordnance_disposal_team_member_guides_bomb_disposal_robot_DVIDS365826.jpg/480px-Explosive_ordnance_disposal_team_member_guides_bomb_disposal_robot_DVIDS365826.jpg'
_DISR = _T + 'c/c4/EOD_Marines_train_for_unique_threats_131023-M-LI810-324.jpg/480px-EOD_Marines_train_for_unique_threats_131023-M-LI810-324.jpg'
_MDET = _T + '7/73/ANA_conducts_handheld_mine_detector_training_in_Zabul_140204-Z-HP669-004.jpg/480px-ANA_conducts_handheld_mine_detector_training_in_Zabul_140204-Z-HP669-004.jpg'
_HOOK = _T + '7/73/Kyrgyz%2C_U.S._EOD_military_exchange_130424-F-QV958-007.jpg/480px-Kyrgyz%2C_U.S._EOD_military_exchange_130424-F-QV958-007.jpg'
_XRAY = _T + '9/90/Iraqi_army_explosive_ordnance_disposal_%28EOD%29_soldiers_learn_how_to_operate_a_portable_x-ray_unit_during_EOD_training_in_the_Kirkuk_province_of_Iraq_Sept_100901-A-DM673-062.jpg/480px-Iraqi_army_explosive_ordnance_disposal_%28EOD%29_soldiers_learn_how_to_operate_a_portable_x-ray_unit_during_EOD_training_in_the_Kirkuk_province_of_Iraq_Sept_100901-A-DM673-062.jpg'
_XRAY2= _T + 'f/f0/What%27s_inside%3F_EOD_technicians_crack_the_case_in_Italy_161129-M-VA786-048.jpg/480px-What%27s_inside%3F_EOD_technicians_crack_the_case_in_Italy_161129-M-VA786-048.jpg'
_RADS = 'https://upload.wikimedia.org/wikipedia/commons/a/a0/Radiation_warning_symbol.svg'

EXPLOSIVE_IMAGES = {
    'bd_ied_001': {
        'image_url': _IED,
        'gallery': [
            {'label_bn': 'আইইডি — বাগদাদ ২০০৫', 'label_en': 'IED Found — Baghdad 2005', 'url': _IED},
            {'label_bn': 'মূল চার্জ (TNT ব্লক)', 'label_en': 'Main Charge — TNT Block', 'url': _TNT},
            {'label_bn': 'ডেটোনেটর ও ব্লাস্টিং ক্যাপ', 'label_en': 'Detonator / Blasting Cap', 'url': _DET},
        ],
    },
    'bd_ied_002': {
        'image_url': _VBIED,
        'gallery': [
            {'label_bn': 'গাড়ি বোম্ব বিস্ফোরণ — ইরাক', 'label_en': 'Car Bomb Explosion — Iraq', 'url': _VBIED},
            {'label_bn': 'ANFO বিস্ফোরক মিশ্রণ', 'label_en': 'ANFO Explosive Mixture', 'url': _ANFO},
            {'label_bn': 'ডেটোনেটিং সিস্টেম', 'label_en': 'Detonating System', 'url': _DET},
        ],
    },
    'bd_ied_003': {
        'image_url': _IED,
        'gallery': [
            {'label_bn': 'আইইডি উপাদান', 'label_en': 'IED Components', 'url': _IED},
            {'label_bn': 'ডেটোনেটর', 'label_en': 'Detonator / Trigger', 'url': _DET},
            {'label_bn': 'বিস্ফোরক চার্জ', 'label_en': 'Explosive Charge (TNT)', 'url': _TNT},
        ],
    },
    'he_001': {
        'image_url': _TNT,
        'gallery': [
            {'label_bn': 'TNT ব্লক — EOD রেঞ্জ', 'label_en': 'TNT Block at EOD Range', 'url': _TNT},
            {'label_bn': 'RDX ক্রিস্টাল (তুলনা)', 'label_en': 'RDX Crystal (comparison)', 'url': _RDX},
            {'label_bn': 'ANFO (সহজলভ্য বিকল্প)', 'label_en': 'ANFO (common substitute)', 'url': _ANFO},
        ],
    },
    'he_002': {
        'image_url': _C4,
        'gallery': [
            {'label_bn': 'C4 প্লাস্টিক বিস্ফোরক', 'label_en': 'C4 Plastic Explosive Block', 'url': _C4},
            {'label_bn': 'RDX ক্রিস্টাল (মূল উপাদান)', 'label_en': 'RDX Crystal (main component)', 'url': _RDX},
            {'label_bn': 'ডেটোনেটর সহ ব্যবহার', 'label_en': 'Used with Detonator', 'url': _DET},
        ],
    },
    'he_003': {
        'image_url': _RDX,
        'gallery': [
            {'label_bn': 'RDX ক্রিস্টাল', 'label_en': 'RDX Crystal (white solid)', 'url': _RDX},
            {'label_bn': 'C4 (RDX-ভিত্তিক)', 'label_en': 'C4 (RDX-based explosive)', 'url': _C4},
            {'label_bn': 'ডেটোনেটর', 'label_en': 'Detonator for initiation', 'url': _DET},
        ],
    },
    'he_004': {
        'image_url': _NITRO,
        'gallery': [
            {'label_bn': 'নাইট্রোগ্লিসারিন (ফার্মাসিউটিক্যাল)', 'label_en': 'Nitroglycerin — pharmaceutical forms', 'url': _NITRO},
            {'label_bn': 'ANFO (সাধারণ বিকল্প)', 'label_en': 'ANFO (common alternative)', 'url': _ANFO},
        ],
    },
    'he_005': {
        'image_url': _ANFO,
        'gallery': [
            {'label_bn': 'ANFO বিস্ফোরক', 'label_en': 'ANFO Explosive Material', 'url': _ANFO},
            {'label_bn': 'TNT (তুলনীয় বিস্ফোরক)', 'label_en': 'TNT (comparable explosive)', 'url': _TNT},
            {'label_bn': 'ডেটোনেটর', 'label_en': 'Detonator for initiation', 'url': _DET},
        ],
    },
    'det_001': {
        'image_url': _DET,
        'gallery': [
            {'label_bn': 'ডেটোনেটর ৩ ধরন', 'label_en': 'Detonator — 3 types', 'url': _DET},
            {'label_bn': 'EOD প্রশিক্ষণ — ডিসরাপ্টর', 'label_en': 'EOD Training with Disruptor', 'url': _DISR},
            {'label_bn': 'মেটাল ডিটেক্টর (সার্চ)', 'label_en': 'Metal Detector for Search', 'url': _MDET},
        ],
    },
    'mine_001': {
        'image_url': _PMN,
        'gallery': [
            {'label_bn': 'PMN ও PMN-2 মাইন', 'label_en': 'PMN & PMN-2 Mines', 'url': _PMN},
            {'label_bn': 'PMN-2 (মিউজিয়াম)', 'label_en': 'PMN-2 Mine — Museum Display', 'url': _PMN2},
            {'label_bn': 'M18A1 ক্লেমোর মাইন', 'label_en': 'M18A1 Claymore Mine', 'url': _CLAY},
            {'label_bn': 'মাইন ডিটেক্টর দিয়ে সার্চ', 'label_en': 'Mine Search with Detector', 'url': _MDET},
        ],
    },
    'mine_002': {
        'image_url': _NVAL,
        'gallery': [
            {'label_bn': 'মুরড কন্ট্যাক্ট মাইন Mk.6', 'label_en': 'Moored Contact Mine Mk.6', 'url': _NVAL},
            {'label_bn': 'EOD রোবট (প্রতিক্রিয়া)', 'label_en': 'EOD Robot (response)', 'url': _ROBT},
        ],
    },
    'aerial_001': {
        'image_url': _MK82,
        'gallery': [
            {'label_bn': 'Mk-82 500lb GP বোম্ব', 'label_en': 'Mk-82 500lb General Purpose Bomb', 'url': _MK82},
            {'label_bn': 'EOD রোবট (UXO পরীক্ষা)', 'label_en': 'EOD Robot (UXO inspection)', 'url': _ROBT},
            {'label_bn': 'EOD বোম্ব স্যুট', 'label_en': 'EOD Bomb Suit (disposal)', 'url': _SUIT},
        ],
    },
    'cbrn_001': {
        'image_url': _GAS,
        'gallery': [
            {'label_bn': 'সামরিক গ্যাস মাস্ক (Polish MUA)', 'label_en': 'Military Gas Mask — Polish MUA', 'url': _GAS},
            {'label_bn': 'সুইস আর্মি গ্যাস মাস্ক', 'label_en': 'Swiss Army Gas Mask Model-90', 'url': _GAS2},
            {'label_bn': 'গিগার কাউন্টার', 'label_en': 'Geiger Counter (CBRN detection)', 'url': _GEIG},
        ],
    },
    'cbrn_002': {
        'image_url': _GEIG,
        'gallery': [
            {'label_bn': 'গিগার কাউন্টার', 'label_en': 'Geiger-Müller Counter', 'url': _GEIG},
            {'label_bn': 'রেডিয়েশন সতর্কতা চিহ্ন', 'label_en': 'Radiation Warning Symbol', 'url': _RADS},
            {'label_bn': 'CBRN সুরক্ষা গ্যাস মাস্ক', 'label_en': 'CBRN Protective Gas Mask', 'url': _GAS},
        ],
    },
    'switch_001': {
        'image_url': _IED,
        'gallery': [
            {'label_bn': 'আইইডি উপাদান', 'label_en': 'IED Components', 'url': _IED},
            {'label_bn': 'ডেটোনেটর (ট্রিগার)', 'label_en': 'Detonator / Trigger Circuit', 'url': _DET},
            {'label_bn': 'EOD রোবট (নিরাপদ প্রতিক্রিয়া)', 'label_en': 'EOD Robot (safe response)', 'url': _ROBT},
        ],
    },
    'switch_002': {
        'image_url': _SUIT,
        'gallery': [
            {'label_bn': 'EOD বোম্ব স্যুট (প্রতিক্রিয়া)', 'label_en': 'EOD Bomb Suit (response)', 'url': _SUIT},
            {'label_bn': 'EOD রোবট', 'label_en': 'EOD Robot (standoff response)', 'url': _ROBT},
            {'label_bn': 'আইইডি উপাদান', 'label_en': 'IED/PBIED Components', 'url': _IED},
        ],
    },
    # EOD Equipment
    'eod_001': {
        'image_url': _SUIT,
        'gallery': [
            {'label_bn': 'EOD বোম্ব স্যুট — আফগানিস্তান', 'label_en': 'EOD Bomb Suit — Afghanistan', 'url': _SUIT},
            {'label_bn': 'EOD রোবটের সাথে', 'label_en': 'With EOD Robot (team)', 'url': _ROBT},
            {'label_bn': 'ডিসরাপ্টর প্রশিক্ষণ', 'label_en': 'Disruptor Training', 'url': _DISR},
        ],
    },
    'eod_002': {
        'image_url': _ROBT,
        'gallery': [
            {'label_bn': 'EOD রোবট — বোম্ব ডিসপোজাল', 'label_en': 'EOD Robot — Bomb Disposal', 'url': _ROBT},
            {'label_bn': 'ডিসরাপ্টর প্রশিক্ষণ', 'label_en': 'Disruptor on Robot', 'url': _DISR},
            {'label_bn': 'X-রে স্ক্যানিং', 'label_en': 'Portable X-Ray Unit', 'url': _XRAY},
        ],
    },
    'eod_003': {
        'image_url': _DISR,
        'gallery': [
            {'label_bn': 'PAN ডিসরাপ্টর প্রশিক্ষণ', 'label_en': 'PAN Disruptor — Marine EOD Training', 'url': _DISR},
            {'label_bn': 'EOD রোবট (মাউন্ট)', 'label_en': 'EOD Robot (disruptor mounted)', 'url': _ROBT},
            {'label_bn': 'EOD বোম্ব স্যুট', 'label_en': 'EOD Bomb Suit', 'url': _SUIT},
        ],
    },
    'eod_004': {
        'image_url': _MDET,
        'gallery': [
            {'label_bn': 'হ্যান্ডহেল্ড মাইন ডিটেক্টর', 'label_en': 'Handheld Mine Detector — ANA Training', 'url': _MDET},
            {'label_bn': 'PMN-2 মাইন (লক্ষ্যবস্তু)', 'label_en': 'PMN-2 Mine (what is detected)', 'url': _PMN},
            {'label_bn': 'EOD বোম্ব স্যুট', 'label_en': 'EOD Bomb Suit', 'url': _SUIT},
        ],
    },
    'eod_005': {
        'image_url': _HOOK,
        'gallery': [
            {'label_bn': 'হুক ও লাইন কিট — EOD বিনিময়', 'label_en': 'Hook & Line Kit — EOD Exchange', 'url': _HOOK},
            {'label_bn': 'EOD রোবট (বিকল্প)', 'label_en': 'EOD Robot (alternative)', 'url': _ROBT},
            {'label_bn': 'আইইডি (লক্ষ্যবস্তু)', 'label_en': 'IED (target object)', 'url': _IED},
        ],
    },
    'eod_006': {
        'image_url': _XRAY,
        'gallery': [
            {'label_bn': 'পোর্টেবল X-রে — ইরাকি EOD', 'label_en': 'Portable X-Ray — Iraqi EOD Training', 'url': _XRAY},
            {'label_bn': 'X-রে স্ক্যানিং — ইতালি', 'label_en': 'X-Ray Scanning — Italy EOD', 'url': _XRAY2},
            {'label_bn': 'ডেটোনেটর (স্ক্যান টার্গেট)', 'label_en': 'Detonator (scan target)', 'url': _DET},
        ],
    },
}


def get_all_explosives(lang='bn'):
    result = []
    for exp in EXPLOSIVES_DATABASE.get(lang, EXPLOSIVES_DATABASE['bn']):
        item = dict(exp)
        if exp['id'] in EXPLOSIVE_IMAGES:
            item['image_url'] = EXPLOSIVE_IMAGES[exp['id']].get('image_url')
        result.append(item)
    return result


def get_explosive_by_id(explosive_id, lang='bn'):
    for exp in EXPLOSIVES_DATABASE.get(lang, EXPLOSIVES_DATABASE['bn']):
        if exp['id'] == explosive_id:
            result = dict(exp)
            if explosive_id in EXPLOSIVE_IMAGES:
                result.update(EXPLOSIVE_IMAGES[explosive_id])
            return result
    return None


def search_explosives(query, lang='bn'):
    results = []
    query_lower = query.lower()
    for exp in EXPLOSIVES_DATABASE.get(lang, EXPLOSIVES_DATABASE['bn']):
        if (query_lower in exp['name'].lower() or
                query_lower in exp.get('description', '').lower() or
                query_lower in exp.get('english_name', '').lower() or
                query_lower in exp.get('bengali_name', '').lower()):
            results.append(exp)
    return results


def get_explosives_by_category(category, lang='bn'):
    results = []
    for exp in EXPLOSIVES_DATABASE.get(lang, EXPLOSIVES_DATABASE['bn']):
        if exp['category'] == category:
            results.append(exp)
    return results


def find_by_image_keywords(keywords, lang='bn'):
    """Find explosives based on image recognition keywords"""
    results = []
    keywords_lower = [k.lower() for k in keywords]
    for exp in EXPLOSIVES_DATABASE.get(lang, EXPLOSIVES_DATABASE['bn']):
        score = 0
        for keyword in exp.get('image_keywords', []):
            for query_keyword in keywords_lower:
                if query_keyword in keyword.lower() or keyword.lower() in query_keyword:
                    score += 1
        if score > 0:
            results.append((score, exp))
    results.sort(key=lambda x: x[0], reverse=True)
    return [exp for _, exp in results]
