---
unit: training-growth-collect-2026-11-23-001
regular: training
activity: troop-training
segment: 1
priority: 2
created_at: 2026-11-23T08:09:06Z
expires_at: 2026-11-23T21:55:00Z
planned_for:
not_before: 2026-11-23T19:58:00Z
window: collect the Lv.27 T9 batch due about 1956Z and log the exact power change
est_minutes: 10
serves: PL-07
chain_id: growth-collect-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T19:58:24Z
lease_until: 2026-11-23T20:18:24Z
result:
  status: partial
  started_at: 2026-11-23T19:58:24Z
  finished_at: 2026-11-23T20:00:51Z
  duration_seconds: 147
  executor: operator
  summary: The finished Lv.27 batch of 726 was not collected under Drill Ground Full: the ready bubble tap and the pistol both raised 'Drill Ground Full: Unable to add more units.'; Total Power 150,416,946 unchanged; queue still blocked
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/troop-training/1958-queue-run.md and 1958-queue-run.csv; run 20261123T195824Z-93f69a
  follow_up: the collect needs room (or the bubble tap was not the collect control: unverified); retry after the Drill Ground has room or ask the Researcher for the collect control; troop counts per tier unread
  stats:
    target: collect the finished Lv.27 batch and read the toast, Total Power and queue state
    achieved: collect refused by Drill Ground Full; Total Power unchanged
    resources_gained: none
    points: 0
    costs: none spent; model 0.163387 USD
    verified: yes
    run_id: 20261123T195824Z-93f69a
    run_steps: 12
    actions_done: 24
    actions_refused: 0
    cost_usd: 0.163387
    device_takeovers: 0
    slots_idle: 1
    slots_blocked_by_capacity: 1
    capacity_blocker: Drill Ground Full
    power_before: 150416946
    power_after: 150416946
    blocker_category: c capacity: Drill Ground Full
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# training

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: collect finished batches

## Brief (planner, coordinator instruction after the 08:00Z operator read)

serves: PL-07

The Lv.27 T9 x726 batch is due about 19:56Z on 2026-11-23. Power registers only on collection. Read Total Power from the HUD with its decimals, tap the Lv.27 barracks (re-ground it fresh; tent taps often miss, two failed taps end the unit as partial) to collect the finished batch, read Total Power again, and log the exact power change. Do not press the Hospital Collect: it is all-or-nothing (at least 5,306 free slots at once). This unit tells whether a batch collect works under Drill Ground Full: log the exact Total Power before and after, and the toast verbatim if one appears. The green arrow on a barracks is the building Upgrade: never press it.

After collecting, requeue the barracks at its top tier only if it now shows idle, capacity allows and stocks pass the fill rule (decision 2350: at most one third of each stock and above the reserves); a Drill Ground Full toast ends the requeue, record it. Run `python3 _tools_/resource_map.py snap food=<n> iron=<n> coin=<n> --note <this unit id>` (write 1.1G as 1100M; the tool reads only K and M). Do not enqueue a chain successor; the planner owns this chain. Run one growth unit at a time.

Red lines: no purchase or diamond spend, no PvP, attack, rally, march, Arena fight or General's Trial fight, no alliance diplomacy, no ally-exchange trade, no speedup or Finish Now, no owner name or identifier values in any record. Any such surface stops the unit as needs-owner.

Barracks taps (base map `_records_/2026-11-22/growth/1030-base-map.md`, fresh frame): Lv.27 (462,585), Lv.30 (530,637), Lv.24 (628,562), Lv.20 (668,535); the pistol is the middle button under the tag; a portrait bubble may be the Hospital. Close menus with the bare spot (310,660) (not (400,640) after a camera shift); never tap WORLD (660,940) with a menu open low.

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; stop with one named reason, never improvise.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
