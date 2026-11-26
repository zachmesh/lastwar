---
unit: research-complete-oil-output-i-001
regular: research
activity: research-queue
segment: 2
priority: 1
created_at: 2026-11-24T17:40:10Z
expires_at: 2026-11-28T05:20:00Z
planned_for:
not_before: 2026-11-27T23:20:22Z
window: complete oil output i when it finishes
est_minutes: 6
serves: PL-04
chain_id: complete-oil-output-i
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-04

## Brief (definition pointer, from the roster)

This unit is the regular `research`: Research queue - press Complete on finished research and record the power change; never start new research without a standing owner direction. Its definition is the activity folder `_activities_/research-queue/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, RESEARCH COMPLETE: Oil Output I in lab 2, PL-04)

serves: PL-04

Facts [M] (builders read 04:54Z): Oil Output I in lab 2 ends about 2026-11-27T23:20:07Z. DISPATCH ONLY WHEN NAMED. FIRST read both labs: if the Oil Output I entry shows more than 5 minutes left, write the time left and RELEASE this unit unrun (`queue.py release --unit <this unit>`). Routes and stop reasons, with the Age of Oil tree route (the running node's icon at (456,925), never (603,925)): `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.
1. Re-read coin, food, iron and oil in a fresh frame: write them.
2. If finished: press COMPLETE on Oil Output I; write Total Power before and after.
3. Read both labs again; write each timer to the second. Start NOTHING here: the next node is the Strategist's, named by the Coordinator; an idle lab is reported, not filled. Never Finish Now, never a speed-up here, no diamond or item spend.
4. H112 (read only): before and after any research start write the oil counter (income 1.5K an hour) with the UTC time; scroll a running node's panel PAST THE FOOD ROW to its LAST row once and write whether an oil row shows.
FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken Complete tap or a verified nothing-to-do (`--state-change no` plus a `state_read:` line naming the lab timers read); else PARTIAL.
Cost cap, stated: 0.50 USD.
