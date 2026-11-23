---
unit: scout-midday-growth-snapshot-2026-11-23-032
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-23T13:00:12Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T13:15:00Z
window: hq 31 upgrade preview all rows and prerequisite lines read only
est_minutes: 10
serves: builder B2 read, HQ 31 prerequisite buildings
chain_id: growth-snapshot-2026-11-23
chain_seq: 32
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T13:45:51Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the HQ 31 prerequisites were measured in the 1308 read
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

Serves: builder B2 read, HQ 31 prerequisite buildings

## Brief (planner, HQ 31 preview and prerequisites, read-only)

serves: builder B2 read, HQ 31 prerequisite buildings

Context: Steer A put the Oil Well and the HQ 31 prerequisite buildings first for the builders at 2026-11-24T09:20Z; the Strategist decides builders 3 and 4 by 08:00Z from these reads. Base map for tap points: `_records_/2026-11-22/growth/1030-base-map.md`.

Open the Headquarters (Lv.30) and its Upgrade preview. Read EVERY row, including the ones cut off at the edge (a left-edge swipe or a second look): the prerequisite lines with their check marks (the Base Expansion research, the Tech Center, a Tank, Aircraft or Missile Center and the Barracks, each with its required level), and the coin, iron, food and oil costs, the BASE and EFFECTIVE time, the power gain, the Hero Level Cap and the hero lines. Write which prerequisite lines are met and which are red. A Go button beside a prerequisite line may jump to that building: allowed, then close it.

Never press Upgrade, Finish Now, Speed Up, Obtain or any Go that starts something; close panels with X, a base menu with an empty-ground tap such as (400,640); never tap WORLD (660,940) with a menu open low (the green Upgrade arrow can sit there). A TIPS dialog about another device: STOP and report, never Confirm. Tag text beside every number (the name and level above the building after the tap); none means [G]; one row per building with the frame time. Rules and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD per run (the harness stops near 0.36 of it).
