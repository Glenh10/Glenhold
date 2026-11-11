"""Five industry pages, written in first person.

Open question for Jack: whether these six, with the others named on the hub,
match how he actually works. The pages stay open to every local business.
"""

from bits import checklist, help_table, paras, plans, steps

PWC = (
    "I've been in accounting since 2021, including audit work at PwC, "
    "and I'm a Certified QuickBooks ProAdvisor."
)


def ind(**kwargs):
    return kwargs


INDUSTRIES = [
    ind(
        slug="contractors",
        name="Contractors and trades",
        title="Bookkeeping for contractors and trades | Glenhold",
        description="I keep monthly books for contractors and trades around Simi Valley. Job costs, deposits, and owner draws, reconciled and reported. Plans from $349.",
        h1="Bookkeeping for contractors and trades",
        lede="Contractor bookkeeping has to show the job, the materials, and the money you still owe or are still owed. I categorize those transactions, reconcile the bank and the cards, and send a profit and loss and a balance sheet, usually by the 15th. Plans start at $349. You work with me.",
        hub="Job costs, customer deposits, and the draws you take all get a name, so the month shows what the work earned.",
        faqs=[
            ("Can you track costs by job?", "Tell me the report you want to see. If the job names are in the file, I categorize to those jobs and you can read them on the profit and loss."),
            ("How should customer deposits be recorded?", "Money you are still holding for a job sits as a liability until you earn it. I record it that way when you tell me the job is open."),
            ("The truck card mixes fuel and personal stops. Is that usable?", "Yes. Flag the personal stops and I code them to owner draw so the job costs stay clean."),
            ("Do you run payroll for the crew?", "Your payroll company runs payroll. On the Strategic plan I record the payroll journal entries in the books."),
            ("What does a small crew pay to start?", "Essential starts at $349 a month. A busier set of accounts, or job reporting, may be Core or Strategic."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "A contracting month moves through more accounts than it looks like from the truck. Materials, subcontractors, fuel, customer deposits, and the money you pull out for yourself can all hit the same checking account in one week. I separate them. The profit and loss then shows what the jobs earned, and the balance sheet shows deposits you are still holding and what the business owes.",
                "I ask for a list of every card, including the one in the glove box. Transfers between your own accounts get labeled as transfers. A personal grocery stop on the business card becomes an owner draw. A payment you made from personal funds for a job becomes money you put back into the company. Those three labels are the difference between a month you can trust and a month that looks busy and says nothing.",
                "If you want reporting by job, bring an example of the report you already wish you had. I will match the categories and the job names to that picture when the file can support it. If the jobs live only in your head, I start with solid company-level books and add job names as you go. The first call is where I quote that scope.",
                "Open months are a catch-up, priced from the records. A current file goes on Essential, Core, or Strategic. Love your first month of books, or it's free. Reports are aimed at the 15th. " + PWC,
            )
            + steps(
                "How I take a trade through the month",
                [
                    ("List the accounts and the cards", "Operating account, tax savings, materials cards, and the personal account you sometimes use for the business."),
                    ("Mark deposits and draws", "Customer money still tied to an open job, money you took out, and money you put back in."),
                    ("Code job costs", "Materials, subcontractors, fuel, dumps, permits, and the tools you want to see on their own line."),
                    ("Reconcile", "Bank and every card. A difference stays on a list until it has a name."),
                    ("Send the reports", "Profit and loss and balance sheet. Job detail when that was part of the quote. A monthly call on Strategic."),
                ],
            )
            + checklist(
                "What helps a contractor close",
                [
                    "Account and card list, including closed cards from the period",
                    "Customer deposits you are still holding",
                    "Subcontractor payments and the jobs they belong to",
                    "Loan or vehicle statements if you want balances tracked",
                    "The last month you believe is finished",
                ],
            )
            + help_table("A current crew starts with monthly bookkeeping. A shoebox of statements starts with catch-up. A file you want to run yourself starts with QuickBooks Online setup and training.")
            + plans('Plans start at $349, $599, and $1,499 a month. Your price follows volume, accounts, and whether you want job-level reports. See <a href="/pricing/">pricing</a>.')
            + paras('Read <a href="/monthly-bookkeeping/">monthly bookkeeping</a> and <a href="/cleanup-catch-up/">cleanup and catch-up</a>. Home-service companies with a similar rhythm are on <a href="/who-we-work-with/home-services/">home services</a>.')
        ),
    ),
    ind(
        slug="home-services",
        name="Home service businesses",
        title="Bookkeeping for home service businesses | Glenhold",
        description="I keep books for plumbers, electricians, landscapers, cleaners, and other home-service owners around Simi Valley. Plans from $349.",
        h1="Bookkeeping for home service businesses",
        lede="Home-service bookkeeping follows the truck and the invoice. I categorize parts, fuel, and labor-related costs, reconcile the accounts, and send a profit and loss and a balance sheet, usually by the 15th. Plans start at $349. You work with me.",
        hub="Parts, fuel, and the invoices you collected each get a place, so a week in the truck becomes a month you can read.",
        faqs=[
            ("I am a one-truck company. Is that enough to hire you?", "Yes. Essential starts at $349 a month for straightforward books, and a single truck is a common place to begin."),
            ("Customers pay by card in the driveway. How do you record it?", "I reconcile the reader or app report to the deposit, including the fee the processor kept."),
            ("Can you separate maintenance work from install work?", "Yes, when you can tell those jobs apart on the invoice or the memo. I follow that split."),
            ("What about the van payment?", "I can record the payment and, when you want the balance sheet to show the loan, split principal and interest."),
            ("Who will I hear from?", "You hear from me. The same person closes the month and answers the question about a part that looked personal."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Plumbers, electricians, HVAC crews, landscapers, cleaners, and the other trades that work in people's houses share a bookkeeping shape. Money comes in from invoices and driveway card readers. Money goes out for parts, fuel, dumps, insurance, and the van. I build the categories around that shape so the month answers a simple question: after the parts and the truck, what did the work earn?",
                "The card in the truck is where these files get muddy. Parts, fuel, and a stop for lunch can share a statement. I ask you to flag what you already know is personal. The rest gets coded to the job cost it belongs to. A transfer to your personal account is a draw. A part you bought with personal cash and want the company to carry is money you contributed.",
                "If you use a field app that invoices and takes cards, I want the payout report next to the bank deposit. The fee stays visible. Sales tax you collected, when the job includes it, is a liability at the statewide base of 7.25 percent plus any district tax for the job location. I look up the rate that applies. Your preparer files the return.",
                "Catch-up is common in this work because the month gets finished in the driveway, and the books wait. I quote the open months from the statements and the app exports. Then the monthly plan keeps the new months from stacking up. " + PWC,
                "If you run two trucks or two trades under one company, say so. I can keep the costs visible by crew when the memos support it, and the company profit and loss still closes as one month.",
            )
            + steps(
                "A home-service close",
                [
                    ("Name the apps and the accounts", "Invoicing tool, card reader, operating account, and the truck card."),
                    ("Match payouts to deposits", "Gross, fees, and the net that hit the bank."),
                    ("Code the truck card", "Parts, fuel, and the personal items you flag."),
                    ("Record the van and the insurance", "So those costs stay visible every month."),
                    ("Send the 15th reports", "Profit and loss and balance sheet, with a call on the Strategic plan."),
                ],
            )
            + checklist(
                "Bring this to the first call",
                [
                    "The field app or invoicing tool you use",
                    "Truck cards and the operating account",
                    "A recent payout report",
                    "Vehicle or equipment loans you want tracked",
                    "How far behind the books are",
                ],
            )
            + help_table("Monthly bookkeeping keeps the trucks current. Catch-up clears the months that piled up during a busy season. QuickBooks Online training is there if you want to code the easy weeks yourself.")
            + plans('Essential starts at $349 a month, Core at $599, and Strategic at $1,499. Love your first month of books, or it\'s free. Compare plans on <a href="/pricing/">pricing</a>.')
            + paras('Contractors with a similar job-cost question can read <a href="/who-we-work-with/contractors/">contractors and trades</a>. The monthly routine is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>, and a backlog starts at <a href="/cleanup-catch-up/">cleanup and catch-up</a>.')
        ),
    ),
    ind(
        slug="medical-dental",
        name="Medical and dental practices",
        title="Bookkeeping for medical and dental practices | Glenhold",
        description="I keep the business books for medical and dental practices around Simi Valley. Insurance deposits, rent, and owner activity, reconciled monthly. Plans from $349.",
        h1="Bookkeeping for medical and dental practices",
        lede="Practice bookkeeping is the business side of the office: insurance deposits, patient payments, rent, supplies, equipment, and owner draws. I categorize those, reconcile the accounts, and send a profit and loss and a balance sheet. I keep patient records out of the books and out of the contact form.",
        hub="I reconcile insurance deposits and office costs so you and your CPA can see the practice, with patient records left out of the file.",
        faqs=[
            ("Do you need patient names?", "Leave patient names and clinical records out of the books and out of the contact form. I work from deposits, reports, and account activity."),
            ("Insurance deposits never match a single day. Can you still reconcile?", "Yes. I use the billing report that lists the payments inside the deposit and tie that total to the bank."),
            ("Can my CPA keep preparing the return?", "Yes. I hand your CPA clean, reconciled books. They file the return."),
            ("What about equipment loans?", "I record the payment and track the balance when you want it on the balance sheet."),
            ("Which plan do practices usually start on?", "It depends on account volume and reporting. Essential starts at $349 a month. Many practices want Core for the quarterly view."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "I keep the business books for the practice. Rent, supplies, equipment payments, insurance deposits, patient payments that arrive as a batch, payroll through your payroll company, and the draws you take are the transactions that change the reports. I categorize them and reconcile the accounts. Clinical records stay in your practice system.",
                "An insurance deposit is a total. The explanation is the remittance or the billing export. I want that export beside the bank line so collections, adjustments, and the amount that actually arrived can be told apart. A card payment at the front desk gets the same treatment: the batch report and the deposit should agree.",
                "Please keep patient names, treatment notes, and insurance cards out of the introductory form and out of the bookkeeping file. Account numbers for the practice's own bank, the vendor list, and the deposit reports are what I need. If a report includes patient detail, ask me how to share a version that shows the money.",
                "Associates, hygiene payroll, and owner compensation each deserve their own presentation when you want to read them. Your payroll company runs payroll. On Strategic I record the journal entries. Equipment leases and practice loans can sit on the balance sheet with a balance you recognize. " + PWC + " You work with me, and the reports are aimed at the 15th.",
                "A new associate or a new operatory changes the month. Tell me in the month it happens. I would rather show the change on purpose than leave you comparing two months that quietly mean different things.",
            )
            + steps(
                "How a practice month is closed",
                [
                    ("List the business accounts", "Operating, payroll, cards, and the loans. Patient records stay in the practice system."),
                    ("Pair each deposit with its report", "Insurance remits and front-desk batches."),
                    ("Code overhead in plain groups", "Rent, supplies, labs, equipment, insurance, and owner activity."),
                    ("Reconcile", "Every business account ties to QuickBooks Online."),
                    ("Send the package your CPA can use", "Profit and loss and balance sheet. They file the return."),
                ],
            )
            + checklist(
                "What to gather, and what to leave out",
                [
                    "Business bank, card, and loan accounts",
                    "A billing or remittance export that explains deposits",
                    "Payroll reports from your payroll company",
                    "The last closed month",
                    "Patient names and clinical files, which stay with you",
                ],
            )
            + help_table("A current practice starts on monthly bookkeeping. A file that stopped when the office got busy starts as catch-up. A new entity that needs the chart of accounts built starts with QuickBooks Online.")
            + plans('Plans start at $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. The comparison is on <a href="/pricing/">pricing</a>.')
            + paras('The handoff to your preparer is described on <a href="/cpa-ready-books/">CPA-ready books</a>. The monthly routine is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Thousand Oaks and Simi Valley practices can also see the <a href="/service-areas/">service-area pages</a>.')
        ),
    ),
    ind(
        slug="professional-services",
        name="Professional services",
        title="Bookkeeping for professional services | Glenhold",
        description="I keep books for consultants, firms, and other professional-service owners. Retainers, draws, and overhead, closed monthly. Plans from $349.",
        h1="Bookkeeping for professional services",
        lede="Professional-service bookkeeping turns retainers, invoices, and a short list of overhead into a month you can read. I categorize the activity, reconcile the accounts, and send a profit and loss and a balance sheet, usually by the 15th. Plans start at $349. You work with me.",
        hub="Retainers, invoices, and owner draws get a clean month, so you can see what the practice earned after overhead.",
        faqs=[
            ("I bill retainers. When is that income?", "When you have earned it. Until then I can hold it as a liability so the profit and loss shows work you have already done."),
            ("It is just me and a laptop. Do I need a monthly close?", "A one-person firm still has a year to hand a CPA. Essential starts at $349 a month and is built for that shape."),
            ("Can you separate two lines of work?", "Yes. Consulting and a product, or two practices, can be categories or classes when you want them apart."),
            ("What about the home office and personal cards?", "Tell me which charges are the business. Personal charges on a business card become draws."),
            ("Will you file my return?", "I hand your CPA clean, reconciled books. They file the return."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Consultants, designers, advisors, agencies, and the other professional firms I work with often have a simple bank picture and a tricky timing picture. A retainer arrives in March for work you will do in May. A project invoice gets paid in pieces. Software, contractors, and your own draw all leave the same account. I time the income to the work you have earned and I label the draw so profit is profit.",
                "A one-person firm and a small office with a coordinator can use the same close. The difference is volume and whether payroll exists. Your payroll company runs payroll. I record the entries on the Strategic plan. On Essential and Core I still reconcile the payroll drafts and the tax payments that leave the bank, and I ask you when a draft needs a name.",
                "If you sell a service and a product, or you run two offers under one entity, say so. I can keep them visible on the profit and loss. If the entity is an LLC, the $800 California franchise tax is a real bill in most years. A first-year waiver covered only registrations in 2021, 2022, and 2023. I record the payment. Your CPA files the form and confirms the current rule.",
                "The first call is the accounts, the unearned retainers, and whether the books are current. I quote before I start. Reports are aimed at the 15th. " + PWC,
                "If you pay yourself a mix of draws and a payroll check, both can be visible. The draw stays on the balance sheet. The payroll check follows the report from your payroll company. You can read them side by side.",
            )
            + steps(
                "How I close a professional month",
                [
                    ("List retainers and invoices", "What has been earned, and what is still a deposit."),
                    ("Code overhead", "Software, contractors, rent, insurance, and dues."),
                    ("Label owner activity", "Draws, contributions, and personal charges on the firm card."),
                    ("Reconcile the accounts", "Bank, cards, and the processor if clients pay online."),
                    ("Send the reports", "Profit and loss and balance sheet, with the extra views on Core and Strategic."),
                ],
            )
            + checklist(
                "Useful on day one",
                [
                    "Bank, card, and payment-processor accounts",
                    "A list of retainers collected for work still ahead of you",
                    "Contractor payments you want visible",
                    "The last closed month",
                    "Your CPA's deadline",
                ],
            )
            + help_table("Monthly bookkeeping is the steady close. Catch-up is the open year. QuickBooks Online setup is the right start when the file itself needs to be built around retainers.")
            + plans('Plans start at $349, $599, and $1,499 a month. Love your first month of books, or it\'s free. Read <a href="/pricing/">pricing</a> for the differences.')
            + paras('See <a href="/cpa-ready-books/">CPA-ready books</a> for the handoff, and <a href="/monthly-bookkeeping/">monthly bookkeeping</a> for the rhythm. Westlake Village and the Conejo have many of these firms on the <a href="/service-areas/">area pages</a>.')
        ),
    ),
    ind(
        slug="ecommerce",
        name="Ecommerce and online sellers",
        title="Bookkeeping for ecommerce and online sellers | Glenhold",
        description="I reconcile payouts from Shopify, Amazon, and other channels to your bank and send a monthly profit and loss. Plans from $349.",
        h1="Bookkeeping for ecommerce and online sellers",
        lede="Ecommerce bookkeeping starts from the payout, because the payout is the bank deposit. Fees, refunds, and sales sit inside it. I reconcile that report to your accounts and send a profit and loss and a balance sheet, usually by the 15th. Plans start at $349. You work with me.",
        hub="I tie each channel payout to the bank so fees, refunds, and sales stay visible on the monthly reports.",
        faqs=[
            ("I sell on Shopify and Amazon. Can one file hold both?", "Yes. I keep the channels separate in the categories so you can see each payout's sales and fees."),
            ("Do you track inventory?", "I record the purchases and the payouts. If you want a full inventory subledger, tell me what your channel already tracks and I will quote that scope."),
            ("Sales tax collected by the channel is confusing. How do you record it?", "I follow the payout report. Tax the channel collected and remitted stays out of your income. Tax you still owe sits as a liability."),
            ("What if the books are a year behind?", "I quote the open months from the payout exports you can still download. Monthly bookkeeping starts after that."),
            ("Is the QuickBooks subscription included?", "You keep your own QuickBooks Online subscription with Intuit. My fee is for the bookkeeping."),
        ],
        body=(
            "<!-- VIDEO -->"
            + paras(
                "Online sellers get paid in payouts. A Shopify payout, an Amazon settlement, an Etsy deposit, and a Stripe batch each arrive as one number that contains sales, fees, refunds, and sometimes tax. I break the payout into those parts and I tie the net to the bank. The profit and loss then shows sales and fees. The bank reconciliation shows the deposit you actually received.",
                "Tell me every channel, including the one you think is too small to matter. A forgotten payout account is the usual reason a seller's books drift. I also want the account that pays for inventory, ads, and shipping supplies. Those costs belong in the same month as the sales they support when the reports let me see the timing. When the timing is less obvious, I still record them clearly and I tell you which comparisons that month supports.",
                "Inventory purchases are part of the close. I record what you bought and what the payouts say you sold. If you want a deeper inventory count than the channel already keeps, that is a scope I quote on the call. I will match the work to the report you can actually export.",
                "Sales tax depends on who remits it. When the channel collects and remits, I keep that tax off your income. When you collect it yourself, I record a liability. The California statewide base rate is 7.25 percent, and district rates vary. I look up the rate that applies to you. Your preparer files what the channel does not. " + PWC,
            )
            + steps(
                "An online seller's month",
                [
                    ("List the channels and the bank", "Every payout source, and the account that receives them."),
                    ("Open the settlement report", "Sales, fees, refunds, and tax, next to the deposit."),
                    ("Code inventory, ads, and shipping", "From the card or account that paid them."),
                    ("Reconcile", "Each payout ties to a bank line. Each card ties to a statement."),
                    ("Send the reports", "Profit and loss by channel when that was in scope, plus the balance sheet, aimed at the 15th."),
                ],
            )
            + checklist(
                "Exports that make this faster",
                [
                    "A payout or settlement report for each channel",
                    "The bank account that receives payouts",
                    "The card or account that buys inventory and ads",
                    "A note on who remits sales tax",
                    "The last month you trust",
                ],
            )
            + help_table("Monthly bookkeeping keeps the payouts current. Catch-up rebuilds the months you can still export. QuickBooks Online setup is the start when the file has no channel accounts yet.")
            + plans('Plans start at $349, $599, and $1,499 a month. More channels and more payouts move the quote. Love your first month of books, or it\'s free. See <a href="/pricing/">pricing</a>.')
            + paras('The close is described on <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. A skipped year starts on <a href="/cleanup-catch-up/">cleanup and catch-up</a>. The file itself is <a href="/quickbooks-online/">QuickBooks Online</a>.')
        ),
    ),
]
