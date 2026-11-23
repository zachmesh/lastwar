---
unit: scout-midday-growth-snapshot-2026-11-23-015
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:08:27Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot S1b read only never press Upgrade
est_minutes: 10
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 15
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T13:45:50Z
  duration_seconds: 
  executor:
  summary: retired by the planner: S1b superseded by the W1 weapon reads
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot S1b, Story 868, from the scout's updated unit table)

serves: snapshot (Story 868)

Read-only unit S1b. Queue placement: Runs after H1, whose section route it needs; Squad 1 rows may come from H2 and H3 instead.

Question: Which heroes have an exclusive weapon, is it unlocked, at what level, and how many named shards sit toward the next step?

Route: HEROES list, open the detail of each hero that can have a weapon, exclusive weapon section as H1 recorded; back. A guide lists Kimberly, DVA, Tesla (Season 1) and Murphy, Carlie, Swift (Season 2) as weapon heroes, sourced and unverified, so check the real list.

Read: Hero, stars, weapon present, locked or unlocked, weapon level, named shards owned over needed, universal shard count shown, stat lines, power line if shown.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-s1b-weapons.csv, schema h_weapons. Depends on H1 for the section route and S1 for the universal count. Three steps a hero, so two or three heroes a run; Squad 1 rows may come from H2 and H3 instead. Never press Unlock, Upgrade, Use or Equip. Weapon power 2,182,608 has not moved since 2026-11-08. Guide figures (unverified): 5 stars and 50 named shards to unlock, 1,080 shards from level 1 to 20, about +0.3M squad power at unlock and at levels 10, 20, 30.

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
