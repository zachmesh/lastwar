---
unit: zombie-invasion-zombie-2026-11-10-012
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-11T15:59:29Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 12
attempts: 1
max_attempts: 3
claimed_by: ticker-0804
claimed_at: 2026-11-11T16:22:41Z
lease_until: 2026-11-11T16:42:41Z
result:
  status: partial
  started_at: 2026-11-11T16:22:41Z
  finished_at: 2026-11-11T16:33:45Z
  duration_seconds: 664
  executor: ticker-0804
  summary: 1 Lv.10 kill X:463 Y:324, 268000 coins claimed, squads_parallel 1 (stamina-bound), wave still live, successor enqueued
  claimed: [loot-268000-x1]
  claimed_count: 1
  evidence: _records_/2026-11-11/zombie-invasion/0832-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 123000000
    coin_after: 123300000
    coins_collected: 268000
    medals_before: unread
    medals_after: unread
    chests_opened: 0
    squads_parallel: 1
    target: 2 parallel kills plus LOOT claim
    achieved: 1 kill, 268000 coins claimed
    resources_gained: coin 268000, iron 268000, food 268000, medals 10 (card-stated), hero EXP 263000, gold ticket 1
    costs: stamina 10 spent (net 8 after regen), duration about 10 minutes
    verified: yes
    blocker_category: h
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
