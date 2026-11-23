---
unit: scout-midday-growth-snapshot-2026-11-23-016
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T08:08:28Z
expires_at: 2026-11-23T11:14:00Z
planned_for:
not_before: 2026-11-23T09:05:00Z
window: growth snapshot C1 read only never press Upgrade
est_minutes: 10
chain_id: growth-snapshot-2026-11-23
chain_seq: 16
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, growth snapshot C1, Story 868, from the scout's updated unit table)

serves: snapshot (Story 868)

Read-only unit C1. Queue placement: Runs after F1, F2 and H1, whose coin lines and route it copies.

Question: What does each coin sink really cost in coin and add in power, and where does coin come from?

Route: Upgrade previews as in F1 (building body, green arrow, read, X or swipe-back) for the Gold Mine and Farmland; research node previews as in A1 for the next Units, Hero and Economy nodes; one gear step preview once H1 names the route. Copy the Drill Ground and barracks coin lines from F1 and F2 rather than re-reading them.

Read: Per sink: from level, to level, coin, food, iron, other cost, time, power gain; coin on the HUD before and after the unit.

Budget: at most 8 steps and 10 minutes. Notes: Output _records_/<date>/growth/<HHMM>-c1-coin.csv, schema i_coin. Reading only; S1 and S5 apply. Sinks in the records: Gold Mine to Lv.30 cost 1.9M coin for +14,800 power; each alliance donation costs 600 to 800 coin, 30 a day; coin read 109.2M at 13:09 PT on 2026-11-22 and 9.6M at 23:49, cause unrecorded. Sources in the records (partial scan of 2,641 done units, unverified): radar gold gathers up to 5.5M a unit, truck plunder up to 8.5M, mail rewards 12.1M once, harvest bubbles up to 5.2M, zombie loot about 1.1M.

Stop rules from `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md` (here S1 to S7 are the protocol's rule numbers, not unit names): R1 never press Upgrade, Finish Now, Speed Up, Construct, Research, Train, Hire, Complete, Claim, Quick Dispatch, Promote, Unlock, Use, Open, Sell or Equip. R2 read a diamond or price figure, never tap it. R3 stop at any march, attack, rally, Arena or PvP surface. R4 close any Confirm dialog with Cancel or X. R5 close a preview only by X or left-edge swipe-back, never a low tap. R6 two failed taps on one target end the unit as partial. R7 no owner name or ID; skip profile and ranking screens.

If this unit reads the HUD, run `python3 _tools_/resource_map.py snap food=<n> iron=<n> coin=<n> --note <this unit id>`. The tool reads only plain numbers with a K or M suffix: write 1.1G as 1100M. Do not enqueue a chain successor; the planner owns this chain.

Red lines: no purchase or diamond spend, no PvP, attack, rally, march, Arena fight or General's Trial fight, no alliance diplomacy, no ally-exchange trade, no speedup or Finish Now, no owner name or identifier values in any record. Any such surface stops the unit as needs-owner.
