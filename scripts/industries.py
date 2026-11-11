"""Practical preparation notes for prospective clients across industries."""

INDUSTRIES = [{'slug': 'contractors',
  'name': 'Contractors and trades',
  'intro': 'Keep project spending, business expenses, and owner transactions organized.',
  'paragraphs': ['Materials, subcontractor payments, fuel, and customer deposits can move through several '
                 'accounts during a busy month. Clear categories help you see what the business earned and where '
                 'the money went.',
                 'Glenhold reconciles your bank and credit card accounts and prepares monthly financial reports. '
                 'If you want reporting by project, bring an example of the report you need to the first call so '
                 'we can discuss whether the work is a fit.'],
  'points': ['Provide a list of all business accounts, including cards used for materials.',
             'Flag transfers and money the owner put into or took out of the business.',
             'Share any reporting requests from your tax preparer.']},
 {'slug': 'restaurants',
  'name': 'Restaurants and food businesses',
  'intro': 'Make sense of sales reports, card deposits, and the costs of running your business.',
  'paragraphs': ['A bank deposit may combine sales, refunds, tips, and processing fees. Your point-of-sale '
                 'reports provide the detail behind that deposit. Keeping those reports with your statements '
                 'makes reconciliation more reliable.',
                 'Glenhold can help organize the bookkeeping and produce a profit and loss statement and balance '
                 'sheet. During the first call, explain how you collect payments, which reports you can export, '
                 'and whether you need help with the current month or a backlog.'],
  'points': ['Identify your point-of-sale system and payment processors.',
             'Gather operating account and credit card statements.',
             'Discuss which expense categories you want to see in your reports.']},
 {'slug': 'medical-dental',
  'name': 'Medical and dental practices',
  'intro': 'Understand the business finances behind your practice.',
  'paragraphs': ['Rent, supplies, equipment payments, insurance deposits, and owner transactions all affect the '
                 'practice’s financial reports. Organized books give you and your tax preparer a clearer view of '
                 'those finances.',
                 'Glenhold’s work focuses on business bookkeeping: categorizing transactions, reconciling '
                 'accounts, and preparing financial statements. Tell Jack which accounting and payment systems '
                 'you use. Please keep patient records and other sensitive information out of the introductory '
                 'contact form.'],
  'points': ['List the practice’s bank, credit card, and financing accounts.',
             'Identify the financial reports available from your existing systems.',
             'Discuss the bookkeeping information you need without sending patient records.']},
 {'slug': 'real-estate',
  'name': 'Real estate businesses',
  'intro': 'Keep your operating income, expenses, and account balances organized.',
  'paragraphs': ['Commission income, marketing, dues, software, and property-related expenses can make it '
                 'difficult to see the performance of the business. A consistent chart of accounts and regular '
                 'reconciliation help keep the records useful.',
                 'Explain whether you work as an agent, own rental property, or operate another real estate '
                 'business. If client funds or trust accounts are involved, mention that during the first '
                 'conversation so the requirements can be assessed before a scope is agreed.'],
  'points': ['Describe the business and the accounts you need help with.',
             'Separate the company’s operating activity from owner transactions.',
             'Bring any property-level reporting requirements to the first call.']},
 {'slug': 'ecommerce',
  'name': 'Ecommerce and online sellers',
  'intro': 'Connect marketplace payouts with the sales and fees behind them.',
  'paragraphs': ['Marketplace and payment-processor payouts often arrive after fees and refunds have been '
                 'deducted. Looking only at the bank deposit can hide the detail of your revenue and expenses. '
                 'Platform reports help explain the amounts received.',
                 'Tell Jack which platforms you sell through, the reports you can export, and whether you hold '
                 'inventory. Those details help establish the bookkeeping work and reporting you need before a '
                 'quote is prepared.'],
  'points': ['List your stores, marketplaces, and payment processors.',
             'Have payout summaries and bank statements available.',
             'Discuss inventory and reporting needs before agreeing on scope.']},
 {'slug': 'nonprofits',
  'name': 'Small nonprofits',
  'intro': 'Give your board and tax preparer a clearer view of the organization’s finances.',
  'paragraphs': ['A nonprofit needs organized records of money received and spent, along with reconciled '
                 'accounts. Reports should be easy for the people overseeing the organization to understand.',
                 'Explain your reporting requirements before work begins, including any program categories, '
                 'restricted contributions, or requests from a grant provider. Jack can assess the bookkeeping '
                 'scope and whether Glenhold is the right fit.'],
  'points': ['Identify who reviews and approves the bookkeeping.',
             'Gather account statements and existing financial reports.',
             'Share board, grant, and tax-preparer reporting requirements up front.']},
 {'slug': 'professional-services',
  'name': 'Professional services',
  'intro': 'Spend less time sorting transactions and more time running your business.',
  'paragraphs': ['Consultants, agencies, designers, and other service firms often have a mix of client payments, '
                 'software subscriptions, professional fees, and owner transactions. Consistent bookkeeping makes '
                 'it easier to understand income, expenses, and profit over time.',
                 'Glenhold provides monthly bookkeeping, cleanup, and QuickBooks Online support. Tell Jack how '
                 'you bill clients and which reports you need. Retainers, client funds, or other special '
                 'accounting requirements should be discussed before the scope is agreed.'],
  'points': ['Identify your business bank and credit card accounts.',
             'Share the reports you already use to review performance.',
             'Mention retainers or other transactions that need particular attention.']},
 {'slug': 'retail',
  'name': 'Retail shops',
  'intro': 'Get clear financial reports from your sales activity and operating expenses.',
  'paragraphs': ['Register totals, card deposits, refunds, and processing fees do not always line up on the same '
                 'day. Sales reports and bank statements help explain those differences and support a reliable '
                 'monthly reconciliation.',
                 'Tell Jack about your point-of-sale system, payment processors, and inventory records. The '
                 'bookkeeping scope should reflect the information you have and the reports you need to run the '
                 'shop.'],
  'points': ['Identify your sales and payment systems.',
             'Keep sales summaries alongside bank and credit card statements.',
             'Discuss inventory reporting before choosing a monthly plan.']},
 {'slug': 'home-services',
  'name': 'Home service businesses',
  'intro': 'Organize the bookkeeping while you focus on your customers.',
  'paragraphs': ['Cleaning companies, landscapers, pool services, and other local service businesses may use '
                 'several payment methods and cards. Keeping receipts, customer deposits, and owner transactions '
                 'organized helps prevent gaps in the books.',
                 'Glenhold helps with transaction categorization, reconciliation, monthly reports, and catch-up '
                 'work. The first conversation is a chance to explain how you get paid, which accounts you use, '
                 'and what you want to hand off.'],
  'points': ['List every account used for the business.',
             'Flag business expenses paid personally.',
             'Describe any seasonal changes in your transaction volume.']},
 {'slug': 'salons',
  'name': 'Salons and personal care businesses',
  'intro': 'See your business income and expenses more clearly each month.',
  'paragraphs': ['Services, product sales, tips, and rental arrangements can create different streams of activity '
                 'in a salon’s records. Reports from your existing systems help explain what reached the bank and '
                 'how it should be organized.',
                 'Tell Jack how your business operates, whether you work independently or manage a location, and '
                 'what bookkeeping you already have in place. The work can then be scoped around your accounts '
                 'and reporting needs.'],
  'points': ['Identify the booking and payment systems you use.',
             'Gather bank and card statements and available sales reports.',
             'Explain any rental arrangements or other special transactions.']},
 {'slug': 'fitness',
  'name': 'Fitness and wellness businesses',
  'intro': 'Keep memberships, business expenses, and financial reports organized.',
  'paragraphs': ['Memberships, class packages, individual sessions, and retail sales can all appear in the same '
                 'payment account. Consistent records help connect those receipts with your operating costs and '
                 'account balances.',
                 'Bring your reporting goals to the first call. If advance payments or class packages need '
                 'special treatment, discuss that with Jack and your tax preparer before choosing the bookkeeping '
                 'scope.'],
  'points': ['Identify membership, booking, and payment systems.',
             'List operating accounts, cards, and equipment loans.',
             'Describe the reports you need to review the business.']},
 {'slug': 'auto-repair',
  'name': 'Auto repair and service businesses',
  'intro': 'Keep operating expenses and sales activity connected to your financial reports.',
  'paragraphs': ['Shop reports can contain details about labor, parts, refunds, and fees that a bank deposit does '
                 'not show. Keeping those reports with account statements helps support accurate categorization '
                 'and reconciliation.',
                 'Tell Jack which shop-management and payment systems you use, whether inventory reporting is '
                 'needed, and how current the books are. Glenhold can assess the work before proposing a monthly '
                 'plan or cleanup project.'],
  'points': ['Identify the reports available from your shop system.',
             'Gather statements for the business bank and credit card accounts.',
             'Discuss inventory and financing records during the assessment.']}]
