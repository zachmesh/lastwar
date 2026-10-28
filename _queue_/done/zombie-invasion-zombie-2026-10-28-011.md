---
unit: zombie-invasion-zombie-2026-10-28-011
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T12:49:12Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 11
attempts: 1
max_attempts: 3
claimed_by: ticker-0734
claimed_at: 2026-10-28T14:38:16Z
lease_until: 2026-10-28T14:58:16Z
result:
  status: partial
  started_at: 2026-10-28T14:38:16Z
  finished_at: 2026-10-28T14:47:14Z
  duration_seconds: 538
  executor: ticker-0734
  summary: Two Lv.10 kills X985 Y963 and X992 Y963 sequential - parallel batch misrouted by shifted Events tab bar into Level Swap page (untouched) and marches lasted about 10s; LOOT Claim All 536000 coins (49059336 to 49595336), medals 120 to 140, below 160 SR chest price, cleared false
  claimed: [loot-row-x985-y963, loot-row-x992-y963]
  claimed_count: 2
  evidence: _records_/2026-10-28/zombie-invasion/0738-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 2
    cleared: false
    coin_before: 49059336
    coin_after: 49595336
    coins_collected: 536000
    medals_before: 120
    medals_after: 140
    chests_opened: 0
    squads_parallel: 1
    tasks_badge: 2
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
