---
unit: scout-midday-growth-snapshot-2026-11-23-026
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-23T11:13:01Z
expires_at: 2026-11-24T08:30:00Z
planned_for:
not_before: 2026-11-23T11:14:00Z
window: chest quantity limits and speed up tab read only never press Use
est_minutes: 10
serves: baseline coin conversion
chain_id: growth-snapshot-2026-11-23
chain_seq: 26
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T11:15:13Z
lease_until: 2026-11-23T11:35:13Z
result:
  status: done
  started_at: 2026-11-23T11:15:13Z
  finished_at: 2026-11-23T11:23:24Z
  duration_seconds: 491
  executor: operator
  summary: RC1 chest quantity limits, runs 20261123T111538Z-948aa9, 20261123T111730Z-3c32e0 and 20261123T112025Z-6085b3 (claude-gateway/claude-sonnet-5-5, 30 steps; claimed 11:15:13Z): Resource Chest owned 20,862, selecting it sets the full stock 20862 (handle at the far right), a tap on the number field does nothing (no typed quantity), no batch button; Coin Chest UR 87 owned, max 87 per Use, Total 211.97M coin, no cap; Coin Chest SR 122, max 122, Total 12.38M, no cap; SSR 71 owned, slider end not measured (inferred); Speed-up tab general 351,647 minutes, construction 167,760 minutes read as text. Nothing used, opened, typed or spent; Use never pressed.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/growth/1115-rc1-chest-limits.md and 1115-rc1-chest-limits.csv; runs 20261123T111538Z-948aa9, 20261123T111730Z-3c32e0, 20261123T112025Z-6085b3
  follow_up: owner and Strategist rank the one-Use coin conversion (UR 87 chests = 211.97M coin); SSR slider end and the Speed-up blue-disc rows unread; the Resources tab opens with the 5,000 Diamonds x16 tile selected and a live Use
  stats:
    target: record quantity, typed quantity, max per Use, slider cap and batch button of the Resource Chest and Coin Chests UR, SSR, SR, and the Speed-up tab
    achieved: Resource Chest, Coin Chest UR and SR measured; SSR cap inferred; Speed-up tab read
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.430832 USD in three runs; nothing used or spent
    verified: yes
    run_id: 20261123T112025Z-6085b3
    run_steps: 30
    actions_done: 65
    actions_refused: 0
    model_s_per_step: 7.0
    cost_usd: 0.430832
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: none
    rule_gap: Resources tab opens with the 5,000 Diamonds tile selected and a live Use; the digest warns of neither it nor the full-stock default.
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: baseline coin conversion

## Brief (planner, chest quantity limits read, Steer A verdict on decision 2603, read-only)

serves: baseline coin conversion

The third Drill Ground step needs 119.0M coin, about 19,800 plain Resource Chests (inventory read `_records_/2026-11-22/growth/0009-inventory-read.md`: about 20,753, the choice of 10K food, 10K iron or 6K coin; Coin Chests UR 87, SSR 71, SR 122). Whether one Use can open that many decides if the third ground is feasible in a few runs or must come from SSR and SR Coin Chests. Steer A is told before any choice chest is touched.

1. Backpack, Resources tab (bottom bar Inventory; ground it fresh; a drag must start inside the grid). Select by ONE tap, never Use: the plain Resource Chest, then the Coin Chest UR, SSR and SR.
2. For each tile record the name as shown (the tag text), the quantity owned, and what the quantity field and slider show after selecting: can a quantity be typed, what is the maximum per Use, does the slider cap below the stock, and is there a Use-all or batch button (record its text, never press it). The Use button stays untouched.
3. Then the Speed-up tab: read the construction speed-up minutes and the general minutes as text, and any other rows.

NEVER press Use, Open, Convert, Sell or Buy; if a dialog opens press Cancel or X; stop at any price or diamond. Close the Backpack with its X; close any base menu with an empty-ground tap such as (200,610); never tap WORLD (660,940) with a menu open low. Record one line per tile with the frame time.

At most 8 steps and 10 minutes. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (write 1.1G as 1100M). Do not enqueue a chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
