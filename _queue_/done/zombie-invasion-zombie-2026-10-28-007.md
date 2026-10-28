---
unit: zombie-invasion-zombie-2026-10-28-007
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-10-28T11:49:30Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-10-28
chain_seq: 7
attempts: 1
max_attempts: 3
claimed_by: ticker-0434
claimed_at: 2026-10-28T11:49:36Z
lease_until: 2026-10-28T12:09:36Z
result:
  status: partial
  started_at: 2026-10-28T11:49:36Z
  finished_at: 2026-10-28T11:51:50Z
  duration_seconds: 134
  executor: ticker-0434
  summary: Settled unit 006 in-flight kill - LOOT row X905 Y465 claimed, coin 35756573 to 36024573 (+268000, second consecutive 268k row), medals 80 to 90 by row; March Queues bar reads 1 of 4 so march queue cap is 4; one more Squad 1 march dispatched in flight at pass end toward X871 Y458 for unit 008 to settle; no redemption (medals 90 below 160 SR price)
  claimed: [zombie-loot-x1]
  claimed_count: 1
  evidence: _records_/2026-10-28/zombie-invasion/0450-queue-run.md
  follow_up: none
  stats:
    zombies_killed: 1
    cleared: false
    coin_before: 35756573
    coin_after: 36024573
    coins_collected: 268000
    medals_before: 80
    medals_after: 90
    chests_opened: 0
    squads_parallel: 1
    tasks_badge: 1
    stamina_spent: 0
---

# zombie-invasion

Produced by tools/queue.py. The executor reads the activity metadata and the standing rules before acting.
