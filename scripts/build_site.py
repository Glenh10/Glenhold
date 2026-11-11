#!/usr/bin/env python3
"""Generate the static Glenhold site. Run from anywhere: python3 scripts/build_site.py

GitHub Pages serves the HTML this writes. Re-running overwrites those pages.
"""

from __future__ import annotations

import re
import sys
from collections import OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cities import CITIES
from faqs import FAQ
from industries import INDUSTRIES
from sitegen import (  # noqa: E402
    CALENDAR,
    EMAIL,
    INDEXNOW_KEY,
    LASTMOD,
    PAGES,
    ROOT,
    YOUTUBE,
    abs_url,
    area_nodes,
    chips,
    contact_block,
    crumb_html,
    cta,
    esc,
    fact_bar,
    faq_html,
    faq_node,
    hub_cards,
    offer,
    related_links,
    service_node,
    write_page,
)

EXTRAS = [
    {"schema_type": "Place", "schema_name": "Oak Park", "contained": "Ventura County, California"},
    {"schema_type": "Place", "schema_name": "Winnetka, Los Angeles", "contained": "Los Angeles, California"},
    {"schema_type": "Place", "schema_name": "Tarzana, Los Angeles", "contained": "Los Angeles, California"},
]

CITY_BY = {c["slug"]: c for c in CITIES}
IND_BY = {i["slug"]: i for i in INDUSTRIES}


def area():
    return area_nodes(CITIES, EXTRAS)


def price_cards() -> str:
    return '''<div class="pricing-grid">
      <div class="pricing-card">
        <h3>Essential</h3>
        <p class="pricing-tagline">For small businesses with simple accounting needs who want clean books at tax time</p>
        <div class="pricing-price"><span class="pricing-prefix">Starting at</span>$349 <span>/ mo</span></div>
        <hr class="pricing-divider" />
        <ul class="pricing-list">
          <li>Expense categorization</li>
          <li>Monthly bank &amp; card reconciliation</li>
          <li>Monthly financial statements</li>
          <li>Clean books for tax season</li>
        </ul>
        <a href="#contact" class="btn-slate">Get Started</a>
      </div>
      <div class="pricing-card featured">
        <div class="pricing-badge">Most Popular</div>
        <h3>Core</h3>
        <p class="pricing-tagline">For growing businesses that want clean books and a clearer picture of performance</p>
        <div class="pricing-price"><span class="pricing-prefix">Starting at</span>$599 <span>/ mo</span></div>
        <hr class="pricing-divider" />
        <ul class="pricing-list">
          <li>Expense categorization</li>
          <li>Monthly bank &amp; card reconciliation</li>
          <li>Monthly financial statements</li>
          <li>Clean books for tax season</li>
          <li>Quarterly profit and expense summary</li>
          <li>Year-to-date performance comparison</li>
          <li>Priority support</li>
        </ul>
        <a href="#contact" class="btn-sage">Get Started</a>
      </div>
      <div class="pricing-card">
        <h3>Strategic</h3>
        <p class="pricing-tagline">For established businesses that want tailored reports and a monthly financial walkthrough</p>
        <div class="pricing-price"><span class="pricing-prefix">Starting at</span>$1499 <span>/ mo</span></div>
        <hr class="pricing-divider" />
        <ul class="pricing-list">
          <li>Expense categorization</li>
          <li>Monthly bank &amp; card reconciliation</li>
          <li>Monthly financial statements</li>
          <li>Clean books for tax season</li>
          <li>Quarterly profit and expense summary</li>
          <li>Year-to-date performance comparison</li>
          <li>Priority support</li>
          <li>Custom financial reports for your business</li>
          <li>Accrual accounting, payroll journal entries, and loan tracking</li>
          <li>Monthly call to walk through your numbers</li>
        </ul>
        <a href="#contact" class="btn-slate">Get Started</a>
      </div>
    </div>'''


def write_inner(title, description, path, h1, lede, body, crumbs, extra, faqs=None, faq_heading="Questions"):
    nodes = list(extra)
    faq_block = ""
    if faqs:
        faq_block = f"<section><h2>{esc(faq_heading)}</h2>{faq_html(faqs)}</section>"
        nodes.append(faq_node(faqs, path))
    main = f'''<header class="page-hero"><div class="breadcrumb">{crumb_html(crumbs)}</div><h1>{esc(h1)}</h1><p>{esc(lede)}</p><a class="btn-primary" href="{CALENDAR}" target="_blank" rel="noopener noreferrer">Book a Free Call</a></header>
<article class="article-body">{fact_bar()}{body}{faq_block}</article>
{cta()}
{contact_block(path)}'''
    write_page(title, description, path, main, crumbs, nodes, CITIES, area())


def service_links():
    return related_links([
        ("/monthly-bookkeeping/", "Monthly bookkeeping"),
        ("/cleanup-catch-up/", "Cleanup &amp; catch-up"),
        ("/quickbooks-online/", "QuickBooks setup &amp; training"),
        ("/financial-statements/", "Financial statements"),
        ("/cpa-ready-books/", "CPA-ready books"),
        ("/loan-ready-books/", "Loan-ready financials"),
        ("/pricing/", "Pricing"),
        ("/service-areas/", "Service areas"),
        ("/who-we-work-with/", "Who we work with"),
        ("/bookkeeping-faq/", "Bookkeeping FAQ"),
    ])


def build_services():
    pages = [
        {
            "path": "/monthly-bookkeeping/",
            "name": "Monthly bookkeeping",
            "title": "Monthly Bookkeeping in Simi Valley & Nearby | Glenhold",
            "description": "Monthly bookkeeping from $349 for small businesses near Simi Valley. Reconciliation, a P&L and balance sheet by the 15th, and three plans.",
            "h1": "Monthly bookkeeping for small businesses",
            "lede": "Keep the month current. Know where the business stands.",
            "offer": offer("Essential monthly bookkeeping", "349", "Starting at $349 per month. Love your first month of books, or it is free."),
            "body": '''<section><h2>I'll close the month for you</h2><p>If the books are always a week behind, you can't tell whether the business made money. I keep them current for small businesses around Simi Valley. You work with me. I'm a former Big 4 accountant and a Certified QuickBooks ProAdvisor. Any kind of small business is welcome. I price the work from your accounts, your volume, and the reports you want.</p></section>
<section><h2>What is included</h2><ul><li><strong>Transaction categorization</strong> against a chart of accounts built for how you operate.</li><li><strong>Bank and credit card reconciliation</strong> so missing entries, duplicates, and transfers can be seen.</li><li><strong>Monthly financial statements:</strong> a profit and loss and a balance sheet.</li><li><strong>Email between closes</strong> for the questions that hold a month up.</li></ul><p>The target is a P&amp;L and balance sheet by the 15th. That date depends on statements and answers arriving in time.</p></section>
<section><h2>Essential, Core, and Strategic</h2><div class="table-wrap"><table><thead><tr><th scope="col">Plan</th><th scope="col">Starting price</th><th scope="col">What changes</th></tr></thead><tbody><tr><th scope="row">Essential</th><td>$349 / month</td><td>Categorization, reconciliation, monthly statements, clean books for tax season.</td></tr><tr><th scope="row">Core</th><td>$599 / month</td><td>Essential, plus a quarterly profit and expense summary, a year-to-date comparison, and priority support.</td></tr><tr><th scope="row">Strategic</th><td>$1,499 / month</td><td>Core, plus custom reports, accrual accounting, payroll journal entries, loan tracking, and a monthly call.</td></tr></tbody></table></div><p>These are starting prices. The quote depends on transaction volume, the number of accounts, and reporting complexity. Love your first month of books, or it's free. See <a href="/pricing/">the full comparison</a>.</p></section>
<section><h2>If the past is not current</h2><p>Start with <a href="/cleanup-catch-up/">cleanup and catch-up</a> when months are unfinished. Stay on <a href="/quickbooks-online/">QuickBooks training</a> if you want to keep doing the entry. Monthly bookkeeping is for handing the close to Jack.</p></section>''',
            "faqs": [
                ("What does monthly bookkeeping include?", "Expense categorization, monthly bank and credit card reconciliation, a profit and loss, a balance sheet, and clean books for tax season. Core and Strategic add the reporting listed on the pricing page."),
                ("Does the monthly price include tax filing or payroll?", "No. Tax returns stay with your CPA. Glenhold does not run payroll. Strategic can record payroll journal entries from your payroll provider."),
            ],
        },
        {
            "path": "/cleanup-catch-up/",
            "name": "Cleanup and catch-up bookkeeping",
            "title": "Bookkeeping Cleanup & Catch-Up | Glenhold Bookkeeping",
            "description": "Catch up months or years of books for Simi Valley-area businesses. Reconciled records and a CPA handoff. Quoted separately from monthly plans.",
            "h1": "Cleanup and catch-up bookkeeping",
            "lede": "Behind on the books? I'll tell you what it will take before we start.",
            "offer": None,
            "body": '''<section><h2>Bring the backlog current</h2><p>Cleanup means the books exist and they're wrong. Catch-up means the months were never entered. A lot of projects are both. I do this for small businesses around Simi Valley. We can stop when the backlog is done, or keep going month to month.</p></section>
<section><h2>What a project can cover</h2><ul><li>Organizing statements, exports, and the existing accounting file.</li><li>Importing missing transactions and classifying income and expenses.</li><li>Reviewing duplicates, unmatched transfers, and balances that do not tie.</li><li>Reconciling bank and credit card accounts to the statements you have.</li><li>Tidying the chart of accounts so the reports can be read.</li><li>A package your CPA can use. They file the return.</li></ul><p>If an entry is unclear, I'll ask you. I'd rather wait than guess what a transfer was for.</p></section>
<section><h2>What to gather</h2><p>The months in question, every business bank and credit card account including accounts you closed, and statements that show opening and closing balances. Add loans, payroll reports, and owner contributions or draws when they matter. If you changed banks, include both sides. The <a href="/getting-started/">handoff checklist</a> is the longer version. Ask how to send files before you email anything sensitive.</p></section>
<section><h2>Price and timing</h2><p>I quote cleanup from the periods, accounts, transactions, and fixes. The monthly starting prices of $349, $599, and $1,499 are for ongoing work. Tell me any tax or lender date on the first call so I can plan around it.</p><p>When the project is done you can move to <a href="/monthly-bookkeeping/">monthly bookkeeping</a> or to <a href="/quickbooks-online/">training and check-ins</a> if you want the file back.</p></section>''',
            "faqs": [
                ("How much does catch-up bookkeeping cost?", "It is quoted from the months, accounts, transactions, and corrections involved. It is not priced off the monthly plans. Jack scopes it before you commit."),
                ("Will the books be ready for my CPA?", "That is the handoff: classified transactions, reconciled accounts, financial statements, and a note of anything the records could not support. Your CPA files the return."),
            ],
        },
        {
            "path": "/quickbooks-online/",
            "name": "QuickBooks Online setup and training",
            "title": "QuickBooks Online Setup & Training | Glenhold Bookkeeping",
            "description": "QuickBooks Online setup, chart of accounts, and training from a Certified ProAdvisor in Simi Valley. Scoped separately from monthly plans.",
            "h1": "QuickBooks Online setup and training",
            "lede": "A file that matches the business, and a routine you can actually follow.",
            "offer": None,
            "body": '''<section><h2>I'll set QuickBooks up so it fits your business</h2><p>If the file is noisy or you want to keep doing the entry yourself, I can set it up, train you, and check your work. I'm a Certified QuickBooks ProAdvisor and a former Big 4 accountant, in Simi Valley. I work in QuickBooks Online. If you're still on Desktop, tell me on the intro call before we start.</p></section>
<section><h2>What setup covers</h2><ul><li>A QuickBooks Online file built around how money moves through the business.</li><li>A chart of accounts for income, expenses, assets, liabilities, and equity.</li><li>A routine for reviewing activity, separating transfers from income and expenses, and reconciling.</li><li>Accuracy check-ins on a schedule you agree to, if you want a review rather than a handoff.</li></ul><p>Too many overlapping accounts make a profit and loss hard to read. Too few hide the thing you meant to see. Setup starts by asking which reports you actually use.</p></section>
<section><h2>Training or a monthly plan</h2><p>Choose training when you want to keep the day-to-day work. Choose <a href="/monthly-bookkeeping/">monthly bookkeeping</a> when you want me to categorize, reconcile, and send the statements. You can start with one and move to the other. Training is quoted on its own. Monthly plans start at $349. You pay Intuit for the QuickBooks subscription.</p><p>An existing file does not have to be thrown out. It may need a chart review, or a <a href="/cleanup-catch-up/">cleanup</a>, before a routine makes sense.</p></section>''',
            "faqs": [
                ("Is Jack a QuickBooks ProAdvisor?", "Yes. Jack is a Certified QuickBooks ProAdvisor. The setup, training, and consulting on this page are for QuickBooks Online."),
                ("Does monthly bookkeeping include the QuickBooks subscription?", "No. Intuit bills the subscription. Glenhold's prices are for the bookkeeping work. Check Intuit for the current software price."),
            ],
        },
        {
            "path": "/financial-statements/",
            "name": "Financial statements",
            "title": "Monthly Financial Statements | Glenhold Bookkeeping",
            "description": "Profit and loss and balance sheet by the 15th for Simi Valley-area small businesses. Included in monthly plans from $349. Not a separate product.",
            "h1": "Financial statements for small businesses",
            "lede": "A profit and loss and a balance sheet, on a schedule, from reconciled accounts.",
            "offer": None,
            "body": '''<section><h2>What you actually get each month</h2><p>Every monthly plan includes a profit and loss and a balance sheet. I aim for the 15th of the following month, once your statements and answers are in. These reports come with the bookkeeping. Your CPA still files the return.</p><p>A profit and loss shows income, expenses, and profit for a stretch of time. It does not, by itself, show the cash in the bank. A balance sheet shows what the business owns, what it owes, and the owner's equity on one date. You usually need both.</p></section>
<section><h2>What Core and Strategic add</h2><ul><li><strong>Essential, from $349:</strong> the monthly statements and the reconciliation behind them.</li><li><strong>Core, from $599:</strong> those statements, plus a quarterly profit and expense summary and a year-to-date performance comparison.</li><li><strong>Strategic, from $1,499:</strong> Core, plus custom financial reports, accrual accounting, payroll journal entries, loan tracking, and a monthly call to walk through the numbers.</li></ul><p>Accrual accounting is part of Strategic. If unearned deposits or unpaid bills should sit on the balance sheet, tell me before you pick a plan. Your CPA can confirm which basis the return expects. They file it.</p></section>
<section><h2>Who the statements are for</h2><p>You use them to see the month. Your CPA uses them at tax time. A lender may ask for them when you apply for financing. I prepare the bookkeeping reports. If the history is incomplete, <a href="/cleanup-catch-up/">we'll catch the books up</a> before you lean on a statement.</p></section>''',
            "faqs": [
                ("Are financial statements included in the monthly price?", "Yes. A profit and loss and a balance sheet are part of Essential, Core, and Strategic. They are not billed as an extra report fee on this site."),
                ("Is this an audit or a review?", "No. Glenhold does bookkeeping and management statements from the reconciled accounts. Audits and reviews are attestation services this firm does not offer."),
            ],
        },
        {
            "path": "/cpa-ready-books/",
            "name": "CPA-ready books",
            "title": "CPA-Ready Books for Tax Season | Glenhold Bookkeeping",
            "description": "I reconcile the year and hand your CPA financial statements they can file from. I'm in Simi Valley. Plans support the monthly work from $349.",
            "h1": "Books your CPA can actually use",
            "lede": "Tax season goes faster when the year is reconciled before the CPA opens the file.",
            "offer": None,
            "body": '''<section><h2>Clean books for your CPA</h2><p>I categorize the accounts, reconcile the bank and cards, and send a profit and loss and balance sheet your preparer can use. That's what I mean by clean books for tax season. Your CPA still reviews them and files. I'm a former Big 4 accountant. I keep the books. They file the return.</p></section>
<section><h2>What usually goes in the package</h2><ul><li>A profit and loss for the year, and a balance sheet at year end.</li><li>Accounts reconciled to statements, including accounts closed during the year.</li><li>A chart of accounts that did not change meaning halfway through the year.</li><li>A short list of items the records could not support, so the CPA is not left to discover them in March.</li><li>Loan balances and owner draws identified, when those records were provided.</li></ul><p>California LLC owners often ask about the $800 minimum franchise tax at the same time. That tax is filed with the Franchise Tax Board, not paid to Glenhold. The <a href="/bookkeeping-faq/#llc-800">FAQ states the general rule</a> and tells you to confirm it with your preparer.</p></section>
<section><h2>When the year is already a mess</h2><p>If months were never closed, start with <a href="/cleanup-catch-up/">cleanup and catch-up</a>. The monthly plans assume a current rhythm. Name the filing deadline on the first call. Do not email source documents until Jack tells you how to share them.</p></section>''',
            "faqs": [
                ("Does Glenhold file my tax return?", "No. The service is the books and the statements. Your CPA or tax preparer files the return."),
                ("What if I do not have a CPA yet?", "You can still get the books current. You will need a preparer, or another arrangement you choose, to file. Glenhold does not shop that role for you on this site."),
            ],
        },
        {
            "path": "/loan-ready-books/",
            "name": "Loan-ready financials",
            "title": "Loan-Ready Bookkeeping | Glenhold Bookkeeping",
            "description": "I reconcile the books and prepare the statements lenders ask to see. You send the package. Plans from $349 support the monthly work.",
            "h1": "Books a lender can read",
            "lede": "Lenders ask for statements that match the bank. I'll get the books there. They still make the decision.",
            "offer": None,
            "body": '''<section><h2>Give the lender statements that tie</h2><p>Lenders usually ask for a recent profit and loss, a balance sheet, and bank statements for the same months. They want the cash on the balance sheet to match the statement. I catch the books up and reconcile them so those reports agree. You or your broker send the package. Your CPA may still provide the tax returns.</p></section>
<section><h2>If you're on a deadline</h2><p>If the books are months behind, we start with <a href="/cleanup-catch-up/">catch-up</a> for the periods the lender named. If they're current, <a href="/financial-statements/">monthly statements</a> are already part of the plans that start at $349, $599, and $1,499. Tell me the date on the first call. I can only use the statements you actually have.</p></section>''',
            "faqs": [
                ("Can you guarantee my loan will be approved?", "No. Glenhold prepares reconciled financial statements. The lender decides."),
                ("Do I still need my tax returns?", "Often yes. Lenders ask the CPA's returns as well as the bookkeeping statements. Glenhold does not file the returns."),
            ],
        },
    ]
    for page in pages:
        body = page["body"] + "<section><h2>Keep going</h2>" + service_links() + "</section>"
        extra = []
        if page["offer"]:
            extra.append(service_node(page["name"], page["path"], page["description"], area(), page["offer"]))
        else:
            extra.append(service_node(page["name"], page["path"], page["description"], area()))
        write_inner(
            page["title"], page["description"], page["path"], page["h1"], page["lede"], body,
            [("Home", "/"), ("Services", "/services/"), (page["name"], page["path"])],
            extra, page["faqs"], "Questions about this work",
        )


def build_service_hub():
    cards = [
        ("/monthly-bookkeeping/", "Monthly bookkeeping", "Categorize, reconcile, and issue statements every month. From $349."),
        ("/cleanup-catch-up/", "Cleanup and catch-up", "Months or years behind. A quoted project, then a handoff to your CPA."),
        ("/quickbooks-online/", "QuickBooks Online", "Setup, chart of accounts, training, and check-ins from a ProAdvisor."),
        ("/financial-statements/", "Financial statements", "Profit and loss and balance sheet by the 15th, included in the monthly plans."),
        ("/cpa-ready-books/", "CPA-ready books", "Reconciled records your CPA can use at tax time."),
        ("/loan-ready-books/", "Loan-ready financials", "Statements a lender can read, prepared from reconciled books."),
    ]
    body = f'''<section><h2>Tell me where the books stand</h2><p>Most people call because the month never quite closes, a year got away from them, or QuickBooks feels harder than it should. I do monthly bookkeeping, catch-up, and QuickBooks Online setup and training. The statements, the CPA handoff, and the lender package come out of that work. Monthly plans start at $349, $599, and $1,499. Love your first month of books, or it's free.</p>{hub_cards(cards)}</section>
<section><h2>You still keep your CPA</h2><p>I hand your CPA clean, tax-ready books. They file the return. If you already have a payroll company, the Strategic plan includes recording those journal entries. You pay Intuit for QuickBooks Online. You work with me, whatever kind of small business you run. <a href="/who-we-work-with/">See a few of them</a>.</p></section>'''
    write_inner(
        "Bookkeeping Services | Glenhold Bookkeeping",
        "I do monthly bookkeeping, catch-up, and QuickBooks Online setup for small businesses around Simi Valley. Plans from $349. You work with me.",
        "/services/",
        "Bookkeeping services",
        "Monthly books, a cleanup, or QuickBooks help. You work with me.",
        body,
        [("Home", "/"), ("Services", "/services/")],
        [],
    )


def build_industries():
    for ind in INDUSTRIES:
        points = "<ul>" + "".join(f"<li>{esc(p)}</li>" for p in ind["points"]) + "</ul>"
        city_links = related_links([(f"/service-areas/{s}/", CITY_BY[s]["name"]) for s in ind["cities"]])
        rel = related_links([(f"/who-we-work-with/{s}/", IND_BY[s]["name"]) for s in ind["related"]])
        body = "".join(ind["paragraphs"])
        body += f"<section><h2>What the books usually need</h2>{points}<p>{esc(ind['limit'])}</p></section>"
        body += f"<section><h2>Where I see this work</h2><p>These are a few of the cities where this kind of business is common. I work with you wherever you are in the area, and with plenty of other businesses too.</p>{city_links}</section>"
        body += f"<section><h2>Other businesses I help</h2><p>Your business might look like one of these, or like something else entirely. Call me either way.</p>{rel}<p><a href=\"/who-we-work-with/\">All the business types</a></p></section>"
        body += "<section><h2>Services that apply</h2>" + service_links() + "</section>"
        write_inner(
            ind["title"], ind["description"], f"/who-we-work-with/{ind['slug']}/",
            ind["h1"], ind["lede"], body,
            [("Home", "/"), ("Who we work with", "/who-we-work-with/"), (ind["name"], f"/who-we-work-with/{ind['slug']}/")],
            [service_node(ind["name"] + " bookkeeping", f"/who-we-work-with/{ind['slug']}/", ind["description"], area())],
            ind["faqs"], "Questions",
        )
    cards = [(f"/who-we-work-with/{i['slug']}/", i["name"], i["lede"]) for i in INDUSTRIES]
    body = f'''<section><h2>I work with all kinds of small businesses</h2><p>These pages show how I usually set up the books for businesses I see around Simi Valley, so you can tell if it sounds like yours. If your business is missing, call anyway. What I need to know is your accounts, your volume, and the reports you want.</p>{hub_cards(cards)}</section>
<section><h2>The plans stay the same</h2><p>Monthly plans start at $349, $599, and $1,499. Catch-up and QuickBooks training are quoted on their own. I hand your CPA clean books, and they file the return. If you already have a payroll company, Strategic includes recording those entries. You work with me.</p>{service_links()}</section>'''
    write_inner(
        "Who I Work With | Glenhold Bookkeeping",
        "I keep books for contractors, restaurants, practices, shops, and every other small business around Simi Valley. Plans from $349.",
        "/who-we-work-with/",
        "Who I work with",
        "Find a business that sounds like yours. If it isn't listed, call me anyway.",
        body,
        [("Home", "/"), ("Who we work with", "/who-we-work-with/")],
        [],
    )


def build_cities():
    for city in CITIES:
        neighbors = related_links([(f"/service-areas/{s}/", CITY_BY[s]["name"]) for s in city["neighbors"]])
        inds = related_links([(f"/who-we-work-with/{s}/", IND_BY[s]["name"]) for s in city["industries"]])
        body = "".join(city["paragraphs"])
        body += f"<section><h2>Businesses in {esc(city['name'])}</h2><p>These are a few of the businesses I help here. If yours is different, I still want to hear about it.</p>{inds}</section>"
        body += f"<section><h2>Nearby</h2>{neighbors}<p><a href=\"/service-areas/\">The full service area</a></p></section>"
        body += "<section><h2>How to start</h2>" + service_links() + "</section>"
        write_inner(
            city["title"], city["description"], f"/service-areas/{city['slug']}/",
            city["h1"], city["lede"], body,
            [("Home", "/"), ("Service areas", "/service-areas/"), (city["name"], f"/service-areas/{city['slug']}/")],
            [service_node(f"Bookkeeping in {city['name']}", f"/service-areas/{city['slug']}/", city["description"], area())],
            city["faqs"], f"Questions about {city['name']}",
        )

    groups = []
    for city in CITIES:
        if city["group"] not in [g for g, _ in groups]:
            groups.append((city["group"], []))
        groups[[g for g, _ in groups].index(city["group"])][1].append(city)
    sections = []
    for group, members in groups:
        blocks = []
        for city in members:
            blocks.append(
                f'<section id="{city["slug"]}"><h3><a href="/service-areas/{city["slug"]}/">{esc(city["name"])}</a></h3><p>{esc(city["hub"])}</p></section>'
            )
        sections.append(f"<h2>{esc(group)}</h2><div class=\"region-grid\">{''.join(blocks)}</div>")
    body = '''<section><h2>Cities where I keep the books</h2><p>I'm in Simi Valley, and I work with small businesses across Ventura County and nearby Los Angeles. Pick your city and you'll see the kinds of local businesses I help and how a monthly close works. Oak Park, Winnetka, and Tarzana sit between cities on this list. Name your neighborhood when you write, and I'll take it from there.</p><p>We'll meet in person when that helps. The plans are the same everywhere: $349, $599, and $1,499 to start.</p></section>'''
    body += "".join(sections)
    body += "<section><h2>Same services in every city</h2>" + service_links() + "</section>"
    write_inner(
        "Bookkeeping Service Area | Simi Valley and Nearby",
        "I keep books for small businesses across Ventura County and nearby Los Angeles, from Simi Valley outward. Plans from $349. You work with me.",
        "/service-areas/",
        "Bookkeeping around Simi Valley",
        "Find your city. I'll show you how I help local owners keep the month clear.",
        body,
        [("Home", "/"), ("Service areas", "/service-areas/")],
        [],
    )


def build_faq():
    groups = OrderedDict()
    for item in FAQ:
        groups.setdefault(item["cat"], []).append(item)
    toc = '<div class="toc">' + "".join(
        f'<a href="#{cat.lower().replace(" ", "-")}">{esc(cat)}</a>' for cat in groups
    ) + "</div>"
    parts = ["<section><h2>Straight answers before we talk</h2><p>These are my prices and the way I work. Tax answers are general. Confirm anything that touches a return with your CPA or the agency named.</p>" + toc + "</section>"]
    for cat, items in groups.items():
        cid = cat.lower().replace(" ", "-")
        blocks = []
        for item in items:
            blocks.append(f'<details id="{esc(item["id"])}"><summary>{esc(item["q"])}</summary><p>{esc(item["a"])}</p></details>')
        parts.append(f'<section id="{cid}"><h2>{esc(cat)}</h2>{"".join(blocks)}</section>')
    parts.append("<section><h2>Go deeper</h2>" + service_links() + related_links([
        ("/resources/", "Resource hub"),
        ("/getting-started/", "What to give your bookkeeper"),
    ]) + "</section>")
    faqs = [(item["q"], item["a"]) for item in FAQ]
    write_inner(
        "Small Business Bookkeeping FAQ | Glenhold Bookkeeping",
        "Answers on Glenhold's prices, catch-up, QuickBooks, bookkeeper vs CPA, and California basics such as the $800 LLC tax and sales tax.",
        "/bookkeeping-faq/",
        "Small business bookkeeping FAQ",
        "What I charge, how catch-up works, and the California questions people ask me first.",
        "".join(parts),
        [("Home", "/"), ("Bookkeeping FAQ", "/bookkeeping-faq/")],
        [faq_node(faqs, "/bookkeeping-faq/")],
    )


def build_resources():
    body = '''<section><h2>A few places to start</h2><p>If you want the price, the handoff list, or a plain answer on the California $800 tax or sales tax, start here. I keep the books. Your CPA files the return.</p></section>
<section><h2>Start here</h2><ul>
<li><a href="/bookkeeping-faq/#pricing">What I charge</a> in Ventura County and nearby Los Angeles.</li>
<li><a href="/bookkeeping-faq/#bookkeeper-and-cpa">Bookkeeper and CPA</a>, and how we work together.</li>
<li><a href="/bookkeeping-faq/#california-basics">The $800 LLC tax and sales tax</a>, in plain language.</li>
<li><a href="/getting-started/">What to send me</a> before a cleanup or a monthly start.</li>
<li><a href="/pricing/">Essential, Core, and Strategic</a> side by side.</li>
</ul></section>
<section><h2>Services behind the answers</h2>''' + service_links() + "</section>"
    write_inner(
        "Bookkeeping Resources | Glenhold Bookkeeping",
        "A short index of Glenhold's bookkeeping answers: pricing, catch-up, QuickBooks, the $800 California LLC tax, and what to send a bookkeeper.",
        "/resources/",
        "Bookkeeping resources",
        "The answers, the checklist, and the services they point to.",
        body,
        [("Home", "/"), ("Resources", "/resources/")],
        [],
    )


def build_getting_started():
    body = '''<section><h2>What should you give a new bookkeeper?</h2><p>Start with a complete list of business accounts, statements for the periods being worked on, and access to the books you already have. A clear picture of what is available helps identify gaps. This checklist is for <a href="/monthly-bookkeeping/">ongoing bookkeeping</a> or a <a href="/cleanup-catch-up/">cleanup</a>. Not every line will apply. Ask how to share records before you send anything sensitive.</p></section>
<section><h2>Handoff checklist</h2><ol>
<li><strong>Business and contact details.</strong> The name you operate under, and who can explain a transaction.</li>
<li><strong>Every account.</strong> Checking, savings, cards, loans, and payment processors. Include accounts you closed or replaced.</li>
<li><strong>Statements.</strong> Every statement for the period, including opening and closing balances. Exports help. They do not replace the statement.</li>
<li><strong>The existing file.</strong> Your QuickBooks Online company, the last month that was finished, the last month that was reconciled, and any known problems. Those two months are often different.</li>
<li><strong>Loans.</strong> Statements or schedules that separate principal, interest, and the balance, when you have them.</li>
<li><strong>Payroll reports.</strong> If I need to record payroll journals, name the payroll provider and the reports it gives you. Your payroll company keeps running payroll.</li>
<li><strong>Owner transactions.</strong> Money you put in, money you took out, and business costs you paid personally.</li>
<li><strong>Deadlines and the CPA.</strong> Tax-preparer requests, lender dates, and who should receive the finished reports.</li>
</ol></section>
<section><h2>Three details that keep a handoff from stalling</h2><h3>Both sides of a transfer</h3><p>If cash moved between accounts, the records for both accounts need to be in the pile. One withdrawal does not explain the destination.</p><h3>The last reconciled month</h3><p>The last month with transactions typed in may not be the last month tied to a statement. Share both if you know them. If you do not, say that.</p><h3>What you cannot find</h3><p>A missing statement is useful information. Keep a short list of gaps so the work can be planned around them.</p></section>
<section><h2>After the handoff</h2><p>I'll talk through what matters first: a cleanup, monthly support, or <a href="/quickbooks-online/">QuickBooks help</a>. A free call is enough before you gather documents you may not need.</p><p class="byline">By Jack, Glenhold Bookkeeping. Updated November 11, 2026.</p></section>
<section><h2>Related</h2>''' + service_links() + "</section>"
    write_inner(
        "What to Give Your Bookkeeper | Glenhold Checklist",
        "A handoff checklist for small businesses: accounts, statements, loans, payroll reports, owner draws, and the questions to settle before files are sent.",
        "/getting-started/",
        "What to give your bookkeeper",
        "A shorter cleanup starts with a complete pile, including the gaps.",
        body,
        [("Home", "/"), ("Getting started", "/getting-started/")],
        [],
    )


def build_about():
    body = f'''<section class="about" style="padding-top:0"><div class="about-inner"><div class="about-photo-box"><picture><source srcset="/aboutme.webp" type="image/webp" /><img src="/aboutme.jpg" width="1100" height="1467" alt="Jack standing on coastal rocks holding a fishing rod" loading="lazy" decoding="async" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;object-position:center top;display:block;" /></picture></div><div class="about-content">
<p>As a Simi Valley local, I am proud to raise my family in this beautiful community. I've always had a natural affinity for math, and a college professor showed me it was a perfect fit for accounting.</p>
<p>After earning my Accounting degree, I began my career at a Big 4 firm, handling high-level accounting and bookkeeping work for multi-million dollar enterprises and auditing Fortune 500 financial services companies.</p>
<p>I founded Glenhold to bring that high-level expertise and insight to the local businesses that serve as the backbone of our country.</p>
<p>When I'm not working, I enjoy fly fishing, going on walks, and attending Mass with my wife and two children. I believe that professional excellence is rooted in personal character; as I often say, integrity is not something you can choose on a whim—it must be practiced daily over a lifetime.</p>
<div class="about-badges"><span class="badge">Former Big 4 Accountant</span><span class="badge">Certified QuickBooks ProAdvisor</span><span class="badge">LA &amp; Ventura County</span></div>
</div></div></section>
<section><h2>How we'll work together</h2><p>I'm Jack. I live in Simi Valley, and I do the books myself. Call me at <a href="tel:8054193451">(805) 419-3451</a> or email <a href="mailto:{EMAIL}">jack&#64;glenhold.com</a>. I'm around Monday through Saturday, 6am to 6pm Pacific.</p><p>You work with me. Monthly plans start at $349, $599, and $1,499. If you don't love the first month, it's free. I started at a Big 4 firm. I get the books clean so your CPA can file. I also post videos on YouTube at <a href="{YOUTUBE}" target="_blank" rel="noopener noreferrer">@BookkeepingWithJack</a>.</p><p>We'll meet in person when that helps, across the <a href="/service-areas/">cities I serve</a>. Day to day I work from your statements and QuickBooks.</p></section>'''
    write_inner(
        "About Jack | Glenhold Bookkeeping",
        "I'm Jack, in Simi Valley. Former Big 4 accountant and Certified QuickBooks ProAdvisor. I keep your books, and you work with me. Plans from $349.",
        "/about/",
        "About Jack",
        "I live here, I do the books myself, and you work with me.",
        body,
        [("Home", "/"), ("About", "/about/")],
        [],
    )


def build_pricing():
    body = f'''<section><h2>Three monthly starting prices</h2><p>Your quote reflects transaction volume, the number of accounts, and reporting complexity. Cleanup, catch-up, consulting, and training are scoped separately. The QuickBooks Online subscription is billed by Intuit, not included here.</p><div class="pricing-guarantee"><span>★</span> Love your first month of books, or it's free</div>{price_cards()}<p class="byline" style="margin-top:28px">The guarantee applies to the first month of monthly bookkeeping.</p></section>
<section><h2>What you can count on</h2><p>The same starting prices apply in every city I serve. I hand your CPA clean books. If you already use a payroll company, Strategic includes recording those journal entries. You pay Intuit for QuickBooks Online.</p><p>Read what I charge in <a href="/bookkeeping-faq/#ventura-cost">Ventura County</a> and <a href="/bookkeeping-faq/#los-angeles-cost">nearby Los Angeles</a>.</p></section>'''
    write_inner(
        "Bookkeeping Pricing from $349 a Month | Glenhold",
        "Glenhold monthly bookkeeping starts at $349, $599, and $1,499. Love your first month or it's free. Catch-up and QuickBooks training are quoted separately.",
        "/pricing/",
        "Straightforward monthly pricing",
        "Essential, Core, and Strategic. I'll tell you the quote before we start.",
        body,
        [("Home", "/"), ("Pricing", "/pricing/")],
        [],
        [
            ("How much does Glenhold bookkeeping cost?", "Monthly plans start at $349, $599, and $1,499. The quote depends on volume and complexity. Cleanup and training are extra."),
            ("What does the guarantee cover?", "Love your first month of monthly books, or that month is free. It does not price a cleanup project or the QuickBooks subscription."),
        ],
        "Pricing questions",
    )


def build_contact():
    body = '''<section><h2>What happens after you write</h2><p>I'll reply within one business day. I'm around Monday through Saturday, 6am to 6pm Pacific. Tell me your city, what kind of business you run, whether the books are current, and roughly how many accounts you have. Leave the statements out of this first note. Ask me how to send files.</p><p>You can also book a free call. I'll learn enough to tell you what the work looks like, and the quote follows once I understand the volume.</p><p>I'm in Simi Valley. If you're outside the communities I list, say so and I'll tell you if I can help.</p></section>'''
    write_inner(
        "Contact Glenhold Bookkeeping in Simi Valley",
        "Call Glenhold Bookkeeping at (805) 419-3451 or email jack@glenhold.com. Simi Valley, Monday through Saturday, 6am to 6pm Pacific.",
        "/contact/",
        "Contact Glenhold Bookkeeping",
        "Call, email, or send a note. A reply within one business day.",
        body,
        [("Home", "/"), ("Contact", "/contact/")],
        [],
    )


def build_home():
    home_faqs = [(item["q"], item["a"]) for item in FAQ if item.get("home")]
    city_chips = chips([(f"/service-areas/{c['slug']}/", c["name"]) for c in CITIES])
    ind_chips = chips([(f"/who-we-work-with/{i['slug']}/", i["name"]) for i in INDUSTRIES])
    main = f'''<section class="hero">
    <div class="hero-content">
      <div class="hero-eyebrow">Ventura County &amp; the Greater LA Area</div>
      <h1>Small business bookkeeping.<br/><em>Local. Clear. Personal.</em></h1>
      <p class="hero-sub">Your books should be current, and you should be able to read them. I keep them that way for small businesses around Simi Valley, from $349 a month. You work with me. Love your first month, or it's free.</p>
      <div class="hero-ctas">
        <a href="{CALENDAR}" target="_blank" rel="noopener noreferrer" class="btn-primary">Book a Free Call</a>
        <a href="#contact" class="btn-ghost">Send a Message</a>
      </div>
      <div class="hero-photo-mobile">
        <picture>
          <source srcset="/headshot.webp" type="image/webp" />
          <img src="/headshot.jpg" width="1000" height="1333" alt="Jack, founder of Glenhold Bookkeeping" decoding="async" style="width:80%;display:block;border-radius:6px;margin:0 auto;" />
        </picture>
      </div>
      <div class="hero-social">
        <a href="https://share.google/ZFSpIuhD39akrC2DT" target="_blank" rel="noopener noreferrer">★★★★★ &nbsp;Google Reviews</a>
        <a href="https://www.yelp.com/biz/glenhold-bookkeeping-simi-valley" target="_blank" rel="noopener noreferrer">★★★★★ &nbsp;Yelp Reviews</a>
      </div>
      <div class="hero-credentials" style="margin-top: 12px; display: flex; flex-direction: column; gap: 8px;">
        <div style="display: flex; align-items: center; gap: 8px;"><span style="color: var(--sage); font-size: 1rem; font-weight: 700;">✓</span><span style="color: rgba(255,255,255,0.55); font-size: 0.8rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;">Former Big 4 Accountant</span></div>
        <div style="display: flex; align-items: center; gap: 8px;"><span style="color: var(--sage); font-size: 1rem; font-weight: 700;">✓</span><span style="color: rgba(255,255,255,0.55); font-size: 0.8rem; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase;">Certified QuickBooks ProAdvisor</span></div>
      </div>
    </div>
    <div class="hero-photo">
      <div class="hero-photo-box">
        <picture>
          <source srcset="/headshot.webp" type="image/webp" />
          <img src="/headshot.jpg" width="1000" height="1333" alt="Jack, founder of Glenhold Bookkeeping" decoding="async" fetchpriority="high" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;object-position:center -10%;display:block;" />
        </picture>
      </div>
    </div>
  </section>
  <section class="services" id="services">
    <div class="section-label">What I Do</div>
    <h2 class="section-title">Bookkeeping services</h2>
    <p class="section-sub">Choose the level of support that fits where your business is right now. You can always adjust as you grow.</p>
    <div class="services-grid">
      <div class="service-card"><div class="service-icon">📅</div><h3>Monthly Bookkeeping</h3><p>Books closed on schedule every month, with real numbers when you need them.</p><ul class="service-list"><li>P&amp;L and balance sheet by the 15th</li><li>Categorization rules built for your business</li><li>Monthly bank and credit card reconciliation</li><li>Email support between closes</li><li>Optional monthly video call (Strategic tier)</li></ul><a class="text-link" href="/monthly-bookkeeping/">Explore monthly bookkeeping →</a></div>
      <div class="service-card"><div class="service-icon">🧹</div><h3>Cleanup &amp; Catch-Up</h3><p>Months or years behind? I'll sort it out and hand back records ready for filing or financing.</p><ul class="service-list"><li>Rebuild books for any time period</li><li>Every transaction classified and matched</li><li>Bulk import from statements and exports</li><li>Clean handoff to your CPA</li></ul><a class="text-link" href="/cleanup-catch-up/">Explore cleanup &amp; catch-up →</a></div>
      <div class="service-card"><div class="service-icon">🎓</div><h3>Consulting &amp; Training</h3><p>Doing your own books but want it done right? I'll set up your system and review your work on your schedule.</p><ul class="service-list"><li>QuickBooks Online setup for your business</li><li>Chart of accounts built for how you operate</li><li>Accuracy check-ins on your schedule</li><li>Easy to move to full monthly service later</li></ul><a class="text-link" href="/quickbooks-online/">Explore QuickBooks support →</a></div>
    </div>
    <div class="content-links" style="margin-top:28px"><a href="/services/">All services</a><a href="/financial-statements/">Financial statements</a><a href="/cpa-ready-books/">CPA-ready books</a><a href="/loan-ready-books/">Loan-ready financials</a></div>
  </section>
  <section class="pricing" id="pricing">
    <div class="section-label">Pricing</div>
    <h2 class="section-title">Straightforward monthly pricing</h2>
    <p class="section-sub">Choose clean books, clearer insights, or a monthly walkthrough. Your final quote reflects transaction volume, number of accounts, and reporting complexity.</p>
    <div class="pricing-guarantee"><span>★</span> Love your first month of books, or it's on me</div>
    {price_cards()}
  </section>
  <section class="local-section" id="service-areas"><div class="section-label">Close to home</div><h2 class="section-title">I keep the books for the businesses around Simi Valley</h2><p class="section-sub">Shops, trades, practices, restaurants, and everything in between. I set the books up around how you operate.</p><p class="section-sub">I'm in Simi Valley. I work with owners across Ventura County and nearby Los Angeles, and we meet when that helps.</p>{city_chips}<div class="content-links"><a href="/service-areas/">Find your city</a><a href="/getting-started/">What to send me</a></div></section>
  <section class="faq-section" id="who"><div class="section-label">Every kind of small business</div><h2 class="section-title">If you run it, I can keep the books</h2><p class="section-sub">A few of the businesses I help are listed here. If yours is missing, you're still in the right place.</p>{ind_chips}<div class="content-links"><a href="/who-we-work-with/">See how I work with each</a></div></section>
  <section class="faq-section" id="faq"><div class="section-label">Before we talk</div><h2 class="section-title">Common bookkeeping questions</h2>{faq_html(home_faqs)}<div class="content-links"><a href="/bookkeeping-faq/">Read all bookkeeping FAQs</a></div></section>
  <section class="about" id="about"><div class="about-inner"><div class="about-photo-box"><picture><source srcset="/aboutme.webp" type="image/webp" /><img src="/aboutme.jpg" width="1100" height="1467" alt="Jack standing on coastal rocks holding a fishing rod" loading="lazy" decoding="async" style="position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;object-position:center top;display:block;" /></picture></div><div class="about-content"><div class="section-label">About Me</div><h2 class="section-title">Hi, I'm Jack</h2>
<p>As a Simi Valley local, I am proud to raise my family in this beautiful community. I've always had a natural affinity for math, and a college professor showed me it was a perfect fit for accounting.</p>
<p>After earning my Accounting degree, I began my career at a Big 4 firm, handling high-level accounting and bookkeeping work for multi-million dollar enterprises and auditing Fortune 500 financial services companies.</p>
<p>I founded Glenhold to bring that high-level expertise and insight to the local businesses that serve as the backbone of our country.</p>
<p>When I'm not working, I enjoy fly fishing, going on walks, and attending Mass with my wife and two children. I believe that professional excellence is rooted in personal character; as I often say, integrity is not something you can choose on a whim—it must be practiced daily over a lifetime.</p>
<div class="about-badges"><span class="badge">Former Big 4 Accountant</span><span class="badge">Certified QuickBooks ProAdvisor</span><span class="badge">LA &amp; Ventura County</span></div>
<p style="margin-top:18px"><a href="/about/">More about Jack</a></p>
</div></div></section>
{cta("Every month you wait costs you clarity", "One free call today could save you hours of stress this year.")}
{contact_block("/")}'''
    write_page(
        "Small Business Bookkeeping in Simi Valley | Glenhold",
        "I keep the books for small businesses around Simi Valley. Monthly plans from $349, catch-up when you're behind, and QuickBooks Online help. You work with me.",
        "/",
        main,
        [("Home", "/")],
        [faq_node(home_faqs, "/")],
        CITIES,
        area(),
    )


def write_robots():
    lines = [
        "# AI and search crawlers are explicitly welcome.",
        "# xAI has no single documented crawler token. The Grok names below are the ones",
        "# in public crawler lists. User-agent: * already allows any other agent.",
        "",
    ]
    for bot in [
        "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-Web",
        "Claude-SearchBot", "anthropic-ai", "PerplexityBot", "Perplexity-User",
        "Google-Extended", "Googlebot", "Bingbot", "Applebot", "Applebot-Extended",
        "GrokBot", "xAI-Grok", "Grok-DeepSearch", "xAI-SearchBot",
    ]:
        lines.append(f"User-agent: {bot}")
        lines.append("Allow: /")
        lines.append("")
    lines.append("User-agent: *")
    lines.append("Allow: /")
    lines.append("")
    lines.append("Sitemap: https://glenhold.com/sitemap.xml")
    lines.append("")
    (ROOT / "robots.txt").write_text("\n".join(lines), encoding="utf-8")


def write_sitemap():
    urls = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for page in sorted(PAGES, key=lambda p: (p["path"] != "/", p["path"])):
        urls.append(f"  <url><loc>{abs_url(page['path'])}</loc><lastmod>{LASTMOD}</lastmod></url>")
    urls.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(urls) + "\n", encoding="utf-8")


def write_llms():
    facts = f'''# Glenhold Bookkeeping

> I'm Jack. I keep the books for small businesses around Simi Valley, California, in every kind of industry. Monthly bookkeeping starts at $349, $599, and $1,499. Love your first month of books, or it's free.

## Facts

- Owner: Jack, former Big 4 accountant and Certified QuickBooks ProAdvisor
- You work directly with Jack
- Based in Simi Valley, California, serving Ventura County and nearby Los Angeles communities
- Phone: (805) 419-3451
- Email: jack@glenhold.com
- Website: https://glenhold.com/
- Hours: Monday through Saturday, 6:00 a.m. to 6:00 p.m. Pacific Time
- We meet in person when that helps. Day to day I work from your statements and QuickBooks Online
- YouTube: {YOUTUBE}
- I hand your CPA clean, tax-ready books. Your preparer files the return
- If you already have a payroll company, the Strategic plan includes recording those journal entries
- QuickBooks Online is a separate subscription you pay to Intuit
- I set up and teach QuickBooks Online
- Guarantee: love your first month of monthly books, or that month is free

## Prices

- Essential monthly bookkeeping: starting at $349 per month. Categorization, reconciliation, monthly statements, clean books for tax season
- Core monthly bookkeeping: starting at $599 per month. Essential, plus a quarterly profit and expense summary, year-to-date comparison, and priority support
- Strategic monthly bookkeeping: starting at $1,499 per month. Core, plus custom reports, accrual accounting, payroll journal entries, loan tracking, and a monthly call
- Cleanup, catch-up, consulting, and training are quoted separately
- Quotes move with transaction volume, number of accounts, and reporting complexity
- No city surcharge is published

## California notes, general only

- Most California LLCs owe an annual minimum franchise tax of $800. A first-year waiver applied only to LLCs that registered in 2021, 2022, or 2023. Your CPA files it. I keep the books
- Sole proprietors pay income tax in a different way. The $800 minimum is for LLCs and corporations
- An additional LLC fee can apply based on total income, historically starting at $250,000. Confirm current tiers with the Franchise Tax Board or a CPA
- California statewide base sales and use tax is 7.25 percent. District taxes add more and change. I record tax collected as a liability. Your preparer files the return

## Key pages

- [Home](https://glenhold.com/): landing page, services, pricing, contact form
- [Services](https://glenhold.com/services/): monthly, cleanup, QuickBooks, statements, CPA-ready, loan-ready
- [Pricing](https://glenhold.com/pricing/): Essential, Core, Strategic
- [FAQ](https://glenhold.com/bookkeeping-faq/): {len(FAQ)} standalone answers
- [Service areas](https://glenhold.com/service-areas/): Ventura County and nearby Los Angeles cities where I keep the books
- [Who we work with](https://glenhold.com/who-we-work-with/): every kind of small business
- [About](https://glenhold.com/about/): Jack
- [Contact](https://glenhold.com/contact/): (805) 419-3451, jack@glenhold.com
'''
    (ROOT / "llms.txt").write_text(facts, encoding="utf-8")
    full = [facts, "\n## Every page\n"]
    for page in sorted(PAGES, key=lambda p: p["path"]):
        full.append(f"- [{page['title']}]({abs_url(page['path'])}): {page['description']}")
    full.append("\n## FAQ answers\n")
    for item in FAQ:
        full.append(f"### {item['q']}\n\n{item['a']}\n")
    (ROOT / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")


def write_indexnow():
    (ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY + "\n", encoding="utf-8")


def validate():
    errors = []
    html_files = list(ROOT.glob("index.html")) + list(ROOT.glob("*/index.html")) + list(ROOT.glob("*/*/index.html"))
    titles, descriptions = {}, {}
    required = [
        "AW-17998714201",
        "CFtmLaAKWainpP7irzAdWa",
        "allow_enhanced_conversions: false",
        "xvzwqvgv",
        "oaiq(",
        'src="/site.js"',
    ]
    for path in html_files:
        text = path.read_text(encoding="utf-8")
        rel = "/" + str(path.relative_to(ROOT))
        for token in required:
            if token not in text:
                errors.append(f"{rel} missing {token}")
        if "AggregateRating" in text or '"@type":"Review"' in text or '"@type": "Review"' in text:
            errors.append(f"{rel} has review schema")
        if len(re.findall(r"<h1[\s>]", text)) != 1:
            errors.append(f"{rel} h1 count {len(re.findall(r'<h1[\\s>]', text))}")
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text):
            try:
                import json
                json.loads(blob)
            except Exception as exc:
                errors.append(f"{rel} json-ld {exc}")
        title = re.search(r"<title>(.*?)</title>", text)
        desc = re.search(r'<meta name="description" content="(.*?)"', text)
        if not title or not desc:
            errors.append(f"{rel} missing title or description")
        else:
            titles.setdefault(title.group(1), []).append(rel)
            descriptions.setdefault(desc.group(1), []).append(rel)
        for href in re.findall(r'href="(/[^"#?]*)', text):
            target = href
            if target.endswith("/"):
                file = ROOT / "index.html" if target == "/" else ROOT / target.strip("/") / "index.html"
            else:
                file = ROOT / target.lstrip("/")
            if not file.exists():
                errors.append(f"{rel} broken {href}")
        if "our clients" in text.lower() or "we have served" in text.lower():
            errors.append(f"{rel} invented client claim")
    for title, paths in titles.items():
        if len(paths) > 1:
            errors.append(f"duplicate title {title}: {paths}")
    for desc, paths in descriptions.items():
        if len(paths) > 1:
            errors.append(f"duplicate description: {paths}")
    if not (40 <= len(FAQ) <= 60):
        errors.append(f"FAQ count {len(FAQ)}")
    for slug in {s for c in CITIES for s in c["neighbors"]}:
        if slug not in CITY_BY:
            errors.append(f"bad neighbor {slug}")
    for slug in {s for c in CITIES for s in c["industries"]} | {s for i in INDUSTRIES for s in i["related"]}:
        if slug not in IND_BY:
            errors.append(f"bad industry {slug}")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"OK pages={len(html_files)} faqs={len(FAQ)} cities={len(CITIES)} industries={len(INDUSTRIES)}")


def main():
    PAGES.clear()
    build_home()
    build_services()
    build_service_hub()
    build_industries()
    build_cities()
    build_faq()
    build_resources()
    build_getting_started()
    build_about()
    build_pricing()
    build_contact()
    write_robots()
    write_sitemap()
    write_llms()
    write_indexnow()
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    validate()


if __name__ == "__main__":
    main()
