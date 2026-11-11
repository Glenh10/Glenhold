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
    INDEXNOW_KEY, area_nodes, write_page, faq_node, faq_html, service_node,
    offer, esc, crumb_html, contact_block, chips, hub_cards, related_links, cta)

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

def price_cards():
    plans=[('Essential','349','For straightforward books and reliable monthly reports',[
        'Expense categorization','Monthly bank &amp; card reconciliation','Monthly financial statements','Clean books for tax season']),
        ('Core','599','For owners who want a clearer picture of business performance',[
        'Everything in Essential','Quarterly profit and expense summary','Year-to-date performance comparison','Priority support']),
        ('Strategic','1,499','For businesses that need tailored reporting and a monthly walkthrough',[
        'Everything in Core','Custom financial reports for your business','Accrual accounting, payroll journal entries, and loan tracking','Monthly call to walk through your numbers'])]
    return '<div class="pricing-grid">'+''.join(
        '<div class="pricing-card'+(' featured' if name=='Core' else '')+'"><h3>'+name+'</h3><p class="pricing-tagline">'+tagline+'</p><div class="pricing-price"><span class="pricing-prefix">Starting at</span>$'+price+' <span>/ mo</span></div><hr class="pricing-divider"><ul class="pricing-list">'+''.join('<li>'+p+'</li>' for p in points)+'</ul><a class="'+('btn-sage' if name=='Core' else 'btn-slate')+'" href="#contact">Get Started</a></div>' for name,price,tagline,points in plans)+'</div>'

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
    main=header+'</header><article class="article-body">'+body+'</article>'
    if contact:main+=contact_block(path)
    write_page(title,description,path,main,crumbs,nodes,CITIES,AREA)

SERVICES=[
    dict(slug='monthly-bookkeeping',name='Monthly bookkeeping',description='Monthly bookkeeping from $349 for small businesses near Simi Valley. Transaction categorization, reconciliation, and clear financial reports.',lede='Keep your books current and understand how your business is doing.',body=
        section('A monthly routine you can rely on','<p>Glenhold Bookkeeping helps small business owners keep their records organized throughout the year. You work directly with Jack, a former Big 4 accountant and Certified QuickBooks ProAdvisor based in Simi Valley.</p><p>The work starts with your accounts, how you get paid, and the reports you need. We agree on the scope and a monthly schedule before getting started.</p>')+
        section('What is included','<ul><li><strong>Transaction categorization:</strong> organize income and expenses in accounts suited to your business.</li><li><strong>Bank and credit card reconciliation:</strong> check the books against statements and resolve differences.</li><li><strong>Monthly financial reports:</strong> receive a profit and loss statement and balance sheet.</li><li><strong>Email support:</strong> get answers to bookkeeping questions between closes.</li></ul><p>The target is to deliver reports by the 15th of the following month, once the necessary statements and answers are available.</p>')+
        section('Choose your level of support','<p>Essential starts at $349 per month. Core starts at $599 and adds quarterly profit and expense summaries, year-to-date comparisons, and priority support. Strategic starts at $1,499 and includes tailored reporting and a monthly call to walk through your numbers.</p><p>Your quote reflects transaction volume, the number of accounts, and reporting complexity. <a href="/pricing/">Compare the monthly plans</a>.</p>')+
        section('Need to catch up first?','<p>If previous months are unfinished, <a href="/cleanup-catch-up/">cleanup and catch-up</a> can establish a reliable starting point. If you prefer to maintain the books yourself, ask about <a href="/quickbooks-online/">QuickBooks Online training</a>.</p>')),
    dict(slug='cleanup-catch-up',name='Cleanup and catch-up bookkeeping',description='Catch up on unfinished bookkeeping, reconcile accounts, and prepare clear financial reports. Simi Valley-based Glenhold quotes each cleanup by scope.',lede='Get unfinished bookkeeping back on track.',body=
        section('Start with a clear picture of the work','<p>Whether you are a few months behind or need to sort through older records, Glenhold can help assess what needs attention. Cleanup corrects existing records; catch-up completes periods that have not been finished. A project may involve both.</p>')+
        section('What a project can include','<ul><li>Organizing available statements and transaction exports.</li><li>Recording missing transactions and reviewing duplicates.</li><li>Resolving unmatched transfers and unclear entries with you.</li><li>Reconciling bank and credit card accounts.</li><li>Organizing the chart of accounts and preparing financial reports.</li><li>Identifying open questions for you or your tax preparer.</li></ul>')+
        section('Pricing and timing','<p>Each project is quoted based on the number of periods, accounts, transactions, and corrections involved. Monthly plan starting prices are separate from historical cleanup work. Mention any deadlines during the first conversation so we can discuss a realistic schedule.</p>')+
        section('What to prepare','<p>Start with an account list, the periods you need help with, and a note of any missing records. Include accounts closed during the period. See the <a href="/getting-started/">handoff checklist</a> before gathering documents, or book a call to find out what is needed.</p>')),
    dict(slug='quickbooks-online',name='QuickBooks Online setup and training',description='QuickBooks Online setup, chart of accounts organization, training, and accuracy check-ins from a Certified QuickBooks ProAdvisor in Simi Valley.',lede='Build a system you understand and a routine you can maintain.',body=
        section('Help with your QuickBooks Online file','<p>Jack is a Certified QuickBooks ProAdvisor who can help you set up QuickBooks Online, organize your chart of accounts, or work through an existing bookkeeping issue.</p><p>Tell him what you want to do yourself and where you would like support. Training can focus on the tasks you handle rather than features you do not need.</p>')+
        section('Setup and training can cover','<ul><li>A chart of accounts that fits your business.</li><li>A routine for reviewing and categorizing transactions.</li><li>Understanding transfers and reconciling accounts.</li><li>Reading your profit and loss statement and balance sheet.</li><li>Accuracy check-ins on an agreed schedule.</li></ul>')+
        section('A specific question or ongoing support','<p>You can ask for help with a particular issue, discuss a cleanup, or move to <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Consulting and training are quoted separately. Software arrangements and the work included will be discussed as part of your quote.</p>')),
    dict(slug='financial-statements',name='Financial statements',description='Understand your profit and loss statement and balance sheet. Monthly financial reports are included in Glenhold bookkeeping plans from $349.',lede='Clear reports that help you understand your business.',body=
        section('What you receive each month','<p>All monthly bookkeeping plans include a profit and loss statement and a balance sheet, prepared from the bookkeeping records. The target is the 15th of the following month when the necessary information is available.</p>')+
        section('What the reports tell you','<p><strong>A profit and loss statement</strong> shows income, expenses, and profit over a period. <strong>A balance sheet</strong> shows assets, liabilities, and equity at a particular date. Together, they give you a fuller view than the bank balance alone.</p>')+
        section('More context as your business grows','<p>Core adds a quarterly profit and expense summary and year-to-date comparisons. Strategic adds reports tailored to your business and a monthly call to discuss them. <a href="/pricing/">Compare the plans</a>.</p><p>These are bookkeeping reports for management use and sharing with your tax preparer. If a lender or another recipient requires a specific report or assurance engagement, share that request before work begins.</p>')),
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
    body+=section('A clear scope from the start','<p>Monthly plans start at $349. Cleanup and training are quoted separately. Tell Jack about any special reporting, software, or filing requirements so the proposal accurately reflects what you need.</p><p><a href="/pricing/">View pricing</a> or <a href="/getting-started/">see what to prepare</a>.</p>')
    write_inner('Bookkeeping Services | Glenhold Bookkeeping','Monthly bookkeeping, cleanup, and QuickBooks Online support for small businesses around Simi Valley. Work directly with Jack. Plans from $349.','/services/','Bookkeeping services','Practical help with your books, from setup to the monthly close.',body)

def build_industries():
    for i in INDUSTRIES:
        path='/who-we-work-with/'+i['slug']+'/'
        body=section('Bookkeeping that fits how you operate',''.join('<p>'+esc(p)+'</p>' for p in i['paragraphs']))
        body+=section('Useful details for the first call','<ul>'+''.join('<li>'+esc(p)+'</li>' for p in i['points'])+'</ul>')
        body+=section('Choose the help you need','<p><a href="/monthly-bookkeeping/">Monthly bookkeeping</a> keeps the records current. <a href="/cleanup-catch-up/">Cleanup and catch-up</a> address unfinished periods. <a href="/quickbooks-online/">QuickBooks Online support</a> helps with setup, training, or specific questions.</p><p>Glenhold is based in Simi Valley and works with small businesses across <a href="/service-areas/">surrounding communities</a>. Monthly plans start at $349, with the scope and final quote based on your needs.</p>')
        write_inner('Bookkeeping for '+i['name']+' | Glenhold','Bookkeeping for '+i['name'].lower()+' in Simi Valley and surrounding communities. Monthly support, cleanup, and QuickBooks Online help.',path,'Bookkeeping for '+i['name'].lower(),i['intro'],body,
            [('Home','/'),('Who we work with','/who-we-work-with/'),(i['name'],path)])
    cards=[('/who-we-work-with/'+i['slug']+'/',i['name'],i['intro']) for i in INDUSTRIES]
    write_inner('Small Businesses We Work With | Glenhold Bookkeeping','Glenhold works with small businesses across industries around Simi Valley. Explore bookkeeping for service firms, shops, trades, practices, and more.','/who-we-work-with/','Bookkeeping for local small businesses','Different businesses. The same care with your books.',
        section('Find the help your business needs','<p>Glenhold works with small businesses across industries. These examples show the information that may be useful when discussing your bookkeeping. If your business is not listed, get in touch—we can still discuss whether it is a fit.</p>'+hub_cards(cards)))


LOCAL_PAGE_CONTENT = {
    'simi-valley': ('Based here in Simi Valley.', 'I’m Jack, a Simi Valley local and the founder of Glenhold Bookkeeping. I offer monthly bookkeeping, catch-up work, and QuickBooks Online support for small businesses across industries.', 'If bookkeeping keeps slipping behind the day-to-day work, we can discuss which tasks you want to hand off and the reports you need. You work directly with me throughout the engagement.'),
    'moorpark': ('Bookkeeping support from neighboring Simi Valley.', 'I offer monthly bookkeeping, cleanup, and QuickBooks Online support for Moorpark small businesses. The scope is based on your accounts, transaction volume, and reporting needs.', 'You can hand off the monthly work or ask for help improving the routine you manage yourself. During the first call, tell me which periods are complete and where you need support.'),
    'thousand-oaks': ('Monthly bookkeeping, catch-up, and QuickBooks Online help.', 'Glenhold offers bookkeeping for small businesses in Thousand Oaks, including Newbury Park. I’m based in Simi Valley, and you work directly with me.', 'If your CPA or tax preparer has asked for financial reports, bring that request to the first conversation. We can discuss the work needed to provide organized records and an agreed reporting schedule.'),
    'westlake-village': ('Work directly with your bookkeeper.', 'I offer bookkeeping support for small businesses in Westlake Village. Choose monthly bookkeeping, cleanup for unfinished periods, or help using QuickBooks Online.', 'Tell me which reports you use today and what you need to understand better. The monthly plans provide different levels of reporting and support, with the final scope agreed before work begins.'),
    'camarillo': ('Bookkeeping for your Camarillo business.', 'Glenhold offers monthly bookkeeping, cleanup, and QuickBooks Online support for small businesses in Camarillo. I work from Simi Valley and handle your bookkeeping directly.', 'If you use several bank accounts, cards, or payment processors, mention them during the first conversation. A complete account list helps establish the work and an appropriate quote.'),
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
        body += section('Services and pricing', '<p><a href="/monthly-bookkeeping/">Monthly bookkeeping</a> starts at $349. <a href="/cleanup-catch-up/">Cleanup and catch-up</a> and <a href="/quickbooks-online/">QuickBooks Online support</a> are quoted separately.</p><p>Every monthly plan includes transaction categorization, bank and credit card reconciliation, and financial statements. Core adds quarterly summaries and year-to-date comparisons. Strategic adds tailored reporting and a monthly walkthrough.</p><p><a href="/pricing/">Compare plans</a> or <a href="/getting-started/">see what to prepare</a> for a handoff.</p>')
        write_inner('Bookkeeping in ' + city['name'] + ' | Glenhold', 'Monthly bookkeeping, cleanup, and QuickBooks Online help for small businesses in ' + city['name'] + '. Work directly with Jack. Monthly plans from $349.', path, 'Bookkeeping for ' + city['name'] + ' small businesses', lede, body, [('Home','/'),('Service areas','/service-areas/'),(city['name'],path)])
    body = section('Based in Simi Valley', '<p>I offer bookkeeping for small businesses in Simi Valley and surrounding Ventura County and Los Angeles County communities. My local focus is generally within about an hour of Simi Valley, depending on traffic.</p><p>The services are the same across the area: monthly bookkeeping, cleanup and catch-up, and QuickBooks Online support.</p>')
    for county in ['Ventura County', 'Los Angeles County']:
        members = [c for c in CITIES if c['group'] == county]
        items = []
        for city in sorted(members, key=lambda c:c['name']):
            label = '<a href="/service-areas/' + city['slug'] + '/">' + esc(city['name']) + '</a>' if city['slug'] in LOCAL_PAGE_CONTENT else esc(city['name'])
            items.append('<li id="' + city['slug'] + '">' + label + '</li>')
        extras = ['Oak Park'] if county == 'Ventura County' else ['Tarzana', 'Winnetka']
        items += ['<li>' + name + '</li>' for name in extras]
        body += section(county, '<ul class="service-city-list">' + ''.join(items) + '</ul>')
    body += section('Not sure whether you are in the area?', '<p>Send your city and a short description of the help you need. I can confirm the fit before we discuss the work.</p>')
    write_inner('Bookkeeping Service Areas | Simi Valley & Nearby', 'Bookkeeping for small businesses in Simi Valley and surrounding Ventura County and Los Angeles County communities. Monthly support, cleanup, and QuickBooks Online help.', '/service-areas/', 'Areas I serve', 'Bookkeeping for businesses in Simi Valley and the surrounding communities.', body)


def build_faq():
    body=section('Before we get started','<p>Here are answers to common questions about pricing, services, and working with Jack. If your situation needs a closer look, book a free call or send a message.</p>')
    body+='<section>'+''.join('<details id="'+i['id']+'"><summary>'+esc(i['q'])+'</summary><p>'+esc(i['a'])+'</p></details>' for i in FAQ)+'</section>'
    write_inner('Bookkeeping FAQ | Glenhold Bookkeeping','Answers about bookkeeping pricing, monthly reports, catch-up, QuickBooks Online, service areas, and getting started with Glenhold.','/bookkeeping-faq/','Your bookkeeping questions, answered','What to expect from the services and the first conversation.',body,extra=[faq_node([(i['q'],i['a']) for i in FAQ],'/bookkeeping-faq/')])

def build_resources():
    cards=[('/getting-started/','What to give your bookkeeper','An account and records checklist for a smoother handoff.'),('/bookkeeping-faq/','Common questions','Pricing, monthly reports, cleanup, and getting started.'),('/financial-statements/','Understand your reports','What a profit and loss statement and balance sheet tell you.'),('/pricing/','Compare monthly plans','Choose the level of reporting and support you need.')]
    write_inner('Bookkeeping Resources | Glenhold Bookkeeping','Practical bookkeeping resources: preparing records, understanding financial reports, choosing a plan, and getting started.','/resources/','Bookkeeping resources','Useful information for choosing support and preparing your records.',section('Start here',hub_cards(cards)))

def build_getting_started():
    body=section('Start with the basics','<p>For an introductory call, tell Jack about your business, the number of accounts, whether your books are current, and the help you need. You do not need to gather every record before that conversation.</p><p>Once the work is scoped, this checklist can help prepare for a handoff. Ask how to share sensitive documents before sending them.</p>')
    records=[('Account list','Include checking, savings, credit cards, loans, and payment processors. Mention accounts closed or replaced during the period.'),('Statements','Gather statements for the agreed periods, including opening and closing balances. Transaction exports can be useful alongside them.'),('Existing bookkeeping','Identify the QuickBooks Online file, last completed month, last reconciled month, and any known issues.'),('Loan and payroll records','If relevant to the work, identify available statements, schedules, and reports from your payroll provider.'),('Owner transactions','Flag contributions, withdrawals, and business costs paid personally.'),('Deadlines and report requests','Share requests from your tax preparer, lender, or other recipient.')]
    body+=section('Handoff checklist','<ol>'+''.join('<li><strong>'+t+'.</strong> '+b+'</li>' for t,b in records)+'</ol>')
    body+=section('Missing something?','<p>A short list of missing records helps plan the work. Include both accounts involved in transfers whenever possible. If you are unsure which months have been reconciled, Jack can discuss how to establish a starting point.</p>')
    write_inner('What to Give Your Bookkeeper | Glenhold Checklist','Prepare for a bookkeeping handoff with a practical checklist of accounts, statements, existing records, and deadlines.','/getting-started/','What to give your bookkeeper','A straightforward checklist for a smoother handoff.',body)

BIO='<p>I’m Jack, a Simi Valley local, former Big 4 accountant, and Certified QuickBooks ProAdvisor. I started Glenhold to help small business owners keep reliable books and understand their financial reports.</p><p>You work directly with me. We’ll discuss what you need, agree on the scope, and set up a routine for your records and questions.</p><p>Outside work, I enjoy fly fishing, walks, and attending Mass with my wife and two children.</p>'

def portrait(source,alt):
    width,height=('1000','1333') if source=='headshot' else ('1100','1467')
    return '<picture><source srcset="/'+source+'.webp" type="image/webp"><img src="/'+source+'.jpg" width="'+width+'" height="'+height+'" alt="'+alt+'" loading="lazy" decoding="async" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top"></picture>'

def youtube_section():
    if not YOUTUBE:
        return ''
    return '<section class="video-section" id="videos"><div class="section-label">Bookkeeping videos</div><h2 class="section-title">Watch how I explain the books</h2><p class="section-sub">Get to know me and how I approach bookkeeping on my YouTube channel.</p><a class="btn-slate-solid" href="' + YOUTUBE + '" target="_blank" rel="noopener noreferrer">Watch on YouTube</a></section>'

def build_about():
    body='<section class="about" style="padding-top:0"><div class="about-inner"><div class="about-photo-box">'+portrait('aboutme','Jack fly fishing on the coast')+'</div><div class="about-content">'+BIO+'</div></div></section>'
    body+=youtube_section()
    body+=section('Working with me','<p>You work with me directly, from the first call through every close. </p>')
    write_inner('About Jack | Glenhold Bookkeeping','Meet Jack, a Simi Valley local, former Big 4 accountant, Certified QuickBooks ProAdvisor, and founder of Glenhold Bookkeeping.','/about/','Hi, I’m Jack','Local roots and a direct relationship with your bookkeeper.',body)

def build_pricing():
    body=section('Choose the support you need','<p>Your quote reflects transaction volume, the number of accounts, and reporting complexity. The plans below are starting prices. Cleanup, catch-up, consulting, and training are quoted separately.</p><div class="pricing-guarantee">Love your first month of books, or it’s free</div>'+price_cards())
    body+=section('What changes between plans','<p>Essential keeps your records current. Core adds a regular view of performance through quarterly summaries and year-to-date comparisons. Strategic adds tailored reporting and time each month to walk through the numbers together.</p><p>Before work begins, we’ll agree on the services, software arrangements, timing, and price. Tax return preparation and filing are separate from the bookkeeping plans listed here.</p><p>The first-month guarantee applies to monthly bookkeeping. Discuss the details with Jack when agreeing on your scope.</p>')
    write_inner('Bookkeeping Pricing from $349 per Month | Glenhold','Compare Glenhold monthly bookkeeping plans: Essential from $349, Core from $599, and Strategic from $1,499. Cleanup and training quoted separately.','/pricing/','Straightforward monthly pricing','Choose reliable books, added reporting, or a monthly walkthrough.',body)

def build_contact():
    body=section('Tell me what you need','<p>Share your city, the kind of business you run, whether your books are current, and the help you want. I’ll reply within one business day to discuss the next step.</p><p>You can also call <a href="tel:8054193451">(805) 419-3451</a>, email <a href="mailto:jack@glenhold.com">jack@glenhold.com</a>, or book a free introductory call. Please leave bank logins, account numbers, and financial documents out of the contact form.</p>')
    write_inner('Contact Glenhold Bookkeeping | Simi Valley','Contact Jack at Glenhold Bookkeeping in Simi Valley. Call (805) 419-3451, email jack@glenhold.com, or book a free introductory call.','/contact/','Let’s talk about your books','A short conversation is a good place to start.',body)

def build_privacy():
    body=section('Information you send','<p>The inquiry form asks for your name, email address, optional phone number, the service you are interested in, and a message. Glenhold uses this information to respond to your inquiry and discuss services. Please do not send bank logins, account numbers, tax documents, or other sensitive financial records through this form.</p><p>Form submissions are processed through Formspree. Booking a call takes you to Google’s scheduling service. The website also loads fonts from Google Fonts. These providers process information according to their own policies.</p>')
    body+=section('Website measurement','<p>This website loads Google Ads and OpenAI Ads measurement tags to help measure visits and actions, including inquiry submissions and clicks on booking or telephone links. The website’s form-submission code does not include the name, email address, phone number, or message fields in the conversion events sent to those tags.</p><p>Third-party services may process technical information, such as browser, device, network, or advertising identifiers, under their own policies and applicable settings. This website also stores campaign parameters in browser session storage to help identify the source of an inquiry.</p>')
    body+=section('Questions about your information','<p>Contact <a href="mailto:jack@glenhold.com">jack@glenhold.com</a> with questions about this website’s information handling or requests concerning information you have provided.</p><p>Website forms and advertising measurement are separate from any arrangements for exchanging client bookkeeping records.</p>')
    write_inner('Website Privacy Notice | Glenhold Bookkeeping','How Glenhold’s website uses inquiry information, form processing, booking services, and advertising measurement.','/privacy/','Website privacy notice','Information about inquiries and website measurement.',body,contact=False)

def build_home():
    photo='<picture><source srcset="/headshot.webp" type="image/webp"><img src="/headshot.jpg" width="1000" height="1333" alt="Jack, founder of Glenhold Bookkeeping" decoding="async" fetchpriority="high" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center -10%"></picture>'
    main='<section class="hero"><div class="hero-content"><div class="hero-eyebrow">Simi Valley &amp; surrounding communities</div><h1>Small business bookkeeping.<br><em>Local. Clear. Personal.</em></h1><p class="hero-sub">Your books should be current, and you should be able to read them. I keep them that way for small businesses around Simi Valley, from $349 a month. You work with me. Love your first month, or it’s free.</p><div class="hero-ctas"><a class="btn-primary" href="'+CALENDAR+'" target="_blank" rel="noopener noreferrer">Book a Free Call</a><a class="btn-ghost" href="#contact">Send a Message</a></div><div class="hero-photo-mobile"><img src="/headshot.webp" width="1000" height="1333" alt="Jack, founder of Glenhold Bookkeeping" style="width:75%;height:auto;display:block;border-radius:6px;margin:0 auto"></div><div class="hero-social"><a href="https://share.google/ZFSpIuhD39akrC2DT" target="_blank" rel="noopener noreferrer">Find us on Google</a><a href="https://www.yelp.com/biz/glenhold-bookkeeping-simi-valley" target="_blank" rel="noopener noreferrer">Yelp profile</a></div><p class="hero-proof">Former Big 4 Accountant · Certified QuickBooks ProAdvisor</p></div><div class="hero-photo"><div class="hero-photo-box">'+photo+'</div></div></section>'
    cards=[('/monthly-bookkeeping/','Monthly bookkeeping','Keep transactions organized, accounts reconciled, and reports current.'),('/cleanup-catch-up/','Cleanup & catch-up','Get unfinished periods in order and establish a reliable starting point.'),('/quickbooks-online/','QuickBooks Online help','Set up your file, improve your routine, or get help with specific questions.')]
    main+='<section class="services" id="services"><div class="section-label">How I can help</div><h2 class="section-title">How I can help with your books</h2><p class="section-sub">Hand off the monthly work, catch up on a backlog, or get help doing it yourself.</p>'+hub_cards(cards)+'</section>'
    main+='<section class="pricing" id="pricing"><div class="section-label">Pricing</div><h2 class="section-title">Straightforward monthly plans</h2><p class="section-sub">Your final quote depends on transaction volume, accounts, and reporting complexity.</p><div class="pricing-guarantee">Love your first month of books, or it’s free</div>'+price_cards()+'<div class="content-links"><a href="/pricing/">Compare plans and scope</a></div></section>'
    main+='<section class="local-section" id="service-areas"><div class="section-label">Close to home</div><h2 class="section-title">Based in Simi Valley. Here for local businesses.</h2><p class="section-sub">I offer bookkeeping for businesses in Simi Valley, Moorpark, Thousand Oaks, Westlake Village, Camarillo, Santa Clarita, and surrounding Ventura County and Los Angeles communities.</p><div class="content-links"><a href="/service-areas/">View the service area</a></div></section>'
    main+='<section class="services" id="who"><div class="section-label">Who I work with</div><h2 class="section-title">Small businesses across industries</h2><p class="section-sub">Service firms, shops, trades, practices, and other local businesses are welcome. We’ll build the scope around how your business operates.</p><div class="content-links"><a href="/who-we-work-with/">Explore business types</a></div></section>'
    homefaq=[(i['q'],i['a']) for i in FAQ if i['id'] in ['industries','catch-up','owner','tax-preparer']]
    main+='<section class="faq-section" id="faq"><h2 class="section-title">Before we talk</h2>'+faq_html(homefaq)+'<div class="content-links"><a href="/bookkeeping-faq/">Read all questions</a></div></section>'
    main+='<section class="about" id="about"><div class="about-inner"><div class="about-photo-box">'+portrait('aboutme','Jack fly fishing on the coast')+'</div><div class="about-content"><div class="section-label">Meet your bookkeeper</div><h2 class="section-title">Hi, I’m Jack</h2>'+BIO+'<p><a href="/about/">More about Glenhold</a></p></div></div></section>'
    main+=youtube_section()
    main+=cta('Ready to get your books in order?','Start with a free call to discuss the help you need.')+contact_block('/')
    write_page('Small Business Bookkeeping in Simi Valley | Glenhold','Monthly bookkeeping, catch-up, and QuickBooks Online help for Simi Valley and nearby small businesses. Work directly with Jack. Plans from $349.','/',main,[('Home','/')],[faq_node(homefaq,'/')],CITIES,AREA)

def write_discovery():
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://glenhold.com/sitemap.xml\n')
    urls=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    urls += ['<url><loc>'+HOME+p['path']+'</loc><lastmod>'+LASTMOD+'</lastmod></url>' for p in sorted(PAGES,key=lambda p:p['path'])]
    (ROOT/'sitemap.xml').write_text('\n'.join(urls+['</urlset>'])+'\n')
    facts='# Glenhold Bookkeeping\n\nSimi Valley-based small business bookkeeping. Work directly with Jack, a former Big 4 accountant and Certified QuickBooks ProAdvisor. Glenhold Bookkeeping is the client-facing name of Glenhold Advisory LLC.\n\nPhone: (805) 419-3451\nEmail: jack@glenhold.com\n\nMonthly plans start at $349 (Essential), $599 (Core), and $1,499 (Strategic). Quotes depend on volume, accounts, and reporting complexity. Cleanup and training are quoted separately. Tax return preparation and filing are separate from the listed bookkeeping plans.\n\n## Pages\n'
    short=[p for p in PAGES if p['path'] in ['/','/services/','/pricing/','/contact/','/service-areas/','/bookkeeping-faq/','/privacy/']]
    line=lambda p:'- ['+p['title']+']('+HOME+p['path']+'): '+p['description']+'\n'
    (ROOT/'llms.txt').write_text(facts+''.join(line(p) for p in short))
    (ROOT/'llms-full.txt').write_text(facts+''.join(line(p) for p in PAGES)+'\n## Questions\n'+''.join('### '+i['q']+'\n\n'+i['a']+'\n\n' for i in FAQ))
    (ROOT/(INDEXNOW_KEY+'.txt')).write_text(INDEXNOW_KEY+'\n')
    (ROOT/'.nojekyll').write_text('')

def main():
    PAGES.clear()
    for build in [build_home,build_services,build_industries,build_cities,build_faq,build_resources,build_getting_started,build_about,build_pricing,build_contact,build_privacy]:build()
    write_discovery()
    print('Generated',len(PAGES),'indexable pages and 24 legacy location redirects.')

if __name__=='__main__':main()
