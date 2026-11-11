"""Shared HTML, schema, and file writer for the static Glenhold site."""

from __future__ import annotations

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = "https://glenhold.com"
LASTMOD = "2026-11-11"
PHONE_DISPLAY = "(805) 419-3451"
PHONE_TEL = "8054193451"
EMAIL = "jack@glenhold.com"
CALENDAR = "https://calendar.app.google/4tubkrcpmxVYzNSRA"
YOUTUBE = "https://www.youtube.com/@BookkeepingWithJack"
FORM_ACTION = "https://formspree.io/f/xvzwqvgv"
INDEXNOW_KEY = "7f3c1a9e4b28d6c0a15e8f47b2d9046c"
HEADSHOT_W, HEADSHOT_H = 1000, 1333
ABOUT_W, ABOUT_H = 1100, 1467
GEO_LAT, GEO_LNG = 34.2694, -118.7815  # Simi Valley city centroid, not a street address

SERVICE_PATHS = {
    "/monthly-bookkeeping/",
    "/cleanup-catch-up/",
    "/quickbooks-online/",
    "/financial-statements/",
    "/cpa-ready-books/",
    "/loan-ready-books/",
}

PAGES: list[dict] = []

NAV = [
    ("/services/", "Services"),
    ("/pricing/", "Pricing"),
    ("/who-we-work-with/", "Who we serve"),
    ("/service-areas/", "Areas"),
    ("/bookkeeping-faq/", "FAQ"),
    ("/about/", "About"),
    ("/contact/", "Contact"),
]

BOTS = [
    "GPTBot",
    "OAI-SearchBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-Web",
    "Claude-SearchBot",
    "anthropic-ai",
    "PerplexityBot",
    "Perplexity-User",
    "Google-Extended",
    "Googlebot",
    "Bingbot",
    "Applebot",
    "Applebot-Extended",
    "GrokBot",
    "xAI-Grok",
    "Grok-DeepSearch",
    "xAI-SearchBot",
]


def esc(value: str) -> str:
    return escape(value, quote=True)


def abs_url(path: str) -> str:
    if path == "/":
        return HOME + "/"
    return HOME + path


def json_ld(obj) -> str:
    payload = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return f'<script type="application/ld+json">{payload}</script>'


def active(path: str, href: str) -> bool:
    if href == "/service-areas/" and path.startswith("/service-areas"):
        return True
    if href == "/who-we-work-with/" and path.startswith("/who-we-work-with"):
        return True
    if href == "/services/" and (path.startswith("/services") or path in SERVICE_PATHS):
        return True
    if href == "/bookkeeping-faq/" and path.startswith("/bookkeeping-faq"):
        return True
    return path == href


def nav(path: str) -> str:
    links = []
    for href, label in NAV:
        current = ' aria-current="page"' if active(path, href) else ""
        links.append(f'<li><a href="{href}"{current}>{label}</a></li>')
    return f'''<nav aria-label="Main navigation">
    <a class="nav-logo" href="/" style="display:flex;align-items:center;gap:10px;"><img src="/logo.png" alt="Glenhold Bookkeeping" width="28" height="38" style="height:38px;width:auto;display:block;" /><span class="nav-wordmark" style="color:white;font-family:'DM Serif Display',serif;font-size:1.25rem;letter-spacing:0.02em;line-height:1.1;">Glenhold <span style="color:var(--white);">Bookkeeping</span></span></a>
    <ul class="nav-links">
      {''.join(links)}
    </ul>
    <a class="nav-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
  </nav>'''


def fact_bar() -> str:
    return f'''<aside class="fact-bar"><p><strong>Glenhold Bookkeeping is a Simi Valley-based bookkeeping firm</strong> owned by Jack Hawley and operated by Glenhold Advisory LLC. Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> or email <a href="mailto:{EMAIL}">jack&#64;glenhold.com</a>. Hours are Monday through Saturday, 6am to 6pm Pacific. No street address is published. Day-to-day bookkeeping is remote, with in-person meetings by arrangement in the service area.</p></aside>'''


def cta(heading: str = "Let's talk about your books", text: str = "Start with a free call, or send a message. You work directly with Jack.") -> str:
    return f'''<div class="cta-banner" id="cta-banner"><h2>{heading}</h2><p>{text}</p><div class="cta-banner-btns"><a class="btn-slate-solid" href="{CALENDAR}" target="_blank" rel="noopener noreferrer">Book a Free Call</a><a class="btn-outline-slate" href="#contact">Send a Message</a></div></div>'''


def contact_block(path: str) -> str:
    return f'''<section class="contact" id="contact">
    <div class="contact-inner">
      <div class="contact-info">
        <div class="section-label">Get In Touch</div>
        <h2>Let's talk about your books</h2>
        <p>Fill out the form and I'll reply within one business day. Please don't attach bank statements or tax documents here. Ask how to share records before sending anything sensitive.</p>
        <div class="contact-details">
          <div class="contact-detail">
            <div class="contact-detail-icon">📞</div>
            <div class="contact-detail-text">
              <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
              <small>Mon–Sat, 6am–6pm PT</small>
            </div>
          </div>
          <div class="contact-detail">
            <div class="contact-detail-icon">✉️</div>
            <div class="contact-detail-text">
              <a href="mailto:{EMAIL}">jack&#64;glenhold.com</a>
              <small>Reply within one business day</small>
            </div>
          </div>
          <div class="contact-detail">
            <div class="contact-detail-icon">📍</div>
            <div class="contact-detail-text">
              Simi Valley, CA
              <small>Serving Ventura County &amp; the Greater LA Area</small>
            </div>
          </div>
        </div>
      </div>
      <form class="contact-form" action="{FORM_ACTION}" method="POST">
        <input type="hidden" name="page" value="{esc(path)}" />
        <div class="form-group">
          <label for="name">Your Name</label>
          <input type="text" id="name" name="name" autocomplete="name" placeholder="John Smith" required />
        </div>
        <div class="form-group">
          <label for="email">Email Address</label>
          <input type="email" id="email" name="email" autocomplete="email" placeholder="john@yourbusiness.com" required />
        </div>
        <div class="form-group">
          <label for="phone">Phone Number</label>
          <input type="tel" id="phone" name="phone" autocomplete="tel" placeholder="(805) 419-3451" />
        </div>
        <div class="form-group">
          <label for="service">What can I help with?</label>
          <select id="service" name="service">
            <option value="">Select a service...</option>
            <option>Monthly Bookkeeping</option>
            <option>Cleanup / Catch-Up</option>
            <option>Consulting &amp; Training</option>
            <option>Not sure yet</option>
          </select>
        </div>
        <div class="form-group">
          <label for="message">Anything else?</label>
          <textarea id="message" name="message" placeholder="Tell me a bit about your business and where things stand with your books..."></textarea>
        </div>
        <button type="submit" class="form-submit">Send Message →</button>
        <p id="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </section>'''


def footer(cities: list[dict]) -> str:
    city_links = "".join(
        f'<a href="/service-areas/{c["slug"]}/">{esc(c["name"])}</a>' for c in cities
    )
    return f'''<footer>
    <div class="footer-top">
      <div>
        <div class="footer-brand">Glenhold <span>Bookkeeping</span></div>
        <p class="footer-desc">Clean books and clear financials for small businesses in Ventura County and the Greater LA Area. Based in Simi Valley. Remote bookkeeping, with in-person meetings by arrangement.</p>
      </div>
      <div class="footer-col">
        <h4>Explore</h4>
        <ul>
          <li><a href="/services/">Services</a></li>
          <li><a href="/pricing/">Pricing</a></li>
          <li><a href="/who-we-work-with/">Who we work with</a></li>
          <li><a href="/service-areas/">Service areas</a></li>
          <li><a href="/bookkeeping-faq/">Bookkeeping FAQ</a></li>
          <li><a href="/resources/">Resources</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">jack&#64;glenhold.com</a></li>
          <li>Mon–Sat, 6am–6pm PT</li>
          <li><a href="/service-areas/">Simi Valley, CA · Service areas</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-resources" aria-label="Bookkeeping services">
      <a href="/monthly-bookkeeping/">Monthly bookkeeping</a>
      <a href="/cleanup-catch-up/">Cleanup &amp; catch-up</a>
      <a href="/quickbooks-online/">QuickBooks setup &amp; training</a>
      <a href="/financial-statements/">Financial statements</a>
      <a href="/cpa-ready-books/">CPA-ready books</a>
      <a href="/loan-ready-books/">Loan-ready financials</a>
      <a href="/getting-started/">Getting started checklist</a>
    </div>
    <div class="footer-cities" aria-label="Cities served"><span>Service area</span>{city_links}</div>
    <div style="padding-top: 8px; text-align: center;">
      <p style="color: rgba(255,255,255,0.3); font-size: 0.8rem;">© 2026 Glenhold Advisory LLC · Doing business as Glenhold Bookkeeping</p>
    </div>
  </footer>'''


def ads() -> str:
    return '''  <!-- OpenAI Ads conversion measurement. -->
  <script>
    !function(w,d,s,u){if(w.oaiq)return;var q=function(){q.q.push(arguments)};q.q=[];w.oaiq=q;var j=d.createElement(s);j.async=1;j.src=u;var f=d.getElementsByTagName(s)[0];f.parentNode.insertBefore(j,f)}(window,document,"script","https://bzrcdn.openai.com/sdk/oaiq.min.js");
    oaiq("init", {pixelId: "CFtmLaAKWainpP7irzAdWa"});
  </script>
  <!-- Google Ads measurement: anonymous events only; contact fields are never sent to Google. -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-17998714201"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'AW-17998714201', {allow_enhanced_conversions: false});
  </script>'''


def crumb_html(crumbs: list[tuple[str, str]]) -> str:
    parts = []
    for i, (name, path) in enumerate(crumbs):
        if i:
            parts.append(" / ")
        if i == len(crumbs) - 1:
            parts.append(esc(name))
        else:
            parts.append(f'<a href="{path}">{esc(name)}</a>')
    return "".join(parts)


def area_nodes(cities: list[dict], extras: list[dict]) -> list[dict]:
    nodes = []
    for city in cities:
        nodes.append({
            "@type": city["schema_type"],
            "name": city["schema_name"],
            "containedInPlace": {"@type": "AdministrativeArea", "name": city["contained"]},
        })
    for extra in extras:
        nodes.append({
            "@type": extra["schema_type"],
            "name": extra["schema_name"],
            "containedInPlace": {"@type": "AdministrativeArea", "name": extra["contained"]},
        })
    return nodes


def offer(name: str, price: str, description: str) -> dict:
    return {
        "@type": "Offer",
        "name": name,
        "url": abs_url("/pricing/"),
        "priceCurrency": "USD",
        "description": description,
        "priceSpecification": {
            "@type": "UnitPriceSpecification",
            "price": price,
            "minPrice": price,
            "priceCurrency": "USD",
            "unitText": "month",
            "description": "Starting monthly price before adjustment for transaction volume, number of accounts, and reporting complexity.",
        },
    }


def business_graph(area: list[dict]) -> list[dict]:
    business = {
        "@type": ["AccountingService", "LocalBusiness"],
        "@id": HOME + "/#business",
        "name": "Glenhold Bookkeeping",
        "legalName": "Glenhold Advisory LLC",
        "url": HOME + "/",
        "image": {
            "@type": "ImageObject",
            "url": HOME + "/headshot.webp",
            "width": HEADSHOT_W,
            "height": HEADSHOT_H,
            "caption": "Jack Hawley, founder of Glenhold Bookkeeping",
        },
        "logo": {
            "@type": "ImageObject",
            "url": HOME + "/logo.png",
            "width": 791,
            "height": 1080,
        },
        "telephone": "+18054193451",
        "email": EMAIL,
        "currenciesAccepted": "USD",
        "description": "Glenhold Bookkeeping is a Simi Valley-based bookkeeping firm owned by Jack Hawley and operated by Glenhold Advisory LLC. Monthly bookkeeping, cleanup and catch-up, and QuickBooks Online setup and training for small businesses of every kind. Remote service, with in-person meetings by arrangement. No street address is published.",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Simi Valley",
            "addressRegion": "CA",
            "addressCountry": "US",
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": GEO_LAT,
            "longitude": GEO_LNG,
        },
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "06:00",
            "closes": "18:00",
        }],
        "priceRange": "$349-$1499",
        "areaServed": area,
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Bookkeeping services and monthly plans",
            "itemListElement": [
                {"@type": "OfferCatalog", "name": "Services", "itemListElement": [
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Monthly bookkeeping", "url": abs_url("/monthly-bookkeeping/")}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Cleanup and catch-up bookkeeping", "url": abs_url("/cleanup-catch-up/")}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "QuickBooks Online setup and training", "url": abs_url("/quickbooks-online/")}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Financial statements", "url": abs_url("/financial-statements/")}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "CPA-ready books", "url": abs_url("/cpa-ready-books/")}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Loan-ready financials", "url": abs_url("/loan-ready-books/")}},
                ]},
                {"@type": "OfferCatalog", "name": "Monthly plans", "itemListElement": [
                    offer("Essential monthly bookkeeping", "349", "Starting at $349 per month. Expense categorization, monthly bank and credit card reconciliation, monthly financial statements, and clean books for tax season. Love your first month of books, or it is free."),
                    offer("Core monthly bookkeeping", "599", "Starting at $599 per month. Essential services plus a quarterly profit and expense summary, a year-to-date performance comparison, and priority support."),
                    offer("Strategic monthly bookkeeping", "1499", "Starting at $1,499 per month. Core services plus custom financial reports, accrual accounting, payroll journal entries, loan tracking, and a monthly call to walk through your numbers."),
                ]},
            ],
        },
        "founder": {"@id": HOME + "/#jack-hawley"},
        "sameAs": [YOUTUBE],
        "knowsAbout": ["Small business bookkeeping", "QuickBooks Online", "Bank reconciliation", "Financial statements"],
    }
    person = {
        "@type": "Person",
        "@id": HOME + "/#jack-hawley",
        "name": "Jack Hawley",
        "jobTitle": "Founder",
        "url": abs_url("/about/"),
        "image": HOME + "/headshot.webp",
        "worksFor": {"@id": HOME + "/#business"},
        "description": "Jack Hawley is the founder of Glenhold Bookkeeping in Simi Valley, California. He is a former Big 4 accountant and a Certified QuickBooks ProAdvisor.",
        "hasCredential": {
            "@type": "EducationalOccupationalCredential",
            "name": "Certified QuickBooks ProAdvisor",
            "credentialCategory": "certification",
        },
        "sameAs": [YOUTUBE],
        "knowsAbout": ["Bookkeeping", "QuickBooks Online"],
    }
    website = {
        "@type": "WebSite",
        "@id": HOME + "/#website",
        "url": HOME + "/",
        "name": "Glenhold Bookkeeping",
        "description": "Small business bookkeeping in Simi Valley and nearby Ventura County and Los Angeles communities.",
        "publisher": {"@id": HOME + "/#business"},
        "inLanguage": "en-US",
    }
    return [business, person, website]


def breadcrumb_node(crumbs: list[tuple[str, str]]) -> dict:
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": abs_url(path),
            }
            for i, (name, path) in enumerate(crumbs)
        ],
    }


def webpage_node(path: str, title: str, description: str) -> dict:
    return {
        "@type": "WebPage",
        "@id": abs_url(path) + "#page",
        "url": abs_url(path),
        "name": title,
        "description": description,
        "dateModified": LASTMOD,
        "inLanguage": "en-US",
        "isPartOf": {"@id": HOME + "/#website"},
        "about": {"@id": HOME + "/#business"},
        "publisher": {"@id": HOME + "/#business"},
        "primaryImageOfPage": {"@id": HOME + "/#business"},
    }


def faq_html(items: list[tuple[str, str]]) -> str:
    blocks = []
    for question, answer in items:
        blocks.append(
            f"<details><summary>{esc(question)}</summary><p>{esc(answer)}</p></details>"
        )
    return "\n".join(blocks)


def faq_node(items: list[tuple[str, str]], path: str) -> dict:
    return {
        "@type": "FAQPage",
        "@id": abs_url(path) + "#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer},
            }
            for question, answer in items
        ],
    }


def service_node(name: str, path: str, description: str, area: list[dict], offer_node=None) -> dict:
    node = {
        "@type": "Service",
        "@id": abs_url(path) + "#service",
        "name": name,
        "serviceType": name,
        "description": description,
        "provider": {"@id": HOME + "/#business"},
        "url": abs_url(path),
        "areaServed": area,
    }
    if offer_node:
        node["offers"] = offer_node
    return node


def head(title: str, description: str, path: str, graph: list) -> str:
    url = abs_url(path)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{ads()}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />
  <link rel="canonical" href="{url}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="author" content="Jack Hawley" />
  <meta name="geo.region" content="US-CA" />
  <meta name="geo.placename" content="Simi Valley" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Glenhold Bookkeeping" />
  <meta property="og:locale" content="en_US" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{HOME}/headshot.webp" />
  <meta property="og:image:width" content="{HEADSHOT_W}" />
  <meta property="og:image:height" content="{HEADSHOT_H}" />
  <meta property="og:image:alt" content="Jack Hawley, founder of Glenhold Bookkeeping" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(title)}" />
  <meta name="twitter:description" content="{esc(description)}" />
  <meta name="twitter:image" content="{HOME}/headshot.webp" />
  <link rel="icon" type="image/png" href="/favicon.png" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&amp;family=DM+Sans:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/site.css" />
  {json_ld({"@context": "https://schema.org", "@graph": graph})}
</head>'''


def layout(title, description, path, main_html, crumbs, extra_nodes, cities, area) -> str:
    graph = business_graph(area) + [webpage_node(path, title, description), breadcrumb_node(crumbs)] + extra_nodes
    doc = f'''{head(title, description, path, graph)}
<body>
<a class="skip-link" href="#main-content">Skip to content</a>
{nav(path)}
<main id="main-content">
{main_html}
</main>
{footer(cities)}
<script src="/site.js" defer></script>
</body>
</html>
'''
    return doc


def write_page(title, description, path, main_html, crumbs, extra_nodes, cities, area) -> None:
    html = layout(title, description, path, main_html, crumbs, extra_nodes, cities, area)
    rel = "" if path == "/" else path.strip("/")
    dest = ROOT / "index.html" if path == "/" else ROOT / rel / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    PAGES.append({"path": path, "title": title, "description": description})


def chips(items: list[tuple[str, str]]) -> str:
    return '<div class="chip-list">' + "".join(f'<a href="{href}">{esc(label)}</a>' for href, label in items) + "</div>"


def hub_cards(cards: list[tuple[str, str, str]]) -> str:
    parts = []
    for href, title, text in cards:
        parts.append(f'<a class="hub-card" href="{href}"><h3>{esc(title)}</h3><p>{esc(text)}</p></a>')
    return '<div class="hub-grid">' + "".join(parts) + "</div>"


def related_links(pairs: list[tuple[str, str]]) -> str:
    return '<div class="content-links">' + "".join(f'<a href="{href}">{label}</a>' for href, label in pairs) + "</div>"
