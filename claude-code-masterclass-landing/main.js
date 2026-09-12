/* ============================================================
   Claude Code Masterclass — landing page behaviour
   No dependencies. Everything degrades gracefully without JS.
   ============================================================ */
(function () {
  'use strict';

  document.documentElement.classList.add('js');

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- analytics -------------------------------------------------
     Wire this to your provider. Examples:
       plausible('cta_click', { props: { section: section } })
       gtag('event', 'cta_click', { section: section })
       posthog.capture('cta_click', { section: section })
  ---------------------------------------------------------------------- */
  function trackCta(section) {
    if (typeof window.plausible === 'function') {
      window.plausible('cta_click', { props: { section: section } });
    }
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'cta_click', { section: section });
    }
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: 'cta_click', section: section });
  }

  document.querySelectorAll('[data-cta]').forEach(function (el) {
    el.addEventListener('click', function () {
      trackCta(el.getAttribute('data-cta'));
    });
  });

  /* ---------- footer year ---------------------------------------------- */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* ---------- nav: stuck state + mobile menu ---------------------------- */
  var nav = document.getElementById('nav');

  if (nav && 'IntersectionObserver' in window) {
    // Hairline border: the moment the page moves at all.
    var sentinel = document.getElementById('scroll-sentinel');
    if (sentinel) {
      new IntersectionObserver(function (entries) {
        nav.classList.toggle('is-scrolled', !entries[0].isIntersecting);
      }).observe(sentinel);
    }

    // CTA: only once the whole hero has left the viewport. Observing the hero
    // itself (not its buttons) — on a short viewport the buttons start below
    // the fold, which would reveal the CTA before the user has scrolled.
    var hero = document.querySelector('.hero');
    if (hero) {
      new IntersectionObserver(function (entries) {
        nav.classList.toggle('is-past-hero', !entries[0].isIntersecting);
      }, { rootMargin: '-72px 0px 0px 0px' }).observe(hero);
    }
  }

  var toggle = document.getElementById('nav-toggle');
  var links = document.getElementById('nav-links');

  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      links.classList.toggle('is-open', !open);
    });

    links.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        toggle.setAttribute('aria-expanded', 'false');
        links.classList.remove('is-open');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && links.classList.contains('is-open')) {
        toggle.setAttribute('aria-expanded', 'false');
        links.classList.remove('is-open');
        toggle.focus();
      }
    });
  }

  /* ---------- accordions (curriculum + FAQ) ----------------------------- */
  document.querySelectorAll('.acc__btn').forEach(function (btn) {
    var panel = document.getElementById(btn.getAttribute('aria-controls'));
    if (!panel) return;

    // Sync the initial CSS state with the authored aria-expanded value.
    panel.classList.toggle('is-open', btn.getAttribute('aria-expanded') === 'true');

    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      panel.classList.toggle('is-open', !open);
    });
  });

  /* ---------- scroll reveal --------------------------------------------- */
  var revealables = document.querySelectorAll('.reveal');

  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });

    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ---------- hero terminal --------------------------------------------
     The <pre> is aria-hidden; the full transcript is on the container's
     aria-label, so assistive tech gets the content without the animation.
  ---------------------------------------------------------------------- */
  var code = document.getElementById('term-code');
  var caret = document.getElementById('term-caret');

  if (code) {
    var LINES = [
      { html: '<span class="d">$</span> <span class="u">claude</span>' },
      { html: '' },
      { html: '<span class="p">&gt;</span> ', type: 'refactor the checkout flow onto the new' },
      { html: '  ', type: 'PaymentIntent API and update the tests' },
      { html: '' },
      { html: '<span class="k">●</span> Reading <span class="u">src/checkout/</span>…   <span class="d">12 files</span>' },
      { html: '<span class="k">●</span> Editing <span class="u">session.ts</span>       <span class="d">+48 −31</span>' },
      { html: '<span class="k">●</span> Running <span class="u">npm test</span>         <span class="d">24 passed</span>' },
      { html: '' },
      { html: '<span class="u">Done. Want me to open a PR?</span>' }
    ];

    var finalHtml = LINES.map(function (l) {
      return l.html + (l.type ? '<span class="u">' + l.type + '</span>' : '');
    }).join('\n');

    if (reduceMotion) {
      code.innerHTML = finalHtml;
    } else {
      playTerminal(LINES, code, caret);
    }
  }

  function playTerminal(lines, target, caretEl) {
    var out = '';
    var i = 0;

    function nextLine() {
      if (i >= lines.length) {
        if (caretEl) caretEl.style.opacity = '.35';
        return;
      }

      var line = lines[i];
      out += (i ? '\n' : '') + line.html;
      target.innerHTML = out;

      if (!line.type) {
        i++;
        setTimeout(nextLine, line.html === '' ? 120 : 260);
        return;
      }

      typeText(line.type, function () {
        i++;
        setTimeout(nextLine, 340);
      });
    }

    function typeText(text, done) {
      var n = 0;
      var base = out;
      (function step() {
        n++;
        target.innerHTML = base + '<span class="u">' + text.slice(0, n) + '</span>';
        if (n < text.length) {
          setTimeout(step, 16 + Math.random() * 26);
        } else {
          out = base + '<span class="u">' + text + '</span>';
          done();
        }
      })();
    }

    // Only start once the terminal is actually on screen.
    var term = target.closest('.term');
    if (term && 'IntersectionObserver' in window) {
      var seen = false;
      var termIo = new IntersectionObserver(function (entries) {
        if (entries[0].isIntersecting && !seen) {
          seen = true;
          termIo.disconnect();
          setTimeout(nextLine, 400);
        }
      }, { threshold: 0.25 });
      termIo.observe(term);
    } else {
      setTimeout(nextLine, 400);
    }
  }
})();
