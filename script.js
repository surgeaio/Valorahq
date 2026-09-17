/* =========================================================
   valorahq — interaction + animation layer
   Vanilla JS, no dependencies.
   ========================================================= */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------
     1. Page load curtain
     --------------------------------------------------------- */
  function curtain() {
    if (reduced) return;
    var el = document.createElement('div');
    el.className = 'curtain';
    el.innerHTML = '<span class="curtain__word">valorahq</span>';
    document.body.appendChild(el);
    document.documentElement.style.overflow = 'hidden';

    window.setTimeout(function () {
      el.classList.add('is-gone');
      document.documentElement.style.overflow = '';
      window.setTimeout(function () { el.remove(); }, 1200);
    }, 1100);
  }

  /* ---------------------------------------------------------
     2. Split headlines into animatable lines (keeps inline tags)
     --------------------------------------------------------- */
  function splitByBr(node) {
    var lines = [document.createDocumentFragment()];

    Array.prototype.forEach.call(node.childNodes, function (child) {
      if (child.nodeName === 'BR') { lines.push(document.createDocumentFragment()); return; }

      if (child.nodeType === 1 && child.querySelector('br')) {
        var parts = splitByBr(child);
        parts.forEach(function (frag, i) {
          var shell = child.cloneNode(false);
          shell.appendChild(frag);
          if (i > 0) lines.push(document.createDocumentFragment());
          lines[lines.length - 1].appendChild(shell);
        });
        return;
      }
      lines[lines.length - 1].appendChild(child.cloneNode(true));
    });
    return lines;
  }

  function prepareHeadlines() {
    $$('.display, .hero__title').forEach(function (h) {
      if (!h.querySelector('br')) return;

      var lines = splitByBr(h).filter(function (f) {
        return (f.textContent || '').trim().length > 0;
      });
      if (lines.length < 2) return;

      h.innerHTML = '';
      lines.forEach(function (frag, i) {
        var wrap  = document.createElement('span');
        var inner = document.createElement('span');
        wrap.className = 'line-wrap';
        inner.className = 'line-inner';
        inner.style.setProperty('--d', (i * 0.09).toFixed(2) + 's');
        inner.appendChild(frag);
        wrap.appendChild(inner);
        h.appendChild(wrap);
      });
      h.classList.add('line-reveal');
    });
  }

  /* ---------------------------------------------------------
     3. Reveal on scroll (with per-container stagger)
     --------------------------------------------------------- */
  function reveals() {
    var targets = $$('.reveal, .line-reveal, .diagram, .mock');

    // stagger siblings inside grids/lists
    ['.statement__cols', '.steps', '.mosaic', '.blist', '.insights__grid', '.post-list', '.brand__mocks', '.match__grid']
      .forEach(function (sel) {
        $$(sel).forEach(function (group) {
          $$(':scope > *', group).forEach(function (child, i) {
            child.style.setProperty('--d', (i * 0.08).toFixed(2) + 's');
          });
        });
      });

    if (!('IntersectionObserver' in window) || reduced) {
      targets.forEach(function (t) { t.classList.add('is-in'); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        // reveal when entering, or when it was skipped past during a fast scroll
        var passed = !e.isIntersecting && e.boundingClientRect.top < 0;
        if (!e.isIntersecting && !passed) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

    targets.forEach(function (t) { io.observe(t); });

    // Backstop: a very fast scroll (or an anchor jump) can move an element from
    // below the viewport to above it between observer samples, so no entry ever
    // fires and the content would stay invisible. Sweep the remainder on scroll.
    var pending = targets.slice();
    var queued = false;

    function sweep() {
      var limit = window.innerHeight * 0.92;
      pending = pending.filter(function (el) {
        if (el.classList.contains('is-in')) return false;
        if (el.getBoundingClientRect().top > limit) return true;
        el.classList.add('is-in');
        io.unobserve(el);
        return false;
      });
      queued = false;
      if (!pending.length) {
        window.removeEventListener('scroll', onScroll);
        window.removeEventListener('resize', sweep);
      }
    }

    function onScroll() {
      if (queued) return;
      queued = true;
      window.requestAnimationFrame(sweep);
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', sweep);
  }

  /* ---------------------------------------------------------
     4. Header: shrink, auto-hide, scroll progress
     --------------------------------------------------------- */
  function header() {
    var head = $('#siteHeader');
    var bar  = document.createElement('div');
    bar.className = 'scroll-progress';
    head.appendChild(bar);

    var last = 0;
    var toTop = $('#toTop');

    function onScroll() {
      var y   = window.scrollY || document.documentElement.scrollTop;
      var max = document.documentElement.scrollHeight - window.innerHeight;
      var p   = max > 0 ? y / max : 0;

      bar.style.transform = 'scaleX(' + p.toFixed(4) + ')';
      head.classList.toggle('is-stuck', y > 20);

      // hide on scroll down, reveal on scroll up (not while menu is open)
      if (!$('#primaryNav').classList.contains('is-open')) {
        head.classList.toggle('is-hidden', y > last && y > 320);
      }
      last = y;

      toTop.classList.toggle('is-on', y > 700);
      toTop.style.setProperty('--p', (p * 100).toFixed(1));
    }

    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------------------------------------------------------
     5. Mobile navigation
     --------------------------------------------------------- */
  function nav() {
    var btn = $('#navToggle');
    var menu = $('#primaryNav');
    if (!btn) return;

    function close() {
      menu.classList.remove('is-open');
      btn.classList.remove('is-open');
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-label', 'Open menu');
    }

    btn.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      btn.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      if (open) $('#siteHeader').classList.remove('is-hidden');
    });

    $$('#primaryNav a').forEach(function (a) { a.addEventListener('click', close); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    window.addEventListener('resize', function () { if (window.innerWidth > 900) close(); });
  }

  /* ---------------------------------------------------------
     6. Parallax (hero image, chapter image, mosaic drift)
     --------------------------------------------------------- */
  function parallax() {
    if (reduced) return;

    var items = [
      { el: $('.chapter > img'),   speed: 0.12, scale: 1.14 },
      { el: $('.life__media img'), speed: 0.06, scale: 1.10 },
      { el: $('.mos--e img'),      speed: 0.05, scale: 1.08 }
    ].filter(function (i) { return !!i.el; });

    if (!items.length) return;
    var ticking = false;

    // let the load-in settle before parallax takes over a transform
    window.setTimeout(function () {
      items.forEach(function (i) { i.hold = false; });
    }, 2700);

    function run() {
      var vh = window.innerHeight;
      items.forEach(function (item) {
        if (item.hold) return;
        var host = item.el.closest('section') || item.el.parentElement;
        var r = host.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var mid = r.top + r.height / 2 - vh / 2;
        var shift = (-mid * item.speed).toFixed(2);
        item.el.style.transform = 'translate3d(0,' + shift + 'px,0) scale(' + item.scale + ')';
      });
      ticking = false;
    }

    window.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(run);
    }, { passive: true });

    window.addEventListener('resize', run);
    run();
  }

  /* ---------------------------------------------------------
     7. Animated stat counters
     --------------------------------------------------------- */
  function counters() {
    var nums = $$('.stat__num[data-count]');
    if (!nums.length) return;

    function format(n, el) {
      var v = Math.round(n);
      var out = v >= 1000 ? v.toLocaleString('en-US') : String(v);
      return (el.dataset.prefix || '') + out + (el.dataset.suffix || '');
    }

    function run(el) {
      var target = parseFloat(el.dataset.count);
      if (reduced) { el.textContent = format(target, el); return; }

      var dur = 1600, t0 = performance.now();
      el.classList.add('is-counting');

      (function step(now) {
        var p = Math.min((now - t0) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = format(target * eased, el);
        if (p < 1) requestAnimationFrame(step);
        else el.classList.remove('is-counting');
      })(t0);
    }

    if (!('IntersectionObserver' in window)) { nums.forEach(run); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        run(e.target);
        io.unobserve(e.target);
      });
    }, { threshold: 0.4 });
    nums.forEach(function (n) { io.observe(n); });
  }

  /* ---------------------------------------------------------
     8. Accordion
     --------------------------------------------------------- */
  function accordion() {
    var root = $('#accordion');
    if (!root) return;
    var items = $$('.acc__item', root);

    function setHeight(item, open) {
      var panel = $('.acc__panel', item);
      panel.style.height = open ? panel.scrollHeight + 'px' : '0px';
    }

    items.forEach(function (item) {
      setHeight(item, item.classList.contains('is-open'));

      $('.acc__head', item).addEventListener('click', function () {
        var willOpen = !item.classList.contains('is-open');

        items.forEach(function (other) {
          other.classList.remove('is-open');
          $('.acc__head', other).setAttribute('aria-expanded', 'false');
          setHeight(other, false);
        });

        if (willOpen) {
          item.classList.add('is-open');
          $('.acc__head', item).setAttribute('aria-expanded', 'true');
          setHeight(item, true);
        }
      });
    });

    window.addEventListener('resize', function () {
      items.forEach(function (i) { setHeight(i, i.classList.contains('is-open')); });
    });
  }

  /* ---------------------------------------------------------
     9. Advisor filter + search
     --------------------------------------------------------- */
  function advisors() {
    var grid = $('#advisorGrid');
    if (!grid) return;

    var cards = $$('.acard', grid);
    var chips = $$('.chip');
    var input = $('#advisorSearch');
    var empty = $('#matchEmpty');
    var filter = 'all';

    function apply() {
      var q = input ? (input.value || '').trim().toLowerCase() : '';
      var shown = 0;

      cards.forEach(function (card, i) {
        var tags = card.dataset.tags || '';
        var hay  = ((card.dataset.name || '') + ' ' + tags + ' ' + card.textContent).toLowerCase();
        var ok   = (filter === 'all' || tags.indexOf(filter) > -1) && (!q || hay.indexOf(q) > -1);

        card.classList.toggle('is-hidden', !ok);
        if (ok) {
          shown++;
          // restart the entry animation
          card.style.animation = 'none';
          void card.offsetWidth;
          card.style.animation = '';
          card.style.animationDelay = (i * 0.06).toFixed(2) + 's';
        }
      });

      empty.hidden = shown > 0;
    }

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (c) {
          c.classList.remove('is-active');
          c.setAttribute('aria-selected', 'false');
        });
        chip.classList.add('is-active');
        chip.setAttribute('aria-selected', 'true');
        filter = chip.dataset.filter;
        apply();
      });
    });

    if (input) {
      var t;
      input.addEventListener('input', function () {
        clearTimeout(t);
        t = setTimeout(apply, 140);
      });
    }
  }

  /* ---------------------------------------------------------
     10. Services switcher (click + keyboard + autoplay)
     --------------------------------------------------------- */
  function services() {
    var list = $('#serviceList');
    if (!list) return;

    var btns   = $$('.slist__btn', list);
    var panels = $$('.spanel');
    var timer;
    var idle = true;

    function show(id) {
      btns.forEach(function (b) { b.classList.toggle('is-active', b.dataset.service === id); });
      panels.forEach(function (p) { p.classList.toggle('is-active', p.dataset.panel === id); });
    }

    btns.forEach(function (b) {
      b.addEventListener('click', function () { idle = false; show(b.dataset.service); });
      b.addEventListener('mouseenter', function () { if (idle) show(b.dataset.service); });
      b.addEventListener('focus', function () { show(b.dataset.service); });
    });

    // gentle autoplay until the visitor interacts
    if (reduced) return;
    var i = 0;
    timer = setInterval(function () {
      if (!idle) { clearInterval(timer); return; }
      i = (i + 1) % btns.length;
      show(btns[i].dataset.service);
    }, 4200);

    list.addEventListener('pointerdown', function () { idle = false; });
  }

  /* ---------------------------------------------------------
     11. Magnetic buttons
     --------------------------------------------------------- */
  function magnetic() {
    if (reduced || !window.matchMedia('(pointer:fine)').matches) return;

    $$('.btn').forEach(function (btn) {
      btn.classList.add('btn--magnetic');

      btn.addEventListener('mousemove', function (e) {
        var r = btn.getBoundingClientRect();
        var x = (e.clientX - r.left - r.width / 2) * 0.22;
        var y = (e.clientY - r.top - r.height / 2) * 0.32;
        btn.style.transform = 'translate(' + x.toFixed(1) + 'px,' + y.toFixed(1) + 'px)';
      });

      btn.addEventListener('mouseleave', function () { btn.style.transform = ''; });
    });
  }

  /* ---------------------------------------------------------
     12. Form validation
     --------------------------------------------------------- */
  var SHEET_ENDPOINT = 'https://script.google.com/macros/s/AKfycbzCcuopJyN1MVXsCEjJMBm0T9qXnR4zXHZwtCplq0gmqR6_ap2uuYjiWVCiOHqG70Td/exec';

  /* shared lead helpers (used by the hero card, the page form and the modal) */
  var LEAD_FIELDS = ['name', 'email', 'phone', 'goal'];
  var LEAD_FAIL   = 'Sorry \u2014 we could not send that. Please email barot@valorahq.com.';

  function setLeadError(f, fieldSel, name, msg) {
    var slot  = $('[data-err="' + name + '"]', f);
    var field = f.elements[name].closest(fieldSel);
    if (slot) slot.textContent = msg || '';
    if (field) field.classList.toggle('has-error', !!msg);
  }

  function validateLead(f, fieldSel) {
    var v = {
      name:  f.elements.name.value.trim(),
      email: f.elements.email.value.trim(),
      phone: f.elements.phone.value.trim(),
      goal:  f.elements.goal.value,
      note:  f.elements.note ? f.elements.note.value.trim() : ''
    };
    var msgs = {
      name:  v.name.length < 2 ? 'Please enter your name.' : '',
      email: !/^[^\s@]+@[^\s@]+\.[a-z]{2,}$/i.test(v.email) ? 'Please enter a valid email.' : '',
      phone: v.phone.replace(/\D/g, '').length < 7 ? 'Please enter a valid phone number.' : '',
      goal:  !v.goal ? 'Pick the closest match.' : ''
    };

    var ok = true;
    LEAD_FIELDS.forEach(function (n) {
      if (msgs[n]) ok = false;
      setLeadError(f, fieldSel, n, msgs[n]);
    });

    if (!ok) {
      var bad = $('.has-error input, .has-error select', f);
      if (bad) bad.focus();
      return null;
    }
    return v;
  }

  /* clear a field's error as soon as the visitor edits it */
  function watchLeadFields(f, fieldSel) {
    LEAD_FIELDS.forEach(function (n) {
      var el = f.elements[n];
      if (!el) return;
      ['input', 'change'].forEach(function (ev) {
        el.addEventListener(ev, function () { setLeadError(f, fieldSel, n, ''); });
      });
    });
  }

  function sendLead(v) {
    if (!/^https:\/\//.test(SHEET_ENDPOINT)) {
      return Promise.resolve({ status: 'success', skipped: true });
    }
    return fetch(SHEET_ENDPOINT, { method: 'POST', body: new URLSearchParams(v) })
      .then(function (r) { return r.json().catch(function () { return { status: 'success' }; }); });
  }

  function form() {
    var f = $('#matchForm');
    if (!f) return;
    var ok  = $('#formSuccess');
    var btn = $('button[type="submit"]', f);

    watchLeadFields(f, '.field');

    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = validateLead(f, '.field');
      if (!v) return;

      function done(msg) {
        if (btn) { btn.disabled = false; btn.textContent = 'Request introductions'; }
        ok.hidden = false;
        ok.textContent = msg;
        ok.scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'center' });
      }

      if (btn) { btn.disabled = true; btn.textContent = 'Sending\u2026'; }

      sendLead(v)
        .then(function (res) {
          if (res && res.status === 'error') { done(LEAD_FAIL); return; }
          f.reset();
          done('Thank you, ' + v.name.split(' ')[0] + ' \u2014 we will send three introductions within two business days.');
        })
        .catch(function () { done(LEAD_FAIL); });
    });
  }

  /* ---------------------------------------------------------
     12b. Hero lead card
     --------------------------------------------------------- */
  function heroLead() {
    var f = $('#heroForm');
    if (!f) return;
    var card = f.closest('.hcard');
    var done = $('#heroDone', card);
    var fine = $('.hcard__fine', card);
    var btn  = $('.hcard__submit', f);
    var fineText = fine ? fine.textContent : '';

    watchLeadFields(f, '.hfield');

    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = validateLead(f, '.hfield');
      if (!v) return;

      function fail() {
        btn.disabled = false;
        btn.textContent = 'Request introductions';
        if (fine) { fine.textContent = LEAD_FAIL; fine.classList.add('is-error'); }
      }

      btn.disabled = true;
      btn.textContent = 'Sending\u2026';
      if (fine) { fine.textContent = fineText; fine.classList.remove('is-error'); }

      sendLead(v)
        .then(function (res) {
          if (res && res.status === 'error') { fail(); return; }
          card.classList.add('is-done');
          f.hidden = true;
          done.hidden = false;
          var t = $('#heroDoneTitle', done);
          if (t) t.textContent = 'Thank you, ' + v.name.split(' ')[0] + '.';
        })
        .catch(fail);
    });
  }

  /* ---------------------------------------------------------
     13. Active nav link while scrolling
     --------------------------------------------------------- */
  function activeLink() {
    var sections = $$('main section[id]');
    var links = {};
    $$('.nav__list a').forEach(function (a) { links[a.getAttribute('href')] = a; });
    if (!sections.length || !('IntersectionObserver' in window)) return;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var a = links['#' + e.target.id];
        if (!a) return;
        if (e.isIntersecting) {
          Object.keys(links).forEach(function (k) { links[k].style.color = ''; });
          a.style.color = 'var(--green)';
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });

    sections.forEach(function (s) { io.observe(s); });
  }

  /* ---------------------------------------------------------
     14. Misc: image fallback, back to top, year
     --------------------------------------------------------- */
  function misc() {
    $$('img').forEach(function (img) {
      img.addEventListener('error', function () {
        img.classList.add('img-fallback');
        img.removeAttribute('src');
      });
    });

    var top = $('#toTop');
    if (top) {
      top.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
      });
    }

    var year = $('#year');
    if (year) year.textContent = new Date().getFullYear();

    var hero = $('.hero');
    if (hero) requestAnimationFrame(function () { hero.classList.add('is-ready'); });
  }

  /* ---------------------------------------------------------
     15. Opening modal (name / email / phone / solving for)
     --------------------------------------------------------- */
  function gate() {
    var g = $('#gate');
    if (!g) return;

    var f      = $('#gateForm', g);
    var done   = $('#gateDone', g);
    var fine   = $('.gate__fine', g);
    var submit = $('.gate__submit', g);
    var fineText = fine ? fine.textContent : '';
    var closing;

    function open() {
      g.hidden = false;
      document.body.classList.add('gate-open');
      requestAnimationFrame(function () {
        g.classList.add('is-open');
        var first = f.elements.name;
        if (first && window.innerWidth > 620) {
          setTimeout(function () { first.focus({ preventScroll: true }); }, 620);
        }
      });
      document.addEventListener('keydown', onKey);
    }

    function close() {
      if (closing) return;
      closing = true;
      g.classList.remove('is-open');
      document.removeEventListener('keydown', onKey);
      document.body.classList.remove('gate-open');
      setTimeout(function () { g.hidden = true; }, reduced ? 0 : 600);
    }

    function onKey(e) {
      if (e.key === 'Escape') close();
    }

    $$('[data-gate-close]', g).forEach(function (el) {
      el.addEventListener('click', close);
    });

    watchLeadFields(f, '.gate__field');

    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = validateLead(f, '.gate__field');
      if (!v) return;

      function showError() {
        submit.disabled = false;
        submit.textContent = 'Request introductions';
        if (fine) { fine.textContent = LEAD_FAIL; fine.style.color = '#e3a493'; }
      }

      submit.disabled = true;
      submit.textContent = 'Sending\u2026';
      if (fine) { fine.textContent = fineText; fine.style.color = ''; }

      sendLead(v)
        .then(function (res) {
          if (res && res.status === 'error') { showError(); return; }
          f.hidden = true;
          done.hidden = false;
          g.classList.add('is-done');
          var t = $('#gateDoneTitle', done);
          if (t) t.textContent = 'Thank you, ' + v.name.split(' ')[0] + '.';
        })
        .catch(showError);
    });

    setTimeout(open, reduced ? 350 : 1900);
  }

  /* ---------------------------------------------------------
     boot
     --------------------------------------------------------- */
  function init() {
    curtain();
    prepareHeadlines();
    reveals();
    header();
    nav();
    parallax();
    counters();
    accordion();
    advisors();
    services();
    magnetic();
    form();
    heroLead();
    gate();
    activeLink();
    misc();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
