"""The rest of the location pages. Imported by cities.py."""

from bits import checklist, help_table, paras, plans, section, steps

PWC = (
    "I've been in accounting since 2021, including audit work at PwC, "
    "and I'm a Certified QuickBooks ProAdvisor."
)


def S(title, items):
    return steps(title, items)


def C(title, items):
    return checklist(title, items)


MORE_CITIES = [
    dict(
        slug="thousand-oaks",
        name="Thousand Oaks",
        schema_type="City",
        schema_name="Thousand Oaks",
        contained="Ventura County, California",
        title="Bookkeeping in Thousand Oaks, CA | Glenhold",
        description="I keep monthly books for Thousand Oaks practices, restaurants, and Boulevard businesses, including Newbury Park. Plans from $349.",
        h1="Bookkeeping for Thousand Oaks small businesses",
        lede="Thousand Oaks bookkeeping, for me, means a month you can read: categorized transactions, reconciled accounts, and a profit and loss and balance sheet, usually by the 15th. I work with owners on the Boulevard and in Newbury Park. Plans start at $349. You work with me.",
        hub="I close the month for Thousand Oaks practices, restaurants, and Boulevard businesses, and Newbury Park is part of that same city.",
        faqs=[
            ("Is Newbury Park included?", "Yes. Newbury Park is part of the City of Thousand Oaks. Wendy, Borchard, and Dos Vientos are on this page with the rest of the city."),
            ("I have a CPA on the Boulevard. What do you send them?", "Reconciled books, a profit and loss, and a balance sheet. They file the return. I keep the months closed so the year is ready."),
            ("Our restaurant deposits never match the sales report. Can you still close the month?", "That match is the job. I reconcile the point-of-sale report to the deposit, including fees, refunds, and tips."),
            ("What does a straightforward practice pay to start?", "Essential starts at $349 a month. A busier practice, or one that wants a quarterly view, is often Core at $599."),
            ("Can the first month be a trial of the working relationship?", "Love your first month of books, or it's free. That covers monthly bookkeeping."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Thousand Oaks Boulevard, the streets around Civic Arts Plaza, and The Oaks sit among professional offices, clinics, restaurants, and shops. I categorize the month around how each of those businesses actually gets paid. A practice's insurance deposits, a restaurant's card batches, and a consultant's invoices are three different puzzles, and each one can be reconciled.",
                "Newbury Park is the west end of the same city. Wendy, Borchard, and Dos Vientos hold local services, trades, clinics, and shops with a rhythm closer to Camarillo than to the east end of the Boulevard. I cover Newbury Park on this page. If your books are there, you are in the right place.",
            )
            + section(
                "Newbury Park",
                paras(
                    "Owners on Wendy and Borchard often want a simple close: one operating account, a card for supplies, and a processor. Dos Vientos adds home-service crews and small professional offices. I set the chart of accounts for that mix, then I reconcile and send the statements. If the file has been quiet for several months, I quote the catch-up from those months and the accounts, and the monthly plan starts after the open period is finished.",
                ),
                anchor="newbury-park",
            )
            + paras(
                "Across the rest of Thousand Oaks, the first call is the same conversation I have in Simi Valley. How do you get paid, which accounts are yours, and what has to be true by the 15th? I quote before I start. You work with me on every close. " + PWC,
                "Westlake Village is the next city east, and it has its own page, because it is its own city. Agoura Hills, Calabasas, and Malibu are on the Conejo and 101 page. If you work across those lines, say so. I can keep one set of books for the business and still know which town the work sits in.",
            )
            + S(
                "A Thousand Oaks close, step by step",
                [
                    ("Name the location and the accounts", "Boulevard office, Newbury Park shop, or a practice that sees people in both. The accounts matter more than the suite number."),
                    ("Match deposits to the report that explains them", "Processor batches, insurance remits, or invoices. The bank line is the total. The report is the detail."),
                    ("Code the month in your language", "Patient revenue, food, professional fees, rent, payroll transfers, owner draws."),
                    ("Reconcile bank and cards", "Each balance ties out. Leftover items stay on a list until you and I name them."),
                    ("Send the 15th package", "Profit and loss and balance sheet. Core adds the quarterly and year-to-date view. Strategic adds the monthly call."),
                ],
            )
            + C(
                "Useful before I start",
                [
                    "Account list and the last closed month",
                    "Point-of-sale or billing exports if deposits are bundled",
                    "A note about Newbury Park versus the rest of the city, only if you want the books split that way",
                    "Your preparer's deadline",
                ],
            )
            + plans('Starting prices are $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. The plan comparison is on <a href="/pricing/">pricing</a>.')
            + paras('The full monthly routine is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Restaurants on this side of the Conejo can read <a href="/who-we-work-with/restaurants/">restaurants and food businesses</a>, and practices can read <a href="/who-we-work-with/medical-dental/">medical and dental</a>.')
        ),
    ),
    dict(
        slug="westlake-village",
        name="Westlake Village",
        schema_type="City",
        schema_name="Westlake Village",
        contained="Los Angeles County, California",
        title="Bookkeeping in Westlake Village, CA | Glenhold",
        description="I keep the books for Westlake Village owners. The city is in Los Angeles County, and the monthly close is the same careful work. Plans from $349.",
        h1="Bookkeeping for Westlake Village businesses",
        lede="Westlake Village bookkeeping starts with a clear month: I categorize your transactions, reconcile the accounts, and send a profit and loss and a balance sheet, usually by the 15th. The city sits in Los Angeles County, on the edge of Thousand Oaks. Plans start at $349. You work with me.",
        hub="Westlake Village is its own city in Los Angeles County, and I keep monthly books for the owners who work there.",
        faqs=[
            ("Is Westlake Village part of Thousand Oaks for the books?", "It is its own city, in Los Angeles County. I keep a page for it so the records and the conversation match the city you are actually in."),
            ("I run a small professional office here. Which plan fits?", "Essential starts at $349 a month when the accounts are straightforward. Core, at $599, adds a quarterly summary and a year-to-date comparison."),
            ("Can you work with the CPA I already have?", "Yes. I hand your CPA clean, reconciled books. They file the return."),
            ("What if QuickBooks Online is only half set up?", "Then setup is the first project. I build the chart of accounts and train you on the parts you want to keep."),
            ("When do the reports arrive?", "I aim for the 15th of the next month, once statements and your answers are in."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Westlake Village is a city of its own, in Los Angeles County, even though daily life runs straight into Thousand Oaks. I treat it that way in the books. Your address, your sales-tax district, and the way you describe the business all stay with Westlake Village. The monthly work is still the work: categorize, reconcile, and send statements you can read.",
                "The businesses I hear from here are often professional offices, consultancies, medical practices, and owner-run firms with a small staff. The transactions are rents, professional income, payroll transfers from a payroll company, owner draws, and a card that mixes software with the occasional personal charge. Naming those cleanly is what makes the profit and loss trustworthy.",
                "On the first call, tell me whether the books are current. A current file becomes a monthly plan. An open stretch of months becomes a catch-up quote, priced from the records, and the monthly plan starts when that stretch is finished. I live in Simi Valley and I am glad to meet in the Conejo when a walkthrough on paper helps. Most questions are handled when I send the reports.",
                PWC + " I bring that care to Westlake Village owners who want one person on the close.",
                "California sales tax, when you collect it, sits on the balance sheet as a liability. The statewide base rate is 7.25 percent, and the district rate for your Westlake Village location can be higher. I look it up. Your preparer files the return. The same split holds for the LLC's $800 franchise tax: I keep the books, and your CPA files the form.",
            )
            + S(
                "What the monthly work looks like here",
                [
                    ("Confirm the city and the accounts", "Westlake Village, Los Angeles County. Checking, savings, cards, and any processor."),
                    ("Separate payroll and owner activity", "Your payroll company runs payroll. I record the journal entries on the Strategic plan, and I label draws and contributions on every plan."),
                    ("Categorize the operating month", "Fees, rent, software, insurance, and the costs that belong to the work."),
                    ("Reconcile", "Bank and cards tie to QuickBooks Online."),
                    ("Deliver the reports", "Profit and loss and balance sheet by the 15th, with the extra views your plan includes."),
                ],
            )
            + C(
                "A short list before the first close",
                [
                    "The QuickBooks Online file, if you have one",
                    "Statements or bank feeds for the months in scope",
                    "Payroll reports, if staff are paid through a payroll company",
                    "The question you most want the profit and loss to answer",
                ],
            )
            + plans('Plans start at $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. Compare them on <a href="/pricing/">pricing</a>.')
            + paras('See <a href="/monthly-bookkeeping/">monthly bookkeeping</a>, <a href="/who-we-work-with/professional-services/">professional services</a>, and the neighboring <a href="/service-areas/thousand-oaks/">Thousand Oaks</a> page if your week spans both cities.')
        ),
    ),
    dict(
        slug="camarillo",
        name="Camarillo",
        schema_type="City",
        schema_name="Camarillo",
        contained="Ventura County, California",
        title="Bookkeeping in Camarillo, CA | Glenhold",
        description="I keep monthly books for Camarillo owners in Old Town, at the outlets, and around the airport. Plans from $349. You work with me.",
        h1="Bookkeeping for Camarillo small businesses",
        lede="Camarillo bookkeeping from me is a closed month you can read. I categorize the transactions, reconcile your bank and credit cards, and send a profit and loss and a balance sheet, usually by the 15th. Old Town, the outlets, and the airport corridor are all in range. Plans start at $349.",
        hub="Old Town, the outlets, and the businesses around the airport get a monthly close and reports they can hand to a CPA.",
        faqs=[
            ("I run a shop in Old Town and the deposits come from a square reader and a few invoices. Can you reconcile both?", "Yes. The reader report and the invoices sit next to the bank deposit. I want those three to agree."),
            ("Does a seasonal outlet shop still need a monthly close?", "Yes, including the quiet months. A short month is still a month, and the year is easier when every month is closed."),
            ("How do you price a backlog?", "From the months and the accounts you have. I quote that work before I start, separate from the monthly plan."),
            ("Can I stay on Essential if I only have one account?", "Essential starts at $349 a month and is built for straightforward books. I confirm the price from your volume."),
            ("Who do I call with a question?", "You call me. The close and the follow-up are with the same person."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Camarillo's work shows up in a few different places: Old Town along Ventura Boulevard, the outlet shops, the airport, and the agricultural businesses on the flats around the city. I keep books for all of them. The categories change with the business. The monthly promise stays the same.",
                "An Old Town retailer needs the card batches explained. A shop at the outlets may have a sharp seasonal swing, and the quiet months still get a close so December is a month and February is a month. A business near the airport may have fuel, hangar or shop rent, and a handful of large invoices. An ag-adjacent owner may have seasonal receipts and equipment payments. I ask which of those is you, then I build the chart of accounts around the answer.",
                "Tell me on the first call if the books are current. Current books go on a monthly plan. Open months are a catch-up, quoted from the records, and the plan starts when that stretch is done. I aim for reports on the 15th. You work with me. " + PWC,
                "Sales tax you collect is a liability in the books, money on its way to the CDTFA. The statewide base rate is 7.25 percent. Camarillo's district rate can be higher, and I look up the one that applies to you. Your preparer files the return.",
            )
            + S(
                "How a Camarillo month moves",
                [
                    ("Place the business", "Old Town, the outlets, the airport, or the fields at the edge of town. The address tells me which sales-tax district to check."),
                    ("Explain the deposit", "Reader report, outlet batches, or invoices. I reconcile that detail to the bank."),
                    ("Name equipment and owner activity", "Loan payments, vehicle costs, draws, and money you put back in."),
                    ("Categorize and reconcile", "The month gets coded, then the bank and the cards tie out."),
                    ("Send the package", "Profit and loss and balance sheet, aimed at the 15th, plus the extra reporting on Core and Strategic."),
                ],
            )
            + C(
                "What I ask Camarillo owners to gather",
                [
                    "Operating accounts and cards",
                    "The last month you trust",
                    "Processor or invoice detail behind the deposits",
                    "Equipment loans, if you want them on the balance sheet",
                    "Any date a lender or CPA has already set",
                ],
            )
            + plans('Essential is $349 a month to start, Core is $599, and Strategic is $1,499. Love your first month of books, or it\'s free. See <a href="/pricing/">pricing</a> for what changes between them.')
            + paras('Start with <a href="/monthly-bookkeeping/">monthly bookkeeping</a> or <a href="/cleanup-catch-up/">cleanup and catch-up</a>. Shops with a counter can also read <a href="/who-we-work-with/restaurants/">restaurants and food businesses</a> if that is the closer fit, and trades can read <a href="/who-we-work-with/contractors/">contractors</a>.')
        ),
    ),
    dict(
        slug="santa-clarita",
        name="Santa Clarita",
        schema_type="City",
        schema_name="Santa Clarita",
        contained="Los Angeles County, California",
        title="Bookkeeping in Santa Clarita, CA | Glenhold",
        description="I keep books for Santa Clarita owners in Valencia, Newhall, Saugus, and Canyon Country. One city, one monthly close. Plans from $349.",
        h1="Bookkeeping for Santa Clarita small businesses",
        lede="Santa Clarita bookkeeping covers the whole city: Valencia, Newhall, Saugus, and Canyon Country. I categorize the month, reconcile your accounts, and send a profit and loss and a balance sheet, usually by the 15th. Plans start at $349. You work with me.",
        hub="Valencia, Newhall, Saugus, and Canyon Country are one city, and I close the month for owners across all four.",
        faqs=[
            ("I say I am in Valencia. Do I use this page?", "Yes. Valencia, Newhall, Saugus, and Canyon Country are neighborhoods of Santa Clarita. One page covers the city."),
            ("My books are in a spreadsheet. Can you move them?", "Yes. QuickBooks Online setup is the path. I build the file from the months you care about and train you on the work you want to keep."),
            ("What does catch-up cost?", "I price it from the open months and the accounts. It is separate from the monthly plans."),
            ("Will the reports be ready for my CPA?", "I hand your CPA clean, reconciled books. They file the return."),
            ("How fast is the monthly turnaround?", "I aim for the 15th of the next month. Missing statements move that date, and I tell you which ones."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Santa Clarita is one city with four names people still use. Valencia, Newhall, Saugus, and Canyon Country show up in addresses, and the books can say Santa Clarita while you keep calling the neighborhood what you have always called it. I work with owners across that whole city from Simi Valley.",
                "The mix I see is trades, medical and dental offices, restaurants, professional firms, and online sellers who happen to live and warehouse here. A Newhall shop, a Valencia practice, and a Canyon Country contractor each need categories that match their deposits. I ask about the deposits first. The chart of accounts follows.",
                "If the file is current, the next step is a monthly close. If several months are open, I quote the catch-up from those months and start the plan when they are finished. Reports are aimed at the 15th. You are working with me. "
                + PWC,
                "Bring the account list and the question you want answered. Some owners want to know if payroll is the whole margin. Some want a lender package. Some want the year to be quiet for their CPA. I can aim the close at that question. Strategic includes a monthly call for the walkthrough. Essential and Core send the reports in writing, and you can always write back.",
                "Santa Clarita owners often work across more than one neighborhood in a week. The books can still be one company. Tell me if a Valencia office and a Canyon Country yard share accounts, and I will keep one close that shows both.",
            )
            + S(
                "Closing a Santa Clarita month",
                [
                    ("Use the neighborhood name you use", "Valencia, Newhall, Saugus, or Canyon Country. I still set the books up as your Santa Clarita business."),
                    ("List every account that touches the work", "Including the card in the truck and the savings account that holds sales tax."),
                    ("Match the way you get paid", "Insurance remits, card batches, progress invoices, or Shopify payouts."),
                    ("Categorize and reconcile", "I code the month and tie the balances."),
                    ("Send what you asked the close to show", "Profit and loss, balance sheet, and the comparison your plan includes."),
                ],
            )
            + C(
                "Have this nearby",
                [
                    "Last closed month, even if it was last year",
                    "Bank and card statements or QuickBooks feeds",
                    "Payroll reports from your payroll company, when you have staff",
                    "The lender's list, if a loan is the reason for the call",
                ],
            )
            + plans('Plans start at $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. <a href="/pricing/">Pricing</a> spells out the differences.')
            + paras('Read <a href="/monthly-bookkeeping/">monthly bookkeeping</a>, <a href="/loan-ready-books/">loan-ready financials</a> if a lender is waiting, and <a href="/who-we-work-with/medical-dental/">medical and dental</a> if you run a practice in the valley.')
        ),
    ),
    dict(
        slug="ventura",
        name="Ventura",
        schema_type="City",
        schema_name="Ventura",
        contained="Ventura County, California",
        title="Bookkeeping in Ventura, CA | Glenhold",
        description="I keep books for Ventura owners along Main Street and the harbor. The city's official name is San Buenaventura. Plans from $349.",
        h1="Bookkeeping for Ventura small businesses",
        lede="Ventura bookkeeping for the city people also call San Buenaventura. I categorize the month, reconcile your accounts, and send a profit and loss and a balance sheet, usually by the 15th. Main Street and the harbor are both welcome. Plans start at $349. You work with me.",
        hub="Main Street and the harbor are full of owner-run businesses, and I close the month for them from Simi Valley.",
        faqs=[
            ("Do you use the name Ventura or San Buenaventura?", "Both are the same city. I say Ventura because that is how owners introduce themselves, and the official name is San Buenaventura."),
            ("I sell on Main Street and online. Can one set of books hold both?", "Yes. I separate the sales channels in the categories so you can see the shop and the online orders."),
            ("What if the summer is busy and the winter is quiet?", "Every month still closes. The quiet month is often when the reports are easiest to read."),
            ("Can you prepare what my CPA needs?", "I hand your CPA clean, reconciled books. They file the return."),
            ("Where do the coastal towns fit?", "Port Hueneme, Santa Paula, Fillmore, and Ojai are on the Ventura County coast page. Ventura itself stays here."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Ventura is the county seat, officially San Buenaventura. On Main Street and around the harbor I hear from shops, restaurants, professional offices, and owner-run firms that live with a seasonal year. I keep their books from Simi Valley. The close is monthly, so a busy August and a quiet January both end with a profit and loss you can compare.",
                "Harbor businesses and Main Street businesses collect money differently enough that the categories should say so. A restaurant batch includes food, drink, tips, and fees. A gallery or a shop may have daily card sales and a few invoices. A harbor-side service may have deposits that sit until a job is done. I ask which pattern is yours and I reconcile the report that explains the deposit.",
                "The first call covers accounts, open months, and any deadline. I quote catch-up from the records and monthly work from the three plans. Reports are aimed at the 15th. You work with me on the close. " + PWC,
                "A harbor month and a Main Street month can share a file when they are the same company. I keep the sales channels visible so you can see which part of Ventura carried the month. Tell me if one location should stay visible on its own line.",
                "Other coast and Highway 126 towns, including Port Hueneme, Santa Paula, Fillmore, and Ojai, are gathered on one regional page. Oxnard, the largest city in the county, has its own page. If you work in Ventura and live in one of those towns, tell me. The books follow the business.",
            )
            + S(
                "A Ventura month with me",
                [
                    ("Say where the work happens", "Main Street, the harbor, or a shop that does both. Seasonal swings belong in the story you tell me."),
                    ("Separate channels", "In-person sales, online orders, and deposits held until a job finishes."),
                    ("Code costs the way you feel them", "Food, rent, harbor or shop costs, payroll transfers, and owner draws."),
                    ("Reconcile the balances", "Bank and cards, with the processor report beside any bundled deposit."),
                    ("Send the 15th reports", "Profit and loss and balance sheet, plus the Core or Strategic extras on those plans."),
                ],
            )
            + C(
                "Helpful for a Ventura close",
                [
                    "Account list and last closed month",
                    "Point-of-sale exports for restaurant or shop deposits",
                    "A note on seasonal months you already expect to look different",
                    "Your CPA's timing",
                ],
            )
            + plans('Starting prices are $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. <a href="/pricing/">Pricing</a> has the comparison.')
            + paras('The monthly path is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Food businesses can read <a href="/who-we-work-with/restaurants/">restaurants</a>. The rest of the coast is on <a href="/service-areas/ventura-county-coast/">Ventura County coast</a>.')
        ),
    ),
    dict(
        slug="oxnard",
        name="Oxnard",
        schema_type="City",
        schema_name="Oxnard",
        contained="Ventura County, California",
        title="Bookkeeping in Oxnard, CA | Glenhold",
        description="I keep monthly books for Oxnard, the largest city in Ventura County, from Oxnard Boulevard to the harbor and the agricultural plain. Plans from $349.",
        h1="Bookkeeping for Oxnard small businesses",
        lede="Oxnard bookkeeping for the largest city in Ventura County. I categorize the month, reconcile your bank and cards, and send a profit and loss and a balance sheet, usually by the 15th. Oxnard Boulevard, the harbor, and the agricultural plain are all part of the work. Plans start at $349.",
        hub="Oxnard is the largest city in Ventura County, and I close the month for owners on the Boulevard, at the harbor, and on the agricultural plain.",
        faqs=[
            ("I farm and I also sell at a stand. Can both live in one file?", "Yes. I split crop or wholesale receipts from stand sales so you can see each one, and the balance sheet still shows one business."),
            ("The harbor shop's deposits include tips. How do you treat them?", "Tips, fees, and sales each get a line. The deposit in the bank is the sum, and the report explains the sum."),
            ("Do you work with Oxnard businesses?", "Yes. I keep the books from Simi Valley, and you work with me directly."),
            ("What do you need for a loan conversation?", "The reports the lender asked for, built from reconciled months. Start with the loan-ready page if that is the deadline."),
            ("When are the monthly reports ready?", "I aim for the 15th of the next month. I tell you if a statement is still missing."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Oxnard is the largest city in Ventura County, and the books I keep here have to cover more than one kind of main street. Oxnard Boulevard has shops and services. The harbor has restaurants and visitor businesses. The plain around the city has agriculture, packing, and the owners who sell what they grow. I ask which of those is the center of your month, then I categorize around it.",
                "A Boulevard service business may be straightforward: invoices, a card for parts, and payroll through a payroll company. A harbor restaurant needs the point-of-sale report beside every batch. An agricultural owner may have seasonal receipts, equipment loans, and a stand or a wholesale account that should stay visible on the profit and loss. Those are different charts of accounts. They get the same monthly reconcile.",
                "Tell me how far behind the file is. I quote catch-up from the months and the accounts, then the monthly plan carries the business forward. Reports are aimed at the 15th. You work with me. " + PWC + " That is the care I bring to Oxnard.",
                "Port Hueneme is its own city next door, with the port and the naval base, and it lives on the coast page. I am glad to keep books for an Oxnard business that also works there. The books follow your company.",
            )
            + S(
                "How I close an Oxnard month",
                [
                    ("Name the center of the business", "Boulevard service, harbor food, agriculture, or a mix. The categories follow that answer."),
                    ("Put seasonal income on its own lines", "So a harvest month and a harbor summer can be read on purpose."),
                    ("Track equipment and loans", "Payments split between interest and principal when you want the balance sheet to show the debt."),
                    ("Reconcile bank, cards, and batches", "Including processor fees and tips when the deposit is a bundle."),
                    ("Send the reports", "Profit and loss and balance sheet by the 15th, with Core and Strategic extras on those plans."),
                ],
            )
            + C(
                "What makes an Oxnard close easier",
                [
                    "Every account, including the one that holds tax you have collected",
                    "Crop, wholesale, or stand reports if you sell in more than one way",
                    "Point-of-sale exports for a food business",
                    "Loan statements if you want balances tracked",
                    "The deadline, if a CPA or a lender set one",
                ],
            )
            + plans('Plans start at $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. Read the differences on <a href="/pricing/">pricing</a>.')
            + paras('See <a href="/monthly-bookkeeping/">monthly bookkeeping</a>, <a href="/who-we-work-with/restaurants/">restaurants</a> for harbor food businesses, and <a href="/service-areas/ventura/">Ventura</a> if that city is part of your week too.')
        ),
    ),
]
