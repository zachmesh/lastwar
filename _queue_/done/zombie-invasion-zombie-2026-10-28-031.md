---
unit: zombie-invasion-zombie-2026-10-28-031
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-29T06:53:13Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 31
attempts: 2
max_attempts: 3
claimed_by: ticker-0034
claimed_at: 2026-10-29T07:34:42Z
lease_until: 2026-10-29T07:54:42Z
result:
  status: partial
  started_at: 2026-10-29T07:34:42Z
  finished_at: 2026-10-29T07:45:48Z
  duration_seconds: 666
  executor: ticker-0034
  summary: Two Lv.10 kills claimed in-unit for 536,000 coins, one 10-stamina item opened, squads_parallel 1, chain continues, successor starts now
  claimed: [LOOT coin 268000 x2, medal x20, hero EXP, iron, food]
  claimed_count: 5
  evidence: _records_/2026-10-29/zombie-invasion/0034-queue-run.md
  follow_up: Open stamina before first dispatch when below 20 so squads overlap; redeem Coin Chest (SSR) from 920 derived medals; locate and open 4 owned Coin Chests
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 77.5M
    coin_after: 78.0M
    coins_collected: 536000
    medals_before: 900
    medals_after: 920
    chests_opened: 0
    squads_parallel: 1
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
