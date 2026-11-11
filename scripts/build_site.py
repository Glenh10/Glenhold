#!/usr/bin/env python3
"""Generate the static site. Copy is first person. customer_voice() is a lint."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cities import CITIES, HUB, INDUSTRY_REDIRECTS, REDIRECTS, REGIONS
from core_pages import (
    ABOUT_FAQS,
    CLEANUP_FAQS,
    CPA_FAQS,
    LOAN_FAQS,
    MONTHLY_FAQS,
    QBO_FAQS,
    STATEMENT_FAQS,
    about,
    cleanup,
    contact,
    cpa,
    getting_started,
    industry_intro,
    loan,
    monthly,
    pricing,
    privacy,
    quickbooks,
    services_hub,
    statements,
)
from faqs import FAQ
from industries import INDUSTRIES
from sitegen import (
    CALENDAR,
    HOME,
    INDEXNOW_KEY,
    LASTMOD,
    PAGES,
    ROOT,
    YOUTUBE,
    ads,
    area_nodes,
    contact_block,
    crumb_html,
    esc,
    faq_html,
    faq_node,
    footer,
    hub_cards,
    nav,
    offer,
    service_node,
    write_page,
)

FOOTER_PLACES = CITIES + REGIONS
EXTRAS = []
_seen = {c["schema_name"] for c in FOOTER_PLACES}
for name, _href, _line in HUB:
    if name not in _seen:
        EXTRAS.append({
            "schema_type": "Place",
            "schema_name": name,
            "contained": "California",
        })
        _seen.add(name)
AREA = area_nodes(FOOTER_PLACES, EXTRAS)

WORD_MIN = {
    "/about/": 700,
    "/pricing/": 600,
    "/services/": 400,
    "/monthly-bookkeeping/": 900,
    "/cleanup-catch-up/": 800,
    "/quickbooks-online/": 800,
    "/financial-statements/": 800,
    "/cpa-ready-books/": 700,
    "/loan-ready-books/": 700,
    "/getting-started/": 500,
}
for city in CITIES + REGIONS:
    WORD_MIN[f"/service-areas/{city['slug']}/"] = 700
for item in INDUSTRIES:
    WORD_MIN[f"/who-we-work-with/{item['slug']}/"] = 800


def section(title, body):
    return f"<section><h2>{title}</h2>{body}</section>"


def price_cards():
    plans = [
        ("Essential", "349", "For straightforward books and reliable monthly reports", [
            "Expense categorization", "Monthly bank &amp; card reconciliation",
            "Monthly financial statements", "Clean books for tax season",
        ]),
        ("Core", "599", "For owners who want a clearer picture of business performance", [
            "Everything in Essential", "Quarterly profit and expense summary",
            "Year-to-date performance comparison", "Priority support",
        ]),
        ("Strategic", "1,499", "For businesses that need tailored reporting and a monthly walkthrough", [
            "Everything in Core", "Custom financial reports for your business",
            "Accrual accounting, payroll journal entries, and loan tracking",
            "Monthly call to walk through your numbers",
        ]),
    ]
    cards = []
    for name, price, tagline, points in plans:
        featured = " featured" if name == "Core" else ""
        button = "btn-sage" if name == "Core" else "btn-slate"
        lis = "".join(f"<li>{point}</li>" for point in points)
        cards.append(
            f'<div class="pricing-card{featured}"><h3>{name}</h3>'
            f'<p class="pricing-tagline">{tagline}</p>'
            f'<div class="pricing-price"><span class="pricing-prefix">Starting at</span>'
            f'${price} <span>/ mo</span></div><hr class="pricing-divider">'
            f'<ul class="pricing-list">{lis}</ul>'
            f'<a class="{button}" href="#contact">Get Started</a></div>'
        )
    return '<div class="pricing-grid">' + "".join(cards) + "</div>"


def portrait(source, alt):
    width, height = ("1000", "1333") if source == "headshot" else ("1100", "1467")
    return (
        f'<picture><source srcset="/{source}.webp" type="image/webp">'
        f'<img src="/{source}.jpg" width="{width}" height="{height}" alt="{alt}" '
        f'loading="lazy" decoding="async" '
        f'style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top">'
        f'</picture>'
    )


def write_inner(title, description, path, h1, lede, body, crumbs=None, extra=None, faqs=None, contact=True):
    crumbs = crumbs or [("Home", "/"), (h1, path)]
    nodes = list(extra or [])
    if faqs:
        for question, answer in faqs:
            count = len(re.findall(r"[A-Za-z0-9$']+", answer))
            if count > 50:
                raise SystemExit(f"FAQ answer is {count} words on {path}: {question}")
        body += section("Common questions", faq_html(faqs))
        nodes.append(faq_node(faqs, path))
    header = (
        f'<header class="page-hero"><div class="breadcrumb">{crumb_html(crumbs)}</div>'
        f"<h1>{esc(h1)}</h1><p>{esc(lede)}</p>"
    )
    if contact:
        header += (
            f'<a class="btn-primary" href="{CALENDAR}" target="_blank" '
            f'rel="noopener noreferrer">Book a Free Call</a>'
        )
    main = header + '</header><article class="article-body">' + body + "</article>"
    if contact:
        main += contact_block(path)
    write_page(title, description, path, main, crumbs, nodes, FOOTER_PLACES, AREA)


def service_extra(name, path, description):
    return [service_node(name, path, description, AREA, offer(
        name,
        "349",
        "Starting monthly price. The quote depends on transaction volume, accounts, and reporting. Catch-up and training are quoted on their own.",
    ))]


def build_services():
    cards = [
        ("/monthly-bookkeeping/", "Monthly bookkeeping", "A categorized, reconciled month and reports you can read."),
        ("/cleanup-catch-up/", "Cleanup and catch-up", "Open months recorded, reconciled, and ready to hand off."),
        ("/quickbooks-online/", "QuickBooks Online", "Setup, a chart of accounts, and training on the work you keep."),
        ("/financial-statements/", "Financial statements", "How to read the profit and loss and the balance sheet I send."),
        ("/cpa-ready-books/", "CPA-ready books", "Closed months for the preparer who files your return."),
        ("/loan-ready-books/", "Loan-ready financials", "The reports a lender asked for, built from reconciled months."),
    ]
    body = services_hub() + hub_cards(cards)
    write_inner(
        "Bookkeeping Services | Glenhold Bookkeeping",
        "Monthly bookkeeping, catch-up, and QuickBooks Online help from Jack in Simi Valley. Plans from $349. You work with me.",
        "/services/",
        "Bookkeeping services",
        "Monthly close, catch-up, or QuickBooks Online. I quote the work before I start.",
        body,
    )


def build_monthly():
    path = "/monthly-bookkeeping/"
    desc = "I close your books every month: categories, reconciled accounts, and a profit and loss and balance sheet by the 15th. Plans from $349."
    write_inner(
        "Monthly Bookkeeping from $349 | Glenhold",
        desc,
        path,
        "Monthly bookkeeping for small businesses around Simi Valley",
        "I close your books every month. I categorize transactions, reconcile your bank and credit cards, and send a profit and loss and a balance sheet, usually by the 15th. Plans start at $349. Love your first month of books, or it's free.",
        monthly(),
        extra=service_extra("Monthly bookkeeping", path, desc),
        faqs=MONTHLY_FAQS,
    )


def build_cleanup():
    path = "/cleanup-catch-up/"
    desc = "I record the months that fell behind, reconcile them, and send the reports. Catch-up is quoted from the records. You work with me."
    write_inner(
        "Cleanup and Catch-Up Bookkeeping | Glenhold",
        desc,
        path,
        "Cleanup and catch-up bookkeeping",
        "I record the months that never got closed, reconcile those accounts, and send the reports. I quote the work from the records you have. A monthly plan can start when that stretch is finished.",
        cleanup(),
        extra=service_extra("Cleanup and catch-up bookkeeping", path, desc),
        faqs=CLEANUP_FAQS,
    )


def build_quickbooks():
    path = "/quickbooks-online/"
    desc = "I set up QuickBooks Online, organize the chart of accounts, and train you on the work you want to keep. Certified QuickBooks ProAdvisor."
    write_inner(
        "QuickBooks Online Setup and Training | Glenhold",
        desc,
        path,
        "QuickBooks Online setup and training",
        "I set up QuickBooks Online, organize the chart of accounts, and train you on the work you want to keep. I am a Certified QuickBooks ProAdvisor. You keep your own subscription with Intuit.",
        quickbooks(),
        extra=service_extra("QuickBooks Online setup and training", path, desc),
        faqs=QBO_FAQS,
    )


def build_statements():
    path = "/financial-statements/"
    desc = "How to read the profit and loss and balance sheet I send with a monthly close. Reports aimed at the 15th."
    write_inner(
        "Understanding Your Financial Statements | Glenhold",
        desc,
        path,
        "How to read your financial statements",
        "The profit and loss shows what the business earned and spent. The balance sheet shows what it owns, what it owes, and what you have taken out. I send both with the monthly close, aimed at the 15th.",
        statements(),
        extra=service_extra("Financial statements", path, desc),
        faqs=STATEMENT_FAQS,
    )


def build_cpa():
    path = "/cpa-ready-books/"
    desc = "I hand your CPA clean, reconciled books. They file the return. Months closed, draws labeled, sales tax recorded."
    write_inner(
        "CPA-Ready Books | Glenhold Bookkeeping",
        desc,
        path,
        "Books your CPA can use",
        "I hand your CPA clean, reconciled books. They file the return. You keep the preparer you trust, and the year arrives as closed months.",
        cpa(),
        extra=service_extra("CPA-ready books", path, desc),
        faqs=CPA_FAQS,
    )


def build_loan():
    path = "/loan-ready-books/"
    desc = "I organize the reconciled months and the reports a lender asked for. You work with me on the package."
    write_inner(
        "Loan-Ready Financials | Glenhold Bookkeeping",
        desc,
        path,
        "Financials a lender asked to see",
        "I organize the books and the reports your lender named: reconciled months, a profit and loss, and a balance sheet through the date they gave you.",
        loan(),
        extra=service_extra("Loan-ready financials", path, desc),
        faqs=LOAN_FAQS,
    )


def build_industries():
    for item in INDUSTRIES:
        path = f"/who-we-work-with/{item['slug']}/"
        write_inner(
            item["title"],
            item["description"],
            path,
            item["h1"],
            item["lede"],
            item["body"],
            crumbs=[("Home", "/"), ("Who I work with", "/who-we-work-with/"), (item["name"], path)],
            faqs=item["faqs"],
        )
    kept = [(f"/who-we-work-with/{item['slug']}/", item["name"], item["hub"]) for item in INDUSTRIES]
    others = [
        ("real-estate", "Real estate", "Agents and property businesses are welcome. Tell me the accounts and how commissions or rents arrive."),
        ("nonprofits", "Nonprofits", "Local organizations can hand me the month. I will quote a close around the accounts you use."),
        ("retail", "Retail shops", "Counter sales, card batches, and inventory purchases can all live in one monthly close."),
        ("salons", "Salons", "Booth rent, service sales, and product sales can be categorized so the month is readable."),
        ("fitness", "Fitness studios", "Memberships, class packs, and a card for the studio get a monthly reconcile."),
        ("auto-repair", "Auto repair", "Parts, labor, and the processor deposit can be tied out every month."),
    ]
    other_html = "".join(
        f'<section id="{slug}"><h2>{esc(title)}</h2><p>{esc(text)}</p></section>'
        for slug, title, text in others
    )
    body = (
        industry_intro()
        + section("Guides with the most particular bookkeeping", hub_cards(kept))
        + section("Other local businesses", "<p>These are part of the work too. The conversation starts the same way.</p>" + other_html)
    )
    write_inner(
        "Who I Work With | Glenhold Bookkeeping",
        "I work with local small businesses of every kind around Simi Valley. Monthly bookkeeping, catch-up, and QuickBooks Online. Plans from $349.",
        "/who-we-work-with/",
        "Who I work with",
        "I work with local small businesses of every kind. Tell me how you get paid and what you want the reports to show.",
        body,
    )


def build_cities():
    for item in CITIES + REGIONS:
        path = f"/service-areas/{item['slug']}/"
        write_inner(
            item["title"],
            item["description"],
            path,
            item["h1"],
            item["lede"],
            item["body"],
            crumbs=[("Home", "/"), ("Service areas", "/service-areas/"), (item["name"], path)],
            faqs=item["faqs"],
        )
    cards = [(href, name, line) for name, href, line in HUB]
    intro = (
        "<p>I live in Simi Valley, and I work with owners across Ventura County and nearby Los Angeles communities. "
        "Pick your town. Every one of these is a place I am glad to keep the books.</p>"
    )
    write_inner(
        "Bookkeeping Service Areas | Glenhold",
        "Simi Valley bookkeeping for Ventura County and nearby Los Angeles communities, including Moorpark, Thousand Oaks, Camarillo, Oxnard, Ventura, and Santa Clarita.",
        "/service-areas/",
        "Service areas",
        "I am in Simi Valley, and I work with owners throughout Ventura County and nearby Los Angeles communities.",
        section("Towns I work with", intro + hub_cards(cards)),
    )


def build_faq():
    body = section(
        "Before the first call",
        "<p>Short answers about price, the monthly close, catch-up, QuickBooks Online, and where I work. If your question is more specific, book a call or send a note.</p>",
    )
    body += "<section>" + "".join(
        f'<details id="{esc(item["id"])}"><summary>{esc(item["q"])}</summary><p>{esc(item["a"])}</p></details>'
        for item in FAQ
    ) + "</section>"
    write_inner(
        "Bookkeeping FAQ | Glenhold Bookkeeping",
        "Answers about pricing, monthly reports, catch-up, QuickBooks Online, and working with Jack in Simi Valley.",
        "/bookkeeping-faq/",
        "Your bookkeeping questions, answered",
        "What the work costs, what a month includes, and how to start.",
        body,
        extra=[faq_node([(item["q"], item["a"]) for item in FAQ], "/bookkeeping-faq/")],
    )


def build_resources():
    cards = [
        ("/getting-started/", "What to give your bookkeeper", "The account and records list for a smooth handoff."),
        ("/bookkeeping-faq/", "Common questions", "Pricing, monthly reports, catch-up, and where I work."),
        ("/financial-statements/", "Read your reports", "What the profit and loss and the balance sheet are saying."),
        ("/cpa-ready-books/", "Books for your CPA", "How I hand a preparer a year of closed months."),
        ("/pricing/", "Compare monthly plans", "Essential, Core, and Strategic, in plain language."),
    ]
    write_inner(
        "Bookkeeping Resources | Glenhold",
        "Practical notes on preparing records, reading reports, and choosing a monthly plan.",
        "/resources/",
        "Bookkeeping resources",
        "A few pages that answer the questions I hear before a first call.",
        section("Start here", hub_cards(cards)),
    )


def build_getting_started():
    write_inner(
        "What to Give Your Bookkeeper | Glenhold",
        "A practical handoff list: accounts, statements, the last closed month, and the deadline that matters.",
        "/getting-started/",
        "What to give your bookkeeper",
        "Book the first call with the story of the business. Gather the records after the scope is set.",
        getting_started(),
    )


def build_about():
    intro, rest = about().split("<!-- PHOTOEND -->", 1)
    body = (
        '<section class="about" style="padding-top:0"><div class="about-inner"><div class="about-photo-box">'
        + portrait("aboutme", "Jack fly fishing on the coast")
        + '</div><div class="about-content">'
        + intro
        + "</div></div></section>"
        + rest
    )
    write_inner(
        "About Jack | Glenhold Bookkeeping",
        "I'm Jack, in Simi Valley. I've been in accounting since 2021, including audit work at PwC, and I'm a Certified QuickBooks ProAdvisor.",
        "/about/",
        "Hi, I'm Jack",
        "I live in Simi Valley, and I keep the books for small businesses around here. You work with me.",
        body,
        faqs=ABOUT_FAQS,
    )


def build_pricing():
    body = pricing()
    body = body.replace(
        "</p>",
        '</p><div class="pricing-guarantee">Love your first month of books, or it’s free</div>' + price_cards(),
        1,
    )
    write_inner(
        "Bookkeeping Pricing from $349 a Month | Glenhold",
        "Essential starts at $349 a month, Core at $599, and Strategic at $1,499. Love your first month of books, or it's free.",
        "/pricing/",
        "Straightforward monthly pricing",
        "Three monthly plans, priced from your volume, your accounts, and the reporting you want.",
        body,
    )


def build_contact():
    write_inner(
        "Contact Glenhold Bookkeeping | Simi Valley",
        "Call Jack at (805) 419-3451, email jack@glenhold.com, or book a free call. Monday through Saturday, 6am to 6pm Pacific.",
        "/contact/",
        "Let's talk about your books",
        "A short note or a call is enough to start.",
        contact(),
    )


def build_privacy():
    write_inner(
        "Website Privacy Notice | Glenhold Bookkeeping",
        "How this website handles inquiry information, form processing, booking, and advertising measurement.",
        "/privacy/",
        "Website privacy notice",
        "What the inquiry form collects, and what the measurement tags leave out.",
        privacy(),
        contact=False,
    )


def build_home():
    frozen_path = Path(__file__).resolve().parent / "home_freeze.snapshot"
    original = frozen_path.read_text(encoding="utf-8")
    old_person = (
        "Jack is the founder of Glenhold Bookkeeping in Simi Valley, California. "
        "He is a former Big 4 accountant and a Certified QuickBooks ProAdvisor."
    )
    new_person = (
        "Jack keeps the books at Glenhold Bookkeeping in Simi Valley. "
        "He has been in accounting since 2021, including audit work at PwC, and is a Certified QuickBooks ProAdvisor."
    )
    old_business = (
        "Glenhold Bookkeeping is a Simi Valley-based bookkeeping firm owned by Jack and operated by Glenhold Advisory LLC. "
        "Monthly bookkeeping, cleanup and catch-up, and QuickBooks Online setup and training for small businesses across industries in Simi Valley and surrounding communities."
    )
    new_business = (
        "Monthly bookkeeping, cleanup and catch-up, and QuickBooks Online setup and training for small businesses around Simi Valley. "
        "Jack has been in accounting since 2021, including audit work at PwC, and is a Certified QuickBooks ProAdvisor."
    )
    if old_person not in original or old_business not in original:
        raise SystemExit("Frozen homepage is missing the JSON-LD descriptions the build expects to update.")
    updated = original.replace(old_person, new_person, 1).replace(old_business, new_business, 1)
    if visible_text(original) != visible_text(updated):
        raise SystemExit("Homepage visible text changed. Only JSON-LD descriptions may change.")
    (ROOT / "index.html").write_text(updated, encoding="utf-8")
    title = re.search(r"<title>(.*?)</title>", updated).group(1)
    description = re.search(r'<meta name="description" content="(.*?)"', updated).group(1)
    PAGES.append({"path": "/", "title": title, "description": description})


def visible_text(html: str) -> str:
    text = re.sub(r"<script[\s\S]*?</script>", " ", html)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def write_redirect(directory: str, name: str, dest: str, canonical: str, sentence: str) -> None:
    dest_path = ROOT / directory / "index.html"
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    title = f"Bookkeeping in {name} | Glenhold"
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
{ads()}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="robots" content="noindex, follow" />
  <link rel="canonical" href="{HOME}{canonical}" />
  <meta http-equiv="refresh" content="0; url={dest}" />
  <link rel="icon" type="image/png" href="/favicon.png" />
  <link rel="stylesheet" href="/site.css" />
</head>
<body>
{nav('/' + directory + '/')}
<main id="main-content" class="page-hero">
  <h1>{esc(name)}</h1>
  <p>{sentence}</p>
</main>
{footer(FOOTER_PLACES)}
<script src="/site.js" defer></script>
</body>
</html>
"""
    dest_path.write_text(doc, encoding="utf-8")


def build_redirects():
    for slug, name, dest, canonical in REDIRECTS:
        if slug == "newbury-park":
            sentence = (
                'Newbury Park is part of Thousand Oaks, and I cover it on the '
                f'<a href="{dest}">Thousand Oaks page</a>.'
            )
        else:
            label = "San Fernando Valley" if "san-fernando" in canonical else (
                "Conejo and the 101" if "conejo" in canonical else "Ventura County coast"
            )
            sentence = (
                f'I still keep the books for {esc(name)}. That write-up now lives on the '
                f'<a href="{dest}">{esc(label)} page</a>.'
            )
        write_redirect(f"service-areas/{slug}", name, dest, canonical, sentence)
    for slug, name in INDUSTRY_REDIRECTS:
        sentence = (
            f'I still work with {esc(name)}. That conversation now lives on the page about '
            f'<a href="/who-we-work-with/#{slug}">who I work with</a>.'
        )
        write_redirect(
            f"who-we-work-with/{slug}",
            name,
            f"/who-we-work-with/#{slug}",
            "/who-we-work-with/",
            sentence,
        )


def write_discovery():
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: https://glenhold.com/sitemap.xml\n", encoding="utf-8")
    urls = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for page in sorted(PAGES, key=lambda item: item["path"]):
        urls.append(f"<url><loc>{HOME}{page['path']}</loc><lastmod>{LASTMOD}</lastmod></url>")
    (ROOT / "sitemap.xml").write_text("\n".join(urls + ["</urlset>"]) + "\n", encoding="utf-8")
    facts = (
        "# Glenhold Bookkeeping\n\n"
        "I'm Jack. I keep the books for small businesses around Simi Valley. "
        "I've been in accounting since 2021, including audit work at PwC, and I'm a Certified QuickBooks ProAdvisor.\n\n"
        "Phone: (805) 419-3451\n"
        "Email: jack@glenhold.com\n"
        "Hours: Monday–Saturday, 6am–6pm PT\n"
        f"YouTube: {YOUTUBE}\n\n"
        "Monthly plans start at $349 (Essential), $599 (Core), and $1,499 (Strategic). "
        "The price depends on transaction volume, the number of accounts, and reporting. "
        "Cleanup and training are quoted on their own. Love your first month of books, or it's free.\n\n"
        "I hand your CPA clean, reconciled books. They file the return.\n\n"
        "## Pages\n"
    )
    line = lambda page: f"- [{page['title']}]({HOME}{page['path']}): {page['description']}\n"
    short_paths = {"/", "/services/", "/pricing/", "/contact/", "/service-areas/", "/bookkeeping-faq/", "/privacy/"}
    short = [page for page in PAGES if page["path"] in short_paths]
    (ROOT / "llms.txt").write_text(facts + "".join(line(page) for page in short), encoding="utf-8")
    (ROOT / "llms-full.txt").write_text(
        facts
        + "".join(line(page) for page in PAGES)
        + "\n## Questions\n"
        + "".join(f"### {item['q']}\n\n{item['a']}\n\n" for item in FAQ),
        encoding="utf-8",
    )
    (ROOT / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY + "\n", encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")


def page_words(path: Path) -> int:
    html = path.read_text(encoding="utf-8")
    main = re.search(r"<main[\s\S]*?</main>", html)
    chunk = main.group(0) if main else html
    chunk = re.sub(r'<section class="contact"[\s\S]*?</section>', " ", chunk)
    chunk = re.sub(r"<script[\s\S]*?</script>", " ", chunk)
    text = re.sub(r"<[^>]+>", " ", chunk)
    text = text.replace("&amp;", " ").replace("&#x27;", "'")
    return len(re.findall(r"[A-Za-z0-9$']+", text))


def lint() -> None:
    banned = [
        "tell jack",
        "let jack",
        "tell him",
        "jack is a",
        "jack will",
        "who will discuss",
        "depending on traffic",
        "confirm the fit",
        "whether it is a fit",
        "do not guarantee",
        "hawley",
        "bookkeepingwithjack",
        "started my career at pwc",
        "features you do not need",
        "if your business is not listed",
    ]
    we_pattern = re.compile(r"\b(we|we'll|we're|we've|we’ll|we’re|we’ve)\b", re.I)
    errors = []
    for path in ROOT.glob("**/*.html"):
        if "scripts" in path.parts:
            continue
        raw = path.read_text(encoding="utf-8").lower()
        text = visible_text(raw)
        rel = str(path.relative_to(ROOT))
        for phrase in banned:
            if phrase in raw or phrase in text:
                errors.append(f"{rel}: {phrase}")
        if "former big 4" in raw and path.name == "index.html" and path.parent == ROOT:
            pass
        elif "former big 4" in raw:
            errors.append(f"{rel}: former big 4")
        if "local. clear. personal." in text and not (path.name == "index.html" and path.parent == ROOT):
            errors.append(f"{rel}: slogan")
        if path.name == "index.html" and path.parent == ROOT:
            continue
        if we_pattern.search(text):
            errors.append(f"{rel}: visible we")
        for answer in re.findall(r"<details[\s\S]*?<p>([\s\S]*?)</p>\s*</details>", path.read_text(encoding="utf-8")):
            plain = re.sub(r"<[^>]+>", " ", answer)
            count = len(re.findall(r"[A-Za-z0-9$']+", plain))
            if count > 50:
                errors.append(f"{rel}: FAQ answer {count} words")
    if errors:
        raise SystemExit("Voice lint failed:\n" + "\n".join(errors[:80]))


def report_words() -> None:
    short = []
    print(f"{'words':>6}  path")
    for page in sorted(PAGES, key=lambda item: item["path"]):
        if page["path"] == "/":
            path = ROOT / "index.html"
        else:
            path = ROOT / page["path"].strip("/") / "index.html"
        count = page_words(path)
        mark = ""
        minimum = WORD_MIN.get(page["path"])
        if minimum and count < minimum:
            mark = f"  UNDER {minimum}"
            short.append((page["path"], count, minimum))
        print(f"{count:6}  {page['path']}{mark}")
    if short:
        raise SystemExit("Pages under the word target: " + ", ".join(path for path, _, _min in short))


def main():
    PAGES.clear()
    build_home()
    for builder in (
        build_services,
        build_monthly,
        build_cleanup,
        build_quickbooks,
        build_statements,
        build_cpa,
        build_loan,
        build_industries,
        build_cities,
        build_faq,
        build_resources,
        build_getting_started,
        build_about,
        build_pricing,
        build_contact,
        build_privacy,
    ):
        builder()
    build_redirects()
    write_discovery()
    lint()
    report_words()
    print(f"Generated {len(PAGES)} indexable pages. Lint passed.")


if __name__ == "__main__":
    main()
