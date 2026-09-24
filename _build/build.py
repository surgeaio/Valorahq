# -*- coding: utf-8 -*-
"""Build Valora's static pages.

    python _build/build.py

Writes:
  /advisors.html                 "For advisors" page
and refreshes the <!-- @build:... --> regions in index.html
(head, header, hero card, contact form, footer, opening modal).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from partials import BRAND, head, page, header, footer, gate, hero_card, contact_section
from advisors_page import for_advisors_body

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write(path, html):
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path.endswith("/") else os.path.join(ROOT, path.strip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


def build_for_advisors():
    html = page(head(f"For Advisors | {BRAND} — Practice Growth & Infrastructure Platform",
                     "Valora for independent financial advisors: verified fiduciary introductions to prospective clients, "
                     "turnkey digital onboarding, tax-intelligent rebalancing, and a practice that stays 100% yours."),
                for_advisors_body(), active="advisors")
    html = html.replace('<a class="btn btn--dark" href="/#contact">Get matched</a>',
                        '<a class="btn btn--dark" href="#apply">Apply to join</a>', 1)
    write("/advisors.html", html)


# ====================================================================== index.html regions
def refresh_index():
    p = os.path.join(ROOT, "index.html")
    with open(p, encoding="utf-8") as f:
        html = f.read()
    regions = {
        "head": head(f"{BRAND} — Your money has a purpose",
                     "Explore independent financial advisors. Valora helps you find advisors who work with "
                     "situations like yours — you decide who you'd like to contact."),
        "header": header(None),
        "hero-card": hero_card(),
        "contact": contact_section(),
        "footer": footer(),
        "gate": gate(),
    }
    for name, content in regions.items():
        pat = re.compile(r"(<!-- @build:%s -->)(.*?)(<!-- /@build:%s -->)" % (re.escape(name), re.escape(name)), re.S)
        if not pat.search(html):
            raise SystemExit(f"index.html is missing the @build:{name} markers")
        html = pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(3), html)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


if __name__ == "__main__":
    build_for_advisors()
    refresh_index()
    print("built /advisors.html + refreshed index.html regions")
