---
title: Word budget review 2026-11-26 12:00Z
created: 2026-11-26T04:05:00-08:00
modified: 2026-11-26T04:05:00-08:00
level: L3
version: 0.1.0
description: The daily word-budget count, the new documents over 500 words, the hooks check and the precedent-phrase gaps
status: done
activity: team-operations
run_id: team-operations-2026-11-26-1203-word-budget-review
trigger: schedule-e1887d97-ba2d-4f9a-b466-bf1838b12813
started_at: 2026-11-26T04:00:00-08:00
finished_at: 2026-11-26T04:05:00-08:00
duration_seconds: 300
verified: the counts are the lint gate watch output of 2026-11-26T12:01:31Z on local main (head 5ca26521, the 12Z delivery branch tip)
---

# Word budget review, 11:55Z

- Documents 12,237; over 300 words 6,166; at or over 500 words 3,407 (3,405 legacy, 2 new). New gate errors against the anchor: 0.
- By top folder at or over 500: records 3,407 (legacy 3,405, new 2); every other folder 0.
- The two new documents over 500 words are both exempt through exempt.txt: the day index of this run folder (56,502 words; owner seat the Coordinator, which only appends one line per record) and the strategy index of this run folder (520 words; owner seat the Strategist).
- Hooks: core.hooksPath is _tools_/lint-gate/hooks (pre-commit and pre-merge-commit present); the word-budget enforcement page is present; the Integrator's landing check passed on every branch delivered today.
- Growth over 20 percent since 11-23 08:27Z: the day index (+109 percent), the unit template (486 words, under the gate), the Strategist, Integrator, Scribe and operator handovers (all under 500), the landings page, the improvements register and the owner-decisions register.

## Precedent gaps (standing check)

Of 319 operator records from the last three days, three carry a precedent phrase.

- Training 11-24 (training/0351, a pistol press collected a finished batch of 274 units): the training units and digest carry it. No gap.
- Donations (alliance-donations/1441): a continuation precedent (the 1002 and 1010 part-two runs). Brief check for the Planner: whether the donations unit carries the continuation rule when the count is live and the panel stays open.
- Scout 11-26 (perception-scout/0420, the takeover retry after the killall approval): the takeover units carry it through the front clause.
