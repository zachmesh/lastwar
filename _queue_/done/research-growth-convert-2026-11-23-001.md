---
unit: research-growth-convert-2026-11-23-001
regular: research
activity: research-queue
segment: 1
priority: 2
created_at: 2026-11-23T08:25:37Z
expires_at: 2026-11-23T12:04:00Z
planned_for:
not_before: 2026-11-23T11:44:00Z
window: convert coin for the Drill Ground Expansion node and start it when the lab frees
est_minutes: 15
serves: capacity source: Drill Ground Expansion (lab at about 11:43Z)
chain_id: growth-convert-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T11:45:03Z
lease_until: 2026-11-23T12:05:03Z
result:
  status: partial
  started_at: 2026-11-23T11:45:03Z
  finished_at: 2026-11-23T12:02:13Z
  duration_seconds: 1030
  executor: operator
  summary: Research conversion runs 20261123T115241Z-cb0c2b, -f92ecc, -9c9d0e, -dcbc2d and -99d0f8 (claude-gateway/claude-sonnet-5-5, 34 steps; claimed 11:45:03Z, start refused by the D-024 desktop gate until 11:52:41Z): COMPLETE pressed on Unlock Oil Well at 11:53:00.984Z, POWER +3,900 (150,211,809 to 150,215,709), slot 1 idle; run paused by a local_input pointer event at 11:53:16.761Z, stopped and retried once; TECH hub read; Development nodes named by tag text (Infirmary Expansion III 4/5 20.1M coin, 6.7M iron and food, 2d 12:57:11; Barracks Expansion III 4/5 same costs; Extra Barracks MAX Unlocked; others MAX); Drill Ground Expansion NOT found, so nothing converted and nothing started (coin 14.4M unchanged); the second research slot is idle.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/research-queue/1144-queue-run.md and 1144-queue-run.csv; growth/ledger.csv row 11:53:00Z; runs 20261123T115241Z-cb0c2b, 20261123T115451Z-f92ecc, 20261123T115642Z-9c9d0e, 20261123T115826Z-dcbc2d, 20261123T120037Z-99d0f8
  follow_up: find Drill Ground Expansion (the nodes below the visible Development tree, or the Units and Economy trees) in the backup unit -002 12:10 to 12:40Z; the idle slot 2 candidates Infirmary Expansion III and Barracks Expansion III need 20.1M coin (15.7M above reserve, 7 UR coin chests are 17.1M); decide the target before converting
  stats:
    target: complete Unlock Oil Well, convert the Drill Ground Expansion coin, start the node
    achieved: COMPLETE pressed (power +3,900); node not found, nothing converted or started
    resources_gained: Total Power +3,900
    points: 3900
    costs: model 0.484035 USD in five runs; no resources spent
    verified: yes
    blocker_category: c
    run_id: 20261123T115241Z-cb0c2b
    run_steps: 34
    actions_done: 75
    actions_refused: 0
    model_s_per_step: 7.0
    cost_usd: 0.484035
    device_takeovers: 1
    rules_used: R1,R4
    rule_failed: none
    rule_gap: Node names appear only in the panel; no rule names the tree holding Drill Ground Expansion.
  stats_missing: []
  stats_warnings: [points duplicates achieved in string, duration exceeds 15-minute unit cap]
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: capacity source: Drill Ground Expansion (lab at about 11:43Z)

## Brief (planner, conversion-and-spend for the lab, coordinator coin plan)

serves: capacity source: Drill Ground Expansion (the lab freeing about 11:43Z)

Conversion rules and amounts: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`; red lines and the snap command: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md` (K or M numbers only: write 1.1G as 1100M).

1. Open the labs with the flask icon. If 'Unlock Oil Well' shows finished, press COMPLETE first, because power registers only on Complete. If no lab is idle, read the time left to the second, write it with the UTC time and stop.
2. Open the Development tree and read the Drill Ground Expansion node preview: next level, coin, food, iron, time and any capacity or slots line. Read the Extra Barracks node the same way, read only. If the Expansion cost cannot be read, start nothing.
3. Convert exactly the node's coin cost by the rules (read Coin Chests first), and no more. Read coin on the HUD before and after. If the node also needs Valor Badges or an item you cannot cover from stock, stop and record it.
4. Press Research once on the Drill Ground Expansion node, read the new timer to the second, then run the snap command.

Budget: 15 minutes, 10 steps. Never convert hero levers; speed-ups, stamina items and diamond items are red lines. Do not enqueue a chain successor.

Cost cap, stated: 0.90 USD (the harness stops near 0.36 of it).
