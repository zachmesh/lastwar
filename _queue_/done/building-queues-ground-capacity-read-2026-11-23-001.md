---
unit: building-queues-ground-capacity-read-2026-11-23-001
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T20:04:10Z
expires_at: 2026-11-23T22:15:00Z
planned_for:
not_before: 2026-11-23T20:15:00Z
window: read only drill ground troop capacity per level for the builder pick
est_minutes: 10
serves: PL-08
chain_id: ground-capacity-read-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T20:15:34Z
lease_until: 2026-11-23T20:35:34Z
result:
  status: done
  started_at: 2026-11-23T20:15:34Z
  finished_at: 2026-11-23T20:19:19Z
  duration_seconds: 225
  executor: operator
  summary: Drill Ground Lv.26 and Lv.28 read: Details Unit Count +8035 and +9211, preview current +7,200 and +7,600 to +7,400 and +7,800 (+200 each), power +21,600 and +30,400, coin short; no capacity or free-room line
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2015-queue-run.md and 2015-queue-run.csv; run 20261123T201534Z-0a99aa
  follow_up: Strategist: a step adds +200 to the preview Unit Count; Lv.30 and Lv.27 unread; the Details figure includes unexplained extras (835 and 1,611)
  stats:
    target: Lv.26 and one more ground: tag, Details figure, preview capacity line
    achieved: 2 grounds read (Lv.26, Lv.28)
    resources_gained: none
    points: 0
    costs: none spent; model 0.234445 USD
    verified: yes
    run_id: 20261123T201534Z-0a99aa
    run_steps: 17
    actions_done: 58
    actions_refused: 0
    cost_usd: 0.234445
    device_takeovers: 0
    grounds_read: 2
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, READ-ONLY: Drill Ground troop capacity per level, for the B2 to B4 pick)

serves: PL-08

Why: a finished batch cannot be collected while the Drill Ground is Full (`_records_/2026-11-22/troop-training/1958-queue-run.md`), so each ground's slot gain per level decides the pick; the Strategist needs it before 22:30Z. READ ONLY: never press Upgrade.

For EACH of the four grounds, Lv.26 first, then 28, 30, and 27 last (tap points and the pan in `_records_/2026-11-22/queue-planning/2540-drill-ground-sheet.md`; one ground per fresh frame):
1. Tap a soldier in the middle; write the tag text (name, level).
2. Open its Details and write the troop capacity figure, any unit count line and the FREE ROOM (capacity minus the troops shown, as x/y if a line shows it), with the tag text.
3. Open the Upgrade preview and write the troop capacity line, current and next, the increase, the power change, the cost and the effective time. The preview 'current' and the Details figure disagreed before: write both exactly.
4. Back out with the bare spot (310,660). Press NOTHING that upgrades, trains, collects or speeds up.

DONE when Lv.26 and one more ground are read; the rest are optional extras. Also write any 'x/y' troop line the HUD or a Barracks panel shows, with its tag text. May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if one opens, STOP.

Up to two runs, 10 steps each. Tag text beside every number; none means [G].
Cost cap, stated: 0.60 USD per run.
