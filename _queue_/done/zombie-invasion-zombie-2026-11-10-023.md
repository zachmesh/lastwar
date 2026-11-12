---
unit: zombie-invasion-zombie-2026-11-10-023
regular: zombie-invasion
activity: zombie-invasion
segment:
priority: 4
created_at: 2026-11-12T07:44:04Z
expires_at:
planned_for:
not_before:
window:
est_minutes: 12
chain_id: zombie-2026-11-10
chain_seq: 23
attempts: 1
max_attempts: 3
claimed_by: ticker-0004
claimed_at: 2026-11-12T08:15:31Z
lease_until: 2026-11-12T08:35:31Z
result:
  status: partial
  started_at: 2026-11-12T08:15:31Z
  finished_at: 2026-11-12T08:31:34Z
  duration_seconds: 963
  executor: ticker-0004
  summary: Event live (1d 17:37 left), stamina refilled 8 to 58 (1x 50-stamina item, 666 to 665), Lv.10 target found but not dispatched - unit cap reached; cleared false, chain continues
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-12/zombie-invasion/0030-queue-run.md
  follow_up: successor 024 enqueued to start now; use crossed-swords point (500,753) after Search; Store redemption backlog open
  stats:
    zombies_killed: 0
    cleared: false
    coin_before: 143400000
    coin_after: 143400000
    coins_collected: 0
    chests_opened: 0
    squads_parallel: 0
    target: 2
    achieved: 0
    resources_gained: none
    costs: 15min, 1x 50-stamina item
    verified: yes
    blocker_category: h
    stamina_before: 8
    stamina_items_50_before: 666
    stamina_items_50_after: 665
    stamina_items_10: 655
  stats_missing: []
  stats_warnings: []
---

# zombie-invasion

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
