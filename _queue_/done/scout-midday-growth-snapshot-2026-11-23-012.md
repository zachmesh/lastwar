---
unit: scout-midday-growth-snapshot-2026-11-23-012
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:08:25Z
expires_at: 2026-11-23T08:44:00Z
planned_for:
not_before: 2026-11-23T08:00:00Z
window: growth snapshot S1 read only never press Upgrade
est_minutes: 8
serves: snapshot (Story 868)
chain_id: growth-snapshot-2026-11-23
chain_seq: 12
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T08:38:32Z
lease_until: 2026-11-23T08:58:32Z
result:
  status: partial
  started_at: 2026-11-23T08:38:32Z
  finished_at: 2026-11-23T08:42:10Z
  duration_seconds: 218
  executor: operator
  summary: Runs 20261123T083839Z-d1edeb (7 steps), 20261123T083955Z-f1b739 (3 steps) and 20261123T084120Z-730fc4 (2 steps, back to the base), claude-gateway/claude-sonnet-5-5, read-only. Heroes tab names read by description: UR Hero Universal Shard and SSR Hero Universal Shard (Use this item to promote hero tier of the same rarity.), Hero Recruitment Ticket x126, Survivor Recruitment Ticket, New Era Recruitment Ticket, Skill Medal x9,521. The counts of the two Universal Shards sit in the cut-off fourth row and were not read; a drag scrolls several rows at once and jumped past them. Below them the grid holds purple, blue and orange hero portrait puzzle pieces and round portrait tiles with counts 1 to 95 (heroes not named). The Universal Exclusive Weapon Shard and Upgrade Ore were not located by name. Nothing used, opened or sold. Game back on the base, no banner. 12 steps in all, 16 actions done, 0 refused, 0.175421 USD. No takeover.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/0038-queue-run.md and _records_/2026-11-22/growth/0038-s1-stocks.csv (schema h_stocks); frame _tools_/state/cu_growth_s1_0038.png
  follow_up: read the UR and SSR Hero Universal Shard counts and the Gear tab names in the approved inventory run with a gentler scroll; name the hero shards only if the plan needs them
  stats:
    target: read stocks of hero shards, skill medals, ore and universal weapon shards with tab and count (S1)
    achieved: Skill Medal 9521 and the two Universal Shard names read; their counts, named hero shards, ore and the weapon shard not read
    resources_gained: none (observe-only)
    points: 0
    costs: model 0.175421 USD; nothing spent, nothing used
    verified: yes
    blocker_category: c
    surfaces_walked: 1
    items_observed: 60
    run_id: 20261123T083839Z-d1edeb,20261123T083955Z-f1b739,20261123T084120Z-730fc4
    run_steps: 12
    actions_done: 16
    actions_refused: 0
    cost_usd: 0.175421
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot S1, Story 868, from the scout's updated unit table)

serves: snapshot (Story 868)

Read-only unit S1. Queue placement: Runs after the barracks reads (T1, P2, T2).

Question: What stocks of hero shards, skill medals, ore and universal weapon shards does the account hold?

Route: Bottom bar Inventory (re-ground, an older framing used about 900,870); open every tab: Special (drag to scroll, items sit below the fold), Resources and any Hero or Materials tab; then the HEROES list for shard bars on the cards if shown.

Read: Named hero shards per hero, universal hero shards, Universal Exclusive Weapon Shards, Skill Medals, Upgrade Ore and other upgrade materials, each with its tab name and exact count; card shard bars as owned over needed.

Budget: at most 8 steps and 8 minutes. Notes: Output _records_/<date>/growth/<HHMM>-s1-stocks.csv, schema h_stocks. Reading only: never Use, Open, Sell or confirm any item, and do not open a red-dot item (it may be a gift). A scroll action did not move the grid once, a drag did. Earlier figure: Universal Exclusive Weapon Shard owned 417 (zombie store, 2026-11-10).

Rules: stop rules R1 to R7 in `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`; red lines and the snap command in `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. Snap takes only K or M numbers: write 1.1G as 1100M. Do not enqueue a chain successor.

Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
