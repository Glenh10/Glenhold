"""Regional pages, hub lines, and redirects for retired city slugs."""

from bits import checklist, paras, plans, section

PWC = (
    "I've been in accounting since 2021, including audit work at PwC, "
    "and I'm a Certified QuickBooks ProAdvisor."
)


def town(anchor, title, text):
    return section(title, f"<p>{text}</p>", anchor=anchor)


REGIONS = [
    dict(
        slug="conejo-and-101",
        name="Conejo and the 101",
        schema_type="Place",
        schema_name="Conejo Valley",
        contained="Ventura County and Los Angeles County, California",
        title="Bookkeeping in the Conejo Valley and along the 101 | Glenhold",
        description="I keep books for Agoura Hills, Calabasas, Malibu, and Oak Park, and I link Thousand Oaks, Newbury Park, and Westlake Village to their own pages. Plans from $349.",
        h1="Bookkeeping along the Conejo and the 101",
        lede="I keep the books for owners in Agoura Hills, Calabasas, Malibu, and Oak Park, and for the Thousand Oaks and Westlake Village businesses that sit on either side of them. The work is a monthly close: categorized transactions, reconciled accounts, and a profit and loss and balance sheet, usually by the 15th.",
        hub="Agoura Hills, Calabasas, Malibu, and Oak Park are welcome here, with Thousand Oaks and Westlake Village on their own pages beside them.",
        faqs=[
            ("Where does Newbury Park fit?", "Newbury Park is part of Thousand Oaks. I cover it on the Thousand Oaks page, including Wendy, Borchard, and Dos Vientos."),
            ("Is Malibu a client you will take?", "Yes. If your business is in Malibu, I am glad to keep the books. Tell me how you get paid and which accounts you use."),
            ("I work in Agoura and live in Oak Park. Which page is mine?", "Use this page. Oak Park is part of the same conversation, and the books follow the business."),
            ("What do the monthly plans cost?", "Essential starts at $349, Core at $599, and Strategic at $1,499. Love your first month of books, or it's free."),
            ("Who does the work?", "You work with me. I live in Simi Valley, and I answer the questions on your close."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "This page is for the communities between Thousand Oaks and the west San Fernando Valley: Agoura Hills, Calabasas, Malibu, and Oak Park. Thousand Oaks, including Newbury Park, and Westlake Village are full pages of their own because the work there is steady enough to deserve a closer description. If you are in those cities, start there. If you are in the towns below, stay here.",
                "The monthly work is the same care I bring to Simi Valley. " + PWC + " I categorize the month around how you get paid, reconcile the bank and the cards, and send reports aimed at the 15th. You work with me.",
            )
            + town(
                "agoura-hills",
                "Agoura Hills",
                "Agoura Hills businesses cluster around Kanan Road and Reyes Adobe Road: professional offices, medical practices, and owner-run shops. I want the deposit and the report behind it, whether that is a card batch or an invoice. Owner draws and the card that mixes personal spending get their own lines, so the profit and loss matches the practice or the shop you actually run. A current file becomes a monthly plan. Open months become a catch-up quote first.",
            )
            + town(
                "calabasas",
                "Calabasas",
                "Calabasas Road, The Commons, and the offices toward Malibu Canyon are full of professional firms, studios-of-one, and local services. The books I keep here often turn on a few large payments, rent, payroll through a payroll company, and a card for software and supplies. I label those so a quiet month and a busy month can be compared. Strategic adds a monthly call if you want to walk the numbers. Essential and Core send the reports in writing.",
            )
            + town(
                "malibu",
                "Malibu",
                "Malibu owners call about shops, design practices, and property-related businesses along the coast and up the canyon. I ask how money arrives and which accounts it lands in. Card batches, retainers, and deposits held until a job is finished each get a treatment that matches the timing. Sales tax you collect sits as a liability. The statewide base rate is 7.25 percent, and the district rate for your Malibu location can be higher. I look it up. Your preparer files the return.",
            )
            + town(
                "oak-park",
                "Oak Park",
                "Oak Park is an unincorporated community beside Thousand Oaks and Agoura Hills. I am glad to keep books for owners there: home-service crews, professional offices, and shops that serve the neighborhood. Tell me the accounts and the last month you trust. I will quote the open stretch if there is one, and the monthly close after that.",
            )
            + paras(
                'Thousand Oaks and Newbury Park are on the <a href="/service-areas/thousand-oaks/">Thousand Oaks page</a>. Westlake Village, a city in Los Angeles County, is on the <a href="/service-areas/westlake-village/">Westlake Village page</a>. If your week crosses those lines, say so on the first call and I will keep one set of books for the company.',
            )
            + checklist(
                "What I need from a Conejo business",
                [
                    "The town you work in, and the accounts in the business name",
                    "The last closed month",
                    "Processor or invoice detail when deposits are bundled",
                    "A CPA or lender date, if one is already on the calendar",
                ],
            )
            + plans('Plans start at $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. The comparison is on <a href="/pricing/">pricing</a>.')
            + paras('The routine itself is written up under <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Practices often start from <a href="/who-we-work-with/medical-dental/">medical and dental</a> or <a href="/who-we-work-with/professional-services/">professional services</a>.')
        ),
    ),
    dict(
        slug="ventura-county-coast",
        name="Ventura County coast",
        schema_type="Place",
        schema_name="Ventura County coast",
        contained="Ventura County, California",
        title="Bookkeeping on the Ventura County coast and the 126 | Glenhold",
        description="I keep books for Port Hueneme, Santa Paula, Fillmore, Ojai, and nearby coast and Highway 126 towns. Ventura and Oxnard have their own pages. Plans from $349.",
        h1="Bookkeeping on the Ventura County coast and Highway 126",
        lede="I keep the books for owners in Port Hueneme, Santa Paula, Fillmore, and Ojai, and I am glad to talk with other towns along the coast and Highway 126. Ventura and Oxnard have their own pages. The close is monthly: categories, reconciled accounts, and reports, usually by the 15th.",
        hub="Port Hueneme, Santa Paula, Fillmore, and Ojai are on this page, with a welcome for the other coast and Highway 126 towns around them.",
        faqs=[
            ("Do Ventura and Oxnard use this page?", "They have their own pages. This page is for Port Hueneme, Santa Paula, Fillmore, Ojai, and the smaller towns nearby."),
            ("I am in Piru or Somis. Can I call?", "Yes. If your business is on the coast or along the 126, I am glad to hear how you get paid and what you want the reports to show."),
            ("Ojai is seasonal. Do quiet months still close?", "Yes. A quiet month is part of the year, and the comparison is clearer when it is closed too."),
            ("How are plans priced?", "Essential starts at $349 a month, Core at $599, and Strategic at $1,499. Catch-up is quoted from the open months."),
            ("Can my CPA keep filing the return?", "Yes. I hand your CPA clean, reconciled books. They file the return."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Ventura and Oxnard are large enough, and different enough, to have their own pages. This page is for the towns around them: the harbor city of Port Hueneme, the Highway 126 cities of Santa Paula and Fillmore, Ojai up the 33, and the smaller places in between. I live in Simi Valley. The books happen in QuickBooks Online, and you work with me.",
                PWC + " I categorize the month, reconcile the accounts, and send a profit and loss and a balance sheet aimed at the 15th.",
            )
            + town(
                "port-hueneme",
                "Port Hueneme",
                "Port Hueneme is its own city, with the port and Naval Base Ventura County beside it. I keep books for the city's shops, trades, and harbor-side businesses. Tell me how you get paid and which accounts are the company's. If your work touches the base, bring the invoices and the accounts you already use. I record the activity that runs through your books.",
            )
            + town(
                "santa-paula",
                "Santa Paula",
                "Santa Paula sits on Highway 126, with Main Street, a citrus history, and owner-run shops and crews that serve the valley. I set categories for a mix of counter sales, invoices, and seasonal receipts. Equipment payments and owner draws get named so the profit is visible. A backlog is quoted from the months you still have open.",
            )
            + town(
                "fillmore",
                "Fillmore",
                "Fillmore is the next city east on the 126. The businesses are local services, trades, and shops that know their customers by name. A monthly close here is often a short account list and a clear question: what did the month earn after fuel, materials, and the owner's draw? I answer that with a profit and loss and a balance sheet.",
            )
            + town(
                "ojai",
                "Ojai",
                "Ojai is reached on Highway 33, with the Arcade, Libbey Park, and a year that swells in certain seasons. Shops, inns, and studios all feel that calendar. I close every month, including the quiet ones, so the seasonal months can be read against a real baseline. Card batches and appointment deposits get reconciled to the report that explains them.",
            )
            + section(
                "Other coast and 126 towns",
                paras(
                    "Somis, Piru, Oak View, Meiners Oaks, and the other small communities along the coast and Highway 126 are welcome. Tell me the town, the accounts, and whether the books are current. I will quote the work and keep the same monthly rhythm.",
                ),
            )
            + paras(
                'Ventura, the county seat, is on the <a href="/service-areas/ventura/">Ventura page</a>. Oxnard, the largest city in the county, is on the <a href="/service-areas/oxnard/">Oxnard page</a>.',
            )
            + checklist(
                "What helps the first close",
                [
                    "Town, accounts, and the last finished month",
                    "Seasonal notes, if some months are expected to look different",
                    "Processor reports when a deposit bundles sales, fees, and refunds",
                    "Your CPA's deadline",
                ],
            )
            + plans('Plans start at $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. See <a href="/pricing/">pricing</a>.')
            + paras('Read <a href="/monthly-bookkeeping/">monthly bookkeeping</a> for the routine, and <a href="/who-we-work-with/home-services/">home services</a> if that is the work.')
        ),
    ),
    dict(
        slug="san-fernando-valley",
        name="San Fernando Valley",
        schema_type="Place",
        schema_name="San Fernando Valley",
        contained="Los Angeles County, California",
        title="Bookkeeping in the San Fernando Valley | Glenhold",
        description="I keep books for Chatsworth, Porter Ranch, Northridge, the Valley cities east to Burbank and Glendale, and the neighborhoods along Ventura Boulevard. Plans from $349.",
        h1="Bookkeeping for San Fernando Valley small businesses",
        lede="I keep the books for small businesses across the San Fernando Valley, from Chatsworth and Porter Ranch through the Boulevard neighborhoods to Burbank and Glendale. I categorize the month, reconcile your accounts, and send a profit and loss and a balance sheet, usually by the 15th. Plans start at $349. You work with me.",
        hub="From Chatsworth to Glendale, including the Ventura Boulevard neighborhoods, I close the month for Valley owners who want a person they can reach.",
        faqs=[
            ("Do you cover the whole Valley?", "Yes. Chatsworth through Glendale, including the neighborhoods along Ventura Boulevard, are on this page."),
            ("I am in Winnetka or Tarzana. Is that included?", "Yes. Both are part of this Valley work. Tell me the accounts and how you get paid."),
            ("Which plan should a small shop start with?", "Essential starts at $349 a month for straightforward books. Core adds a quarterly view. Strategic adds custom reports and a monthly call."),
            ("Can you catch up a file that stopped last year?", "Yes. I quote the open months from the records you have, then a monthly plan can carry the business forward."),
            ("Who files the tax return?", "Your CPA files the return. I hand them clean, reconciled books."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "The San Fernando Valley is a long list of neighborhoods, and owners still use those names. I keep one page for them so you can find your town and see that the close is personal. I live in Simi Valley, just through the pass from Chatsworth. " + PWC + " You work with me on the month.",
                "Winnetka and Tarzana belong in this same welcome. So does every neighborhood below. The first call is how you get paid, which accounts you use, and which months are open. Monthly plans start at $349. Catch-up is quoted on its own.",
            )
            + town("chatsworth", "Chatsworth", "Chatsworth, along Plummer, Mason, and De Soto, is the neighborhood closest to Simi Valley. Trades, warehouses, and owner-run shops are common. I categorize job costs, fuel, and materials, then reconcile the accounts you actually spend from.")
            + town("porter-ranch", "Porter Ranch", "Porter Ranch Town Center and the offices around it mix medical practices, services, and family businesses. Insurance deposits and card batches get matched to the report behind them, and owner draws stay visible.")
            + town("northridge", "Northridge", "Northridge, around CSUN and the Reseda, Nordhoff, and Devonshire corridors, has shops and professional offices. I close the month from the processor report and the bank, including the weeks when the campus calendar changes how busy the door is.")
            + town("granada-hills", "Granada Hills", "Granada Hills, along Balboa and Chatsworth Street, is home to practices, shops, and service firms. A straightforward account list often fits Essential. A practice that wants a quarterly view fits Core.")
            + town("canoga-park", "Canoga Park", "Canoga Park runs along Sherman Way and Topanga. Shops and trades share the month with me when they want the deposit explained and the cards reconciled.")
            + town("reseda", "Reseda", "Reseda Boulevard is a working street of services, shops, and small professional offices. I set the categories in the language you use at the counter, then I send the profit and loss and the balance sheet.")
            + town("woodland-hills", "Woodland Hills", "Woodland Hills covers Warner Center and Ventura Boulevard: larger offices, medical practices, and professional firms. Payroll stays with your payroll company. On Strategic I record the payroll journal entries. On every plan I label owner activity.")
            + town("encino", "Encino", "Encino along Ventura Boulevard is full of professional firms and medical offices. Retainers, insurance deposits, and rent are the usual puzzle. I reconcile them and send reports your CPA can use.")
            + town("tarzana", "Tarzana", "Tarzana sits on the Boulevard between Woodland Hills and Encino. I am glad to keep books for the practices, shops, and firms there. Bring the account list and the last month you trust.")
            + town("winnetka", "Winnetka", "Winnetka is a neighborhood of shops, trades, and home-service businesses. The close is the same personal one: categories that match the work, reconciled balances, and a report by the 15th.")
            + town("van-nuys", "Van Nuys", "Van Nuys Boulevard, the civic center, and the airport area hold a wide mix of owner-run firms. Tell me which accounts are the business. I will quote the open months and start the rhythm from there.")
            + town("sherman-oaks", "Sherman Oaks", "Sherman Oaks, along Ventura Boulevard and near Fashion Square, mixes professional services and shops. Card batches and invoices can live in one file if the categories keep them apart.")
            + town("studio-city", "Studio City", "Studio City along Ventura Boulevard has creative firms and professional offices. I record the month you had, including project deposits that belong to a later month, so the profit and loss stays honest.")
            + town("north-hollywood", "North Hollywood", "North Hollywood, around Lankershim and Magnolia and the Metro B and G lines, has shops, services, and firms that serve the neighborhood. I reconcile the accounts and send a month you can read.")
            + town("burbank", "Burbank", "Burbank's downtown, Magnolia Park, and the area around Hollywood Burbank Airport are full of owner-run businesses. I keep their company books: sales, rent, payroll through your payroll company, and the monthly reports. Bring the accounts you use.")
            + town("glendale", "Glendale", "Glendale, along Brand Boulevard, the Galleria, and the Americana, has professional offices, medical practices, and shops. I close the month and send the profit and loss and balance sheet, aimed at the 15th.")
            + checklist(
                "Before the first Valley close",
                [
                    "Your neighborhood and the accounts",
                    "The last closed month",
                    "Reports behind any bundled deposit",
                    "A lender or CPA date, if you have one",
                ],
            )
            + plans('Essential starts at $349 a month, Core at $599, and Strategic at $1,499. Love your first month of books, or it\'s free. <a href="/pricing/">Pricing</a> compares them.')
            + paras('The monthly routine is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Many Valley calls also fit <a href="/who-we-work-with/professional-services/">professional services</a> or <a href="/who-we-work-with/medical-dental/">medical and dental</a>.')
        ),
    ),
]


# slug, visible name, destination path (with optional hash), canonical path
REDIRECTS = [
    ("newbury-park", "Newbury Park", "/service-areas/thousand-oaks/#newbury-park", "/service-areas/thousand-oaks/"),
    ("agoura-hills", "Agoura Hills", "/service-areas/conejo-and-101/#agoura-hills", "/service-areas/conejo-and-101/"),
    ("calabasas", "Calabasas", "/service-areas/conejo-and-101/#calabasas", "/service-areas/conejo-and-101/"),
    ("malibu", "Malibu", "/service-areas/conejo-and-101/#malibu", "/service-areas/conejo-and-101/"),
    ("port-hueneme", "Port Hueneme", "/service-areas/ventura-county-coast/#port-hueneme", "/service-areas/ventura-county-coast/"),
    ("santa-paula", "Santa Paula", "/service-areas/ventura-county-coast/#santa-paula", "/service-areas/ventura-county-coast/"),
    ("fillmore", "Fillmore", "/service-areas/ventura-county-coast/#fillmore", "/service-areas/ventura-county-coast/"),
    ("ojai", "Ojai", "/service-areas/ventura-county-coast/#ojai", "/service-areas/ventura-county-coast/"),
    ("chatsworth", "Chatsworth", "/service-areas/san-fernando-valley/#chatsworth", "/service-areas/san-fernando-valley/"),
    ("porter-ranch", "Porter Ranch", "/service-areas/san-fernando-valley/#porter-ranch", "/service-areas/san-fernando-valley/"),
    ("northridge", "Northridge", "/service-areas/san-fernando-valley/#northridge", "/service-areas/san-fernando-valley/"),
    ("granada-hills", "Granada Hills", "/service-areas/san-fernando-valley/#granada-hills", "/service-areas/san-fernando-valley/"),
    ("woodland-hills", "Woodland Hills", "/service-areas/san-fernando-valley/#woodland-hills", "/service-areas/san-fernando-valley/"),
    ("canoga-park", "Canoga Park", "/service-areas/san-fernando-valley/#canoga-park", "/service-areas/san-fernando-valley/"),
    ("reseda", "Reseda", "/service-areas/san-fernando-valley/#reseda", "/service-areas/san-fernando-valley/"),
    ("encino", "Encino", "/service-areas/san-fernando-valley/#encino", "/service-areas/san-fernando-valley/"),
    ("van-nuys", "Van Nuys", "/service-areas/san-fernando-valley/#van-nuys", "/service-areas/san-fernando-valley/"),
    ("sherman-oaks", "Sherman Oaks", "/service-areas/san-fernando-valley/#sherman-oaks", "/service-areas/san-fernando-valley/"),
    ("studio-city", "Studio City", "/service-areas/san-fernando-valley/#studio-city", "/service-areas/san-fernando-valley/"),
    ("north-hollywood", "North Hollywood", "/service-areas/san-fernando-valley/#north-hollywood", "/service-areas/san-fernando-valley/"),
    ("burbank", "Burbank", "/service-areas/san-fernando-valley/#burbank", "/service-areas/san-fernando-valley/"),
    ("glendale", "Glendale", "/service-areas/san-fernando-valley/#glendale", "/service-areas/san-fernando-valley/"),
]

INDUSTRY_REDIRECTS = [
    ("real-estate", "real estate"),
    ("nonprofits", "nonprofits"),
    ("retail", "retail shops"),
    ("salons", "salons"),
    ("fitness", "fitness studios"),
    ("auto-repair", "auto repair shops"),
    ("restaurants", "local businesses"),
]


def _hub(name, href, line):
    return (name, href, line)


HUB = [
    _hub("Simi Valley", "/service-areas/simi-valley/", "I live here, and I close the month for shops, trades, clinics, and offices on Los Angeles Avenue, Tapo, Cochran, and First."),
    _hub("Moorpark", "/service-areas/moorpark/", "High Street, the college, and Tierra Rejada are full of owner-run businesses, and I keep their months current."),
    _hub("Thousand Oaks", "/service-areas/thousand-oaks/", "Boulevard practices, shops, and offices get a monthly close and reports they can hand to a CPA."),
    _hub("Newbury Park", "/service-areas/thousand-oaks/#newbury-park", "Newbury Park is part of Thousand Oaks, and Wendy, Borchard, and Dos Vientos are covered on that page."),
    _hub("Westlake Village", "/service-areas/westlake-village/", "Westlake Village is its own city in Los Angeles County, and I keep the books for owners who work there."),
    _hub("Agoura Hills", "/service-areas/conejo-and-101/#agoura-hills", "Kanan and Reyes Adobe hold offices, practices, and shops, and I reconcile their months."),
    _hub("Calabasas", "/service-areas/conejo-and-101/#calabasas", "The Commons and Calabasas Road are welcome, and the close is a person you can email."),
    _hub("Malibu", "/service-areas/conejo-and-101/#malibu", "Coast and canyon businesses can hand me the month and get reports they can read."),
    _hub("Oak Park", "/service-areas/conejo-and-101/#oak-park", "Oak Park owners are part of the Conejo work, and I am glad to keep their books."),
    _hub("Camarillo", "/service-areas/camarillo/", "Old Town, the outlets, and the airport corridor each get categories that match how they collect money."),
    _hub("Oxnard", "/service-areas/oxnard/", "The largest city in Ventura County, from the Boulevard and the harbor to the agricultural plain."),
    _hub("Ventura", "/service-areas/ventura/", "San Buenaventura, the county seat, with Main Street and the harbor on a monthly close."),
    _hub("Port Hueneme", "/service-areas/ventura-county-coast/#port-hueneme", "A harbor city with its own shops and trades, and a monthly close from me."),
    _hub("Santa Paula", "/service-areas/ventura-county-coast/#santa-paula", "Main Street and the citrus valley, with books that can show a seasonal year."),
    _hub("Fillmore", "/service-areas/ventura-county-coast/#fillmore", "A Highway 126 city of local services and shops, closed month by month."),
    _hub("Ojai", "/service-areas/ventura-county-coast/#ojai", "The Arcade and Libbey Park, with every month closed so the seasonal ones make sense."),
    _hub("Santa Clarita", "/service-areas/santa-clarita/", "Valencia, Newhall, Saugus, and Canyon Country, kept as one city and one set of books."),
    _hub("Chatsworth", "/service-areas/san-fernando-valley/#chatsworth", "Plummer, Mason, and De Soto, the Valley neighborhood closest to home."),
    _hub("Porter Ranch", "/service-areas/san-fernando-valley/#porter-ranch", "Town Center practices and family businesses, reconciled every month."),
    _hub("Northridge", "/service-areas/san-fernando-valley/#northridge", "CSUN and the Reseda, Nordhoff, and Devonshire corridors."),
    _hub("Granada Hills", "/service-areas/san-fernando-valley/#granada-hills", "Balboa and Chatsworth Street, with a close sized to the practice or the shop."),
    _hub("Woodland Hills", "/service-areas/san-fernando-valley/#woodland-hills", "Warner Center and Ventura Boulevard offices, practices, and professional firms."),
    _hub("Canoga Park", "/service-areas/san-fernando-valley/#canoga-park", "Sherman Way and Topanga shops, services, and trades."),
    _hub("Reseda", "/service-areas/san-fernando-valley/#reseda", "Reseda Boulevard services and shops, categorized in plain language."),
    _hub("Winnetka", "/service-areas/san-fernando-valley/#winnetka", "Neighborhood shops, trades, and home services, on the Valley page with everyone else."),
    _hub("Tarzana", "/service-areas/san-fernando-valley/#tarzana", "Boulevard practices and firms between Woodland Hills and Encino."),
    _hub("Encino", "/service-areas/san-fernando-valley/#encino", "Ventura Boulevard firms and medical offices, ready for your CPA."),
    _hub("Van Nuys", "/service-areas/san-fernando-valley/#van-nuys", "Van Nuys Boulevard, the civic center, and the airport area."),
    _hub("Sherman Oaks", "/service-areas/san-fernando-valley/#sherman-oaks", "Ventura Boulevard and Fashion Square shops, services, and offices."),
    _hub("Studio City", "/service-areas/san-fernando-valley/#studio-city", "Ventura Boulevard creative firms, with project deposits timed correctly."),
    _hub("North Hollywood", "/service-areas/san-fernando-valley/#north-hollywood", "Lankershim and Magnolia, near the Metro lines, closed like every other month."),
    _hub("Burbank", "/service-areas/san-fernando-valley/#burbank", "Downtown, Magnolia Park, and the airport-area businesses, with company books kept monthly."),
    _hub("Glendale", "/service-areas/san-fernando-valley/#glendale", "Brand Boulevard, the Galleria, and the Americana, on a monthly close."),
]
