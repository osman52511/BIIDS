/**
 * BIIDS - Bomb & IED Identification System
 * Main JavaScript
 */

'use strict';

// Auto-dismiss alerts after 4 seconds
document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 4000);
    });

    // Initialize tooltips
    const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltips.forEach(el => new bootstrap.Tooltip(el));

    // Mark active nav items
    markActiveNav();

    // Progressive markdown rendering for bomb_ied_page
    renderMarkdown();
});

// Mark bottom nav active item
function markActiveNav() {
    const path = window.location.pathname;
    document.querySelectorAll('.bottom-nav-item').forEach(item => {
        const href = item.getAttribute('href');
        if (href && path === href) {
            item.classList.add('active');
        }
    });
}

// Simple markdown renderer for content
function renderMarkdown() {
    const content = document.querySelector('.chapter-body');
    if (!content) return;

    let html = content.innerHTML;

    // h2 headers (##)
    html = html.replace(/##\s+(.+?)(?=<br>|$)/gm,
        '<h5 class="mt-4 mb-2" style="color:#7dc87d; border-bottom:1px solid #2d4a2d; padding-bottom:5px;">$1</h5>');

    // h3 headers (###)
    html = html.replace(/###\s+(.+?)(?=<br>|$)/gm,
        '<h6 class="mt-3 mb-2 fw-bold" style="color:#9dc49d;">$1</h6>');

    // Bold (**text**)
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong style="color:#dce8dc;">$1</strong>');

    // Italic (*text*)
    html = html.replace(/\*([^*]+?)\*/g, '<em>$1</em>');

    // Code blocks (```...```)
    html = html.replace(/```([\s\S]*?)```/g,
        '<pre class="code-block">$1</pre>');

    // Inline code (`code`)
    html = html.replace(/`([^`]+?)`/g,
        '<code style="background:#0a0f0a; color:#7dc87d; padding:2px 5px; border-radius:3px;">$1</code>');

    // Tables - detect and render
    html = renderTables(html);

    // Lists (- item)
    html = renderLists(html);

    // Ordered lists (1. item)
    html = renderOrderedLists(html);

    // Clean up extra <br> tags after headers and lists
    html = html.replace(/<\/h[1-6]><br>/g, '</h$1>');

    content.innerHTML = html;
}

function renderTables(html) {
    // Find table blocks (lines starting with |)
    const tableRegex = /(\|.*?\|<br>)+/g;
    return html.replace(tableRegex, function(match) {
        const rows = match.split('<br>').filter(r => r.trim() && r.includes('|'));
        if (rows.length < 2) return match;

        let tableHtml = '<div class="table-responsive"><table class="table table-dark table-bordered table-sm" style="font-size:0.85rem;">';

        rows.forEach((row, i) => {
            if (row.includes('---')) return; // separator row
            const cells = row.split('|').filter(c => c.trim());
            if (cells.length === 0) return;

            const tag = i === 0 ? 'th' : 'td';
            tableHtml += '<tr>';
            cells.forEach(cell => {
                tableHtml += `<${tag} style="${i === 0 ? 'background:#0d2b0d; color:#9dc49d;' : ''}">${cell.trim()}</${tag}>`;
            });
            tableHtml += '</tr>';
        });

        tableHtml += '</table></div>';
        return tableHtml;
    });
}

function renderLists(html) {
    // Replace bullet list items
    html = html.replace(/^- (.+?)(?=<br>)/gm, '<li>$1</li>');
    // Wrap consecutive <li> items
    html = html.replace(/(<li>.*?<\/li>\s*)+/g, '<ul class="mb-2" style="padding-left:20px;">$&</ul>');
    return html;
}

function renderOrderedLists(html) {
    html = html.replace(/^\d+\.\s+(.+?)(?=<br>)/gm, '<li>$1</li>');
    return html;
}

// Smooth scroll to section
function scrollToSection(id) {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Copy to clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast(document.documentElement.lang === 'bn' ?
            'কপি হয়েছে!' : 'Copied!', 'success');
    });
}

// Toast notification
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast-notification toast-${type}`;
    toast.textContent = message;
    toast.style.cssText = `
        position: fixed; bottom: 80px; left: 50%; transform: translateX(-50%);
        background: ${type === 'success' ? '#1a4a1a' : '#1a1a4a'};
        color: #fff; padding: 10px 20px; border-radius: 20px;
        font-size: 0.85rem; z-index: 9999;
        animation: fadeInUp 0.3s ease, fadeOut 0.5s ease 2s forwards;
    `;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2500);
}

// Add fadeInUp/fadeOut animations
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInUp { from { opacity:0; transform: translate(-50%, 20px); } to { opacity:1; transform: translate(-50%, 0); } }
    @keyframes fadeOut { from { opacity:1; } to { opacity:0; } }
`;
document.head.appendChild(style);

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Escape to close any open modals
    if (e.key === 'Escape') {
        const modals = document.querySelectorAll('.modal.show');
        modals.forEach(m => bootstrap.Modal.getInstance(m)?.hide());
    }
});

// Service Worker registration for PWA (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        // Uncomment to enable PWA:
        // navigator.serviceWorker.register('/sw.js');
    });
}
