# -*- coding: utf-8 -*-
"""advisors_page.py — The comprehensive "For Advisors" page for Valora."""
from partials import EMAIL, PHONE_DISPLAY, PHONE_TEL, TICK_SVG

ADVISOR_GOALS = [
    "Client introductions & growth",
    "Turnkey platform & back office",
    "Breakaway transition from broker-dealer",
    "Full RIA infrastructure partnership",
]

FOR_ADVISORS_FAQ = [
    ("How does Valora match advisors with prospective clients?",
     "Valora matches consumers based on what they are specifically solving for (e.g. retirement decumulation, tech equity/RSUs, business sale, generational wealth transfer), their investable asset tier, and the advisor's verified niche expertise and geographic preference. Consumers review advisor profiles and actively choose to connect — these are qualified, intentional introductions, not cold leads."),
    ("Are client introductions exclusive to my firm?",
     "Yes, 100% exclusive. Unlike lead brokers who auction the same contact information to five or six competing advisors, Valora introduces each prospective client exclusively to one fiduciary advisor at a time based on mutual fit and stated preference."),
    ("Who owns the client relationship, data, and Form ADV?",
     "You do, completely. Clients engage your firm directly under your own advisory agreements, your published fee schedule, and your Form ADV Part 2. Valora does not provide investment advice or intermediate your advisory sovereignty. If you ever leave, your clients, data, and book stay entirely yours."),
    ("Which custodians and technology partners does Valora support?",
     "Valora is built to integrate with major institutional custodians including Charles Schwab Institutional, Fidelity Institutional, BNY Mellon Pershing, and Apex Clearing. Our platform also bridges with standard industry planning and CRM tools like eMoney, RightCapital, Orion, Black Diamond, and Wealthbox."),
    ("What context do I receive before the first consultation?",
     "Every introduction arrives with verified investable assets, primary financial objectives, timeline urgency, employer stock or business details (if applicable), and any specific questions the prospective client shared during our intake process."),
    ("What is the fee or economic model for partner advisors?",
     "Valora operates with transparent, advisor-friendly economics aligned with your growth. We offer flexible plans depending on whether your firm seeks client introductions, our complete back-office operational suite, or both. We discuss specific tiers and territory availability during your 15-minute introductory call."),
    ("How does the onboarding and transition process work for breakaway advisors?",
     "Our dedicated Breakaway Concierge team handles end-to-end transition logistics: ACATS custodial account transfer tracking, bulk paperless client repapering, compliant client communications, and tech stack configuration — typically completing full book transitions in under 14 business days with zero client interruption."),
]


def _goal_opts():
    return '<option value="">Select your primary goal</option>' + "".join(f"<option>{g}</option>" for g in ADVISOR_GOALS)


def _faq_accordion():
    items = []
    for q, a in FOR_ADVISORS_FAQ:
        items.append(f'<details class="faq__item"><summary>{q}</summary><p>{a}</p></details>')
    return "\n".join(items)


def for_advisors_body():
    faq_html = _faq_accordion()
    return f"""
<!-- ================= HERO ================= -->
<section class="hero hero--sub" id="top">
  <div class="hero__grid" aria-hidden="true">
    <span class="hero__cell hero__cell--gold"></span>
    <span class="hero__cell hero__cell--wide"></span>
    <span class="hero__cell hero__cell--ring"></span>
    <span class="hero__cell hero__cell--green"></span>
  </div>

  <div class="container hero__inner">
    <div class="hero__copy">
      <p class="eyebrow reveal">⭐ Vetted Fiduciary Network · SEC &amp; State Registered Advisors</p>
      <h1 class="hero__title reveal">
        Scale your practice.<br>
        Protect your independence.<br>
        <em>Deliver advice that<br>actually moves lives.</em>
      </h1>
      <p class="adv-hero__sub reveal">Valora connects independent wealth advisors with high-intent individuals and business owners seeking fiduciary guidance — backed by turnkey digital onboarding, tax-intelligent rebalancing, automated billing, and compliance. Your clients, your ADV, your brand on the door.</p>
      <div class="hero__actions reveal">
        <a class="btn btn--dark" href="#apply">Apply to join network</a>
        <a class="btn btn--outline" href="#calculator">Model practice growth</a>
      </div>
    </div>
  </div>

  <!-- Animated Metrics Ribbon -->
  <div class="hero__bar">
    <div class="container hero__bar-grid">
      <div class="stat">
        <span class="stat__num" data-count="1.4" data-prefix="$" data-suffix="M+" data-decimals="1">$1.4M+</span>
        <span class="stat__label">Average investable assets per match</span>
      </div>
      <div class="stat">
        <span class="stat__num" data-count="3.2" data-suffix="x" data-decimals="1">3.2x</span>
        <span class="stat__label">Organic AUM growth rate vs. industry avg</span>
      </div>
      <div class="stat">
        <span class="stat__num" data-count="100" data-suffix="%">100%</span>
        <span class="stat__label">Exclusive client matches &amp; book ownership</span>
      </div>
      <div class="stat stat--note">
        <span class="stat__label">Fiduciary RIA network.<br>Limited territory availability per market.</span>
      </div>
    </div>
  </div>
</section>

<!-- ================= CUSTODIAN & TECH ECOSYSTEM STRIP ================= -->
<section class="partner-strip" aria-label="Supported custodians and technology partners">
  <div class="container partner-strip__inner">
    <p class="partner-strip__label">Engineered to integrate seamlessly with your preferred custodians and wealth tech</p>
    <div class="partner-strip__list">
      <span class="partner-pill"><span class="partner-pill__dot"></span>Charles Schwab Institutional</span>
      <span class="partner-pill"><span class="partner-pill__dot"></span>Fidelity Institutional</span>
      <span class="partner-pill"><span class="partner-pill__dot"></span>BNY Mellon Pershing</span>
      <span class="partner-pill"><span class="partner-pill__dot"></span>Apex Clearing</span>
      <span class="partner-pill"><span class="partner-pill__dot"></span>Orion Advisor Tech</span>
      <span class="partner-pill"><span class="partner-pill__dot"></span>Black Diamond</span>
      <span class="partner-pill"><span class="partner-pill__dot"></span>eMoney</span>
      <span class="partner-pill"><span class="partner-pill__dot"></span>RightCapital</span>
      <span class="partner-pill"><span class="partner-pill__dot"></span>Wealthbox</span>
    </div>
  </div>
</section>

<!-- ================= STRATEGIC STATEMENT / WHY ADVISORS JOIN ================= -->
<section class="section section--cream statement" id="why">
  <div class="statement__glow" aria-hidden="true"></div>
  <div class="container">
    <p class="eyebrow statement__eyebrow reveal">Why independent advisors choose Valora</p>
    <span class="statement__mark reveal" aria-hidden="true"></span>

    <div class="statement__head">
      <h2 class="display display--xl">
        Too many advisors spend 70% of the week<br>
        <em>not giving advice.<br>We built Valora to flip that ratio.</em>
      </h2>
    </div>

    <div class="statement__cols">
      <p class="reveal"><span class="statement__lede">The Client Acquisition Dilemma.</span> Traditional referral streams are unpredictable, cold marketing erodes your premium positioning, and legacy lead brokers auction off raw phone numbers to five competing firms at once. Valora delivers 100% exclusive introductions to high-intent individuals and business founders who specifically chose your firm for your credentials and specialty.</p>
      <p class="reveal"><span class="statement__lede">The Operational Friction.</span> Paperwork, repapering, transfer tracking, manual rebalancing, and billing reconciliations are the silent killers of advisory enterprise value. Valora provides the institutional operating leverage of a mega-RIA while preserving 100% of your independence, branding, and equity.</p>
    </div>

    <ul class="statement__proof">
      <li class="reveal">
        <span class="statement__proof-num">01</span>
        <h3>High-Intent Client Matches</h3>
        <p>Pre-screened on liquid investable assets ($500K to $10M+) and immediate financial milestones: business sales, tech equity, retirement, or legacy transfers.</p>
      </li>
      <li class="reveal">
        <span class="statement__proof-num">02</span>
        <h3>Turnkey Operating Leverage</h3>
        <p>Paperless onboarding, multi-custodial trading, automated tax-loss harvesting, billing, and compliance vault unified in one login.</p>
      </li>
      <li class="reveal">
        <span class="statement__proof-num">03</span>
        <h3>Absolute Practice Sovereignty</h3>
        <p>Clients are 100% yours. Your agreements, your published fee schedules, your Form ADV, and your equity on the cap table.</p>
      </li>
    </ul>

    <div class="statement__rule reveal" aria-hidden="true"></div>
  </div>
</section>

<!-- ================= THE INTRODUCTIONS ENGINE ================= -->
<section class="section section--paper platform adv-pipe" id="introductions">
  <div class="container platform__grid">
    <div class="platform__copy">
      <p class="eyebrow reveal">Client Acquisition Engine</p>
      <h2 class="display display--lg reveal">Every introduction arrives with<br><em>the rich context you need.</em></h2>
      <p class="reveal">No cold calls. No mystery inquiries. Before you ever jump on an introductory conversation, you already understand their liquid asset range, specific timeline urgency, and primary financial goal.</p>

      <ul class="adv-ticks reveal">
        <li><strong>100% Exclusive Introductions:</strong> Never shared or shopped to other advisors</li>
        <li><strong>Pre-Qualified Investable Assets:</strong> Minimum thresholds verified before matching</li>
        <li><strong>High-Intent Urgency:</strong> Prospects have actively requested fiduciary guidance</li>
        <li><strong>Direct Calendar Booking:</strong> Integrates with Calendly, Google Calendar, and Outlook</li>
        <li><strong>Full Advisory Discretion:</strong> You review the dossier and decide whether to engage</li>
      </ul>
    </div>

    <!-- Interactive Pipeline Simulator -->
    <div class="adv-mock" id="advisorPipeline">
      <div class="mock reveal" aria-hidden="true">
        <div class="mock__bar"><span></span><span></span><span></span><em>Valora Advisor Portal · Active Introductions</em></div>
        <div class="mock__body">
          <div class="mock__row">
            <div>
              <p class="mock__label">This Month's Inbound</p>
              <p class="mock__h">4 Verified Matches Ready</p>
            </div>
            <div class="mock__pill">Accepting Matches</div>
          </div>

          <!-- Interactive Category Filter Chips -->
          <div class="pipe-filter-wrap">
            <button type="button" class="pipe-chip is-active" data-cat="all">All Specialties</button>
            <button type="button" class="pipe-chip" data-cat="tech">Tech Equity</button>
            <button type="button" class="pipe-chip" data-cat="business">Business Sale</button>
            <button type="button" class="pipe-chip" data-cat="retire">Retirement</button>
            <button type="button" class="pipe-chip" data-cat="estate">Estate &amp; Trust</button>
          </div>

          <ul class="pipe">
            <li class="pipe__row" data-cat="tech">
              <div class="pipe__who">
                <span class="pipe__av">01</span>
                <div>
                  <p class="pipe__name">Tech Equity &amp; RSUs · $2.4M Liquid</p>
                  <p class="pipe__need">"VP of Engineering at Snowflake with $2.4M in vested RSUs and ISOs. Seeking tax-minimization strategy and concentrated stock collar."</p>
                  <div class="pipe__meta-row">
                    <span class="pipe__meta-tag">San Francisco, CA</span>
                    <span class="pipe__meta-tag">Goal: Tax &amp; Diversification</span>
                  </div>
                </div>
              </div>
              <span class="mock__pill mock__pill--good">Call Booked</span>
            </li>
            <li class="pipe__row" data-cat="business">
              <div class="pipe__who">
                <span class="pipe__av">02</span>
                <div>
                  <p class="pipe__name">Business Liquidity Exit · $4.5M Expected</p>
                  <p class="pipe__need">"Manufacturing founder in LOI stage for $4.5M cash sale within 9 months. Needs pre-liquidity trust structure and QSBS optimization."</p>
                  <div class="pipe__meta-row">
                    <span class="pipe__meta-tag">Austin, TX</span>
                    <span class="pipe__meta-tag">Goal: Exit &amp; Legacy</span>
                  </div>
                </div>
              </div>
              <span class="mock__pill">Dossier Sent</span>
            </li>
            <li class="pipe__row" data-cat="retire">
              <div class="pipe__who">
                <span class="pipe__av">03</span>
                <div>
                  <p class="pipe__name">Retirement Income &amp; Decumulation · $1.8M Rollover</p>
                  <p class="pipe__need">"Orthopedic surgeon retiring in 18 months. Wants tax-efficient 401(k) rollover, Social Security timing, and multi-year Roth conversion plan."</p>
                  <div class="pipe__meta-row">
                    <span class="pipe__meta-tag">Denver, CO</span>
                    <span class="pipe__meta-tag">Goal: Retirement Ladder</span>
                  </div>
                </div>
              </div>
              <span class="mock__pill">Intro Scheduled</span>
            </li>
            <li class="pipe__row" data-cat="estate">
              <div class="pipe__who">
                <span class="pipe__av">04</span>
                <div>
                  <p class="pipe__name">Generational Wealth &amp; Family Trusts · $3.2M AUM</p>
                  <p class="pipe__need">"Family enterprise principal seeking comprehensive fiduciary review of existing irrevocable trusts and philanthropic foundation strategy."</p>
                  <div class="pipe__meta-row">
                    <span class="pipe__meta-tag">Chicago, IL</span>
                    <span class="pipe__meta-tag">Goal: Dynasty Planning</span>
                  </div>
                </div>
              </div>
              <span class="mock__pill mock__pill--good">New Match</span>
            </li>
          </ul>
        </div>
      </div>
      <figcaption class="adv-mock__cap">Live illustrative simulation of Valora advisor introduction pipeline.</figcaption>
    </div>
  </div>
</section>

<!-- ================= INTERACTIVE PRACTICE GROWTH & ROI CALCULATOR ================= -->
<section class="section section--green adv-calc" id="calculator">
  <div class="container">
    <div class="adv-calc__head">
      <p class="eyebrow eyebrow--light reveal">Practice Growth Modeling</p>
      <h2 class="display display--lg reveal">Estimate your firm's revenue potential<br><em>with Valora introductions.</em></h2>
      <p class="reveal">Use the interactive model below to project your firm's annual AUM expansion, new recurring revenue, and practice equity value based on your conversion profile.</p>
    </div>

    <div class="calc-card reveal" id="advisorCalc">
      <div class="calc-grid">
        <!-- Input Sliders -->
        <div class="calc-inputs">
          <div class="calc-input-group">
            <div class="calc-label-row">
              <span class="calc-label">Monthly Exclusive Introductions</span>
              <span class="calc-val-badge" id="valMatches">5 / mo</span>
            </div>
            <div class="calc-slider-wrap">
              <input type="range" class="calc-slider" id="calcMatches" min="3" max="15" step="1" value="5" aria-label="Monthly Introductions">
            </div>
            <div class="calc-range-marks">
              <span>3 / mo</span>
              <span>8 / mo</span>
              <span>15 / mo</span>
            </div>
          </div>

          <div class="calc-input-group">
            <div class="calc-label-row">
              <span class="calc-label">Average Investable Assets per Client</span>
              <span class="calc-val-badge" id="valAum">$1.25M</span>
            </div>
            <div class="calc-slider-wrap">
              <input type="range" class="calc-slider" id="calcAum" min="500000" max="3500000" step="50000" value="1250000" aria-label="Average Investable Assets">
            </div>
            <div class="calc-range-marks">
              <span>$500K</span>
              <span>$2.0M</span>
              <span>$3.5M+</span>
            </div>
          </div>

          <div class="calc-input-group">
            <div class="calc-label-row">
              <span class="calc-label">Discovery-to-Client Close Rate</span>
              <span class="calc-val-badge" id="valCloseRate">25%</span>
            </div>
            <div class="calc-slider-wrap">
              <input type="range" class="calc-slider" id="calcCloseRate" min="15" max="45" step="5" value="25" aria-label="Close Rate">
            </div>
            <div class="calc-range-marks">
              <span>15%</span>
              <span>30%</span>
              <span>45%</span>
            </div>
          </div>

          <div class="calc-input-group">
            <div class="calc-label-row">
              <span class="calc-label">Average Annual Advisory Fee</span>
              <span class="calc-val-badge" id="valFee">0.95%</span>
            </div>
            <div class="calc-slider-wrap">
              <input type="range" class="calc-slider" id="calcFee" min="0.65" max="1.25" step="0.05" value="0.95" aria-label="Advisory Fee">
            </div>
            <div class="calc-range-marks">
              <span>0.65%</span>
              <span>0.95%</span>
              <span>1.25%</span>
            </div>
          </div>
        </div>

        <!-- Calculated Live Results -->
        <div class="calc-results">
          <div class="calc-res-title">Projected Annual Practice Impact</div>

          <div class="calc-res-box">
            <div class="calc-res-num" id="resAum">$18.75M</div>
            <div class="calc-res-label">Estimated New AUM Added per Year</div>
          </div>

          <div class="calc-res-box">
            <div class="calc-res-num" id="resRevenue">$178,125 <em>/ yr</em></div>
            <div class="calc-res-label">New Annual Recurring Revenue (ARR)</div>
          </div>

          <div class="calc-res-box">
            <div class="calc-res-num" id="resEquity">$498,750</div>
            <div class="calc-res-label">Estimated Practice Enterprise Value Created (2.8x ARR multiple)</div>
          </div>

          <div class="calc-cta-wrap">
            <a class="btn btn--cream" href="#apply">Apply for territory availability</a>
            <p class="calc-fine">Calculations are illustrative estimates based on stated inputs and industry standard valuation benchmarks. Outcomes vary based on advisor diligence and market dynamics.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ================= COMPLETE RIA OPERATING PLATFORM ================= -->
<section class="section section--cream adv-feat" id="platform">
  <div class="container">
    <div class="adv-feat__head">
      <p class="eyebrow reveal">The Turnkey RIA Platform</p>
      <h2 class="display display--lg reveal">Behind every great advisor<br><em>is a back office that just works.</em></h2>
      <p class="reveal">Consolidate five disjointed fintech subscriptions and an ops hire into one unified, elegant workspace engineered for modern wealth practices.</p>
    </div>

    <ul class="feat">
      <li class="feat__item reveal">
        <span class="feat__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><rect x="4" y="3" width="16" height="18" rx="2" stroke="currentColor" stroke-width="1.3"/><path d="M8 8h8M8 12h8M8 16h5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
        </span>
        <h3>Paperless Digital Onboarding</h3>
        <p>1-click account opening, automated e-signatures, and instant custodial ACATS transfer tracking. 94% reduction in NIGO paperwork errors.</p>
      </li>

      <li class="feat__item reveal">
        <span class="feat__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><path d="M4 17l5-5 4 4 7-8" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 8h5v5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <h3>Tax-Intelligent Rebalancer</h3>
        <p>Year-round automated tax-loss harvesting, household asset location, and single-stock exclusion rules to honor client executive stock restrictions.</p>
      </li>

      <li class="feat__item reveal">
        <span class="feat__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><rect x="3" y="6" width="18" height="12" rx="2" stroke="currentColor" stroke-width="1.3"/><circle cx="12" cy="12" r="2.4" stroke="currentColor" stroke-width="1.3"/></svg>
        </span>
        <h3>Automated Fee Billing &amp; Invoicing</h3>
        <p>Tiered AUM schedules, flat planning retainers, and subscription billing calculated, audited, and debited directly from custodians.</p>
      </li>

      <li class="feat__item reveal">
        <span class="feat__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6l7-3z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/><path d="M9 12l2 2 4-4" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <h3>Fiduciary Compliance Vault</h3>
        <p>Automated archiving of email and text communications, Form ADV Part 2 maintenance, and audit-ready inspection logs that take the anxiety out of SEC exams.</p>
      </li>

      <li class="feat__item reveal">
        <span class="feat__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>
        </span>
        <h3>Branded Client Portal</h3>
        <p>A sophisticated mobile and desktop client experience showcasing aggregated net worth, portfolio performance, document vault, and financial planning milestones.</p>
      </li>

      <li class="feat__item reveal">
        <span class="feat__icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none"><circle cx="6" cy="12" r="2.5" stroke="currentColor" stroke-width="1.3"/><circle cx="18" cy="6" r="2.5" stroke="currentColor" stroke-width="1.3"/><circle cx="18" cy="18" r="2.5" stroke="currentColor" stroke-width="1.3"/><path d="M8.3 10.8l7.4-3.6M8.3 13.2l7.4 3.6" stroke="currentColor" stroke-width="1.3"/></svg>
        </span>
        <h3>Breakaway Concierge Support</h3>
        <p>Transitioning from a wirehouse or broker-dealer? Our specialized transition team handles client repapering and account migration in under 14 days.</p>
      </li>
    </ul>
  </div>
</section>

<!-- ================= ADVISOR DIRECTORY ADVANTAGE (SAVVY WEALTH STYLE) ================= -->
<section class="section section--paper dir-showcase" id="directory">
  <div class="dir-showcase__copy reveal">
    <p class="eyebrow">Your Digital Flagship</p>
    <h2 class="display display--lg">Your firm, showcased to thousands<br><em>of investors searching for your specialty.</em></h2>
    <p style="margin-top:16px; font-size:.95rem; color:var(--ink-soft); max-width:48ch;">Every approved Valora advisor receives an authoritative, search-optimized directory profile that commands instant credibility. Consumers view your fiduciary credentials, fee philosophy, focus areas, and book an introductory consultation directly onto your calendar.</p>
    <ul class="adv-ticks" style="margin-top:22px;">
      <li>Verified Fiduciary Badge &amp; Clean Regulatory Record Highlight</li>
      <li>Custom niche tags (Tech RSUs, Physician Planning, Business Exit)</li>
      <li>Direct calendar scheduling link with no friction</li>
      <li>Local SEO positioning in your target metropolitan area</li>
    </ul>
  </div>

  <div class="dir-card-mock reveal reveal--right">
    <div class="dir-profile-head">
      <img class="dir-profile-img" src="https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?auto=format&amp;fit=crop&amp;crop=faces&amp;w=200&amp;h=200&amp;q=80" alt="Elena Rostova, CFP®" loading="lazy">
      <div>
        <h4>Elena Rostova, CFP®</h4>
        <p>Managing Principal · Summit Crest Wealth (Denver, CO)</p>
      </div>
    </div>
    <div class="dir-tags">
      <span class="dir-tag">Fee-Only Fiduciary</span>
      <span class="dir-tag">Tech Executive Equity</span>
      <span class="dir-tag">Retirement Decumulation</span>
      <span class="dir-tag">14 Yrs Experience</span>
    </div>
    <p class="dir-quote">"We believe financial planning should give clients clarity and confidence before any portfolio allocation is ever discussed."</p>
    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid var(--line); padding-top:14px;">
      <span style="font-size:.78rem; color:var(--muted);">⭐ 5.0 (24 Client Reviews)</span>
      <span class="btn btn--dark" style="padding:8px 18px; font-size:.78rem; pointer-events:none;">Schedule 20-Min Intro</span>
    </div>
  </div>
</section>

<!-- ================= DETAILED COMPARISON TABLE ================= -->
<section class="section section--paper adv-compare">
  <div class="container">
    <div class="adv-compare__head">
      <div>
        <p class="eyebrow reveal">Clear Economics &amp; Autonomy</p>
        <h2 class="display display--lg reveal">Independence,<br><em>without doing it alone.</em></h2>
      </div>
      <p class="reveal">How partnering with Valora compares against building a DIY solo RIA from scratch or remaining trapped at a traditional wirehouse broker-dealer.</p>
    </div>

    <div class="ctable reveal" role="table" aria-label="Comparison of advisory practice models">
      <div class="ctable__row ctable__row--head" role="row">
        <span role="columnheader">Key Capability</span>
        <span role="columnheader">On Your Own (DIY RIA)</span>
        <span role="columnheader">Wirehouse / Broker-Dealer</span>
        <span role="columnheader" class="is-us">Valora Partner Network</span>
      </div>
      <div class="ctable__row" role="row">
        <span role="rowheader">You own 100% of client relationships &amp; equity</span>
        <span role="cell" class="yes">Yes</span>
        <span role="cell" class="no">Firm owns clients</span>
        <span role="cell" class="yes is-us">Yes (100% yours)</span>
      </div>
      <div class="ctable__row" role="row">
        <span role="rowheader">Your brand on the door &amp; your own Form ADV</span>
        <span role="cell" class="yes">Yes</span>
        <span role="cell" class="no">Never</span>
        <span role="cell" class="yes is-us">Yes (Always)</span>
      </div>
      <div class="ctable__row" role="row">
        <span role="rowheader">Exclusive, pre-qualified client introductions</span>
        <span role="cell" class="no">DIY marketing only</span>
        <span role="cell" class="no">Shared call center leads</span>
        <span role="cell" class="yes is-us">100% Exclusive</span>
      </div>
      <div class="ctable__row" role="row">
        <span role="rowheader">Paperless onboarding &amp; ACATS custodial transfer tracking</span>
        <span role="cell" class="no">Stitch 5+ vendors</span>
        <span role="cell" class="yes">Yes</span>
        <span role="cell" class="yes is-us">Turnkey Digital</span>
      </div>
      <div class="ctable__row" role="row">
        <span role="rowheader">Automated tax-loss harvesting &amp; rebalancing</span>
        <span role="cell" class="no">Manual or costly software</span>
        <span role="cell" class="no">Limited model portfolios</span>
        <span role="cell" class="yes is-us">Built-in Year Round</span>
      </div>
      <div class="ctable__row" role="row">
        <span role="rowheader">Compliance monitoring &amp; audit-ready record keeping</span>
        <span role="cell" class="no">You are the CCO</span>
        <span role="cell" class="yes">Yes (Restrictive)</span>
        <span role="cell" class="yes is-us">Automated Vault</span>
      </div>
      <div class="ctable__row" role="row">
        <span role="rowheader">Advisory fee retention &amp; payout economics</span>
        <span role="cell" class="yes">100% (High tech overhead)</span>
        <span role="cell" class="no">35% – 50% Haircut</span>
        <span role="cell" class="yes is-us">100% Fee Control</span>
      </div>
    </div>
  </div>
</section>

<!-- ================= ADVISOR TESTIMONIALS & CASE STUDIES ================= -->
<section class="section section--cream adv-testimonials" id="testimonials">
  <div class="container">
    <div style="max-width:720px;">
      <p class="eyebrow reveal">Partner Case Studies</p>
      <h2 class="display display--lg reveal">Trusted by independent advisors<br><em>building high-conviction practices.</em></h2>
      <p class="reveal" style="margin-top:16px; font-size:.95rem; color:var(--ink-soft);">Hear how independent RIA owners use Valora to accelerate organic growth, delegate back-office friction, and serve their clients at the highest level.</p>
    </div>

    <div class="adv-test-grid">
      <!-- Testimonial 1 -->
      <article class="tcard reveal">
        <div>
          <span class="tcard__badge">+$16.2M AUM Added · 1st Year</span>
          <p class="tcard__quote">"In our first twelve months on Valora, we onboarded nine new high-net-worth households. The clients arrived with verified liquid assets and an immediate financial milestone. It transformed our growth trajectory without any cold prospecting."</p>
        </div>
        <div>
          <div class="tcard__author">
            <img class="tcard__av" src="https://images.unsplash.com/photo-1573496358961-3c82861ab8f4?auto=format&amp;fit=crop&amp;crop=faces&amp;w=120&amp;h=120&amp;q=80" alt="Elena Rostova" loading="lazy">
            <div>
              <p class="tcard__name">Elena Rostova, CFP®</p>
              <p class="tcard__role">Founder · Summit Crest Wealth Management</p>
            </div>
          </div>
          <div class="tcard__stat">100% Client Retention Rate · Denver, CO</div>
        </div>
      </article>

      <!-- Testimonial 2 -->
      <article class="tcard reveal">
        <div>
          <span class="tcard__badge">15 Hours Saved / Week · Operations</span>
          <p class="tcard__quote">"The biggest bottleneck for growing RIAs is back-office drag. Valora eliminated 15 hours of weekly paperwork, billing reconciliations, and custodial transfer chasing. That extra time allowed our team to add $22M in net new assets this year."</p>
        </div>
        <div>
          <div class="tcard__author">
            <img class="tcard__av" src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&amp;fit=crop&amp;crop=faces&amp;w=120&amp;h=120&amp;q=80" alt="Marcus Vance" loading="lazy">
            <div>
              <p class="tcard__name">Marcus Vance, CFA</p>
              <p class="tcard__role">Managing Partner · Prairie Capital Partners</p>
            </div>
          </div>
          <div class="tcard__stat">4.8x ROI on Partnership Fees · Chicago, IL</div>
        </div>
      </article>

      <!-- Testimonial 3 -->
      <article class="tcard reveal">
        <div>
          <span class="tcard__badge">38% Discovery Conversion Rate</span>
          <p class="tcard__quote">"Generic lead generation companies sell raw phone numbers to anyone with a checkbook. Valora's introductions are different: the clients have already studied our firm's fee-only philosophy and specifically requested our equity compensation specialty."</p>
        </div>
        <div>
          <div class="tcard__author">
            <img class="tcard__av" src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&amp;fit=crop&amp;crop=faces&amp;w=120&amp;h=120&amp;q=80" alt="Sofía Marín" loading="lazy">
            <div>
              <p class="tcard__name">Sofía Marín, CPA, PFS</p>
              <p class="tcard__role">Founder · Beacon Equity Wealth Advisors</p>
            </div>
          </div>
          <div class="tcard__stat">$2.4M Average Household AUM · Seattle, WA</div>
        </div>
      </article>
    </div>
  </div>
</section>

<!-- ================= PARTNER CRITERIA + EXTENDED FAQ ================= -->
<section class="section section--paper life adv-faq" id="faq">
  <div class="container life__grid">
    <div class="adv-criteria reveal">
      <p class="eyebrow">Selective Fiduciary Network</p>
      <h2 class="display display--md">A high bar,<br><em>on purpose.</em></h2>
      <p>Investors trust Valora because our network is curated rather than open to anyone with a marketing budget. We partner exclusively with qualified fiduciaries who share our standard for transparent, conflict-free advice.</p>
      <ul class="adv-ticks" style="margin-top:24px;">
        <li>Registered Investment Adviser (RIA) or IAR registration</li>
        <li>Strict Fiduciary Duty to clients at all times</li>
        <li>Clean regulatory history verified on SEC IAPD / FINRA BrokerCheck</li>
        <li>Professional designation: CFP®, CFA, CPA/PFS or 10+ years experience</li>
        <li>Transparent, published fee schedule (fee-only or fee-transparent)</li>
      </ul>
      <div style="margin-top:28px;">
        <a class="btn btn--dark" href="#apply" style="width:100%;">Apply to join network</a>
      </div>
    </div>

    <div class="life__body">
      <div class="faq" style="margin-top:0;">
        <h2 class="faq__title" style="padding-top:0;">Frequently Asked Questions</h2>
        {faq_html}
      </div>
    </div>
  </div>
</section>

<!-- ================= APPLY SECTION (HIGH-CONVERSION FORM) ================= -->
<section class="section section--green cta" id="apply">
  <div class="container cta__grid">
    <div class="cta__copy">
      <p class="eyebrow eyebrow--light reveal">Advisor Network Application</p>
      <h2 class="display display--lg reveal">Spend your week advising.<br><em>We'll handle everything else.</em></h2>
      <p class="reveal">Tell us a little about your firm and advisory focus. A partner from our advisor team — not a robot or automated dialer — will reach out within one business day to discuss platform access, practice fit, and regional territory availability.</p>

      <ul class="direct reveal">
        <li>
          <span class="direct__label">Advisor Partnerships</span>
          <a class="direct__link" href="mailto:{EMAIL}">{EMAIL}</a>
        </li>
        <li>
          <span class="direct__label">Direct Advisory Desk</span>
          <a class="direct__link" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        </li>
      </ul>
      <p class="direct__note reveal">Prefer a confidential conversation first? Call or email directly — our leadership team reviews every application.</p>
    </div>

    <form class="form reveal" id="advisorForm" data-lead="Advisor" data-success="Thank you, {{name}} — our advisor partnership team will be in touch within one business day." novalidate>
      <div class="field" data-field>
        <label for="aname">Full name</label>
        <input id="aname" name="name" type="text" required placeholder="Alex Morgan, CFP®" autocomplete="name">
        <small class="err" data-err="name"></small>
      </div>
      <div class="field" data-field>
        <label for="aemail">Work email</label>
        <input id="aemail" name="email" type="email" required placeholder="alex@yourfirm.com" autocomplete="email">
        <small class="err" data-err="email"></small>
      </div>
      <div class="field" data-field>
        <label for="aphone">Phone number</label>
        <input id="aphone" name="phone" type="tel" required placeholder="+1 (415) 909-4100" autocomplete="tel" inputmode="tel">
        <small class="err" data-err="phone"></small>
      </div>
      <div class="field" data-field>
        <label for="afirm">Firm name <span class="opt">(or current broker-dealer)</span></label>
        <input id="afirm" data-extra="Firm" type="text" placeholder="Morgan Wealth Partners" autocomplete="organization">
      </div>
      <div class="field" data-field>
        <label for="aaum">Current Assets Under Management (AUM)</label>
        <select id="aaum" data-extra="AUM">
          <option value="">Select current AUM range</option>
          <option>Under $25M</option>
          <option>$25M – $75M</option>
          <option>$75M – $200M</option>
          <option>$200M – $500M</option>
          <option>$500M+</option>
          <option>Breakaway / Transitioning</option>
        </select>
      </div>
      <div class="field" data-field>
        <label for="agoal">Primary objective</label>
        <select id="agoal" name="goal" required>{_goal_opts()}</select>
        <small class="err" data-err="goal"></small>
      </div>
      <div class="field field--full" data-field>
        <label for="anote">Practice details &amp; primary custodian <span class="opt">(optional)</span></label>
        <textarea id="anote" name="note" rows="3" placeholder="Primary custodian (Schwab, Fidelity, Pershing), target niches, certifications — a couple sentences is plenty."></textarea>
      </div>
      <div class="field field--full form__foot">
        <button class="btn btn--cream" type="submit">Submit application</button>
        <p class="form__fine">Strictly confidential. Exclusively for registered fiduciaries. We never sell your data.</p>
      </div>
      <p class="form__success" role="status" hidden></p>
    </form>
  </div>
</section>
"""
