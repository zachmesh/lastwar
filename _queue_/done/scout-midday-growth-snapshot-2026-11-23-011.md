---
unit: scout-midday-growth-snapshot-2026-11-23-011
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:08:25Z
expires_at: 2026-11-23T08:43:00Z
planned_for:
not_before: 2026-11-23T08:00:00Z
window: growth snapshot P2 read only never press Upgrade
est_minutes: 10
chain_id: growth-snapshot-2026-11-23
chain_seq: 11
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T08:22:29Z
lease_until: 2026-11-23T08:42:29Z
result:
  status: partial
  started_at: 2026-11-23T08:22:29Z
  finished_at: 2026-11-23T08:24:43Z
  duration_seconds: 134
  executor: operator
  summary: Run 20261123T082236Z-f0bb84 (claude-gateway/claude-sonnet-5-5, max-steps 8, completed in 5 steps), read-only. From the Backpack back to the base (no boarding banner). Barracks Lv.30 busy: pistol opened TRAIN UNITS, Training in progress 1d 02:55:29 (Lv.10 x793); cards Lv.7 1,116, Lv.8 2,141, Lv.9 1,878, Lv.10 35.1K, Lv.6 cut off; green up arrows on the corners of Lv.7 to Lv.9, enabled, no red dot; no (i) icon, no Promote button, no promote panel, no cost or requirement line; only Speed Up, not tapped. Arrows not tapped (counts not zero); the 08:02Z run showed an arrow tap only selects the card. Panel Power 1647 (Lv.10) and 1352 (Lv.9) match the guide per-troop figures. Second read not done: the upper-right tent read Hospital Lv.20 (no pistol). Promote cost per troop, requirements and time unknown, panel unreachable while barracks are busy or the Drill Ground is full. 5 steps, 10 actions done, 0 refused, 7.7 s model time per step, 0.087692 USD. No takeover. Game on the base.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0022-queue-run.md and _records_/2026-11-22/growth/0022-p2-promote.csv; run 20261123T082236Z-f0bb84; frame _tools_/state/cu_growth_p2_0022.png
  follow_up: retry the promote read when a barracks is idle with Drill Ground room (Lv.27 batch ends about 19:56Z); resolve whether the upper-right building is Hospital Lv.20 or Barracks Lv.20
  stats:
    target: find the troop Promote control: label, position, state, cost per troop, requirements, toast (P2)
    achieved: control not found: only card-corner arrows, no (i), no Promote panel; cost, time and requirements unread
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.087692 USD; nothing spent, nothing pressed
    verified: yes
    blocker_category: f
    surfaces_walked: 2
    items_observed: 14
    run_id: 20261123T082236Z-f0bb84
    run_steps: 5
    actions_done: 10
    actions_refused: 0
    model_s_per_step: 7.7
    cost_usd: 0.087692
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot P2, Story 868, from the scout's updated unit table)

serves: snapshot (Story 868)

Read-only unit P2. Queue placement: Runs right after T1 on the same barracks (queue order: T1, then P2, then T2).

Question: What does the troop promote function cost per troop, what does it need, and why did the arrow do nothing?

Route: Lv.30 barracks as in T1: tent body, read the label, pistol opens TRAIN UNITS. Look for a Promote or up-arrow control near the tier cards, an (i) help icon and any lower-tier card. Tap (i) first. Tap the arrow itself once only when the lower-tier count it would promote reads 0, and copy the toast. If a promote panel opens, read it and close by X.

Read: Control label, position and state (enabled, greyed, red dot); panel title; from tier, to tier, count cap; cost per troop in food, iron and coin; time; power per troop; requirement lines with check marks; lower-tier counts T7 to T9; toast text verbatim; whether Drill Ground Full or capacity is named.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-p2-promote.csv, schema j_promote. Run right after T1 on the same barracks. S1 bars the confirm step: never press Promote, Confirm or Train; if a dialog with Confirm and a count above zero appears press Cancel and record it. No promote panel appears anywhere in the records, so the route is designed, not known. Guide claim, sourced and unverified (lastwarvault waterfall guide): a barracks promotes any lower tier to its own max tier, Lv.24 T8, Lv.27 T9, Lv.30 T10, at 1,063, 1,352 and 1,647 power per troop. Earlier tier counts (T7 715, T8 1,332, T9 1,152, T10 35.8K) may be account-wide or per type.

Operator read 08:00Z: the portrait bubble is the Hospital (5,306 healed troops cannot be collected: Drill Ground Full); the green arrow on a barracks is the building Upgrade, never Promote and never pressed. Read-only: do not tap Collect.

Record any Promote control you find, its label, position and state.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.
