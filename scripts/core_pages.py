"""Core page copy: about, pricing, services, and the six service pages."""

from bits import checklist, help_table, paras, plans, section, steps

PWC_PARAS = (
    "I've been in accounting since 2021, including audit work at PwC, "
    "and I'm a Certified QuickBooks ProAdvisor. Now I bring that same care "
    "to small businesses around Simi Valley."
)


def monthly():
    return (
        "<!-- VIDEO -->"
        + paras(
            "The month has a shape. Transactions get a category, the bank and the credit cards get reconciled, and you receive a profit and loss and a balance sheet. I aim for the 15th of the next month, once your statements and answers are in. You work with me on that close. Plans start at $349 a month. Love your first month of books, or it's free.",
            "I start by learning how you get paid. A shop with card batches, a contractor with deposits, a practice with insurance remits, and a consultant with retainers all need different categories. I set the chart of accounts around your version, then I use that same map every month so March and October can be compared.",
            "Reconciliation is the part that makes the reports believable. The bank balance in QuickBooks Online matches the bank. Each card matches its statement. A transfer between your own accounts is a transfer, an owner draw is a draw, and a personal charge on the business card is labeled. When something is still unnamed, it stays on a short list I send with the reports.",
            "Your payroll company runs payroll. On the Strategic plan I record the payroll journal entries so wages, taxes, and the net draft agree with the books. On Essential and Core I still reconcile the cash that left the account and I ask when a draft needs a name. Sales tax you collected is a liability, the amount you will send on. The statewide base rate is 7.25 percent. District taxes can make your city's rate higher, and I look up the one that applies. Your preparer files the return.",
            "The quote follows transaction volume, the number of accounts, and how much reporting you want. Essential keeps the month current. Core adds a quarterly summary, a year-to-date comparison, and priority support. Strategic adds custom reports, accrual, payroll journal entries, loan tracking, and a monthly call. Cleanup of older months is priced on its own. You keep your QuickBooks Online subscription with Intuit. My fee is for the bookkeeping.",
            PWC_PARAS,
        )
        + steps(
            "Seven steps in a monthly close",
            [
                ("The first call", "You tell me the business, the accounts, and whether the books are current. I tell you which plan or catch-up quote fits, before any work starts."),
                ("Access and a starting month", "The last month you trust is the handoff. Bank feeds or statements cover everything after it. Logins stay off the public contact form. I show you how to share them."),
                ("A chart of accounts in your words", "Income the way you earn it, costs the way you feel them, and owner activity on its own lines."),
                ("Categorize the new month", "Every transaction gets a home. Recurring vendors get a rule once the pattern is real."),
                ("Reconcile bank and cards", "Balances tie. Differences get a note you can answer in one reply."),
                ("Send the reports", "Profit and loss and balance sheet, aimed at the 15th. Core adds the quarterly and year-to-date view. Strategic adds the call."),
                ("Carry the open questions", "Anything still unnamed waits on a list, and the next month starts from a file that agrees with the bank."),
            ],
        )
        + checklist(
            "What I do every month",
            [
                "Code new transactions to the categories you and I agreed on",
                "Reconcile each bank and credit card account",
                "Label draws, contributions, and transfers",
                "Record sales tax you collected as a liability",
                "Send a profit and loss and a balance sheet",
                "Tell you what I still need, if anything is outstanding",
            ],
        )
        + plans('Essential starts at $349 a month, Core at $599, and Strategic at $1,499. Love your first month of books, or it\'s free. That promise covers monthly bookkeeping. The side-by-side description is on <a href="/pricing/">pricing</a>.')
        + paras('If older months are the real problem, start with <a href="/cleanup-catch-up/">cleanup and catch-up</a>. If you want the file built or a lesson in running it, start with <a href="/quickbooks-online/">QuickBooks Online</a>. The handoff list is on <a href="/getting-started/">getting started</a>.')
    )


def cleanup():
    return (
        "<!-- VIDEO -->"
        + paras(
            "Catch-up bookkeeping is the work of recording the months that never got closed. I categorize the backlog, reconcile the accounts for those months, and send you the reports. When the open stretch is finished, a monthly plan can keep the new months from stacking up again. You work with me. I quote the catch-up before I start.",
            "I price that work from the records you have: how many months, how many accounts, and how complete the statements and reports are. A three-month gap with clean bank feeds is a different project from a year of mixed personal and business charges. I will tell you the price after I see the shape of the pile. I am glad to give you a range on the first call and a firm quote once the list of accounts is clear.",
            "The first product of a catch-up is a starting point you can trust. That means a reconciled balance at the end of the last month in scope, a profit and loss for the period, and a balance sheet that ties. It also means a list of what I still could not see, so you and your CPA know the edges of the file. I hand your CPA clean, reconciled books. They file the return.",
            "Bring what you have. Statements, processor exports, a half-used QuickBooks Online file, a spreadsheet, a box of PDFs. I can start from any of those. Months without a statement stay visible as a question, and I will tell you what that gap blocks. Plenty of catch-ups begin with 'the file stops in June' and end with a December that matches the bank.",
            "After the backlog, most owners want the monthly rhythm. Essential, Core, and Strategic are the same plans as on a current file. Love your first month of books, or it's free, once that monthly work begins. The catch-up itself is quoted on its own. " + PWC_PARAS,
        )
        + steps(
            "How a catch-up actually moves",
            [
                ("You show me the last month you trust", "That month is the floor. Everything after it is the project."),
                ("I list the accounts and the gaps", "Missing statements and missing months are named before I quote the final price."),
                ("I categorize the open period", "Using categories that match the business you have now, so the new monthly close can continue them."),
                ("I reconcile each month or the period in the quote", "Bank and cards tie at the end of the scope."),
                ("You receive reports and a leftover list", "Profit and loss, balance sheet, and the items that still need a human answer."),
                ("The next month can be a plan", "Monthly bookkeeping starts from the reconciled balance, on the plan that fits your volume."),
            ],
        )
        + checklist(
            "What to send for a catch-up quote",
            [
                "The last month you believe is finished",
                "Bank and card statements, or an invitation to the bank feeds",
                "Any QuickBooks, spreadsheet, or processor export you already have",
                "A note about personal spending on business accounts",
                "The deadline, if a CPA or a lender is waiting",
            ],
        )
        + help_table("Catch-up is the open history. Monthly bookkeeping is the month after that. QuickBooks Online setup is the right first step when there is no file yet, only statements.")
        + paras('The ongoing close is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Prices for the plans that follow a catch-up are on <a href="/pricing/">pricing</a>. The practical list of records is on <a href="/getting-started/">getting started</a>.')
    )


def quickbooks():
    return (
        "<!-- VIDEO -->"
        + paras(
            "I set up QuickBooks Online, organize the chart of accounts, and train you on the work you want to keep. I am a Certified QuickBooks ProAdvisor. The subscription itself stays with you and Intuit. My fee is for the setup, the training, and any monthly bookkeeping you want beside it.",
            "A useful file starts from how you get paid. Card batches, invoices, retainers, and job deposits each need an account that means something when you read the profit and loss. I would rather build a short chart you will use than a long one copied from a template. Bank feeds, a clearing account for payouts, and a clear place for owner draws are usually the bones of that file.",
            "Training follows the tasks you actually touch. If you want to send invoices and code the obvious expenses, I will teach those screens and I will keep the reconciliation. If you want to hand me the month entirely, training can be a short orientation so the reports make sense when they arrive. Tell me which of those you want. The lesson fits that answer.",
            "If the file already exists and the balances disagree with the bank, setup turns into a cleanup. I quote that from the open months. If you are starting from zero, I can open the file, connect the accounts, and close the first month with you. You work with me. " + PWC_PARAS,
            "QuickBooks Online is the system I keep the books in. Bring the questions you already have about the product, including reports you have tried to run. I will sit in the file with you, on a call, and leave you with a chart and a routine. Monthly plans, if you want me to keep closing, start at $349. Love your first month of books, or it's free.",
            "A setup is finished when you can find last month's profit without hunting, and when the bank balance on the screen matches the bank. That is the bar I use, whether you take the monthly plan afterward or keep the coding yourself.",
        )
        + steps(
            "What setup and training include",
            [
                ("A conversation about the work you will keep", "Invoicing, coding, or reading reports. The lesson follows that list."),
                ("A chart of accounts in your language", "Income, costs, sales tax payable, and owner draws, named for your business."),
                ("Bank and card feeds", "Connected, with a first reconciliation so the opening picture matches the statements."),
                ("Payouts and processors", "A way to split fees from sales when the deposit is a single number."),
                ("A live walkthrough", "The screens you will use, and the screens you can leave to me."),
                ("A written routine", "What you do each week, and what I do at the close, if a monthly plan is part of the quote."),
            ],
        )
        + checklist(
            "Have this before a setup call",
            [
                "The legal name you want on the file, and the business you actually run",
                "Bank and card accounts to connect",
                "A recent statement if the feed needs a starting balance",
                "The processors or apps that pay you",
                "The tasks you want to keep doing yourself",
            ],
        )
        + help_table("Setup and training build the file. Monthly bookkeeping keeps it closed. Catch-up repairs a file that already drifted.")
        + paras('See <a href="/monthly-bookkeeping/">monthly bookkeeping</a> if you want the close handled, and <a href="/pricing/">pricing</a> for the monthly plans. A backlog of unreconciled months is <a href="/cleanup-catch-up/">cleanup and catch-up</a>.')
    )


def statements():
    return (
        "<!-- VIDEO -->"
        + paras(
            "A profit and loss and a balance sheet are the two reports I send with a monthly close. The profit and loss shows what the business earned and spent over a period. The balance sheet shows what it owns, what it owes, and the owner's stake on a single date. I want you to be able to read both without a glossary.",
            "On the profit and loss, start at the top. Income should match the way you get paid: sales, fees you earned, or the channels you sell through. Costs come next. A contractor looks at materials and subcontractors. A shop looks at inventory and processor fees. A practice looks at rent, supplies, and labor. The bottom of the report is the profit after those costs. If a number surprises you, the transaction list behind it is the next click, and I will point you to it.",
            "The balance sheet is the snapshot. Cash should match the reconciled bank. Credit cards should match the statements. Sales tax you have collected and not yet sent sits as a liability. Customer deposits you are still holding sit as a liability too. Loans show the balance you still owe when loan tracking is part of the work. Owner draws reduce equity. They are money you took out. They are a balance-sheet movement.",
            "I send these reports aimed at the 15th of the next month. Core adds a quarterly summary and a year-to-date comparison, which is how you see whether this March looks like last March. Strategic adds custom reports and a call so you and I can walk the lines that matter. The reports are built from reconciled accounts. That is what makes them worth reading.",
            "A useful comparison needs the same categories in both months. That is why I keep account names steady once the file is settled. A new kind of income can have a new line. An old line keeps its name so last year and this year sit on the same row. If something in the business changed, tell me in the month it changed and I will show it on purpose. Bring the question you hope the report will answer, and I will make sure that line is easy to find.",
            "I hand your CPA the same books. They file the return. If a lender has asked for a period of statements, I organize the months they named. " + PWC_PARAS,
        )
        + steps(
            "How to read the month I send",
            [
                ("Read income first", "Does it match what you remember collecting?"),
                ("Read the costs you feel", "Food, materials, rent, payroll, fees. The ones you talk about at the counter."),
                ("Check the bottom", "Profit after those costs, for the month and, on Core, for the year so far."),
                ("Open the balance sheet", "Cash, cards, tax you still owe, and loans."),
                ("Ask about one line", "Reply with the number that looks off. I would rather explain it than have you guess."),
            ],
        )
        + checklist(
            "A reliable pair of statements has",
            [
                "A profit and loss for the month you asked about",
                "A balance sheet dated the last day of that month",
                "Bank and card balances that match the statements",
                "Owner draws labeled as draws",
                "A note listing anything still open",
            ],
        )
        + section(
            "Monthly reports at a glance",
            """<div class="table-wrap"><table>
<thead><tr><th>Report</th><th>What it answers</th><th>When you get it</th></tr></thead>
<tbody>
<tr><td>Profit and loss</td><td>What you earned and spent</td><td>With the monthly close, aimed at the 15th</td></tr>
<tr><td>Balance sheet</td><td>What you own, owe, and have taken out</td><td>Same package</td></tr>
<tr><td>Quarterly and year-to-date view</td><td>How this stretch compares</td><td>Core and Strategic</td></tr>
</tbody></table></div>""",
        )
        + paras('The work that produces these reports is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. Plan differences are on <a href="/pricing/">pricing</a>. The version your preparer wants is on <a href="/cpa-ready-books/">CPA-ready books</a>.')
    )


def cpa():
    return (
        "<!-- VIDEO -->"
        + paras(
            "I hand your CPA clean, reconciled books. They file the return. That is the whole relationship. You keep the preparer you trust. I make the year a set of closed months instead of a folder of statements and a question mark.",
            "Clean, for this handoff, means the bank and the cards are reconciled through the period they asked for, the profit and loss covers that period, and the balance sheet ties to those reconciliations. Owner draws and contributions are labeled. Sales tax you collected is a liability. Personal charges that slipped onto a business card are identified. I send that package, and I stay available for the questions your preparer asks about a line.",
            "California items show up in almost every handoff I do. The statewide sales-tax base rate is 7.25 percent, and district taxes can raise the rate in your city. I look up the rate and I record what you collected. Most California LLCs owe an $800 minimum franchise tax each year. A first-year waiver covered only LLCs registered in 2021, 2022, and 2023. The LLC fee has historically started when total income reaches $250,000. Your CPA confirms the current FTB rule and files the form. I keep the books those forms are built from.",
            "If the year is behind, the handoff starts as a catch-up. I quote the open months, close them, and then the monthly plan keeps the next year from arriving in the same shape. Tell me the preparer's deadline on the first call so the quote respects it. " + PWC_PARAS,
            "Your preparer may also ask for a general ledger, a detail of fixed assets, or the payroll reports from your payroll company. Send me that list with the deadline. I would rather assemble what they named than guess at a package.",
        )
        + steps(
            "Getting a year ready for your preparer",
            [
                ("Ask what period they need", "Usually the calendar year, sometimes a fiscal year. I follow their date."),
                ("Close each month in that period", "Categories and reconciliations, month by month, so the year is a stack of finished months."),
                ("Label owner and tax items", "Draws, contributions, sales tax collected, and payroll drafts."),
                ("Send the reports and the leftover list", "So the preparer sees both the numbers and the open questions."),
                ("Answer their follow-ups", "You can loop me in. I would rather explain a deposit than leave it guessed."),
            ],
        )
        + checklist(
            "What your preparer is glad to receive",
            [
                "Reconciled bank and card accounts",
                "A profit and loss for the year",
                "A year-end balance sheet",
                "Payroll reports from your payroll company",
                "A note of anything still estimated",
            ],
        )
        + help_table("Monthly bookkeeping makes the handoff ordinary. Catch-up builds it when the year is open. QuickBooks Online is the file I keep those months in.")
        + paras('Start with <a href="/monthly-bookkeeping/">monthly bookkeeping</a> or <a href="/cleanup-catch-up/">cleanup and catch-up</a>. Report definitions are on <a href="/financial-statements/">financial statements</a>.')
    )


def loan():
    return (
        "<!-- VIDEO -->"
        + paras(
            "When a lender asks for financials, I organize the books and the reports they named. That usually means reconciled months, a profit and loss, a balance sheet, and sometimes a stretch of statements that matches the application. I build that package from your accounts. Your lender reads it and makes the credit decision.",
            "Tell me the list they sent. Some want the last twelve months. Some want the last two years and a debt schedule. Some want the statements stamped to a specific month. I quote the work from that list and from how complete the file already is. If the months are open, the first task is the catch-up that makes those months real. If they are already closed, I assemble what the lender asked to see.",
            "Loan tracking on the Strategic plan keeps balances, payments, and the split between principal and interest visible on the balance sheet. That is useful while you are borrowing and after. Essential and Core still reconcile the payment that left the bank. The extra tracking is a Strategic item because it takes a schedule and a monthly check against it.",
            "I am glad to be on a call with you before you send the package, so you know which lines the lender is likely to ask about. Bring the questions they already asked. I will answer from the books. " + PWC_PARAS + " You work with me on the package.",
            "If the business has more than one entity, say which one the lender is underwriting. I keep the package tied to that entity's accounts so a transfer between companies is labeled as a transfer.",
        )
        + steps(
            "Putting a lender package together",
            [
                ("Read their list", "Months, entities, and any debt schedule they named."),
                ("Close the months that are still open", "A catch-up quote if the file stops short of their date."),
                ("Reconcile through that date", "Bank and cards, so the cash on the balance sheet is the cash in the account."),
                ("Lay out debt", "Balances and payments, in detail on Strategic and as cleared cash on every plan."),
                ("Send you the set", "Profit and loss, balance sheet, and the notes that explain a one-time month."),
            ],
        )
        + checklist(
            "What I ask you to forward",
            [
                "The lender's document list",
                "The entity they are underwriting",
                "Loan and credit-card statements for the balances they asked about",
                "The last closed month",
                "The date they gave you",
            ],
        )
        + plans('Monthly plans start at $349, $599, and $1,499. A lender package that includes open months is quoted as catch-up plus the reports. See <a href="/pricing/">pricing</a> and <a href="/cleanup-catch-up/">cleanup and catch-up</a>.')
        + paras('The reports themselves are explained on <a href="/financial-statements/">financial statements</a>. The monthly rhythm after the application is <a href="/monthly-bookkeeping/">monthly bookkeeping</a>.')
    )


def about():
    return (
        paras(
            "I'm Jack. I live in Simi Valley. " + PWC_PARAS,
            "I started Glenhold to help small business owners keep reliable books and understand their financial reports. You work with me from the first call through every close. I answer the email. When it helps, you and I sit down and walk through the numbers.",
            "Outside the work, I fish, I walk, and I go to Mass with my wife and our two children. The fly-fishing photo on this page is from one of those days.",
        )
        + "<!-- PHOTOEND -->"
        + section(
            "How you and I start",
            paras(
                "The first conversation is short and practical. You tell me what the business does, how you get paid, which accounts you use, and whether the books are current. I tell you whether the next step is a monthly plan, a catch-up, or a QuickBooks Online setup, and I quote it before I begin.",
                "You can book a call, call (805) 419-3451, or send a note. I reply within one business day. Leave bank logins and statements off that first form. I will show you a direct way to share files once the work is scoped.",
                "On that call I also want the deadline, if you have one. A CPA appointment, a lender date, or a quiet wish to start the year current all change the order of the work. They change the price when they change the size of the project.",
                "People ask what the first month feels like. I learn your vendors, I ask about the odd transactions once, and I send reports you can reply to in plain language. By the second month the categories are familiar and the close is shorter. You still hear from me, and the questions get more specific: a new loan, a new sales channel, a draw that was larger than usual.",
            ),
        )
        + section(
            "What a month looks like",
            paras(
                "After the scope is set, the month has a rhythm. I categorize transactions in the language of your business. I reconcile the bank and the credit cards. I send a profit and loss and a balance sheet, aimed at the 15th of the next month. If a statement or an answer is still out, I tell you what is missing and send the reports as soon as I have it.",
                "Essential, at $349 a month to start, is that close. Core, at $599, adds a quarterly summary, a year-to-date comparison, and priority support. Strategic, at $1,499, adds custom reports, accrual, payroll journal entries, loan tracking, and a monthly call. Your price moves with volume, accounts, and reporting. Love your first month of books, or it's free.",
                "Your payroll company runs payroll. Your CPA files the return. I hand them clean, reconciled books. You keep your own QuickBooks Online subscription with Intuit.",
            ),
        )
        + section(
            "Where to find me between closes",
            paras(
                'I post bookkeeping videos on YouTube at <a href="https://www.youtube.com/@BookkeepingBizBlueprint" target="_blank" rel="noopener noreferrer">@BookkeepingBizBlueprint</a>. The channel is a place to see how I talk about the work. The books themselves still happen between you and me, one business at a time. A video can show how a reconciliation works. Your file still gets my attention, with you, one close at a time.',
                'If you want the longer description of the monthly close, it is on <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. The plans are on <a href="/pricing/">pricing</a>. The towns I cover are on <a href="/service-areas/">service areas</a>.',
            ),
        )
    )


def pricing():
    return (
        paras(
            "Monthly bookkeeping starts at $349, $599, or $1,499. Those are starting prices. I set yours from transaction volume, the number of accounts, and the reporting you want. Love your first month of books, or it's free. That promise covers monthly bookkeeping. Catch-up and QuickBooks training are quoted on their own.",
            "On a call I ask three questions. How many accounts and cards touch the business? How many transactions move in a typical month? Do you want the reports in writing, or do you also want a monthly walkthrough and custom views? The answers pick the plan. A one-account shop with a clear processor often starts on Essential. A business that wants the year visible every quarter is Core. A business with accrual, payroll entries, loans, and a standing call is Strategic.",
            "I would rather quote a plan you will keep than a plan that looks thorough and goes unused. If Core's quarterly view is the thing you actually want, say that. If you want the call every month, Strategic is the honest fit. The starting prices are the floor. A very busy account list moves the number, and I tell you the new number before you say yes. Catch-up months, if you have them, stay on their own quote beside the plan.",
        )
        + section(
            "What each plan is for",
            paras(
                "Essential keeps the month current. I categorize transactions, reconcile the bank and the cards, and send a profit and loss and a balance sheet. The aim is the 15th of the next month. It is the right plan when the books are straightforward and you want them reliable.",
                "Core is Essential, plus a quarterly profit and expense summary, a year-to-date comparison, and priority support. Owners pick Core when they want to see the year forming, and when they want a faster reply in a busy month.",
                "Strategic is Core, plus custom reports, accrual accounting, payroll journal entries, loan tracking, and a monthly call. Your payroll company still runs payroll. I record the entries. The call is where you and I walk the numbers instead of trading emails about them.",
            ),
        )
        + section(
            "Side by side",
            """<div class="table-wrap"><table>
<thead><tr><th></th><th>Essential</th><th>Core</th><th>Strategic</th></tr></thead>
<tbody>
<tr><td>Starts at</td><td>$349 a month</td><td>$599 a month</td><td>$1,499 a month</td></tr>
<tr><td>Categorized, reconciled month</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Profit and loss and balance sheet</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Quarterly and year-to-date view</td><td></td><td>Yes</td><td>Yes</td></tr>
<tr><td>Custom reports, accrual, payroll entries, loan tracking, monthly call</td><td></td><td></td><td>Yes</td></tr>
</tbody></table></div>""",
        )
        + paras(
            "Cleanup of older months, a QuickBooks Online setup, and training are separate quotes. You keep your QuickBooks Online subscription with Intuit. I hand your CPA clean, reconciled books. They file the return.",
            'The day-to-day of the close is on <a href="/monthly-bookkeeping/">monthly bookkeeping</a>. If the file is behind, read <a href="/cleanup-catch-up/">cleanup and catch-up</a> before you pick a plan. Questions about the first month are on the <a href="/bookkeeping-faq/">FAQ</a>.',
        )
    )


def services_hub():
    return (
        paras(
            "I can keep the month closed, rebuild the months that fell behind, or set up QuickBooks Online and teach you the parts you want to run. You work with me. I quote the work before I start, from the accounts, the volume, and the reports you need.",
            "Monthly plans start at $349. Love your first month of books, or it's free. Catch-up and training are priced from the project. The six pages below are the ways that work usually shows up. If you are unsure which one fits, say what is happening in the business and I will tell you where I would start.",
            "Monthly bookkeeping is the ongoing close: categories, reconciled accounts, and reports aimed at the 15th. Cleanup and catch-up is the same care applied to months that are still open, quoted from the size of that pile. QuickBooks Online setup builds the file and teaches the screens you want to keep. The subscription stays between you and Intuit.",
            "Financial statements is a plain-language guide to the two reports I send. CPA-ready books is the handoff: I give your preparer closed months, and they file the return. Loan-ready financials is the same closed months, arranged as the package a lender listed. You can start on any one of them. Most owners who begin with a catch-up or a setup move to a monthly plan once the file agrees with the bank. The plan you land on is a conversation about your actual month, and the three starting prices live on the pricing page. Call or write if you want help choosing.",
        )
        + paras(
            'A full comparison of Essential, Core, and Strategic is on <a href="/pricing/">pricing</a>. The records that make a first month easier are on <a href="/getting-started/">getting started</a>. The questions people ask first are on the <a href="/bookkeeping-faq/">FAQ</a>.',
        )
    )


def getting_started():
    return (
        paras(
            "You can book the first call with almost nothing in hand. Tell me the business, roughly how many accounts you have, whether the books are current, and what you want help with. I will reply with the next step and a quote. The checklist below is for the moment after that yes, when it is time to hand me the file.",
            "Leave account numbers and statements out of the public form. I will show you how to share them once the scope is set. A missing statement slows one account. The rest of the month can still move.",
        )
        + checklist(
            "The handoff, in order",
            [
                "<strong>Account list.</strong> Checking, savings, credit cards, loans, and processors. Mention accounts you closed during the period.",
                "<strong>The last finished month.</strong> If you are unsure, say so. I can help you find a starting balance.",
                "<strong>Statements or feeds.</strong> For the months in scope, including opening and closing balances.",
                "<strong>The file, if one exists.</strong> QuickBooks Online, a spreadsheet, or the name of the app you invoice from.",
                "<strong>Payroll and loans.</strong> Reports from your payroll company, and statements for balances you want tracked.",
                "<strong>Owner activity.</strong> Draws, contributions, and personal costs you already know are on a business card.",
                "<strong>Deadlines.</strong> A CPA date, a lender date, or the month you want to be current.",
            ],
        )
        + paras(
            "Once those pieces are in, I categorize, reconcile, and send reports. The aim for a monthly plan is the 15th of the next month. A catch-up follows the schedule in the quote.",
            "Here is what those first weeks feel like. I connect or upload the accounts, I code a sample of the month, and I send you the transactions I could not name from the bank description alone. A one-line reply is enough: 'that was a draw,' 'that was a part for the Johnson job,' 'that was personal.' I finish the month from those answers and send the profit and loss and the balance sheet.",
            "You stay in the loop without living in the file. Some owners want a weekly look. Most want the 15th package and a way to ask about one number. Tell me which of those you prefer on the call. Essential and Core deliver the reports in writing. Strategic adds the monthly walkthrough. Either way, the person who closed the month is the person who answers. If a week is unusually busy, send the note when you can. The close waits on that answer and then it goes out. You can also forward a preparer's checklist or a lender's list with the same handoff, and I will fold that date into the scope I quote before any work starts at all.",
            'Read <a href="/monthly-bookkeeping/">monthly bookkeeping</a> if the ongoing close is the job, or <a href="/cleanup-catch-up/">cleanup and catch-up</a> if the open months are the job. Prices are on <a href="/pricing/">pricing</a>.',
        )
    )


def contact():
    return paras(
        "Tell me the business, the town, whether the books are current, and the help you want. I reply within one business day. You can also call (805) 419-3451, email jack@glenhold.com, or book a free call. I am available Monday through Saturday, 6am to 6pm Pacific.",
        "Leave bank logins, account numbers, and financial documents out of this form. You work with me, and the detailed file-sharing starts after the scope is clear.",
    )


def privacy():
    return (
        section(
            "Information you send",
            paras(
                "The inquiry form asks for your name, email address, optional phone number, the service you are interested in, and a message. I use this information to reply and to talk with you about the work. Please leave bank logins, account numbers, tax documents, and other sensitive financial records out of this form.",
                "Form submissions are processed through Formspree. Booking a call takes you to Google's scheduling service. The website also loads fonts from Google Fonts. Those providers handle information under their own policies.",
            ),
        )
        + section(
            "Website measurement",
            paras(
                "This website loads Google Ads and OpenAI Ads measurement tags to measure visits and actions, including inquiry submissions and clicks on booking or telephone links. The form-submission code leaves your name, email address, phone number, and message out of the conversion events sent to those tags.",
                "Third-party services may process technical information, such as browser, device, network, or advertising identifiers, under their own policies. This website also stores campaign parameters in browser session storage to help identify the source of an inquiry.",
            ),
        )
        + section(
            "Questions",
            paras(
                'Email <a href="mailto:jack@glenhold.com">jack@glenhold.com</a> with questions about this notice or about information you have sent through the site.',
                "Website forms and advertising measurement are separate from the way client bookkeeping records are exchanged once work is underway.",
            ),
        )
    )


def resources():
    return section(
        "Start here",
        "",
    )


def industry_intro():
    return paras(
        "I work with local small businesses of every kind. The five guides below are the ones with the most particular bookkeeping, because the money moves in a distinct way. Contractors, home services, medical and dental practices, professional firms, and online sellers each get a full page.",
        "Real estate, nonprofits, retail shops, salons, fitness studios, and auto repair shops are welcome too. Tell me how you get paid and what you want the reports to show. I will quote the same kinds of help: a monthly close, a catch-up, or QuickBooks Online setup. You work with me either way.",
    )


MONTHLY_FAQS = [
    ("When will I get my reports?", "I aim for the 15th of the following month. If a statement or a question is still outstanding, I tell you what is missing and send the reports as soon as I have it."),
    ("What is included each month?", "I categorize transactions, reconcile bank and credit cards, and send a profit and loss and a balance sheet. Core and Strategic add the comparisons, reports, and call described on the pricing page."),
    ("Does the guarantee cover catch-up?", "Love your first month of books, or it's free. That covers monthly bookkeeping. Catch-up and training are quoted on their own."),
    ("Do you run payroll?", "Your payroll company runs payroll. On the Strategic plan I record the payroll journal entries."),
    ("Who does the work?", "You work with me. I categorize the month and I answer the question about a number that looks off."),
]

CLEANUP_FAQS = [
    ("How do you price a catch-up?", "From the number of months, the accounts, and how complete the records are. I quote it before I start."),
    ("Can the monthly plan start immediately after?", "Yes. The plan starts from the reconciled balance at the end of the catch-up."),
    ("What if a statement is missing?", "I tell you which account it blocks. The rest of the period can still be categorized."),
    ("Will my CPA accept this?", "I hand your CPA clean, reconciled books for the period in scope. They file the return."),
    ("Is there a standard timeline?", "It follows the size of the pile and the deadline you have. I put the timing in the quote."),
]

QBO_FAQS = [
    ("Are you a ProAdvisor?", "Yes. I am a Certified QuickBooks ProAdvisor."),
    ("Is the QuickBooks subscription included?", "You keep your own QuickBooks Online subscription with Intuit. My fee covers setup, training, and bookkeeping."),
    ("Can you train me and still close the month?", "Yes. Tell me which tasks you want to keep. I teach those and I can reconcile the rest."),
    ("What if my current file does not match the bank?", "That is a cleanup. I quote the open months, then setup and a monthly rhythm can follow."),
    ("Do you work in QuickBooks Online?", "Yes. QuickBooks Online is where I set up the file and keep the books."),
]

STATEMENT_FAQS = [
    ("Which reports do I get every month?", "A profit and loss and a balance sheet. Core adds a quarterly summary and a year-to-date comparison."),
    ("What if cash on the balance sheet looks wrong?", "It should match the reconciled bank. Reply with the line and I will trace it."),
    ("Where do owner draws show up?", "On the balance sheet, as money you took out. They stay off the profit and loss."),
    ("Can I share these with my CPA?", "Yes. I hand your CPA clean, reconciled books. They file the return."),
    ("When do they arrive?", "I aim for the 15th of the next month, once statements and your answers are in."),
]

CPA_FAQS = [
    ("Do you file the tax return?", "Your CPA files the return. I hand them clean, reconciled books."),
    ("What does clean mean?", "Reconciled accounts, a profit and loss, a balance sheet, and owner activity labeled for the period they asked for."),
    ("Can you work from their checklist?", "Yes. Send me the list and the date. I will quote the months that are still open."),
    ("How is sales tax shown?", "Tax you collected sits as a liability. I look up your rate. Your preparer files the return."),
    ("What about the California $800 LLC tax?", "Most LLCs owe it each year. I record the payment. Your CPA files the form and confirms the current rule."),
]

LOAN_FAQS = [
    ("What do you send a lender?", "The reports they asked for, built from reconciled months: usually a profit and loss, a balance sheet, and the period they named."),
    ("Can you include a debt schedule?", "On the Strategic plan I track balances and payments. Send me the schedule they requested and I will quote anything beyond that."),
    ("What if the months they want are unclosed?", "I quote a catch-up through their date, then assemble the package."),
    ("Will you talk with the lender?", "I am glad to walk you through the reports first. You can share them, and you can loop me in on a question about a line."),
    ("Who closes the months?", "You work with me. The package comes from the same close as the monthly work."),
]

ABOUT_FAQS = [
    ("Who will I work with?", "You work with me, from the first call through every close."),
    ("Where are you based?", "I live in Simi Valley and I work with owners throughout Ventura County and nearby Los Angeles communities."),
    ("What is your background?", "I have been in accounting since 2021, including audit work at PwC, and I am a Certified QuickBooks ProAdvisor."),
    ("How do I reach you?", "Call (805) 419-3451, email jack@glenhold.com, or book a call. I reply within one business day."),
    ("Where are the videos?", "On YouTube at @BookkeepingBizBlueprint."),
]
