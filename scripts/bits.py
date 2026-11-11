"""Small HTML helpers for the rewrite. Copy stays in the data files."""

from __future__ import annotations

TABLE = """<div class="table-wrap"><table>
<thead><tr><th>Plan</th><th>Starts at</th><th>What you get</th></tr></thead>
<tbody>
<tr><td>Essential</td><td>$349 a month</td><td>Categorized transactions, reconciled bank and card accounts, and a monthly profit and loss and balance sheet</td></tr>
<tr><td>Core</td><td>$599 a month</td><td>Essential, plus a quarterly summary, a year-to-date comparison, and priority support</td></tr>
<tr><td>Strategic</td><td>$1,499 a month</td><td>Core, plus custom reports, accrual, payroll journal entries, loan tracking, and a monthly call</td></tr>
</tbody></table></div>"""

HELP_TABLE = """<div class="table-wrap"><table>
<thead><tr><th>If this is you</th><th>Where I start</th><th>What you leave with</th></tr></thead>
<tbody>
<tr><td>The current month is the job</td><td><a href="/monthly-bookkeeping/">Monthly bookkeeping</a></td><td>A close I can repeat, aimed at the 15th</td></tr>
<tr><td>Older months are still open</td><td><a href="/cleanup-catch-up/">Cleanup and catch-up</a></td><td>Those months recorded, reconciled, and reported</td></tr>
<tr><td>You want the file, and the skill, in your hands</td><td><a href="/quickbooks-online/">QuickBooks Online setup and training</a></td><td>A chart of accounts and a routine you can run</td></tr>
</tbody></table></div>"""


def paras(*parts: str) -> str:
    return "".join(f"<p>{part}</p>" for part in parts)


def section(title: str, inner: str, anchor: str | None = None) -> str:
    attr = f' id="{anchor}"' if anchor else ""
    return f"<section{attr}><h2>{title}</h2>{inner}</section>"


def steps(title: str, items: list[tuple[str, str]]) -> str:
    lis = "".join(f"<li><strong>{title_}.</strong> {body}</li>" for title_, body in items)
    return section(title, f"<ol>{lis}</ol>")


def checklist(title: str, items: list[str]) -> str:
    lis = "".join(f"<li>{item}</li>" for item in items)
    return section(title, f"<ul>{lis}</ul>")


def plans(intro: str) -> str:
    return section("Monthly plans", f"<p>{intro}</p>{TABLE}")


def help_table(intro: str) -> str:
    return section("Which kind of help", f"<p>{intro}</p>{HELP_TABLE}")
