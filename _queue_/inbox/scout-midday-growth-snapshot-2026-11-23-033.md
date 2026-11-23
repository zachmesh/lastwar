---
unit: scout-midday-growth-snapshot-2026-11-23-033
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T13:00:13Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T13:15:00Z
window: hq 31 prerequisite buildings below level 30 upgrade previews read only
est_minutes: 10
serves: builder B2 read, HQ 31 prerequisite buildings
chain_id: growth-snapshot-2026-11-23
chain_seq: 33
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# scout-midday

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: builder B2 read, HQ 31 prerequisite buildings

## Brief (planner, HQ 31 prerequisite buildings, upgrade previews, read-only)

serves: builder B2 read, HQ 31 prerequisite buildings

Context: Steer A put the Oil Well and the HQ 31 prerequisite buildings first for the builders at 2026-11-24T09:20Z; the Strategist decides builders 3 and 4 by 08:00Z from these reads. Base map for tap points: `_records_/2026-11-22/growth/1030-base-map.md`.

For each of the Tech Center (about Lv.21 to 26), the Tank, Aircraft and Missile Centers and the Barracks: find the building, tap it, read the tag text (name and level), and open its Upgrade preview. Read the level, the coin, iron and food cost, the BASE and EFFECTIVE time, the power gain and the prerequisite lines; mark which are below Lv.30. The Barracks at Lv.30 already exists (tent B in the base map). Up to three runs, 10 steps each, about two buildings a run.

Never press Upgrade, Finish Now, Speed Up, Obtain or any Go that starts something; close panels with X, a base menu with an empty-ground tap such as (400,640); never tap WORLD (660,940) with a menu open low (the green Upgrade arrow can sit there). A TIPS dialog about another device: STOP and report, never Confirm. Tag text beside every number (the name and level above the building after the tap); none means [G]; one row per building with the frame time. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
