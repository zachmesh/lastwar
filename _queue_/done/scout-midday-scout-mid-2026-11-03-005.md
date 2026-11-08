---
unit: scout-midday-scout-mid-2026-11-03-005
regular: scout-midday
activity: perception-scout
segment:
priority: 2
created_at: 2026-11-08T10:30:05Z
expires_at:
planned_for:
not_before:
window: explain 3 unexplained red dots from 0204 unit: VIP panel top-right cart icon dot, base left-column blue bus icon dot, base left-column white truck icon dot; re-check VIP Daily Freebie claim state (claim belongs to vip regular, observe only)
est_minutes: 10
chain_id: scout-mid-2026-11-03
chain_seq: 5
attempts: 1
max_attempts: 3
claimed_by: ticker-0534
claimed_at: 2026-11-08T13:39:44Z
lease_until: 2026-11-08T13:59:44Z
result:
  status: done
  started_at: 2026-11-08T13:39:44Z
  finished_at: 2026-11-08T13:42:54Z
  duration_seconds: 190
  executor: ticker-0534
  summary: 3 unexplained red dots from the 0204 unit explained live: blue bus icon = Trucks (0/5, 4 waiting); white truck icon = Secret Command Post (17+5 claimable tasks, secrets regular) - corrects the 0022 mapping; VIP cart icon = VIP Store entry, no dot now (weekly-stock signal cleared by the 0204 visit); stale 2026-11-03 midday chain now complete
  claimed: [none]
  claimed_count: 1
  evidence: _records_/2026-11-08/perception-scout/0542-queue-run.md
  follow_up: none
  stats:
    surfaces_walked: scout-store
    items_observed: 12
    red_dots_seen: 3
    red_dots_explained: 3
    unexplained_red_dots: 0
    unknown_items: 4
    target: explain 3 unexplained red dots
    achieved: 3 dots explained live
    resources_gained: none (observe-only)
    costs: duration about 480s
    verified: yes
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
