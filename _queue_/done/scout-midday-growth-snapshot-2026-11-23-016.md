---
unit: scout-midday-growth-snapshot-2026-11-23-016
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:08:28Z
expires_at: 2026-11-23T13:30:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot C1 read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 16
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T13:22:49Z
lease_until: 2026-11-23T13:42:49Z
result:
  status: partial
  started_at: 2026-11-23T13:22:49Z
  finished_at: 2026-11-23T13:25:39Z
  duration_seconds: 170
  executor: operator
  summary: C1 coin sinks, run 20261123T132249Z-240560 (claude-gateway/claude-sonnet-5-5, 12 steps; claimed 13:22:49Z): no different-device dialog; Gold Mine Lv.28 to 29: coin 23.8M (stock 55,963), iron 73.1M, +14,800 power, Coin Output/hr 20,160 to 20,880, effective 4d 14:20:24; Farmland Lv.28 to 29: coin 23.8M, iron 110.5M, +14,900 power, effective 4d 14:20:24; about 620 power per million coin; one unintended tap on the Farmland food harvest bubbles collected them (food 653.9M to 654.6M, Total Power unchanged, ledger row added); research node and gear previews not reachable; nothing else pressed.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1323-c1-coin.md and _records_/2026-11-22/growth/1323-c1-coin.csv; growth/ledger.csv row 13:24Z; run 20261123T132249Z-240560
  follow_up: research node previews wait for an idle lab; gear step route unnamed; tap the Farmland crops not its harvest bubbles; coin sources and the 109.2M to 9.6M fall of 2026-11-22 remain unexplained
  stats:
    target: read the coin cost and power gain of each coin sink and where coin comes from
    achieved: Gold Mine and Farmland previews read; research and gear previews not reachable
    resources_gained: food +0.7M from an unintended harvest tap
    points: 0
    costs: model 0.162981 USD; no resources spent
    verified: yes
    blocker_category: c
    run_id: 20261123T132249Z-240560
    run_steps: 12
    actions_done: 22
    actions_refused: 0
    model_s_per_step: 6.5
    cost_usd: 0.162981
    device_takeovers: 0
    rules_used: R1,R6
    rule_failed: R6
    rule_gap: Harvest bubbles sit on the Farmland and a tap on them collects: name the crops, not the building centre.
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot C1, Story 868, from the scout's updated unit table)

serves: snapshot (Story 868)

Read-only unit C1. Queue placement: Runs after F1, F2 and H1, whose coin lines and route it copies.

Question: What does each coin sink really cost in coin and add in power, and where does coin come from?

Route: Upgrade previews as in F1 (building body, green arrow, read, X or swipe-back) for the Gold Mine and Farmland; research node previews as in A1 for the next Units, Hero and Economy nodes; one gear step preview once H1 names the route. Copy the Drill Ground and barracks coin lines from F1 and F2 rather than re-reading them.

Read: Per sink: from level, to level, coin, food, iron, other cost, time, power gain; coin on the HUD before and after the unit.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-c1-coin.csv, schema i_coin. Reading only; S1 and S5 apply. Sinks in the records: Gold Mine to Lv.30 cost 1.9M coin for +14,800 power; each alliance donation costs 600 to 800 coin, 30 a day; coin read 109.2M at 13:09 PT on 2026-11-22 and 9.6M at 23:49, cause unrecorded. Sources in the records (partial scan of 2,641 done units, unverified): radar gold gathers up to 5.5M a unit, truck plunder up to 8.5M, mail rewards 12.1M once, harvest bubbles up to 5.2M, zombie loot about 1.1M.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Tag text: beside every number from a building panel write its tag text (name and level above the building after the tap; `_records_/2026-11-22/coach/0255-tag-text-check.md`); none means [G]. Add a tag_text column.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
