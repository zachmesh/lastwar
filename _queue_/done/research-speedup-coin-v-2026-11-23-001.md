---
unit: research-speedup-coin-v-2026-11-23-001
regular: research
activity: research-queue
segment: 1
priority: 1
created_at: 2026-11-23T13:43:43Z
expires_at: 2026-11-23T14:02:00Z
planned_for:
not_before: 2026-11-23T13:45:00Z
window: lab 2 coin output v tech speed up then complete and start iron output v ranks before the wave
est_minutes: 12
serves: PL-04
chain_id: speedup-coin-v-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T13:52:14Z
lease_until: 2026-11-23T14:12:14Z
result:
  status: done
  started_at: 2026-11-23T13:52:14Z
  finished_at: 2026-11-23T14:04:29Z
  duration_seconds: 735
  executor: operator
  summary: Steer A's order, runs 20261123T135214Z-6e7e2b, 20261123T135454Z-845eea, 20261123T140004Z-ea602f (claude-gateway/claude-sonnet-5-5; claimed 13:52:14Z): 7 Coin Chest (UR) used once (number field 7, Total 17.05M; coin 529.2K to 17.5M); Coin Output V sped up with tech items only (8h x3, 1h x1, 5m x1, about 1,505 minutes; one overflow TIPS confirm, no price) and Completed (POWER +3,900, Total Power 150,413,046 to 150,416,946); Iron Output V preview read (Original Time 5d 14:45:00 = 485,100 s, Research button 1d 16:50:00, Finish Now clock 1d 12:38:00; coin 5.6M, iron 1.8M, food 1.8M, no oil) and Research pressed once at 14:00:54Z: timer 1d 12:37:59 = 131,879 s, research speed M = 3.678; coin 11.9M, food 652.8M; Oil Output I panel not read.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/research-queue/1352-speedup-coin-v.md and 1352-speedup-coin-v.csv; growth/ledger.csv rows 13:55Z, 13:56Z, 14:00Z; runs 20261123T135214Z-6e7e2b, 20261123T135454Z-845eea, 20261123T140004Z-ea602f
  follow_up: read Oil Output I, Fast Builder V and Research Enhancement V panels with the Finish Now clock beside the Research button; Food Output V ends about 2026-11-24T17:30Z and Iron Output V about 2026-11-25T02:39Z; coin 11.9M is 1.9M above the 10M floor
  stats:
    target: convert coin, speed up Coin Output V with tech items, Complete it, read and start Iron Output V
    achieved: all four steps done; research speed M 3.678 measured
    resources_gained: Total Power +3,900 (Coin Output V Lv.1); research started
    points: 3900
    costs: 7 UR coin chests, tech speed-up 8h x3 1h x1 5m x1, coin 5.6M, food 1.8M, iron 1.8M; model 0.662871 USD
    verified: yes
    run_id: 20261123T140004Z-ea602f
    run_steps: 50
    actions_done: 70
    actions_refused: 0
    model_s_per_step: 6.8
    cost_usd: 0.662871
    device_takeovers: 0
    rules_used: R1,R4,R5
    rule_failed: none
    rule_gap: The Research button time of an Age of Oil node can exceed the real timer; the Finish Now clock matched it.
  stats_missing: []
  stats_warnings: []
---

# research

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-04

## Brief (planner, Coin Output V tech speed-up then Iron Output V, plan PL-04, Steer A's three conditions)

serves: PL-04

Steer A approved PL-04 with three conditions; a stop note in this unit governs. A TIPS dialog about another device: STOP and report, never Confirm. Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. THE ORDER, one run chain, and never leave lab 2 idle after the Complete:

1. Flask icon: read BOTH labs (tag text, timers to the second); slot 2 should be Coin Output V with about 25.3 h left. Read coin, the oil counter and the Backpack Speed-up tab counts (tech 8h x8, 1h x126).
2. FIRST convert the coin Iron Output V needs, about 4.6M to 6.2M by the guide (plan on 6.2M): N = ceil((6.2M + 10M floor - coin now) / 2.4364M) UR Coin Chests, skip if 0 or less, STOP above 40. HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the Coin Chest UR, confirm the tile name, read the number field AND the Total line in a frame before Use. Read coin after.
3. THEN the tech speed-up on Coin Output V: slot 2 Speed Up, TECH items only (the blue-disc type), never general or construction. Read the item name and the quantity before EACH press (the default may be a full stock: reduce it first); largest first, one press at a time (about 8h x3, then 1h x1); read the remaining time after each; stop when the node completes or the remainder is under 60 minutes, never overshooting by more than one 1h item. Log the inventory counts before and after, the minutes used (about 1,500 to 1,560 of 11,400), the new finish time and the oil.
4. THEN press COMPLETE (Total Power before and after, +3,900 expected); if a remainder is left, wait it out in the next run.
5. THEN open Iron Output V's node panel and READ it BEFORE Start: the effective time with no speed-up applied, the original time, coin, iron, food, oil and power. This is the FIRST CLEAN READ OF THE RESEARCH SPEED: write it at once with the tag text so it goes to the Strategist. If coin is still short, convert only the shortfall by the same formula.
6. START Iron Output V in lab 2 (Research once); read the timer to the second and the oil. Never Finish Now. The second spend on Iron Output V is a separate unit.

Up to three runs, 12 steps each. Tag text beside every number; none means [G]. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`.
Cost cap, stated: 0.90 USD per run (the harness stops near 0.36 of it).
