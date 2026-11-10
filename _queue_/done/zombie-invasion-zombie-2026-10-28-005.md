---
unit: zombie-invasion-zombie-2026-10-28-005
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T11:10:27Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 5
attempts: 1
max_attempts: 3
claimed_by: parallel-exec-005
claimed_at: 2026-10-28T11:11:49Z
lease_until: 2026-10-28T11:31:49Z
result:
  status: partial
  started_at: 2026-10-28T11:11:49Z
  finished_at: 2026-10-28T11:19:37Z
  duration_seconds: 468
  executor: parallel-exec-005
  summary: Wave exhausted - Search answered Monsters not found nearby, next wave about 1144Z, so no target existed and parallel dispatch was impossible for lack of targets (not a game cap; march queue cap still unmeasured). Store recon confirmed Coin Chest (SR) price 160 medals against a balance of 70, so no redemption; the 2 owned SR chests were not located in inventory within the window and stay a follow-up, as does the LOOT badge check. No kills, no spend.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-10-28/zombie-invasion/0411-queue-run.md
  follow_up: Next unit - catch the 1144Z wave, dispatch squads in parallel to the march queue cap and record it; locate and open the 2 owned Coin Chest (SR); check and claim the LOOT icon badge
  stats:
    zombies_killed: 0
    squads_parallel: 0
    coin_before: 35488573
    coin_after: 35488573
    coins_collected: 0
    medals: 70
    coin_chest_sr_price_medals: 160
    stamina_spent: 0
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
