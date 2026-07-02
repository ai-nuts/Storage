/* ResearchStudio — landing page interactivity
 * Vanilla JS, no dependencies.
 * - "Copy" buttons on every .code-block
 * - IntersectionObserver-based reveal-on-scroll
 * - Auto-pause videos when they scroll out of view
 */

(function () {
  'use strict';

  // ---- Copy buttons ---------------------------------------------------------
  document.querySelectorAll('.code-block').forEach(function (block) {
    var btn = block.querySelector('.copy');
    var pre = block.querySelector('pre');
    if (!btn || !pre) return;

    btn.addEventListener('click', function () {
      var text = pre.innerText.replace(/\s+$/, '');
      var done = function () {
        var original = btn.textContent;
        btn.textContent = 'Copied';
        btn.classList.add('copied');
        setTimeout(function () {
          btn.textContent = original;
          btn.classList.remove('copied');
        }, 1400);
      };

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(fallback);
      } else {
        fallback();
      }

      function fallback() {
        var ta = document.createElement('textarea');
        ta.value = text;
        ta.setAttribute('readonly', '');
        ta.style.position = 'absolute';
        ta.style.left = '-9999px';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); done(); }
        catch (_) { /* swallow */ }
        document.body.removeChild(ta);
      }
    });
  });

  // ---- Reveal on scroll -----------------------------------------------------
  var revealTargets = [
    '.hero__chip', '.hero__title', '.hero__lead', '.hero__cta', '.hero__badges',
    '.hero__strip > *', '.hero__caption',
    '.section .eyebrow', '.section .section__title', '.section .section__lead',
    '.pipeline > *',
    '.skill', '.card--demo', '.card--video', '.usecard',
    '.logos li', '.cta-row .btn'
  ].join(',');

  var nodes = document.querySelectorAll(revealTargets);
  nodes.forEach(function (n) { n.classList.add('reveal'); });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

    nodes.forEach(function (n) { io.observe(n); });
  } else {
    nodes.forEach(function (n) { n.classList.add('is-visible'); });
  }

  // ---- Pause off-screen videos to save resources ----------------------------
  if ('IntersectionObserver' in window) {
    var vio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var v = entry.target;
        if (!entry.isIntersecting && !v.paused) v.pause();
      });
    }, { threshold: 0.25 });
    document.querySelectorAll('video').forEach(function (v) { vio.observe(v); });
  }

  // ---- Smooth-scroll offset for sticky nav (anchor links) -------------------
  // CSS `scroll-margin-top` would normally be enough, but Safari sometimes
  // ignores it on first paint — we patch click anchors here.
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    var href = a.getAttribute('href');
    if (!href || href === '#' || href.length < 2) return;
    a.addEventListener('click', function (e) {
      var target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      var navH = (document.querySelector('.nav') || {}).offsetHeight || 0;
      var y = target.getBoundingClientRect().top + window.pageYOffset - navH - 8;
      window.scrollTo({ top: y, behavior: 'smooth' });
      history.replaceState(null, '', href);
    });
  });
})();
