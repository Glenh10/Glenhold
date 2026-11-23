#!/usr/bin/env python3
"""Generate the static site with python3 scripts/build_site.py."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cities import CITIES
from industries import INDUSTRIES
from faqs import FAQ
from sitegen import (ROOT, HOME, LASTMOD, PAGES, CALENDAR, EMAIL, YOUTUBE,
    INDEXNOW_KEY, PHONE_DISPLAY, PHONE_TEL, area_nodes, write_page, faq_node, faq_html, service_node,
    MONTHLY_BOOKKEEPING_TIERS, esc, crumb_html, contact_block, chips, hub_cards, related_links, cta)

CORE_CITIES = ['simi-valley','moorpark','thousand-oaks','westlake-village','camarillo','santa-clarita']
EXTRAS = [dict(schema_type='Place',schema_name=n,contained=c) for n,c in [
    ('Oak Park','Ventura County, California'),('Winnetka, Los Angeles','Los Angeles, California'),
    ('Tarzana, Los Angeles','Los Angeles, California')]]
AREA = area_nodes(CITIES, EXTRAS)

def customer_voice(text):
    changes = [
        ("Glenhold Bookkeeping helps", "I help"),
        ("Glenhold can help", "I can help"),
        ("Glenhold can assess", "I can assess"),
        ("Glenhold provides", "I provide"),
        ("Glenhold helps", "I help"),
        ("Glenhold offers", "I offer"),
        ("Glenhold serves", "I serve"),
        ("Glenhold works", "I work"),
        ("Glenhold reconciles", "I reconcile"),
        ("and prepares monthly", "and prepare monthly"),
        ("Glenhold’s work focuses", "My work focuses"),
        ("Tell Jack", "Tell me"),
        ("tell Jack", "tell me"),
        ("with Jack", "with me"),
        ("to Jack", "to me"),
        ("Jack can", "I can"),
        ("Jack will", "I will"),
        ("Jack works directly with you", "I work directly with you"),
    ]
    for before, after in changes:
        text = text.replace(before, after)
    return text

for item in FAQ:
    item["a"] = customer_voice(item["a"])

def section(title, body):
    return '<section><h2>'+title+'</h2>'+body+'</section>'

PRICING_INTRO = "I review your books before quoting. Your monthly price depends on transaction volume, the accounts I’ll reconcile, and the reporting you need."


def price_cards():
    cards = []
    for name, minimum, points in MONTHLY_BOOKKEEPING_TIERS:
        bullets = ''.join(f'<li>{esc(point)}</li>' for point in points)
        cards.append(
            f'<div class="pricing-card"><h3>{esc(name)}</h3>'
            f'<p class="pricing-price"><span class="pricing-prefix">Starting at</span>${minimum:,} <span>/ mo</span></p>'
            f'<hr class="pricing-divider"><ul class="pricing-list">{bullets}</ul>'
            '<a class="btn-slate" href="#contact">Request a quote</a></div>'
        )
    return '<div class="pricing-grid">' + ''.join(cards) + "</div>"


def write_inner(title,description,path,h1,lede,body,crumbs=None,extra=None,faqs=None,contact=True):
    crumbs=crumbs or [('Home','/'),(h1,path)]
    nodes=list(extra or [])
    if faqs:
        faqs = [(customer_voice(q), customer_voice(a)) for q, a in faqs]
        body+=section('Common questions',faq_html(faqs));nodes.append(faq_node(faqs,path))
    body = customer_voice(body)
    lede = customer_voice(lede)
    header='<header class="page-hero"><div class="breadcrumb">'+crumb_html(crumbs)+'</div><h1>'+esc(h1)+'</h1><p>'+esc(lede)+'</p>'
    if contact:header+='<a class="btn-primary" href="'+CALENDAR+'" target="_blank" rel="noopener noreferrer">Book a Free Call</a>'
    article_class = {"/pricing/": "article-body pricing-page", "/about/": "article-body about-page"}.get(path, "article-body")
    main=header+'</header><article class="'+article_class+'">'+body+'</article>'
    if contact:main+=contact_block(path)
    write_page(title,description,path,main,crumbs,nodes,CITIES,AREA)

SERVICES=[
    dict(slug='monthly-bookkeeping',name='Monthly bookkeeping',description='Monthly bookkeeping from $350 for businesses near Simi Valley. Transaction categorization, reconciliation, and clear financial reports.',lede='Keep your books current and understand how your business is doing.',body=
        section('A monthly routine you can rely on','<p>Glenhold Bookkeeping helps business owners keep their records organized throughout the year. You work directly with Jack, a former Big 4 accountant and Certified QuickBooks ProAdvisor based in Simi Valley.</p><p>The work starts with your accounts, how you get paid, and the reports you need. We agree on the scope and a monthly schedule before getting started.</p>')+
        section('What is included','<ul><li><strong>Transaction categorization:</strong> organize income and expenses in accounts suited to your business.</li><li><strong>Bank and credit card reconciliation:</strong> check the books against statements and resolve differences.</li><li><strong>Monthly financial reports:</strong> receive a profit and loss statement and balance sheet.</li><li><strong>Email support:</strong> get answers to bookkeeping questions between closes.</li></ul><p>The target is to deliver reports by the 15th of the following month, once the necessary statements and answers are available.</p>')+
        section('How monthly pricing works','<p>Monthly bookkeeping starts at $350. I quote after reviewing your books and the reporting you need. <a href="/pricing/">See monthly pricing estimates</a>.</p>')+
        section('Need to catch up first?','<p>If previous months are unfinished, <a href="/cleanup-catch-up/">cleanup and catch-up</a> can establish a reliable starting point. If you prefer to maintain the books yourself, ask about <a href="/quickbooks-online/">QuickBooks Online training</a>.</p>')),
    dict(slug='cleanup-catch-up',name='Cleanup and catch-up bookkeeping',description='Catch up on unfinished bookkeeping, reconcile accounts, and prepare clear financial reports. Simi Valley-based Glenhold quotes each cleanup by scope.',lede='Get unfinished bookkeeping back on track.',body=
        section('Start with a clear picture of the work','<p>Whether you are a few months behind or need to sort through older records, Glenhold can help assess what needs attention. Cleanup corrects existing records; catch-up completes periods that have not been finished. A project may involve both.</p>')+
        section('What a project can include','<ul><li>Organizing available statements and transaction exports.</li><li>Recording missing transactions and reviewing duplicates.</li><li>Resolving unmatched transfers and unclear entries with you.</li><li>Reconciling bank and credit card accounts.</li><li>Organizing the chart of accounts and preparing financial reports.</li><li>Identifying open questions for you or your tax preparer.</li></ul>')+
        section('Pricing and timing','<p>Each project is quoted based on the number of periods, accounts, transactions, and corrections involved. Monthly bookkeeping is priced separately from historical cleanup work. Mention any deadlines during the first conversation so we can discuss a realistic schedule.</p>')+
        section('What to prepare','<p>Start with an account list, the periods you need help with, and a note of any missing records. Include accounts closed during the period. See the <a href="/getting-started/">handoff checklist</a> before gathering documents, or book a call to find out what is needed.</p>')),
    dict(slug='quickbooks-online',name='QuickBooks Online setup and training',description='QuickBooks Online setup, chart of accounts organization, training, and accuracy check-ins from a Certified QuickBooks ProAdvisor in Simi Valley.',lede='Build a system you understand and a routine you can maintain.',body=
        section('Help with your QuickBooks Online file','<p>Jack is a Certified QuickBooks ProAdvisor who can help you set up QuickBooks Online, organize your chart of accounts, or work through an existing bookkeeping issue.</p><p>Tell him what you want to do yourself and where you would like support. Training can focus on the tasks you handle rather than features you do not need.</p>')+
        section('Setup and training can cover','<ul><li>A chart of accounts that fits your business.</li><li>A routine for reviewing and categorizing transactions.</li><li>Understanding transfers and reconciling accounts.</li><li>Reading your profit and loss statement and balance sheet.</li><li>Accuracy check-ins on an agreed schedule.</li></ul>')+
        section('A specific question or ongoing support','<p>You can ask for help with a particular issue, discuss a cleanup, or move to <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Consulting and training are quoted separately. Software arrangements and the work included will be discussed as part of your quote.</p>')),
    dict(slug='financial-statements',name='Financial statements',description='Understand your profit and loss statement and balance sheet. Monthly financial reports are included in monthly bookkeeping from $350.',lede='Clear reports that help you understand your business.',body=
        section('What you receive each month','<p>Monthly bookkeeping includes a profit and loss statement and a balance sheet, prepared from the bookkeeping records. The target is the 15th of the following month when the necessary information is available.</p>')+
        section('What the reports tell you','<p><strong>A profit and loss statement</strong> shows income, expenses, and profit over a period. <strong>A balance sheet</strong> shows assets, liabilities, and equity at a particular date. Together, they give you a fuller view than the bank balance alone.</p>')+
        section('More context as your business grows','<p>If you need quarterly summaries, year-to-date comparisons, or reports tailored to your business, we can include those in your quote. <a href="/pricing/">See monthly pricing estimates</a>.</p><p>These are bookkeeping reports for management use and sharing with your tax preparer. If a lender or another recipient requires a specific report or assurance engagement, share that request before work begins.</p>')),
    dict(slug='cpa-ready-books',name='Books for your tax preparer',description='Organized transactions, reconciled accounts, and year-end financial reports for your CPA or tax preparer. Glenhold Bookkeeping is based in Simi Valley.',lede='Make the year-end handoff easier.',body=
        section('Give your tax preparer organized records','<p>Glenhold helps categorize transactions, reconcile bank and credit card accounts, and prepare financial reports. Keeping this work current means fewer loose ends when it is time to share the books with your CPA or tax preparer.</p>')+
        section('What the handoff can include','<ul><li>A year-to-date profit and loss statement and year-end balance sheet.</li><li>Reconciled bank and credit card accounts for the agreed periods.</li><li>Relevant loan and owner-transaction records, when provided.</li><li>A list of unresolved items or questions that need review.</li></ul><p>Tax return preparation and filing are separate from the bookkeeping services described here.</p>')+
        section('If the deadline is approaching','<p>Let Jack know which periods are unfinished and when your preparer needs the records. A <a href="/cleanup-catch-up/">cleanup assessment</a> can help establish the scope and timeline.</p>')),
    dict(slug='loan-ready-books',name='Bookkeeping for financing requests',description='Organize your books and financial statements for a financing request. Share your lender’s reporting requirements with Glenhold before work begins.',lede='Have organized financial records ready when they are requested.',body=
        section('Start with the lender’s request','<p>If you are applying for financing, ask the lender which reports and periods it needs. Share that list with Jack so the bookkeeping work can be scoped around the actual request.</p>')+
        section('How Glenhold can help','<p>Monthly bookkeeping and cleanup can help organize transactions, reconcile accounts, and prepare a profit and loss statement and balance sheet. If historical periods need work, the timeline will depend on the records available and the size of the backlog.</p><p>Lender requirements vary. Bookkeeping reports do not guarantee approval or replace any tax returns, assurance reports, or other documents the lender may require.</p>')+
        section('Discuss the timeline early','<p>Bring the reporting request and deadline to a free introductory call. <a href="/cleanup-catch-up/">Learn about cleanup</a> or <a href="/monthly-bookkeeping/">ongoing bookkeeping</a>.</p>')),
]

def build_services():
    for p in SERVICES:
        path='/'+p['slug']+'/'
        extra=[service_node(p['name'],path,p['description'],AREA)]
        write_inner(p['name']+' | Glenhold Bookkeeping',p['description'],path,p['name'],p['lede'],p['body'],
            [('Home','/'),('Services','/services/'),(p['name'],path)],extra)
    cards=[('/'+p['slug']+'/',p['name'],p['lede']) for p in SERVICES]
    body=section('Support for the stage you are in','<p>Hand off your monthly bookkeeping, catch up on unfinished records, or get help using QuickBooks Online. You work directly with Jack, who will discuss your needs and prepare a quote before work begins.</p>'+hub_cards(cards))
    body+=section('A clear scope from the start','<p>Monthly bookkeeping starts at $350. Cleanup and training are quoted separately. Tell Jack about any special reporting, software, or filing requirements so the proposal accurately reflects what you need.</p><p><a href="/pricing/">View pricing</a> or <a href="/getting-started/">see what to prepare</a>.</p>')
    write_inner('Bookkeeping Services | Glenhold Bookkeeping','Monthly bookkeeping, cleanup, and QuickBooks Online support for businesses around Simi Valley. Work directly with Jack. Monthly bookkeeping from $350.','/services/','Bookkeeping services','Practical help with your books, from setup to the monthly close.',body)

def build_industries():
    for i in INDUSTRIES:
        path='/who-we-work-with/'+i['slug']+'/'
        body=section('Bookkeeping that fits how you operate',''.join('<p>'+esc(p)+'</p>' for p in i['paragraphs']))
        body+=section('Useful details for the first call','<ul>'+''.join('<li>'+esc(p)+'</li>' for p in i['points'])+'</ul>')
        body+=section('Choose the help you need','<p><a href="/monthly-bookkeeping/">Monthly bookkeeping</a> keeps the records current. <a href="/cleanup-catch-up/">Cleanup and catch-up</a> address unfinished periods. <a href="/quickbooks-online/">QuickBooks Online support</a> helps with setup, training, or specific questions.</p><p>Glenhold is based in Simi Valley and works with businesses across <a href="/service-areas/">surrounding communities</a>. Monthly bookkeeping starts at $350, with the scope and final quote based on your needs.</p>')
        write_inner('Bookkeeping for '+i['name']+' | Glenhold','Bookkeeping for '+i['name'].lower()+' in Simi Valley and surrounding communities. Monthly support, cleanup, and QuickBooks Online help.',path,'Bookkeeping for '+i['name'].lower(),i['intro'],body,
            [('Home','/'),('Who we work with','/who-we-work-with/'),(i['name'],path)])
    cards=[('/who-we-work-with/'+i['slug']+'/',i['name'],i['intro']) for i in INDUSTRIES if i['slug'] != 'restaurants']
    write_inner('Businesses We Work With | Glenhold Bookkeeping','Glenhold works with businesses across industries around Simi Valley. Explore bookkeeping for service firms, shops, trades, practices, and more.','/who-we-work-with/','Bookkeeping for local businesses','Different businesses. The same care with your books.',
        section('Find the help your business needs','<p>Glenhold works with businesses across industries. These examples show the information that may be useful when discussing your bookkeeping. If your business is not listed, get in touch—we can still discuss whether it is a fit.</p>'+hub_cards(cards)))


LOCAL_PAGE_CONTENT = {
    'simi-valley': ('Based here in Simi Valley.', 'I’m Jack, a Simi Valley local and the founder of Glenhold Bookkeeping. I offer monthly bookkeeping, catch-up work, and QuickBooks Online support for businesses across industries.', 'If bookkeeping keeps slipping behind the day-to-day work, we can discuss which tasks you want to hand off and the reports you need. You work directly with me throughout the engagement.'),
    'moorpark': ('Bookkeeping support from neighboring Simi Valley.', 'I offer monthly bookkeeping, cleanup, and QuickBooks Online support for Moorpark businesses. The scope is based on your accounts, transaction volume, and reporting needs.', 'You can hand off the monthly work or ask for help improving the routine you manage yourself. During the first call, tell me which periods are complete and where you need support.'),
    'thousand-oaks': ('Monthly bookkeeping, catch-up, and QuickBooks Online help.', 'Glenhold offers bookkeeping for businesses in Thousand Oaks, including Newbury Park. I’m based in Simi Valley, and you work directly with me.', 'If your CPA or tax preparer has asked for financial reports, bring that request to the first conversation. We can discuss the work needed to provide organized records and an agreed reporting schedule.'),
    'westlake-village': ('Work directly with your bookkeeper.', 'I offer bookkeeping support for businesses in Westlake Village. Choose monthly bookkeeping, cleanup for unfinished periods, or help using QuickBooks Online.', 'Tell me which reports you use today and what you need to understand better. Reporting and support can be tailored, with the final scope agreed before work begins.'),
    'camarillo': ('Bookkeeping for your Camarillo business.', 'Glenhold offers monthly bookkeeping, cleanup, and QuickBooks Online support for businesses in Camarillo. I work from Simi Valley and handle your bookkeeping directly.', 'If you use several bank accounts, cards, or payment processors, mention them during the first conversation. A complete account list helps establish the work and an appropriate quote.'),
    'santa-clarita': ('Clear records and a consistent monthly routine.', 'I offer bookkeeping support for businesses in Santa Clarita, including Valencia, Newhall, Saugus, and Canyon Country. Monthly bookkeeping, cleanup, and QuickBooks Online help can be scoped around your needs.', 'If the books are behind, tell me the last completed month and any accounts closed or replaced during the period. That helps establish a starting point before an ongoing monthly routine begins.'),
}


def build_cities():
    for city in CITIES:
        path = '/service-areas/' + city['slug'] + '/'
        if city['slug'] not in LOCAL_PAGE_CONTENT:
            target = '/service-areas/#' + city['slug']
            doc = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="0; url=' + target + '"><meta name="robots" content="noindex, follow"><link rel="canonical" href="https://glenhold.com/service-areas/"><title>' + esc(city['name']) + ' service area | Glenhold Bookkeeping</title></head><body><main><h1>Glenhold Bookkeeping service areas</h1><p><a href="' + target + '">View coverage for ' + esc(city['name']) + '</a>.</p></main></body></html>'
            dest = ROOT / path.strip('/') / 'index.html'
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(doc)
            continue
        lede, first, second = LOCAL_PAGE_CONTENT[city['slug']]
        body = section('How I can help', '<p>' + esc(first) + '</p><p>' + esc(second) + '</p>')
        body += section('Services and pricing', '<p><a href="/monthly-bookkeeping/">Monthly bookkeeping</a> starts at $350. <a href="/cleanup-catch-up/">Cleanup and catch-up</a> and <a href="/quickbooks-online/">QuickBooks Online support</a> are quoted separately.</p><p>Monthly bookkeeping includes transaction categorization, bank and credit card reconciliation, and financial statements. Additional reporting is quoted based on what you need.</p><p><a href="/pricing/">See monthly pricing</a> or <a href="/getting-started/">see what to prepare</a> for a handoff.</p>')
        write_inner('Bookkeeping in ' + city['name'] + ' | Glenhold', 'Monthly bookkeeping, cleanup, and QuickBooks Online help for businesses in ' + city['name'] + '. Work directly with Jack. Monthly bookkeeping from $350.', path, 'Bookkeeping for ' + city['name'] + ' businesses', lede, body, [('Home','/'),('Service areas','/service-areas/'),(city['name'],path)])
    body = section('Southern California service areas', '<p>Glenhold is based in Simi Valley, California. Explore the Ventura County and Los Angeles County communities below for local bookkeeping information.</p>')
    for county in ['Ventura County', 'Los Angeles County']:
        members = [c for c in CITIES if c['group'] == county]
        items = []
        for city in sorted(members, key=lambda c:c['name']):
            label = '<a href="/service-areas/' + city['slug'] + '/">' + esc(city['name']) + '</a>' if city['slug'] in LOCAL_PAGE_CONTENT else esc(city['name'])
            items.append('<li id="' + city['slug'] + '">' + label + '</li>')
        extras = ['Oak Park'] if county == 'Ventura County' else ['Tarzana', 'Winnetka']
        items += ['<li>' + name + '</li>' for name in extras]
        body += section(county, '<ul class="service-city-list">' + ''.join(items) + '</ul>')
    write_inner('Nationwide Bookkeeping | Simi Valley & Southern California Service Areas', 'Work directly with Jack for remote bookkeeping across the United States. Explore local bookkeeping services in Simi Valley, Ventura County, and Los Angeles County.', '/service-areas/', 'Nationwide bookkeeping', 'I work remotely with business owners across the United States on monthly bookkeeping, catch-up work, and QuickBooks Online.', body, [('Home','/'),('Service areas','/service-areas/')])



def build_faq():
    body=section('Before we get started','<p>Here are answers to common questions about pricing, services, and working with Jack. If your situation needs a closer look, book a free call or send a message.</p>')
    body+='<section>'+''.join('<details id="'+i['id']+'"><summary>'+esc(i['q'])+'</summary><p>'+esc(i['a'])+'</p></details>' for i in FAQ)+'</section>'
    write_inner('Bookkeeping FAQ | Glenhold Bookkeeping','Answers about bookkeeping pricing, monthly reports, catch-up, QuickBooks Online, service areas, and getting started with Glenhold.','/bookkeeping-faq/','Your bookkeeping questions, answered','What to expect from the services and the first conversation.',body,extra=[faq_node([(i['q'],i['a']) for i in FAQ],'/bookkeeping-faq/')])

def build_resources():
    cards=[('/getting-started/','What to give your bookkeeper','An account and records checklist for a smoother handoff.'),('/bookkeeping-faq/','Common questions','Pricing, monthly reports, cleanup, and getting started.'),('/financial-statements/','Understand your reports','What a profit and loss statement and balance sheet tell you.'),('/pricing/','See monthly pricing','See what affects your quote and what to expect each month.')]
    write_inner('Bookkeeping Resources | Glenhold Bookkeeping','Practical bookkeeping resources: preparing records, understanding financial reports, choosing a plan, and getting started.','/resources/','Bookkeeping resources','Useful information for choosing support and preparing your records.',section('Start here',hub_cards(cards)))

def build_getting_started():
    body=section('Start with the basics','<p>For an introductory call, tell Jack about your business, the number of accounts, whether your books are current, and the help you need. You do not need to gather every record before that conversation.</p><p>Once the work is scoped, this checklist can help prepare for a handoff. Ask how to share sensitive documents before sending them.</p>')
    records=[('Account list','Include checking, savings, credit cards, loans, and payment processors. Mention accounts closed or replaced during the period.'),('Statements','Gather statements for the agreed periods, including opening and closing balances. Transaction exports can be useful alongside them.'),('Existing bookkeeping','Identify the QuickBooks Online file, last completed month, last reconciled month, and any known issues.'),('Loan and payroll records','If relevant to the work, identify available statements, schedules, and reports from your payroll provider.'),('Owner transactions','Flag contributions, withdrawals, and business costs paid personally.'),('Deadlines and report requests','Share requests from your tax preparer, lender, or other recipient.')]
    body+=section('Handoff checklist','<ol>'+''.join('<li><strong>'+t+'.</strong> '+b+'</li>' for t,b in records)+'</ol>')
    body+=section('Missing something?','<p>A short list of missing records helps plan the work. Include both accounts involved in transfers whenever possible. If you are unsure which months have been reconciled, Jack can discuss how to establish a starting point.</p>')
    write_inner('What to Give Your Bookkeeper | Glenhold Checklist','Prepare for a bookkeeping handoff with a practical checklist of accounts, statements, existing records, and deadlines.','/getting-started/','What to give your bookkeeper','A straightforward checklist for a smoother handoff.',body)

def bio(*, homepage=False):
    if homepage:
        introduction = '<p>I’m Jack, a former Big 4 accountant and Certified QuickBooks ProAdvisor. I started Glenhold to help business owners keep reliable books and understand their financial reports.</p>'
    else:
        introduction = '<p>I’m Jack, a Simi Valley local, former Big 4 accountant, and Certified QuickBooks ProAdvisor. I started Glenhold to help business owners keep reliable books and understand their financial reports.</p>'
    return introduction + '<p>You work directly with me. We’ll discuss what you need, agree on the scope, and set up a routine for your records and questions.</p><p>Outside work, I enjoy fly fishing, walks, and attending Mass with my wife and two children.</p>'

def portrait(source,alt):
    width,height=('1000','1333') if source=='headshot' else ('1100','1467')
    return '<picture><source srcset="/'+source+'.webp" type="image/webp"><img src="/'+source+'.jpg" width="'+width+'" height="'+height+'" alt="'+alt+'" loading="lazy" decoding="async" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top"></picture>'

def youtube_section():
    if not YOUTUBE:
        return ''
    return '<section class="video-section" id="videos"><div class="video-inner"><div><div class="section-label">On YouTube</div><h2 class="section-title">Watch my bookkeeping videos</h2><p class="section-sub">I also run Bookkeeping Business Blueprint, where I share videos about bookkeeping and building a bookkeeping business.</p><a class="btn-slate-solid" href="' + YOUTUBE + '" target="_blank" rel="noopener noreferrer">Watch on YouTube</a></div><div class="video-channel-card"><svg xmlns="http://www.w3.org/2000/svg" width="64" height="46" viewBox="0 0 64 46" aria-hidden="true" focusable="false"><rect x="0" y="0" width="64" height="46" rx="12" fill="#c62828"/><path d="M26 12 L44 23 L26 34 Z" fill="white"/></svg><h3>Bookkeeping Business Blueprint</h3><p>@bookkeepingbizblueprint</p></div></div></section>'


def build_about():
    about_bio = bio().replace('<p>You work directly with me.', '<h2>Working with me</h2><p>You work directly with me.')
    body='<section class="about"><div class="about-inner"><div class="about-photo-box">'+portrait('aboutme','Jack fly fishing on the coast')+'</div><div class="about-content">'+about_bio+'</div></div></section>'
    body+=youtube_section()
    write_inner('About Jack | Glenhold Bookkeeping','Meet Jack, a Simi Valley local, former Big 4 accountant, Certified QuickBooks ProAdvisor, and founder of Glenhold Bookkeeping.','/about/','Hi, I’m Jack','Local roots and a direct relationship with your bookkeeper.',body)

def build_mission():
    title = 'Why I speak openly about my faith at Glenhold'
    description = 'Jack shares why he speaks openly about his Catholic faith, how it shapes his bookkeeping work, and the Christian economy he wants to help build.'
    body = (
        '<p>I hesitated before putting my Catholic faith on Glenhold’s website. I take seriously the difference between sharing my faith and using it to win business. I also know how easy it is to call a business Christian and how much harder it is to live up to that word.</p>'
        '<p>I decided to speak openly because I want to share the Gospel in every part of my life. My wife and I take our two boys to Mass, and we’re raising them to understand that what we believe on Sunday has a claim on how we spend Monday. That includes the hours I spend at my desk.</p>'
        '<p>I believe God can use ordinary work to make us holy. For me, that often comes down to what I do when a client would never know the difference. Do I take the time to find out why an account is off? If I’ve made a mistake, do I pick up the phone and own it? Those decisions are part of what it means for me to practice my faith as a bookkeeper.</p>'
        '<section><h2>The Christian economy I want to help build</h2>'
        '<p>I’d like it to be easier for Christians to find one another, hire one another, and send work each other’s way. I think of what it means for a family when a contractor has enough steady work to bring on an apprentice, or for a parish when a local business owner can afford to be generous year after year. That’s what I have in mind when I talk about a stronger Christian economy.</p>'
        '<p>My trade is accounting. After working at PwC and going on to lead accounting work for businesses, I started Glenhold so I could work directly with owners. When someone asks, “Can I afford to put another person on payroll?” I want them to have books they can trust and a person they can call who knows their business. That’s the contribution I can make.</p></section>'
        '<p class="mission-signature"><strong>Jack</strong><br>Owner, Glenhold Bookkeeping</p>'
        '<a class="btn-primary" href="' + CALENDAR + '" target="_blank" rel="noopener noreferrer">Book a call with Jack</a>'
    )
    main = (
        '<div class="mission-note"><header class="page-hero"><div class="breadcrumb">'
        + crumb_html([('Home', '/'), ('Mission', '/mission/')])
        + '</div><h1>' + esc(title) + '</h1></header>'
        + '<article class="article-body">' + body + '</article></div>'
    )
    write_page(title + ' | Glenhold Bookkeeping', description, '/mission/', main,
               [('Home', '/'), ('Mission', '/mission/')], [], CITIES, AREA)


def build_pricing():
    body=section('Monthly bookkeeping estimates', '<p>These estimates reflect the work involved in maintaining your books. Cleanup, catch-up, consulting, and training are quoted separately.</p>'+price_cards()+'<div class="pricing-guarantee">Love your first month of books, or it’s free</div>')
    body+=section('What goes into your quote','<p>Before work begins, we’ll agree on what’s included, when to expect your reports, and your monthly price. Tax return preparation and filing are separate from bookkeeping.</p><p>The first-month guarantee applies to monthly bookkeeping. Discuss the details with Jack when agreeing on your scope.</p>')
    write_inner('Bookkeeping Pricing from $350 per Month | Glenhold','Monthly starting prices are $350 for Essential, $450 for Core, and $700 for Strategic. Cleanup and training are quoted separately.','/pricing/','Monthly bookkeeping pricing',PRICING_INTRO,body)


def build_contact():
    body=section('Tell me what you need','<p>Share your city, the kind of business you run, whether your books are current, and the help you want. I’ll reply within one business day to discuss the next step.</p><p>You can also call <a href="tel:8054193451">(805) 419-3451</a>, email <a href="mailto:jack@glenhold.com">jack@glenhold.com</a>, or book a free introductory call. Please leave bank logins, account numbers, and financial documents out of the contact form.</p>')
    write_inner('Contact Glenhold Bookkeeping | Simi Valley','Contact Jack at Glenhold Bookkeeping in Simi Valley. Call (805) 419-3451, email jack@glenhold.com, or book a free introductory call.','/contact/','Let’s talk about your books','A short conversation is a good place to start.',body)

def build_privacy():
    body=section('Information you send','<p>The inquiry form asks for your name, email address, optional phone number, the service you are interested in, and a message. Glenhold uses this information to respond to your inquiry and discuss services. Please do not send bank logins, account numbers, tax documents, or other sensitive financial records through this form.</p><p>Form submissions are processed through Formspree. Booking a call takes you to Google’s scheduling service. YouTube channel links take you to YouTube, where its own policies apply. The website also loads fonts from Google Fonts. These providers process information according to their own policies.</p>')
    body+=section('Website measurement','<p>This website loads Google Ads and OpenAI Ads measurement tags to help measure visits and actions, including inquiry submissions and clicks on booking or telephone links. The website’s form-submission code does not include the name, email address, phone number, or message fields in the conversion events sent to those tags.</p><p>Third-party services may process technical information, such as browser, device, network, or advertising identifiers, under their own policies and applicable settings. This website also stores campaign parameters in browser session storage to help identify the source of an inquiry.</p>')
    body+=section('Questions about your information','<p>Contact <a href="mailto:jack@glenhold.com">jack@glenhold.com</a> with questions about this website’s information handling or requests concerning information you have provided.</p><p>Website forms and advertising measurement are separate from any arrangements for exchanging client bookkeeping records.</p>')
    write_inner('Website Privacy Notice | Glenhold Bookkeeping','How Glenhold’s website uses inquiry information, form processing, booking services, and advertising measurement.','/privacy/','Website privacy notice','Information about inquiries and website measurement.',body,contact=False)

def build_home():
    photo='<picture><img src="/headshot.jpg" width="1000" height="1333" alt="Jack, founder of Glenhold Bookkeeping" decoding="async" fetchpriority="high" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center -10%"></picture>'
    main='<section class="hero"><div class="hero-content"><h1>Books you can trust</h1><p class="hero-sub">I’ll keep your bookkeeping current and walk you through your financial reports, so you know where things stand. You’ll work directly with me from our first call.</p><div class="hero-ctas"><a class="btn-primary" href="'+CALENDAR+'" target="_blank" rel="noopener noreferrer">Book a Free Call</a><a class="btn-ghost" href="#contact">Send a Message</a></div><div class="hero-photo-mobile"><img src="/headshot.jpg" width="1000" height="1333" alt="Jack, founder of Glenhold Bookkeeping" style="width:75%;height:auto;display:block;border-radius:6px;margin:0 auto"></div><div class="hero-social"><a href="https://share.google/ZFSpIuhD39akrC2DT" target="_blank" rel="noopener noreferrer">Find us on Google</a><a href="https://www.yelp.com/biz/glenhold-bookkeeping-simi-valley" target="_blank" rel="noopener noreferrer">Yelp profile</a><a href="https://www.youtube.com/@bookkeepingbizblueprint" target="_blank" rel="noopener noreferrer">YouTube</a></div><p class="hero-proof">Former Big 4 Accountant · Certified QuickBooks ProAdvisor</p></div><div class="hero-photo"><div class="hero-photo-box">'+photo+'</div></div></section>'
    cards=[('/monthly-bookkeeping/','Monthly bookkeeping','Keep transactions organized, accounts reconciled, and reports current.'),('/cleanup-catch-up/','Cleanup & catch-up','Get unfinished periods in order and establish a reliable starting point.'),('/quickbooks-online/','QuickBooks Online help','Set up your file, improve your routine, or get help with specific questions.')]
    main+='<section class="services" id="services"><div class="section-label">Services</div><h2 class="section-title">How I can help with your accounting</h2><p class="section-sub">Hand off the monthly work, catch up on a backlog, or get help doing it yourself.</p>'+hub_cards(cards)+'</section>'
    main+='<section class="pricing" id="pricing"><div class="section-label">Pricing</div><h2 class="section-title">Monthly bookkeeping pricing</h2><p class="section-sub">'+esc(PRICING_INTRO)+'</p><div class="pricing-guarantee">Love your first month of books, or it’s free</div>'+price_cards()+'<div class="content-links"><a href="/pricing/">See how pricing works</a></div></section>'
    main+='<section class="services" id="who"><div class="section-label">Who I work with</div><h2 class="section-title">Bookkeeping across industries</h2><p class="section-sub">I work with service firms, retailers, trades, and professional practices. We’ll build the scope around how your business operates.</p><div class="content-links"><a href="/who-we-work-with/">Explore business types</a></div></section>'
    homefaq=[(i['q'],i['a']) for i in FAQ if i['id'] in ['industries','catch-up','owner','tax-preparer']]
    main+='<section class="faq-section" id="faq"><h2 class="section-title">Before we talk</h2>'+faq_html(homefaq)+'<div class="content-links"><a href="/bookkeeping-faq/">Read all questions</a></div></section>'
    main+='<section class="about" id="about"><div class="about-inner"><div class="about-photo-box">'+portrait('aboutme','Jack fly fishing on the coast')+'</div><div class="about-content"><div class="section-label">Meet your bookkeeper</div><h2 class="section-title">Hi, I’m Jack</h2>'+bio(homepage=True)+'<p><a href="/about/">More about Glenhold</a></p></div></div></section>'
    main+=youtube_section()
    main+=cta('Ready to get your books in order?','Start with a free call to discuss the help you need.')+contact_block('/')
    write_page('Bookkeeping & Financial Reporting | Glenhold','Monthly bookkeeping, catch-up, and QuickBooks Online support. Work directly with Jack. Monthly bookkeeping starts at $350.','/',main,[('Home','/')],[faq_node(homefaq,'/')],CITIES,AREA)

def say(text):
    return text.replace("'", "\u2019")


def faq_pair(fid):
    for item in FAQ:
        if item['id'] == fid:
            return item['q'], item['a']
    raise KeyError(fid)


def build_year_end():
    """Paid-search landing page. Kept out of the nav, sitemap, and llms files.

    noindex, follow: Google Ads can fetch the page, and the offer should not
    compete with the homepage in organic search. robots.txt still allows the URL.
    """
    path = '/year-end-bookkeeping/'
    credentials = say("I've been in accounting since 2021, including audit work at PwC, and I'm a Certified QuickBooks ProAdvisor.")
    short_guarantee = say("Love your first month of books, or it's free")
    price_depends = "Your monthly price depends on transaction volume, the accounts I\u2019ll reconcile, and the reporting you need."
    if price_depends not in PRICING_INTRO:
        raise SystemExit('pricing intro changed; update the landing page quote sentence')
    behind_q, behind_a = faq_pair('catch-up')
    guarantee_q, guarantee_a = faq_pair('guarantee')
    pricing_html = (ROOT / 'pricing' / 'index.html').read_text(encoding='utf-8')
    faq_html_page = (ROOT / 'bookkeeping-faq' / 'index.html').read_text(encoding='utf-8')
    if short_guarantee not in pricing_html:
        raise SystemExit('short guarantee no longer matches the pricing page')
    if guarantee_a not in faq_html_page or behind_a not in faq_html_page:
        raise SystemExit('reused FAQ answers no longer match the bookkeeping FAQ page')

    faqs = [
        (say("What is Year-End Clean Books?"),
         say("I catch up messy books, then keep them current with monthly bookkeeping from $400 a month. Sign up through December 31, 2026, and I waive the setup fee. ") + guarantee_a),
        (behind_q, behind_a),
        (guarantee_q, guarantee_a),
        (say("Is the work remote?"),
         say("The work is remote. I'm based in Simi Valley, and I work with trades and home-service businesses in Simi Valley, Ventura County, and the San Fernando Valley. Share your city when you get in touch so I can confirm the fit.")),
    ]
    photo = '<picture><source srcset="/headshot.webp" type="image/webp"><img src="/headshot.jpg" width="1000" height="1333" alt="Jack, founder of Glenhold Bookkeeping" decoding="async" fetchpriority="high" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center -10%"></picture>'
    book = f'<a class="btn-primary" href="{CALENDAR}" target="_blank" rel="noopener noreferrer">Book a Free Call</a>'
    book_slate = f'<a class="btn-slate-solid" href="{CALENDAR}" target="_blank" rel="noopener noreferrer">Book a Free Call</a>'
    book_sage = f'<a class="btn-sage" href="{CALENDAR}" target="_blank" rel="noopener noreferrer">Book a Free Call</a>'
    call = f'<a class="btn-ghost" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>'
    call_outline = f'<a class="btn-outline-slate" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a>'
    styles = '''<style>
body.lp .lp-nav-actions { display: flex; align-items: center; gap: 14px; }
body.lp .lp-hero { min-height: 0; padding-top: 48px; padding-bottom: 56px; }
body.lp .lp-hero .hero-content { padding-bottom: 0; }
body.lp .lp-hero .hero-sub { margin-bottom: 16px; }
body.lp .lp-for { color: rgba(255,255,255,.88); font-size: 1rem; max-width: 540px; margin: 0 0 28px; line-height: 1.6; }
body.lp .lp-hero .hero-proof { margin-top: 22px; }
body.lp .lp-hero .hero-photo { margin-top: 0; align-items: center; }
body.lp .lp-hero .hero-photo-box { height: 460px; }
body.lp section { padding-top: 56px; padding-bottom: 56px; }
body.lp .section-sub { max-width: 720px; }
body.lp .lp-offer { max-width: 640px; background: var(--white); border: 1px solid var(--border); border-radius: 6px; padding: 32px 28px; }
body.lp .lp-offer .pricing-guarantee { margin-bottom: 20px; }
body.lp .lp-price-label { color: var(--text-muted); font-size: .85rem; font-weight: 500; margin: 0 0 4px; }
body.lp .lp-price { padding-top: 0; }
body.lp .lp-offer-note { margin: 8px 0 22px; color: var(--text-muted); font-size: .95rem; }
body.lp .lp-offer-call { margin: 14px 0 0; text-align: center; }
body.lp .lp-offer-call a { color: var(--slate); font-weight: 700; }
body.lp .lp-steps { counter-reset: step; list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; max-width: none; }
body.lp .lp-steps li { background: var(--cream); border: 1px solid var(--border); border-radius: 6px; padding: 22px; margin: 0; }
body.lp .lp-steps h3 { font-family: "DM Serif Display", serif; color: var(--slate); font-size: 1.35rem; line-height: 1.25; margin: 0 0 8px; }
body.lp .lp-steps h3::before { counter-increment: step; content: counter(step) ". "; }
body.lp .lp-steps p { color: var(--text-muted); margin: 0; }
body.lp .lp-footer .footer-desc { max-width: 540px; }
body.lp .lp-footer ul { list-style: none; padding: 0; margin: 18px 0; display: flex; flex-wrap: wrap; gap: 10px 20px; }
body.lp .lp-footer li, body.lp .lp-footer a { color: #e0e9e7; font-size: .95rem; }
body.lp .lp-bar { display: none; }
@media (max-width: 900px) {
  body.lp .lp-for, body.lp .lp-hero .hero-proof { margin-left: auto; margin-right: auto; }
  body.lp .lp-steps { grid-template-columns: 1fr; }
  body.lp .nav-wordmark { max-width: none; }
}
@media (max-width: 700px) {
  body.lp { padding-bottom: 84px; }
  body.lp .lp-nav-book { display: none; }
  body.lp .lp-bar {
    display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
    position: fixed; left: 0; right: 0; bottom: 0; z-index: 120;
    background: var(--slate); padding: 10px 12px calc(10px + env(safe-area-inset-bottom));
  }
  body.lp .lp-bar a { text-align: center; }
}
@media (max-width: 480px) {
  body.lp .hero-ctas { flex-direction: column; align-items: stretch; }
  body.lp .hero-ctas a { text-align: center; }
}
@media print {
  body.lp { padding-bottom: 0; }
  body.lp .lp-bar { display: none; }
}
</style>'''
    main = styles
    main += '<section class="hero lp-hero"><div class="hero-content">'
    main += '<div class="hero-eyebrow">Year-End Clean Books</div>'
    main += '<h1>' + say("I'll get your books caught up before year-end.") + '</h1>'
    main += '<p class="hero-sub">' + say("I catch up the months that fell behind, then keep them current. Monthly bookkeeping from $400 a month. Sign up through December 31, 2026, and I waive the setup fee.") + '</p>'
    main += '<p class="lp-for">' + say("Remote bookkeeping for HVAC, plumbing, electrical, contracting, landscaping, and cleaning businesses in Simi Valley, Ventura County, and the San Fernando Valley.") + '</p>'
    main += '<div class="hero-ctas">' + book + call + '<a class="btn-ghost" href="#contact">Send a Message</a></div>'
    main += '<p class="hero-proof">' + say("I'm Jack. ") + credentials + '</p>'
    main += '<div class="hero-photo-mobile"><img src="/headshot.webp" width="1000" height="1333" alt="Jack, founder of Glenhold Bookkeeping" style="width:75%;height:auto;display:block;border-radius:6px;margin:0 auto"></div>'
    main += '</div><div class="hero-photo"><div class="hero-photo-box">' + photo + '</div></div></section>'
    main += '<section class="services" id="problem"><div class="section-label">The timing</div>'
    main += '<h2 class="section-title">' + say("I'll get the unfinished months ready for year-end.") + '</h2>'
    main += '<p class="section-sub">' + say("You've been running the jobs. Tax time comes next, and your preparer needs a clean set of records. I'll get the unfinished months in order and keep a monthly close, so you can see where the business stands.") + '</p>'
    main += '<div class="services-grid">'
    main += '<div class="service-card"><h3>Catch-up</h3><p>' + say("I put the unfinished months in order: missing transactions, reconciled accounts, and reports for the periods we agree on.") + '</p></div>'
    main += '<div class="service-card"><h3>Monthly books</h3><p>' + say("Then I keep them current. That means categorization, bank and card reconciliation, and a profit and loss statement and balance sheet. The target is reports by the 15th of the following month, once the necessary statements and answers are available.") + '</p></div>'
    main += '<div class="service-card"><h3>' + say("You work with me") + '</h3><p>' + say("The work is remote. You work directly with me, and I'll reply within one business day.") + '</p></div>'
    main += '</div></section>'
    main += '<section class="pricing" id="offer"><div class="section-label">The offer</div>'
    main += '<h2 class="section-title">' + say("Catch up messy books, then keep them current.") + '</h2>'
    main += '<div class="lp-offer"><div class="pricing-guarantee">' + short_guarantee + '</div>'
    main += '<p class="lp-price-label">Monthly bookkeeping from</p>'
    main += '<div class="pricing-price lp-price">$400 <span>/ mo</span></div>'
    main += '<hr class="pricing-divider"><ul class="pricing-list">'
    main += '<li>' + say("Catch-up on messy books, then monthly bookkeeping") + '</li>'
    main += '<li>' + say("Setup fee waived when you sign up through December 31, 2026") + '</li>'
    main += '<li>' + say("You work directly with me, remotely") + '</li>'
    main += '</ul><p class="lp-offer-note">' + price_depends + ' ' + guarantee_a + '</p>'
    main += book_sage
    main += '<p class="lp-offer-call"><a href="tel:' + PHONE_TEL + '">' + say("Or call ") + PHONE_DISPLAY + '</a></p>'
    main += '</div></section>'
    main += '<section class="services" id="how"><div class="section-label">How it works</div>'
    main += '<h2 class="section-title">' + say("Three steps, then the books stay caught up.") + '</h2>'
    main += '<ol class="lp-steps">'
    main += '<li><h3>' + say("Tell me where things stand") + '</h3><p>' + say("Book a call, call me, or send the form. Tell me the kind of work you do, how far behind the books are, and when your tax preparer needs them.") + '</p></li>'
    main += '<li><h3>' + say("We agree on the scope") + '</h3><p>' + say("I look at the accounts and the backlog. We settle the catch-up and the monthly plan before I start.") + '</p></li>'
    main += '<li><h3>' + say("I catch the books up, then close each month") + '</h3><p>' + say("You get the reports, and you work with me the whole way. I prepare the books. Your tax preparer files the return.") + '</p></li>'
    main += '</ol></section>'
    main += '<section class="faq-section" id="faq"><h2 class="section-title">Common questions</h2>' + faq_html(faqs) + '</section>'
    main += '<div class="cta-banner" id="cta-banner"><h2>' + say("Ready for clean books before year-end?") + '</h2>'
    main += '<p>' + say("Book a free call, send the short form, or call me.") + '</p>'
    main += '<div class="cta-banner-btns">' + book_slate + '<a class="btn-outline-slate" href="#contact">Send a Message</a>' + call_outline + '</div></div>'
    form = contact_block(path)
    hidden = f'<input type="hidden" name="page" value="{path}" />'
    if hidden not in form:
        raise SystemExit('contact form is missing the page field')
    form = form.replace(hidden, hidden + '\n        <input type="hidden" name="offer" value="Year-End Clean Books" />', 1)
    form = form.replace('<option>Cleanup / Catch-Up</option>', '<option selected>Year-End Clean Books</option>\n            <option>Cleanup / Catch-Up</option>', 1)
    main += form
    main += '<div class="lp-bar" role="region" aria-label="Call or book"><a class="btn-ghost" href="tel:' + PHONE_TEL + '">Call</a>' + book + '</div>'
    nav_html = f'''<nav class="lp-nav" aria-label="Main navigation">
    <a class="nav-logo" id="top" href="#top" style="display:flex;align-items:center;gap:10px;"><img src="/logo.png" alt="Glenhold Bookkeeping" width="28" height="38" style="height:38px;width:auto;display:block;" /><span class="nav-wordmark" style="color:white;font-family:'DM Serif Display',serif;font-size:1.25rem;letter-spacing:0.02em;line-height:1.1;">Glenhold <span style="color:var(--white);">Bookkeeping</span></span></a>
    <div class="lp-nav-actions">
      <a class="nav-phone" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      <a class="btn-primary lp-nav-book" href="{CALENDAR}" target="_blank" rel="noopener noreferrer">Book a Free Call</a>
    </div>
  </nav>'''
    footer_html = f'''<footer>
    <div class="lp-footer">
      <div class="footer-brand">Glenhold <span>Bookkeeping</span></div>
      <p class="footer-desc">Remote bookkeeping for trades and home-service businesses around Simi Valley. You work directly with me.</p>
      <ul>
        <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        <li><a href="mailto:{EMAIL}">jack&#64;glenhold.com</a></li>
        <li>Mon\u2013Sat, 6am\u20136pm PT</li>
        <li><a href="/privacy/">Privacy notice</a></li>
      </ul>
      <p class="footer-copy">\u00a9 2026 Glenhold Advisory LLC \u00b7 Doing business as Glenhold Bookkeeping</p>
    </div>
  </footer>'''
    description = say("I'll catch up messy books, then keep monthly bookkeeping current from $400 a month. Setup fee waived through December 31, 2026. Remote bookkeeping for trades and home services around Simi Valley.")
    offer = {
        "@type": "Offer",
        "name": "Year-End Clean Books",
        "url": HOME + path,
        "priceCurrency": "USD",
        "description": say("Catch-up on messy books, then monthly bookkeeping from $400 a month. Setup fee waived for sign-ups through December 31, 2026. Love your first month of monthly bookkeeping, or that month is free."),
        "priceSpecification": {
            "@type": "UnitPriceSpecification",
            "minPrice": 400,
            "priceCurrency": "USD",
            "unitText": "month",
            "description": "Starting monthly price. Final price quoted by transaction volume, accounts, and reporting.",
        },
    }
    service = {
        "@type": "Service",
        "@id": HOME + path + "#service",
        "name": "Year-End Clean Books",
        "serviceType": "Bookkeeping",
        "description": description,
        "provider": {"@id": HOME + "/#business"},
        "url": HOME + path,
        "areaServed": [
            {"@type": "City", "name": "Simi Valley", "containedInPlace": {"@type": "AdministrativeArea", "name": "Ventura County, California"}},
            {"@type": "AdministrativeArea", "name": "Ventura County, California"},
            {"@type": "AdministrativeArea", "name": "San Fernando Valley, California"},
        ],
        "offers": offer,
    }
    write_page(
        'Year-End Clean Books | Glenhold Bookkeeping',
        description,
        path,
        main,
        [('Home', '/'), ('Year-End Clean Books', path)],
        [service, faq_node(faqs, path)],
        CITIES,
        AREA,
        robots='noindex, follow',
        body_class='lp',
        nav_html=nav_html,
        footer_html=footer_html,
        include_business=False,
        indexable=False,
        modified='2026-11-20',
    )
    written = (ROOT / 'year-end-bookkeeping' / 'index.html').read_text(encoding='utf-8')
    lowered = written.lower()
    banned = ['hawley', 'restaurant', 'caf\u00e9', 'cafe', 'diner', 'bakery', 'food', 'big 4', 'former big', 'years of experience', 'started my career', 'started at pwc', 'i started at']
    for word in banned:
        if word in lowered:
            raise SystemExit('landing page contains banned copy: ' + word)
    if written.count(credentials) != 1:
        raise SystemExit('credentials line must appear once')
    if 'noindex, follow' not in written:
        raise SystemExit('landing page must be noindex')
    if '$400' not in written or any(price in written for price in ('$350', '$450', '$700', '$349', '$599')):
        raise SystemExit('landing page price copy is wrong')
    if CALENDAR not in written or f'tel:{PHONE_TEL}' not in written or 'https://formspree.io/f/xvzwqvgv' not in written:
        raise SystemExit('landing page is missing the existing contact paths')
    if short_guarantee not in written or guarantee_a not in written:
        raise SystemExit('landing page is missing the existing guarantee wording')
    if 'year-end-bookkeeping' in (ROOT / 'index.html').read_text(encoding='utf-8'):
        raise SystemExit('landing page leaked into the homepage')


def write_discovery():
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://glenhold.com/sitemap.xml\n')
    urls=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    urls += ['<url><loc>'+HOME+p['path']+'</loc><lastmod>'+LASTMOD+'</lastmod></url>' for p in sorted(PAGES,key=lambda p:p['path'])]
    (ROOT/'sitemap.xml').write_text('\n'.join(urls+['</urlset>'])+'\n')
    facts='# Glenhold Bookkeeping\n\nSimi Valley-based business bookkeeping. Work directly with Jack, a former Big 4 accountant and Certified QuickBooks ProAdvisor. Glenhold Bookkeeping is the client-facing name of Glenhold Advisory LLC.\n\nPhone: (805) 419-3451\nEmail: jack@glenhold.com\nYouTube: https://www.youtube.com/@bookkeepingbizblueprint (Bookkeeping Business Blueprint)\n\nMonthly starting prices are $350 for Essential, $450 for Core, and $700 for Strategic. Quotes depend on volume, accounts, and reporting complexity. Cleanup and training are quoted separately. Tax return preparation and filing are separate from the listed bookkeeping plans.\n\n## Pages\n'
    short=[p for p in PAGES if p['path'] in ['/','/services/','/pricing/','/contact/','/service-areas/','/bookkeeping-faq/','/mission/','/privacy/']]
    line=lambda p:'- ['+p['title']+']('+HOME+p['path']+'): '+p['description']+'\n'
    (ROOT/'llms.txt').write_text(facts+''.join(line(p) for p in short))
    (ROOT/'llms-full.txt').write_text(facts+''.join(line(p) for p in PAGES)+'\n## Questions\n'+''.join('### '+i['q']+'\n\n'+i['a']+'\n\n' for i in FAQ))
    (ROOT/(INDEXNOW_KEY+'.txt')).write_text(INDEXNOW_KEY+'\n')
    (ROOT/'.nojekyll').write_text('')

def main():
    PAGES.clear()
    for build in [build_home,build_services,build_industries,build_cities,build_faq,build_resources,build_getting_started,build_about,build_mission,build_pricing,build_contact,build_privacy]:build()
    build_year_end()
    write_discovery()
    sitemap = (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
    robots = (ROOT / 'robots.txt').read_text(encoding='utf-8')
    if '/year-end-bookkeeping/' in sitemap:
        raise SystemExit('ad landing page must stay out of the sitemap')
    if 'Disallow: /year-end-bookkeeping' in robots:
        raise SystemExit('ad landing page must stay crawlable for Google Ads')
    print('Generated',len(PAGES),'indexable pages and 24 legacy location redirects.')

if __name__=='__main__':main()
