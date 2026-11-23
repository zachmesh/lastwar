---
title: Activity Playbook Card
created: 2026-11-23T09:18:21Z
modified: 2026-11-23T09:18:21Z
level: L2
version: 0.1.0
description: Each activity INDEX is a take-away card of 300 words or fewer with fixed headings, rules cited to records and in-place rewrites
status: unverified
grounded_in:
  - source: owner decision OD-20261123-15 - activity INDEX pages become playbook cards (_records_/retro/owner-decisions-log/od-20261123-15.md)
  - source: improvement IMP-20261123-14 measured by Steer B - 267 digest rules all unverified, 332 of their citations point at run articles (_records_/retro/improvements.md)
---

# Activity playbook card

Each `_activities_/<activity>/INDEX.md` is a playbook card: what an operator needs in one minute, 300 words or fewer (OD-20261123-15). Detail stays in articles; the card does not list them. Start from [the template](activity-card-template.md).

## Shape

Fixed headings, in this order, so tools can read them:

1. `Goal` - one sentence.
2. `Route` - the verified route, 8 steps at most.
3. `Rules` - the 5 that matter: id R1 to R5, the rule, its status (`unverified`, `tested`, `verified` or `refuted`), the date, one record path.
4. `Failures` - the 3 commonest, each with its fix and a record path.
5. `Open questions` - 3, each with the test that settles it and the role that runs it.
6. `Numbers` - one line the coach generates from the records; never typed by hand.
7. `Links` - 5 at most: the rule digest or catalog, the newest record, the next article to read.

## Rules of the card

- A rule cites a record under `_records_/`, never a run note or run article. No record, no rule: it goes to Open questions.
- A superseded or refuted rule is rewritten in place and keeps its id; the history is in git. No Errata or changelog section grows on a card; `version` and `modified` move.
- A status changes only when a record or a test moves it; the date is that record's date.
- 5, 3 and 3 are ceilings: a new rule replaces the weakest.

## Roles, weekly loop

The scribe edits cards. The coach owns quality and the numbers line and names the 3 worst cards each week. The researcher turns an unverified rule into a falsification test. The operator records `rules_used`, `rule_failed` and `gap` in unit stats. The planner stages the work. The owner decides policy conflicts. An improvement closes only when its metric moves.
