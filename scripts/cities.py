"""Eight city pages, three regional pages, hub lines, and retired-slug redirects.

Open question for Jack, not for the page: whether these eight cities and three
regions match how he actually works.
"""

from bits import checklist, help_table, paras, plans, section, steps
from city_rest import MORE_CITIES
from city_regions import HUB, INDUSTRY_REDIRECTS, REDIRECTS, REGIONS

PWC = (
    "I've been in accounting since 2021, including audit work at PwC, "
    "and I'm a Certified QuickBooks ProAdvisor."
)


def _steps(title, items):
    return steps(title, items)


def _ready(title, items):
    return checklist(title, items)


CITIES = [
    dict(
        slug="simi-valley",
        name="Simi Valley",
        schema_type="City",
        schema_name="Simi Valley",
        contained="Ventura County, California",
        title="Bookkeeping in Simi Valley, CA | Glenhold",
        description="I'm in Simi Valley. I categorize the month, reconcile your accounts, and send reports you can read. Plans from $349. You work with me.",
        h1="Small business bookkeeping in Simi Valley",
        lede="I live in Simi Valley, and I keep the books for small businesses here. I categorize the month, reconcile your bank and credit cards, and send a profit and loss and a balance sheet, usually by the 15th. Plans start at $349 a month. You work with me.",
        hub="I live here, and I close the month for shops, trades, clinics, and offices along Los Angeles Avenue, Tapo, Cochran, and First.",
        faqs=[
            ("Can I start if the books live in a shared inbox?", "Yes. Tell me which accounts are the business and who can name a transaction that needs a look. On the first call I will show you how to share files."),
            ("What if I am a few months behind?", "That is a catch-up. Tell me the months and the accounts and I will quote it before I start. After those months are closed, the new ones can stay on a monthly rhythm."),
            ("I already have a CPA in town. Where do you fit?", "Keep your CPA. I hand them clean, reconciled books. They file the return."),
            ("Can you and I meet in Simi Valley?", "Yes. I live here. A call is usually enough, and when the reports help on paper, you and I can meet in town."),
            ("When will I see the month?", "I aim for the 15th of the next month. If a statement or an answer is still out, I tell you and send the reports as soon as I have them."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Los Angeles Avenue, Tapo Street, Cochran Street, and First Street are where a lot of the owner-run businesses sit: trades, clinics, offices, and shops. I set the categories up around how you get paid and what you spend, so a materials run, a payroll transfer, and a personal draw each land where you expect them. Then I reconcile the bank and the cards and send the profit and loss and the balance sheet.",
                "The first conversation covers the accounts, the months you care about, and the question you want the reports to answer. I quote the work before I start. If the file is current, the next step is a monthly close. If a stack of months is still open, I price that catch-up from the records you have, finish those months, and then keep the new ones current. When a meeting helps, you and I can sit down here in town.",
                "Simi businesses often collect money in more than one way. A shop may have a card processor and a handful of checks. A contractor may have deposits in the account until the job is finished. A clinic may see insurance deposits that cover more than one day's appointments. I want the deposit and the report that explains it. Once those agree, the profit and loss is useful on an ordinary Tuesday and useful again when your CPA starts the return.",
                "I aim to send reports by the 15th of the next month, once the statements and your answers are in. If a card statement is late or a transfer needs a name, I tell you what is missing and send the reports as soon as I have it. You are talking to me on that close. " + PWC + " Now I bring that same care to businesses in this town.",
                "Sales tax is part of the close when you collect it. I record the sale as income and the tax you collected as a liability, the amount that goes to the state. The statewide base rate is 7.25 percent, and district taxes can make Simi Valley's rate higher. I look up the rate for your location. Your preparer files the return.",
            )
            + _steps(
                "How a month goes for a Simi Valley business",
                [
                    ("List the accounts", "Checking, savings, cards, loans, and the processor. A shop on Tapo and a crew working from a Cochran yard can start from that same short list."),
                    ("Choose the first month", "If last month is already closed, I start with the new one. If the file stops in the spring, the first job is the open months, quoted before I begin."),
                    ("Mark the odd transactions", "Owner draws, money you put back in, transfers between your own accounts, and the card that sometimes buys groceries. Name them once and later months move faster."),
                    ("I categorize the activity", "Income, job costs, rent, fuel, supplies, and the rest, in names that match how you talk about the work."),
                    ("I reconcile the balances", "The bank and each card tie to the books. A difference gets a note you can see."),
                    ("You get the reports", "A profit and loss and a balance sheet, aimed at the 15th. Core adds a quarterly summary and a year-to-date comparison. Strategic adds a monthly call."),
                ],
            )
            + _ready(
                "What helps me close your month",
                [
                    "The account list, including a card that lives in a truck or a kitchen drawer",
                    "Statements for the months in scope, or bank feeds inside QuickBooks Online",
                    "Processor or point-of-sale reports when a deposit bundles sales, fees, and refunds",
                    "A note on anything you already know is personal",
                    "The date your CPA or a lender asked for, if there is one",
                ],
            )
            + plans("Essential starts at $349 a month, Core at $599, and Strategic at $1,499. The price moves with transaction volume, the number of accounts, and the reporting you want. Love your first month of books, or it's free. Details sit on the <a href=\"/pricing/\">pricing page</a>.")
            + paras('The monthly routine is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. A backlog starts as <a href="/cleanup-catch-up/">cleanup and catch-up</a>. Trades and <a href="/who-we-work-with/home-services/">home-service businesses</a> call from this side of town often, and so do <a href="/who-we-work-with/professional-services/">professional offices</a>.')
        ),
    ),
    dict(
        slug="moorpark",
        name="Moorpark",
        schema_type="City",
        schema_name="Moorpark",
        contained="Ventura County, California",
        title="Bookkeeping in Moorpark, CA | Glenhold",
        description="I keep monthly books for Moorpark owners along High Street, Tierra Rejada, and the college side of town. Plans from $349.",
        h1="Bookkeeping for Moorpark small businesses",
        lede="If your business is in Moorpark, I can keep the month closed for you. I categorize transactions, reconcile the bank and the cards, and send a profit and loss and a balance sheet, usually by the 15th. You work with me, from Simi Valley, a short way down the road.",
        hub="High Street, the college, and Tierra Rejada are full of owner-run shops and services, and I close their months the same careful way.",
        faqs=[
            ("My High Street shop deposits a mix of cards and a few invoices. Can you sort that?", "Yes. Send the processor report with the bank deposit. I match them so sales, fees, and the money in the account tell the same story."),
            ("I am a one-person trade. Is monthly bookkeeping too much?", "Essential starts at $349 a month for straightforward books. If the volume is light, that is the plan I quote from."),
            ("The file at home stops in the summer. What happens first?", "I look at the last closed month and the accounts, then I quote the open stretch. After that, the new months can stay current."),
            ("Do I need QuickBooks Online already?", "It helps, and it is the file I work in. If you are starting fresh, setup and training can come first."),
            ("Who answers when I have a question about a number?", "I do. You work with me on the close and on the email afterward."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Moorpark feels like its own town: High Street, the college, and the businesses scattered along Tierra Rejada. I work with owners there the same way I work in Simi Valley. You tell me how money comes in. I build the categories around that, reconcile the accounts, and send reports you can read without a translation.",
                "A High Street shop and a service business near the college collect money differently, and the books should show that. Retail deposits need the processor report beside them. A tutor, a therapist, or a consultant may have a few larger payments and a simple card for supplies. A crew working along Tierra Rejada all week needs fuel, materials, and the owner's draws named clearly so the profit is the profit.",
                "On the first call I ask which months are finished, which accounts are in play, and whether a CPA or a lender is waiting. I quote before I start. Catch-up is its own price, based on the pile of records. Monthly bookkeeping after that is one of the three plans. Love your first month of books, or it's free.",
                "I live in Simi Valley, so Moorpark is an easy place to meet when you want to look at a report together. Plenty of months never need a meeting. I send the profit and loss and the balance sheet, you reply with the one transaction that looks strange, and I fix the label. The aim is the 15th of the next month.",
                PWC + " The Moorpark owners I talk with want the same thing the Simi owners want: a month they can trust, and a person they can reach.",
            )
            + _steps(
                "How I take on a Moorpark month",
                [
                    ("Map the money", "Where deposits come from, which card pays for materials, and whether High Street sales run through a processor, invoices, or both."),
                    ("Set the starting month", "The last month you trust is the handoff. Everything after it is either a catch-up quote or the first monthly close."),
                    ("Separate the owner from the business", "Draws, contributions, and the grocery run on the business card get their own lines."),
                    ("Categorize and reconcile", "I code the month and tie the bank and the cards to the books."),
                    ("Send reports you can use", "Profit and loss, balance sheet, and a note if something still needs you. Core and Strategic add the comparisons and the call described on the pricing page."),
                ],
            )
            + _ready(
                "Bring these to the first Moorpark close",
                [
                    "Bank and card names for the business",
                    "The last month you believe is finished",
                    "Processor totals if deposits mix sales and fees",
                    "Any loan or vehicle payment you want tracked",
                    "Your CPA's deadline, if the return is the reason for the call",
                ],
            )
            + plans('Plans start at $349, $599, and $1,499 a month. Moorpark shops with a single account often land on Essential. A busier crew, or an owner who wants a monthly walkthrough, is a Core or Strategic conversation. See <a href="/pricing/">pricing</a>.')
            + paras('Read the monthly routine on <a href="/monthly-bookkeeping/">monthly bookkeeping</a>, or the backlog path on <a href="/cleanup-catch-up/">cleanup and catch-up</a>. If the work is a trade, the <a href="/who-we-work-with/contractors/">contractors</a> page is the closer description.')
        ),
    ),
]

CITIES.extend(MORE_CITIES)
