---
unit: building-queues-growth-convert-2026-11-24-003
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T11:27:56Z
expires_at: 2026-11-24T10:50:00Z
planned_for:
not_before: 2026-11-24T09:22:00Z
window: bounded construction speed ups on the three drill ground upgrades inside the Tuesday window
est_minutes: 15
serves: PL-08
chain_id: growth-convert-2026-11-24
chain_seq: 3
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: capacity source: bounded speed-ups on the Drill Ground upgrades (construction items first)

## Brief (planner, bounded speed-ups on the three Drill Ground upgrades, decision 2603 and Steer A's amendments)

serves: PL-08

Third unit, after units 001 and 002 have started the upgrades. Decision `_records_/2026-11-22/team-operations/2603-first-builder-decision.md`; procedure and the item list `_records_/2026-11-22/queue-planning/2541-conversion-and-speedup-sheet.md`; tap points `_records_/2026-11-22/queue-planning/2540-drill-ground-sheet.md`. Never touch the owner's queue; never Finish Now, diamonds or money; no Obtain.

1. Read the Duel screen first, the authority: 2026-11-24 should be Tuesday, Base Expansion, until 2026-11-25T02:00Z. Record the theme and the time left. If it is not that theme, stop and tell.
2. Hammer icon: read the builder queue and the three Drill Ground upgrades by their tag text (Lv.26 to 27, Lv.27 to 28, Lv.28 to 29) with the time left each. If one has not started, skip it.
3. For each started upgrade, open its Speed Up panel and read it before pressing. Use CONSTRUCTION items first, the LARGE ones first (8h x10, 1h x26, then 5m); an item's quantity may default to its full stock, so reduce it before pressing. Stop at 10,000 minutes on that upgrade and 30,000 in all (weekly cap 35,000). Write the minutes used after every press, and nothing is pressed if the number cannot be read. The general items stay in reserve.
4. Record per upgrade: tag text, minutes used by kind, time left before and after, the duel score before and after if shown, and Total Power.

Up to three runs, 10 steps each. Do not enqueue a chain successor.
Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Quiet-window margin: this start (09:21Z trigger) is 56 min after the daily 08:00-08:25Z window; see `_records_/2026-11-22/queue-planning/2830-quiet-window-margins.md`.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
