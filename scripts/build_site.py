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
            "body": '''<section><h2>Monthly bookkeeping for every kind of small business</h2><p>Glenhold Bookkeeping provides ongoing bookkeeping for small businesses in Simi Valley and nearby Ventura County and Los Angeles communities. You work directly with Jack, a former Big 4 accountant and Certified QuickBooks ProAdvisor. You do not need to fit a particular industry. The scope is your accounts, your volume, and the reports you want.</p></section>
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
            "lede": "Behind on the books? Start with a clear scope, not a guess.",
            "offer": None,
            "body": '''<section><h2>Bring unfinished bookkeeping up to date</h2><p>Cleanup means correcting books that already exist. Catch-up means recording periods that were never finished. Many projects are both. Glenhold Bookkeeping, based in Simi Valley, does this for small businesses across industries in nearby Ventura County and Los Angeles communities. You can stop when the backlog is done, or continue with monthly bookkeeping.</p></section>
<section><h2>What a project can cover</h2><ul><li>Organizing statements, exports, and the existing accounting file.</li><li>Importing missing transactions and classifying income and expenses.</li><li>Reviewing duplicates, unmatched transfers, and balances that do not tie.</li><li>Reconciling bank and credit card accounts to the statements you have.</li><li>Tidying the chart of accounts so the reports can be read.</li><li>A handoff your CPA can use. Glenhold does not file the return.</li></ul><p>If an entry is unclear, the next step is to ask you. Guessing the purpose of a transfer is how cleanups fail.</p></section>
<section><h2>What to gather</h2><p>The months in question, every business bank and credit card account including accounts you closed, and statements that show opening and closing balances. Add loans, payroll reports, and owner contributions or draws when they matter. If you changed banks, include both sides. The <a href="/getting-started/">handoff checklist</a> is the longer version. Ask how to send files before you email anything sensitive.</p></section>
<section><h2>Price and timing</h2><p>Cleanup is quoted from the number of periods, accounts, transactions, and corrections. The monthly starting prices of $349, $599, and $1,499 are not a cleanup quote. Timing depends on the backlog, missing records, and how fast open questions get answered. Name any tax or lender deadline on the first call.</p><p>When the project is done you can move to <a href="/monthly-bookkeeping/">monthly bookkeeping</a> or to <a href="/quickbooks-online/">training and check-ins</a> if you want the file back.</p></section>''',
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
            "body": '''<section><h2>QuickBooks Online help from a Certified ProAdvisor</h2><p>Glenhold offers QuickBooks Online setup, consulting, and training for owners who want a clearer system or who want to keep doing the books themselves. Jack is a Certified QuickBooks ProAdvisor and a former Big 4 accountant, based in Simi Valley. The published offer is QuickBooks Online. QuickBooks Desktop is not a listed service. Say so on the intro call if your file is still on Desktop.</p></section>
<section><h2>What setup covers</h2><ul><li>A QuickBooks Online file built around how money moves through the business.</li><li>A chart of accounts for income, expenses, assets, liabilities, and equity.</li><li>A routine for reviewing activity, separating transfers from income and expenses, and reconciling.</li><li>Accuracy check-ins on a schedule you agree to, if you want a review rather than a handoff.</li></ul><p>Too many overlapping accounts make a profit and loss hard to read. Too few hide the thing you meant to see. Setup starts by asking which reports you actually use.</p></section>
<section><h2>Training or a monthly plan</h2><p>Choose training when you want to keep the day-to-day work. Choose <a href="/monthly-bookkeeping/">monthly bookkeeping</a> when you want categorization, reconciliation, and statements handled for you. You can start with one and move to the other. Consulting and training are scoped separately. The monthly plans start at $349. That number is not a training quote and it does not include the QuickBooks subscription, which you pay to Intuit.</p><p>An existing file does not have to be thrown out. It may need a chart review, or a <a href="/cleanup-catch-up/">cleanup</a>, before a routine makes sense.</p></section>''',
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
            "body": '''<section><h2>What you actually get each month</h2><p>Every Glenhold monthly plan includes financial statements: a profit and loss for the period and a balance sheet as of the close. The target is the 15th of the following month, if statements and answers show up in time. These reports are part of monthly bookkeeping. They are not a separately priced product and not a compilation, review, or audit.</p><p>A profit and loss shows income, expenses, and profit for a stretch of time. It does not, by itself, show the cash in the bank. A balance sheet shows what the business owns, what it owes, and the owner's equity on one date. You usually need both.</p></section>
<section><h2>What Core and Strategic add</h2><ul><li><strong>Essential, from $349:</strong> the monthly statements and the reconciliation behind them.</li><li><strong>Core, from $599:</strong> those statements, plus a quarterly profit and expense summary and a year-to-date performance comparison.</li><li><strong>Strategic, from $1,499:</strong> Core, plus custom financial reports, accrual accounting, payroll journal entries, loan tracking, and a monthly call to walk through the numbers.</li></ul><p>Accrual accounting is listed on Strategic, not on Essential or Core. If unearned deposits or unpaid bills need to sit on the balance sheet, say so before you pick a plan. Your CPA can confirm which basis the tax return expects. Glenhold does not file that return.</p></section>
<section><h2>Who the statements are for</h2><p>Owners use them to see the month. CPAs use them at tax time. Lenders often ask for them when you apply for financing. Glenhold prepares the bookkeeping reports. It does not prepare a loan application and it does not provide audit assurance. If the history is incomplete, <a href="/cleanup-catch-up/">catch the books up</a> before you lean on a statement.</p></section>''',
            "faqs": [
                ("Are financial statements included in the monthly price?", "Yes. A profit and loss and a balance sheet are part of Essential, Core, and Strategic. They are not billed as an extra report fee on this site."),
                ("Is this an audit or a review?", "No. Glenhold does bookkeeping and management statements from the reconciled accounts. Audits and reviews are attestation services this firm does not offer."),
            ],
        },
        {
            "path": "/cpa-ready-books/",
            "name": "CPA-ready books",
            "title": "CPA-Ready Books for Tax Season | Glenhold Bookkeeping",
            "description": "Reconciled books and financial statements your CPA can use. Glenhold in Simi Valley does the bookkeeping and does not file the tax return.",
            "h1": "Books your CPA can actually use",
            "lede": "Tax season goes faster when the year is reconciled before the CPA opens the file.",
            "offer": None,
            "body": '''<section><h2>A handoff, not a tax return</h2><p>Glenhold Bookkeeping gets the accounts categorized, the bank and cards reconciled, and the profit and loss and balance sheet ready to send. That is what "clean books for tax season" means on this site. It does not mean the return has been prepared. Your CPA or other tax preparer still reviews the books and files. Jack is a former Big 4 accountant. This site does not list him as your CPA, and Big 4 experience is not a license to file your return.</p></section>
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
            "description": "Reconciled financial statements lenders often ask to see. Glenhold prepares the books, not the loan application, for Simi Valley-area businesses.",
            "h1": "Books a lender can read",
            "lede": "Lenders ask for statements. They do not accept a checkbook. Glenhold can produce the statements. It cannot approve the loan.",
            "offer": None,
            "body": '''<section><h2>What lenders usually ask the books to show</h2><p>A recent profit and loss, a balance sheet, and bank statements for the same months. Sometimes they also want the figures to tie: the cash on the balance sheet should agree with the statement, and transfers should not be hiding inside sales. Glenhold's cleanup and monthly work are built to get you there. The deliverable is reconciled bookkeeping and financial statements. It is not a loan application, a business plan, or a promise that anyone will lend.</p></section>
<section><h2>What this is not</h2><ul><li>Not a conversation with your lender. You or your broker send the package.</li><li>Not a personal financial statement. Those are yours to complete.</li><li>Not a tax return. Lenders often want returns from your CPA as well.</li><li>Not an audit. There is no assurance report.</li></ul><p>If the books are months behind, the first step is <a href="/cleanup-catch-up/">catch-up</a>, scoped to the periods the lender named. If they are current, <a href="/financial-statements/">monthly statements</a> are already part of the plans that start at $349, $599, and $1,499. Tell Jack the deadline on the first call. A date changes the schedule. It does not change the fact that missing statements cannot be invented.</p></section>''',
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
        ("/cpa-ready-books/", "CPA-ready books", "Reconciled records for tax season. Glenhold does not file the return."),
        ("/loan-ready-books/", "Loan-ready financials", "Statements a lender can read. Not a loan application and not an approval."),
    ]
    body = f'''<section><h2>Three ways to start, and the reports they produce</h2><p>The offers on the current Glenhold site are monthly bookkeeping, cleanup and catch-up, and QuickBooks Online consulting and training. Financial statements, a CPA handoff, and lender-ready reports are what that work produces. They are not extra brands with extra prices. Monthly plans start at $349, $599, and $1,499. Love your first month of books, or it's free. Cleanup and training are quoted on their own.</p>{hub_cards(cards)}</section>
<section><h2>Not included, on purpose</h2><ul><li>Tax return preparation and filing.</li><li>Sales-tax return filing.</li><li>Running payroll. Strategic can record payroll journal entries from your payroll provider.</li><li>A QuickBooks Online subscription. That is billed by Intuit.</li><li>Audits, reviews, or trust-account compliance.</li></ul><p>Jack does the work. He is a former Big 4 accountant and a Certified QuickBooks ProAdvisor. The firm does not niche by industry. <a href="/who-we-work-with/">See the kinds of businesses</a> the books often come from, then call even if yours is not on the list.</p></section>'''
    write_inner(
        "Bookkeeping Services | Glenhold Bookkeeping",
        "Monthly bookkeeping, catch-up, and QuickBooks Online setup from Glenhold in Simi Valley. Plans from $349. Tax filing is separate.",
        "/services/",
        "Bookkeeping services",
        "Pick the job. The industry is not the filter.",
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
        body += f"<section><h2>Where this comes up</h2><p>These cities are examples of where this kind of business is common. They are not a client list, and they are not the only places Glenhold works.</p>{city_links}</section>"
        body += f"<section><h2>Other kinds of businesses</h2><p>Glenhold does not niche. If your business is not this one, it can still be a fit.</p>{rel}<p><a href=\"/who-we-work-with/\">All the business types</a></p></section>"
        body += "<section><h2>Services that apply</h2>" + service_links() + "</section>"
        write_inner(
            ind["title"], ind["description"], f"/who-we-work-with/{ind['slug']}/",
            ind["h1"], ind["lede"], body,
            [("Home", "/"), ("Who we work with", "/who-we-work-with/"), (ind["name"], f"/who-we-work-with/{ind['slug']}/")],
            [service_node(ind["name"] + " bookkeeping", f"/who-we-work-with/{ind['slug']}/", ind["description"], area())],
            ind["faqs"], "Questions",
        )
    cards = [(f"/who-we-work-with/{i['slug']}/", i["name"], i["lede"]) for i in INDUSTRIES]
    body = f'''<section><h2>Every kind of small business, listed so you can find yourself</h2><p>Glenhold Bookkeeping does not niche. The pages below describe how the books usually work in businesses that are common around Simi Valley. They are not a gate. A business that is missing from the list is still invited. Scope comes from your accounts, your volume, and the reports you need.</p>{hub_cards(cards)}</section>
<section><h2>What does not change by industry</h2><p>Monthly plans still start at $349, $599, and $1,499. Cleanup and QuickBooks training are still quoted separately. Tax returns, sales-tax filings, and payroll processing are still outside the bookkeeping. Trust accounts for attorneys, brokers, and property managers are still not a service. Jack still does the work.</p>{service_links()}</section>'''
    write_inner(
        "Who Glenhold Works With | Small Businesses of Every Kind",
        "Glenhold does not niche. Bookkeeping for contractors, restaurants, practices, shops, and every other small business near Simi Valley.",
        "/who-we-work-with/",
        "Who we work with",
        "The industry is not the filter. The books are.",
        body,
        [("Home", "/"), ("Who we work with", "/who-we-work-with/")],
        [],
    )


def build_cities():
    for city in CITIES:
        neighbors = related_links([(f"/service-areas/{s}/", CITY_BY[s]["name"]) for s in city["neighbors"]])
        inds = related_links([(f"/who-we-work-with/{s}/", IND_BY[s]["name"]) for s in city["industries"]])
        body = "".join(city["paragraphs"])
        body += f"<section><h2>Businesses in {esc(city['name'])}</h2><p>These are common local business types, not a menu you have to order from. Glenhold works with small businesses across industries.</p>{inds}</section>"
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
    body = '''<section><h2>About an hour from Simi Valley, traffic permitting</h2><p>Glenhold Bookkeeping is based in Simi Valley, California. There is no published street address and no office in each city. Day-to-day bookkeeping is remote. In-person meetings are by arrangement when they help. The focus is roughly an hour's drive. Some cities on this list, including Ojai, Malibu, Glendale, and parts of the east Valley, often take longer. Those pages say so.</p><p>Oak Park, Winnetka, and Tarzana do not have their own pages. They sit between cities that do, and they are part of the same service area. Name the neighborhood when you write.</p></section>'''
    body += "".join(sections)
    body += "<section><h2>Same services in every city</h2>" + service_links() + "</section>"
    write_inner(
        "Bookkeeping Service Area | Simi Valley and Nearby",
        "Glenhold serves small businesses within about an hour of Simi Valley, across Ventura County and nearby Los Angeles. Remote books. No branch offices.",
        "/service-areas/",
        "Bookkeeping around Simi Valley",
        "One firm. A region of cities. No claim of an office in each of them.",
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
    parts = ["<section><h2>Answers written to be used on their own</h2><p>Each answer stands alone. Prices are Glenhold's published starting prices, not a survey of other firms. Tax statements are general. Confirm anything that touches a return with your CPA or the agency named.</p>" + toc + "</section>"]
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
        "Prices, scope, and California basics, in answers a person can quote.",
        "".join(parts),
        [("Home", "/"), ("Bookkeeping FAQ", "/bookkeeping-faq/")],
        [faq_node(faqs, "/bookkeeping-faq/")],
    )


def build_resources():
    body = '''<section><h2>Short paths into the longer answers</h2><p>These pages are the practical ones: what bookkeeping costs here, what to hand a new bookkeeper, and the California items owners ask about before they call. Glenhold Bookkeeping is a Simi Valley-based firm. It does not file tax returns.</p></section>
<section><h2>Start here</h2><ul>
<li><a href="/bookkeeping-faq/#pricing">What monthly bookkeeping costs</a>, including the Ventura County and Los Angeles answers.</li>
<li><a href="/bookkeeping-faq/#bookkeeper-and-cpa">Bookkeeper versus CPA</a>, and what Glenhold will not file.</li>
<li><a href="/bookkeeping-faq/#california-basics">California $800 franchise tax and sales tax</a>, stated generally.</li>
<li><a href="/getting-started/">What to give your bookkeeper</a> before a cleanup or a monthly start.</li>
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
<li><strong>Payroll reports.</strong> If journals need to be recorded, name the payroll provider and the reports it gives you. Glenhold does not run payroll.</li>
<li><strong>Owner transactions.</strong> Money you put in, money you took out, and business costs you paid personally.</li>
<li><strong>Deadlines and the CPA.</strong> Tax-preparer requests, lender dates, and who should receive the finished reports.</li>
</ol></section>
<section><h2>Three details that keep a handoff from stalling</h2><h3>Both sides of a transfer</h3><p>If cash moved between accounts, the records for both accounts need to be in the pile. One withdrawal does not explain the destination.</p><h3>The last reconciled month</h3><p>The last month with transactions typed in may not be the last month tied to a statement. Share both if you know them. If you do not, say that.</p><h3>What you cannot find</h3><p>A missing statement is useful information. Keep a short list of gaps so the work can be planned around them.</p></section>
<section><h2>After the handoff</h2><p>Jack will talk through priorities and whether the next step is cleanup, monthly support, or <a href="/quickbooks-online/">QuickBooks consulting</a>. A free introductory call is enough before you gather documents you may not need.</p><p class="byline">By Jack, founder of Glenhold Bookkeeping. Updated November 11, 2026.</p></section>
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
<section><h2>The firm, in one place</h2><p>Glenhold Bookkeeping is a Simi Valley-based bookkeeping firm owned by Jack. The legal entity is Glenhold Advisory LLC, doing business as Glenhold Bookkeeping. Phone <a href="tel:8054193451">(805) 419-3451</a>. Email <a href="mailto:{EMAIL}">jack&#64;glenhold.com</a>. Hours are Monday through Saturday, 6am to 6pm Pacific. No street address is published.</p><p>You work directly with Jack. Monthly plans start at $349, $599, and $1,499. Love your first month of books, or it's free. Tax return preparation is not a service, even though the career started at a Big 4 firm. Jack also posts bookkeeping videos on YouTube at <a href="{YOUTUBE}" target="_blank" rel="noopener noreferrer">@BookkeepingWithJack</a>.</p><p>The day-to-day work is remote. In-person meetings are by arrangement inside the <a href="/service-areas/">service area</a>, about an hour from Simi Valley, with some cities often taking longer.</p></section>'''
    write_inner(
        "About Jack | Glenhold Bookkeeping",
        "Jack, a Simi Valley local, former Big 4 accountant, and Certified QuickBooks ProAdvisor, owns Glenhold Bookkeeping (Glenhold Advisory LLC).",
        "/about/",
        "About Jack",
        "Former Big 4 accountant. Certified QuickBooks ProAdvisor. Based in Simi Valley.",
        body,
        [("Home", "/"), ("About", "/about/")],
        [],
    )


def build_pricing():
    body = f'''<section><h2>Three monthly starting prices</h2><p>Your quote reflects transaction volume, the number of accounts, and reporting complexity. Cleanup, catch-up, consulting, and training are scoped separately. The QuickBooks Online subscription is billed by Intuit, not included here.</p><div class="pricing-guarantee"><span>★</span> Love your first month of books, or it's free</div>{price_cards()}<p class="byline" style="margin-top:28px">The guarantee applies to the first month of monthly bookkeeping.</p></section>
<section><h2>What the plans do not include</h2><ul><li>Tax returns, sales-tax returns, and payroll tax returns.</li><li>Running payroll. Strategic includes payroll journal entries from your provider.</li><li>Audit, review, or trust-account compliance.</li><li>A city surcharge. The same starting prices apply across the service area.</li></ul><p>Read the <a href="/bookkeeping-faq/#ventura-cost">Ventura County price answer</a> and the <a href="/bookkeeping-faq/#los-angeles-cost">Los Angeles price answer</a>. They cite these prices. They do not invent a market average.</p></section>'''
    write_inner(
        "Bookkeeping Pricing from $349 a Month | Glenhold",
        "Glenhold monthly bookkeeping starts at $349, $599, and $1,499. Love your first month or it's free. Catch-up and QuickBooks training are quoted separately.",
        "/pricing/",
        "Straightforward monthly pricing",
        "Essential, Core, and Strategic. Starting prices, not a surprise menu.",
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
    body = '''<section><h2>What happens after you write</h2><p>Jack replies within one business day. Hours are Monday through Saturday, 6am to 6pm Pacific. The message comes to jack@glenhold.com. It does not need your bank login, and it should not include statements. Say the city, the kind of business, whether the books are current, and roughly how many accounts you have.</p><p>You can also book a free introductory call. That call is a fit conversation, not a finished quote, until the volume is clear.</p><p>Glenhold Bookkeeping is based in Simi Valley. There is no walk-in office. If you are outside the roughly one-hour service area, say so.</p></section>'''
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
      <p class="hero-sub">Small business bookkeeping across industries in Simi Valley and surrounding Ventura County and LA communities, from $349/month. Work directly with a former Big 4 accountant. Love your first month of books, or it's free.</p>
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
  <section class="local-section" id="service-areas"><div class="section-label">Close to home</div><h2 class="section-title">A local bookkeeper for the businesses around Simi Valley</h2><p class="section-sub">Glenhold works with small businesses across industries. From professional services and retail to home services and other owner-run businesses, the bookkeeping is tailored to how you operate.</p><p class="section-sub">Based in Simi Valley. The local focus is roughly an hour away, depending on traffic. Remote bookkeeping, with in-person meetings by arrangement. No street address is published.</p>{city_chips}<div class="content-links"><a href="/service-areas/">Read the service-area guide</a><a href="/getting-started/">Prepare for a bookkeeping handoff</a></div></section>
  <section class="faq-section" id="who"><div class="section-label">Every kind of small business</div><h2 class="section-title">No niche required</h2><p class="section-sub">These are common local businesses, not a limit. If yours is missing, you are still in the right place.</p>{ind_chips}<div class="content-links"><a href="/who-we-work-with/">How Glenhold works with each</a></div></section>
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
        "Small business bookkeeping in Simi Valley and nearby Ventura County and LA communities. Monthly plans from $349, catch-up work, and QuickBooks Online help.",
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
        "# xAI has not published one official user-agent. The Grok tokens below are the names",
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

> Glenhold Bookkeeping is a Simi Valley-based bookkeeping firm owned by Jack and operated by Glenhold Advisory LLC. It serves small businesses of every kind within about an hour of Simi Valley, California. Monthly bookkeeping starts at $349, $599, and $1,499. Love your first month of books, or it is free.

## Facts

- Legal entity: Glenhold Advisory LLC, doing business as Glenhold Bookkeeping
- Owner: Jack, former Big 4 accountant and Certified QuickBooks ProAdvisor
- You work directly with Jack
- Base: Simi Valley, California. No street address is published. No walk-in office
- Phone: (805) 419-3451
- Email: jack@glenhold.com
- Website: https://glenhold.com/
- Hours: Monday through Saturday, 6:00 a.m. to 6:00 p.m. Pacific Time
- Service model: remote bookkeeping, with in-person meetings by arrangement in the service area
- YouTube: {YOUTUBE}
- Not offered: tax return preparation, sales-tax filing, running payroll, audits or reviews, trust-account compliance
- QuickBooks Online subscription is billed by Intuit and is not included in Glenhold's prices
- QuickBooks Desktop is not a published service
- Guarantee: love your first month of monthly books, or that month is free

## Prices

- Essential monthly bookkeeping: starting at $349 per month. Categorization, reconciliation, monthly statements, clean books for tax season
- Core monthly bookkeeping: starting at $599 per month. Essential, plus a quarterly profit and expense summary, year-to-date comparison, and priority support
- Strategic monthly bookkeeping: starting at $1,499 per month. Core, plus custom reports, accrual accounting, payroll journal entries, loan tracking, and a monthly call
- Cleanup, catch-up, consulting, and training are quoted separately
- Quotes move with transaction volume, number of accounts, and reporting complexity
- No city surcharge is published

## California notes, general only

- Most California LLCs owe an annual minimum franchise tax of $800. A first-year waiver applied only to LLCs that registered in 2021, 2022, or 2023. Glenhold does not file it
- Sole proprietors do not pay that LLC tax
- An additional LLC fee can apply based on total income, historically starting at $250,000. Confirm current tiers with the Franchise Tax Board or a CPA
- California statewide base sales and use tax is 7.25 percent. District taxes add more and change. Glenhold records tax collected as a liability and does not file the return

## Key pages

- [Home](https://glenhold.com/): landing page, services, pricing, contact form
- [Services](https://glenhold.com/services/): monthly, cleanup, QuickBooks, statements, CPA-ready, loan-ready
- [Pricing](https://glenhold.com/pricing/): Essential, Core, Strategic
- [FAQ](https://glenhold.com/bookkeeping-faq/): {len(FAQ)} standalone answers
- [Service areas](https://glenhold.com/service-areas/): cities within about an hour of Simi Valley
- [Who we work with](https://glenhold.com/who-we-work-with/): every kind of small business, not a niche
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
