---
unit: research-complete-food-output-v1-001
regular: research
activity: research-queue
segment: 2
priority: 1
created_at: 2026-11-24T17:40:09Z
expires_at: 2026-11-25T21:39:07Z
planned_for:
not_before: 2026-11-25T19:39:22Z
window: complete food output v lv.1 when it finishes
est_minutes: 6
serves: PL-04
chain_id: complete-food-output-v1
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

## Brief (planner, RESEARCH COMPLETE: Food Output V Lv.1 in lab 1, PL-04)

serves: PL-04

Facts [M] (record research-queue/1734, 17:35:35Z, after another actor changed the labs): Food Output V Lv.1 in lab 1 ends about 2026-11-25T19:39:07Z; the exact end comes from the next research read. DISPATCH ONLY WHEN NAMED. FIRST read both labs (tag text, timers to the second): if the Food Output V Lv.1 entry shows more than 5 minutes left, write the time left and RELEASE this unit unrun (`queue.py release --unit <this unit>`). Routes and stop reasons, with the Age of Oil tree route (the running node's icon at (456,925), never (603,925)): `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. A TIPS dialog about another device: STOP, report.
1. Re-read coin, food, iron and oil in a fresh frame (the account moves when the owner's phone moves): write them.
2. If finished: press COMPLETE on Food Output V Lv.1; write Total Power before and after.
3. Read both labs again; write each timer to the second. Start NOTHING here: the next node is the Strategist's, named by the Coordinator; an idle lab is reported, not filled. Never Finish Now, never a speed-up here, no diamond or item spend.
Up to two runs. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.50 USD.
