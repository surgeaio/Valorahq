# -*- coding: utf-8 -*-
"""Shared markup for every Valora page: <head>, header, footer, lead forms.

index.html keeps its own hand-written sections, but its header, footer,
client forms and modal live between <!-- @build:NAME --> markers and are
rewritten from here, so every page stays identical.
"""
from html import escape

BRAND = "Valora"
EMAIL = "barot@valorahq.com"
PHONE_DISPLAY = "+1 (415) 909-4100"
PHONE_TEL = "+14159094100"

# the original "What are you solving for?" options
GOAL_OPTIONS = ["Retirement income", "Equity compensation", "Selling a business",
                "Estate & legacy", "A second opinion"]

LOGO_SVG = ('<svg viewBox="0 0 32 32" fill="none"><circle cx="16" cy="16" r="15" stroke="currentColor" '
            'stroke-width="1.4"/><path d="M6 20.5c4-9 6.5-9 10 0s6 9 10 0" stroke="currentColor" '
            'stroke-width="1.4" stroke-linecap="round"/></svg>')
TICK_SVG = ('<svg viewBox="0 0 32 32" fill="none"><path d="M8 17l5.5 5.5L24 11" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
FAVICON = ("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'>"
           "<rect width='100' height='100' rx='22' fill='%231e3b2a'/><text x='50' y='70' font-size='58' "
           "text-anchor='middle' fill='%23efebe0' font-family='Georgia'>V</text></svg>")


# ------------------------------------------------------------------ head
def head(title, description):
    return f"""<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<link rel="icon" href="{FAVICON}">
</head>"""


# ------------------------------------------------------------------ header / footer
NAV = [
    ("Approach", "/#approach", None),
    ("Find an advisor", "/#advisors", None),
    ("Services", "/#services", None),
    ("For advisors", "/advisors.html", "advisors"),
]


def header(active=None, cta=("Get matched", "/#contact")):
    items = []
    for label, href, key in NAV:
        cur = ' class="is-current" aria-current="page"' if key and key == active else ""
        items.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
    items = "\n".join(items)
    return f"""<header class="site-header" id="siteHeader">
  <div class="container header__inner">
    <a class="logo" href="/" aria-label="{BRAND} home">
      <span class="logo__mark" aria-hidden="true">
        {LOGO_SVG}
      </span>
      <span class="logo__word">{BRAND}</span>
    </a>

    <nav class="nav" id="primaryNav" aria-label="Primary">
      <ul class="nav__list">
{items}
      </ul>
      <div class="nav__cta">
        <a class="btn btn--dark" href="{cta[1]}">{cta[0]}</a>
      </div>
    </nav>

    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="primaryNav" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>"""


def footer():
    return f"""<footer class="footer">
  <div class="container">
    <h2 class="display display--md footer__statement reveal">Independent advice.<br><em>Personal fit.</em></h2>

    <div class="footer__grid">
      <div class="footer__brand">
        <a class="logo logo--light" href="/">
          <span class="logo__mark" aria-hidden="true">{LOGO_SVG}</span>
          <span class="logo__word">{BRAND}</span>
        </a>
        <p>An independent platform helping people discover financial advisors.</p>
        <ul class="footer__contact">
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        </ul>
      </div>

      <nav class="footer__col" aria-label="Company"><h5>Company</h5><ul><li><a href="/#approach">Our approach</a></li><li><a href="/#advisors">Find an advisor</a></li><li><a href="/advisors.html">For advisors</a></li></ul></nav>
      <nav class="footer__col" aria-label="Services"><h5>Services</h5><ul><li><a href="/#services">Financial planning</a></li><li><a href="/#services">Investments</a></li><li><a href="/#services">Tax strategy</a></li><li><a href="/#services">Estate &amp; legacy</a></li></ul></nav>
      <nav class="footer__col" aria-label="Legal"><h5>Legal</h5><ul><li><a href="/#top">Form ADV</a></li><li><a href="/#top">Privacy</a></li><li><a href="/#top">Terms</a></li><li><a href="/#top">Disclosures</a></li></ul></nav>
    </div>

    <div class="footer__base">
      <p>© <span id="year">2026</span> {BRAND}. Financial advisory services are provided independently by the advisors you choose to contact. {BRAND} does not provide investment advice.</p>
      <p>This site is for informational purposes and is not investment advice.</p>
    </div>
  </div>
</footer>

<button class="to-top" id="toTop" aria-label="Back to top"><span aria-hidden="true">↑</span></button>"""


# ------------------------------------------------------------------ client lead forms (original fields)
def _goal_select(uid):
    opts = '<option value="">Select one</option>' + "".join(f"<option>{escape(o)}</option>" for o in GOAL_OPTIONS)
    return f'<select id="{uid}goal" name="goal" required>{opts}</select>'


def client_fields(kind, uid, with_note=False):
    """kind: 'hero' | 'gate' | 'page' — name, email, phone, what are you solving for (+ note on page form)."""
    wrap = {"hero": "hfield", "gate": "gate__field", "page": "field"}[kind]
    out = f"""
        <div class="{wrap}" data-field>
          <label for="{uid}name">Full name</label>
          <input id="{uid}name" name="name" type="text" required placeholder="Jordan Reyes" autocomplete="name">
          <small class="err" data-err="name"></small>
        </div>
        <div class="{wrap}" data-field>
          <label for="{uid}email">Email</label>
          <input id="{uid}email" name="email" type="email" required placeholder="jordan@email.com" autocomplete="email">
          <small class="err" data-err="email"></small>
        </div>
        <div class="{wrap}" data-field>
          <label for="{uid}phone">Phone number</label>
          <input id="{uid}phone" name="phone" type="tel" required placeholder="+1 (415) 909-4100" autocomplete="tel" inputmode="tel">
          <small class="err" data-err="phone"></small>
        </div>
        <div class="{wrap}" data-field>
          <label for="{uid}goal">What are you solving for?</label>
          {_goal_select(uid)}
          <small class="err" data-err="goal"></small>
        </div>"""
    if with_note:
        out += f"""
        <div class="{wrap} field--full" data-field>
          <label for="{uid}note">Anything we should know?</label>
          <textarea id="{uid}note" name="note" rows="3" placeholder="A sentence is plenty."></textarea>
        </div>"""
    return out


def hero_card():
    return f"""<aside class="hcard reveal reveal--right">
      <span class="hcard__edge" aria-hidden="true"></span>
      <p class="hcard__eyebrow">Free · No obligation</p>
      <h2 class="hcard__title">Explore financial advisors<br><em>who may fit your needs.</em></h2>

      <form class="hcard__form" id="heroForm" data-lead="Client" data-done="#heroDone" novalidate>{client_fields("hero", "h")}

        <button class="btn btn--cream hcard__submit" type="submit">Explore advisors</button>
        <p class="hcard__fine">No cost, no obligation. We never sell your information.</p>
      </form>

      <div class="hcard__done" id="heroDone" hidden>
        <span class="hcard__tick" aria-hidden="true">
          {TICK_SVG}
        </span>
        <h3 data-done-title>Thank you.</h3>
        <p>We'll follow up within two business days with advisors who may fit what you're looking for.</p>
      </div>
    </aside>"""


def page_form(goal=None):
    return f"""<form class="form reveal" id="matchForm" data-lead="Client" data-success="Thank you, {{name}} — we'll follow up within two business days with advisors who may fit what you're looking for." novalidate>{client_fields("page", "f", with_note=True)}
      <div class="field field--full form__foot">
        <button class="btn btn--cream" type="submit">Explore advisors</button>
        <p class="form__fine">No cost, no obligation. We never sell your information.</p>
      </div>
      <p class="form__success" role="status" hidden></p>
    </form>"""


def contact_section(goal=None, title='Let\'s build a<br>financial life<br><em>that feels like yours.</em>'):
    form = page_form()
    if goal:  # preselect the matching "solving for" option on specialty pages
        form = form.replace(f"<option>{escape(goal)}</option>", f"<option selected>{escape(goal)}</option>", 1)
    return f"""<section class="section section--green cta" id="contact">
  <div class="container cta__grid">
    <div class="cta__copy">
      <h2 class="display display--lg reveal">{title}</h2>
      <p class="reveal">Answer a few questions and explore advisors who may fit what you're looking for.</p>

      <ul class="direct reveal">
        <li>
          <span class="direct__label">Email</span>
          <a class="direct__link" href="mailto:{EMAIL}">{EMAIL}</a>
        </li>
        <li>
          <span class="direct__label">Phone</span>
          <a class="direct__link" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        </li>
      </ul>
      <p class="direct__note reveal">Prefer to skip the form? Call or write to us directly — we answer every message ourselves.</p>
    </div>

    {form}
  </div>
</section>"""


def gate():
    return f"""<div class="gate" id="gate" hidden>
  <div class="gate__scrim" data-gate-close></div>

  <div class="gate__panel" role="dialog" aria-modal="true" aria-labelledby="gateTitle" aria-describedby="gateSub">
    <span class="gate__glow" aria-hidden="true"></span>

    <button class="gate__x" type="button" aria-label="Close" data-gate-close>
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
    </button>

    <div class="gate__inner">
      <p class="gate__eyebrow gate__i" style="--i:1">Free · No obligation</p>
      <h2 class="gate__title display gate__i" id="gateTitle" style="--i:2">
        Explore advisors<br><em>who may fit your needs.</em>
      </h2>
      <p class="gate__sub gate__i" id="gateSub" style="--i:3">
        Answer a few questions and explore advisors who may fit what you're looking for.
      </p>

      <form class="gate__form gate__i" id="gateForm" data-lead="Client" data-done="#gateDone" style="--i:4" novalidate>{client_fields("gate", "g")}

        <div class="gate__foot">
          <button class="btn btn--cream gate__submit" type="submit">Explore advisors</button>
          <button class="gate__skip" type="button" data-gate-close>I'm just looking</button>
        </div>
        <p class="gate__fine">No cost, no obligation. We never sell your information.</p>
      </form>

      <div class="gate__done" id="gateDone" hidden>
        <span class="gate__tick" aria-hidden="true">
          {TICK_SVG}
        </span>
        <h3 class="display" data-done-title style="font-size:1.5rem">Thank you.</h3>
        <p>We'll follow up within two business days with advisors who may fit what you're looking for.</p>
        <button class="btn btn--cream" type="button" data-gate-close>Explore the site</button>
      </div>
    </div>
  </div>
</div>"""


def faq_block(faq, heading="Common questions"):
    items = "\n".join(
        f'      <details class="faq__item"><summary>{escape(q)}</summary><p>{escape(a)}</p></details>'
        for q, a in faq
    )
    return f"""<div class="faq">
      <h2 class="faq__title">{heading}</h2>
{items}
    </div>"""


def page(head_html, body_html, active=None, with_gate=False, body_class="page-sub"):
    return f"""<!DOCTYPE html>
<html lang="en">
{head_html}
<body class="{body_class}">

<a class="skip-link" href="#main">Skip to content</a>

{header(active)}

<main id="main">
{body_html}
</main>

{footer()}
{gate() if with_gate else ''}
<script src="/script.js"></script>
</body>
</html>
"""
