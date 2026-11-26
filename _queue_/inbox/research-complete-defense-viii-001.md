---
unit: research-complete-defense-viii-001
regular: research
activity: research-queue
segment: 2
priority: 1
created_at: 2026-11-26T05:03:41Z
expires_at: 2026-11-29T18:40:00Z
planned_for:
not_before: 2026-11-29T12:39:00Z
window: complete defense viii when it finishes (phone restarted the lab)
est_minutes: 6
serves: PL-04
chain_id: complete-defense-viii
chain_seq: 1
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

## Brief (planner, RESEARCH COMPLETE: Defense VIII, PL-04)

serves: PL-04

Facts [M] (builders read 04:54Z on 11-26, record building-queues/0453: the phone restarted both labs): Defense VIII ends about 2026-11-29T12:38:45Z. DISPATCH ONLY WHEN NAMED. FIRST read both labs: if the Defense VIII entry shows more than 5 minutes left, write the time left and RELEASE this unit unrun (`queue.py release --unit <this unit>`). Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. The route to Defense VIII's tree is UNREAD [G]: read the lab entry first; if the panel offers no Complete button and the tree route is not shown by a label, close 'route unverified' with the frame and STOP; never (603,925).
1. Re-read coin, food, iron and oil in a fresh frame: write them.
2. If finished: press COMPLETE on Defense VIII; write Total Power before and after.
3. Read both labs again; write each timer to the second. Start NOTHING here: the next node is the Strategist's, named by the Coordinator; an idle lab is reported, not filled. Never Finish Now, never a speed-up here, no diamond or item spend.
4. H112 (read only): before and after any research start write the oil counter (income 1.5K an hour) with the UTC time; scroll a running node's panel PAST THE FOOD ROW to its LAST row once and write whether an oil row shows.
FRONT (Steer A 21:11Z): at the start, if `lsappinfo front` is not LastWar, record it, run the standing front script, record again; still not LastWar: stop, release, tell the Coordinator. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for a taken Complete tap or a verified nothing-to-do (`--state-change no` plus a `state_read:` line naming the lab timers read); else PARTIAL.
Cost cap, stated: 0.50 USD.
