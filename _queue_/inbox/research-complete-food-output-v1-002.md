---
unit: research-complete-food-output-v1-002
regular: research
activity: research-queue
segment: 2
priority: 1
created_at: 2026-11-26T04:09:24Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T04:12:00Z
window: complete food output v lv.1, finished 11-25 19:39z, complete tap waits
est_minutes: 6
serves: PL-04
chain_id: complete-food-output-v1
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# research

Serves: PL-04

## Brief (definition pointer, from the roster)

This unit is the regular `research`: Research queue - press Complete on finished research and record the power change; never start new research without a standing owner direction. Its definition is the activity folder `_activities_/research-queue/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, RESEARCH COMPLETE: Food Output V Lv.1 in lab 1, PL-04)

serves: PL-04

Facts [M]: the Food Output V Lv.1 node ended 2026-11-25T19:39:08Z and its Complete tap has waited since; the lab is idle. DISPATCH ONLY WHEN NAMED. FIRST read both labs (tag text, timers to the second): if the Food Output V Lv.1 entry shows more than 5 minutes left, write the time left and RELEASE this unit unrun (`queue.py release --unit <this unit>`). Routes and stop reasons, with the Age of Oil tree route (the running node's icon at (456,925), never (603,925)): `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. A TIPS dialog about another device: STOP, report.
1. Re-read coin, food, iron and oil in a fresh frame (the account moves when the owner's phone moves): write them.
2. If finished: press COMPLETE on Food Output V Lv.1; write Total Power before and after.
3. Read both labs again; write each timer to the second. Start NOTHING here: the next node is the Strategist's, named by the Coordinator; an idle lab is reported, not filled. Never Finish Now, never a speed-up here, no diamond or item spend.
Up to two runs. FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken Complete tap or a verified nothing-to-do (`--state-change no` plus a `state_read:` line naming the lab timers read); else PARTIAL.
Cost cap, stated: 0.50 USD.
