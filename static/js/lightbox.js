/* BIIDS Lightbox — vanilla JS, no dependencies */
(function () {
    'use strict';

    var overlay, imgEl, captionEl, counterEl, prevBtn, nextBtn, closeBtn;
    var items = [], idx = 0, touchStartX = 0, touchStartY = 0;

    function build() {
        overlay = document.createElement('div');
        overlay.id = 'lb';
        overlay.setAttribute('role', 'dialog');
        overlay.setAttribute('aria-modal', 'true');
        overlay.innerHTML =
            '<div id="lb-inner">' +
                '<img id="lb-img" src="" alt="">' +
                '<div id="lb-caption"></div>' +
            '</div>' +
            '<div id="lb-counter"></div>' +
            '<button id="lb-close" aria-label="Close">&#10005;</button>' +
            '<button id="lb-prev" aria-label="Previous">&#8249;</button>' +
            '<button id="lb-next" aria-label="Next">&#8250;</button>';
        document.body.appendChild(overlay);

        imgEl     = document.getElementById('lb-img');
        captionEl = document.getElementById('lb-caption');
        counterEl = document.getElementById('lb-counter');
        closeBtn  = document.getElementById('lb-close');
        prevBtn   = document.getElementById('lb-prev');
        nextBtn   = document.getElementById('lb-next');

        closeBtn.addEventListener('click', close);
        prevBtn.addEventListener('click', function (e) { e.stopPropagation(); prev(); });
        nextBtn.addEventListener('click', function (e) { e.stopPropagation(); next(); });

        overlay.addEventListener('click', function (e) {
            if (e.target === overlay || e.target.id === 'lb-inner') close();
        });

        document.addEventListener('keydown', function (e) {
            if (!overlay.classList.contains('lb-open')) return;
            if (e.key === 'Escape')      close();
            if (e.key === 'ArrowLeft')   prev();
            if (e.key === 'ArrowRight')  next();
        });

        /* Touch swipe */
        overlay.addEventListener('touchstart', function (e) {
            touchStartX = e.changedTouches[0].screenX;
            touchStartY = e.changedTouches[0].screenY;
        }, { passive: true });
        overlay.addEventListener('touchend', function (e) {
            var dx = touchStartX - e.changedTouches[0].screenX;
            var dy = touchStartY - e.changedTouches[0].screenY;
            if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {
                dx > 0 ? next() : prev();
            }
        }, { passive: true });
    }

    function open(group, startIdx) {
        var els = document.querySelectorAll('[data-lb="' + group + '"]');
        items = [];
        for (var i = 0; i < els.length; i++) {
            items.push({
                src:     els[i].dataset.lbSrc || els[i].src || '',
                caption: els[i].dataset.lbCaption || els[i].alt || ''
            });
        }
        idx = startIdx || 0;
        render();
        overlay.classList.add('lb-open');
        document.body.classList.add('lb-no-scroll');
    }

    function render() {
        var item = items[idx];
        imgEl.src = '';
        imgEl.src = item.src;
        imgEl.alt = item.caption;
        captionEl.textContent = item.caption;
        counterEl.textContent = items.length > 1 ? (idx + 1) + ' / ' + items.length : '';
        prevBtn.style.display = items.length > 1 ? 'flex' : 'none';
        nextBtn.style.display = items.length > 1 ? 'flex' : 'none';
    }

    function close() {
        overlay.classList.remove('lb-open');
        document.body.classList.remove('lb-no-scroll');
        imgEl.src = '';
    }

    function prev() { idx = (idx - 1 + items.length) % items.length; render(); }
    function next() { idx = (idx + 1) % items.length; render(); }

    function initTriggers() {
        document.querySelectorAll('[data-lb]').forEach(function (el) {
            el.style.cursor = 'zoom-in';
            el.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                var group = el.dataset.lb;
                var els   = document.querySelectorAll('[data-lb="' + group + '"]');
                var start = 0;
                for (var i = 0; i < els.length; i++) {
                    if (els[i] === el) { start = i; break; }
                }
                open(group, start);
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () { build(); initTriggers(); });
    } else {
        build();
        initTriggers();
    }

    window.lbOpen = open;
})();
