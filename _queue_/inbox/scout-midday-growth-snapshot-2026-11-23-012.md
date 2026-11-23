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
chain_id: growth-snapshot-2026-11-23
chain_seq: 12
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
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

Stop rules from `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md` (here S1 to S7 are the protocol's rule numbers, not unit names): R1 never press Upgrade, Finish Now, Speed Up, Construct, Research, Train, Hire, Complete, Claim, Quick Dispatch, Promote, Unlock, Use, Open, Sell or Equip. R2 read a diamond or price figure, never tap it. R3 stop at any march, attack, rally, Arena or PvP surface. R4 close any Confirm dialog with Cancel or X. R5 close a preview only by X or left-edge swipe-back, never a low tap. R6 two failed taps on one target end the unit as partial. R7 no owner name or ID; skip profile and ranking screens.

If this unit reads the HUD, run `python3 _tools_/resource_map.py snap food=<n> iron=<n> coin=<n> --note <this unit id>`. The tool reads only plain numbers with a K or M suffix: write 1.1G as 1100M. Do not enqueue a chain successor; the planner owns this chain.

Red lines: no purchase or diamond spend, no PvP, attack, rally, march, Arena fight or General's Trial fight, no alliance diplomacy, no ally-exchange trade, no speedup or Finish Now, no owner name or identifier values in any record. Any such surface stops the unit as needs-owner.
