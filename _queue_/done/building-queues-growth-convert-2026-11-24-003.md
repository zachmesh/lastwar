---
unit: building-queues-growth-convert-2026-11-24-003
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T11:27:56Z
expires_at: 2026-11-24T04:00:00Z
planned_for:
not_before: 2026-11-24T02:30:00Z
window: bounded construction speed ups on the three drill ground upgrades inside the Tuesday window
est_minutes: 15
serves: PL-08
chain_id: growth-convert-2026-11-24
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T03:01:00Z
lease_until: 2026-11-24T03:21:00Z
result:
  status: done
  started_at: 2026-11-24T03:01:00Z
  finished_at: 2026-11-24T03:28:34Z
  duration_seconds: 1654
  executor: operator
  summary: Bounded speed-ups on the three Drill Grounds: 9,970, 9,960 and 9,510 minutes (29,440 in all); ends moved to 2026-11-26T21:10:37Z, 2026-11-30T22:21:48Z and 2026-12-05T11:59:18Z; the Duel personal total rose from 126,000 to 4,542,000 (150 points a minute); Instant Speed-up and Finish Now never pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0301-queue-run.md and 0301-queue-run.csv; run 20261124T030135Z-1c75f6
  follow_up: 29,440 of the 30,000 minutes used; 5m stock 24,069 and 1m 19,065 left; the Lv.26 ground ends 2026-11-26T21:10:37Z; the Oil Well Lv.22 ends 2026-11-24T08:01:46Z (quiet window); cost note: 2.087 USD against 0.90
  stats:
    target: bounded speed-ups, 10,000 minutes per upgrade and 30,000 in all, construction items first, never Finish Now
    achieved: 29,440 minutes, all three under 10,000, no Finish Now
    resources_gained: 29,440 construction speed-up minutes: 8h x10, 1h x26, 5m x4,616
    points: 0
    costs: none spent; model 2.087 USD
    verified: yes
    run_id: 20261124T030135Z-1c75f6
    run_steps: 150
    actions_done: 140
    actions_refused: 0
    cost_usd: 2.087
    device_takeovers: 0
    minutes_lv26: 9970
    minutes_lv27: 9960
    minutes_lv28: 9510
    minutes_total: 29440
    duel_before: 126000
    duel_after: 4542000
    rules_used: 1
  stats_missing: []
  stats_warnings: [duration exceeds 15-minute unit cap]
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

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
Quiet-window margin: this start (02:05Z, the Base Expansion duel day) is 5 h 55 min before the daily 08:00-08:25Z window; see `_records_/2026-11-22/queue-planning/2830-quiet-window-margins.md`.
Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
