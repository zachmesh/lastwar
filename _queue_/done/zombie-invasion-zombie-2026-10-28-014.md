---
unit: zombie-invasion-zombie-2026-10-28-014
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T15:44:37Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 14
attempts: 1
max_attempts: 3
claimed_by: ticker-0904
claimed_at: 2026-10-28T16:04:57Z
lease_until: 2026-10-28T16:24:57Z
result:
  status: partial
  started_at: 2026-10-28T16:04:57Z
  finished_at: 2026-10-28T16:18:33Z
  duration_seconds: 816
  executor: ticker-0904
  summary: Claimed 4 LOOT rows for 1072000 coins exactly (coin 50131336 to 51203336); verified medals 190 in Store and redeemed 1 Coin Chest (SSR) for 160 medals (tooltip Owned 3, 812.16K each, location in inventory still unknown); Store stamina item exhausted Limit 0; 1 Squad 1 kill X914 Y812, squads_parallel 1 because stamina 13 allowed only one 10-cost march
  claimed: [loot-rows-x4, coin-chest-ssr-x1]
  claimed_count: 2
  evidence: _records_/2026-10-28/zombie-invasion/0904-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 50131336
    coin_after: 51203336
    coins_collected: 1072000
    medals_before: 160
    medals_after: 40
    chests_opened: 0
    chests_redeemed: 1
    chests_owned: 3
    squads_parallel: 1
    tasks_badge: 3
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
