---
title: Queue Planning Fixed State Power Units And Snap Fix 2354 2026-11-22
created: 2026-11-22T23:56:00Z
modified: 2026-11-22T23:56:00Z
level: L0
version: 1.0.0
description: Planner pass - the two fixed-state power baseline units minted, Season Photo moved ahead of the growth units by queue order, and a snap crash on G-suffixed values found and fixed in 20 briefs
status: done
activity: queue-planning
run_id: queue-planning-2026-11-22-2354-power-units-and-snap-fix
trigger: coordinator message after the 18 growth units
started_at: 2026-11-22T23:52:00-08:00
finished_at: 2026-11-22T23:56:00-08:00
verified: parse_amount tested on six inputs without writing state; the 20 patched briefs and three unit windows read back; pick order simulated at three instants; validate exit 0
grounded_in:
  - source: _tools_/resource_map.py parse_amount at line 21 and snap at lines 58 to 74
  - source: _records_/2026-11-22/queue-planning/2350-growth-units-staged.md
  - source: coordinator instruction for the fixed-state pair and Season Photo
---

# Power units and the snap fix, 2354

## 1. Fixed-state power pair

Regular `scout-midday`, priority 2, 10 minutes, one chain per slot and day so the ids are unique and predictable:

- **Slot B, today:** `scout-midday-growth-power-b-2026-11-23-001`, 2026-11-23T13:00Z to 15:00Z.
- **Slot A, next:** `scout-midday-growth-power-a-2026-11-24-001`, 2026-11-24T02:00Z to 04:00Z. The coordinator expects the first A read at about 02:10Z.

The brief is P1-type: open Power Details, expand every chevron, record every line including tech and troop with the UTC time of each capture, note whether troops are marching or in the hospital, then run `resource_map.py snap` with the breakdown. Builders are optional if steps remain.

**Daily pass, from now on:** mint the same pair for the next date, chains `growth-power-b-<date>` and `growth-power-a-<date>`, B at 13:00Z to 15:00Z and A at 02:00Z to 04:00Z.

## 2. Season Photo first

`next` returned Season Photo (`passes-2026-11-23-0712`) as the only eligible unit at 07:52Z. But `next` sorts by expiry first, and its expiry of 12:00Z would have ranked it sixth at 08:00Z behind the core units expiring 08:43Z to 08:45Z. I edited that one unclaimed unit's `expires_at` to 08:42Z by hand. It now ranks first at 07:55Z, 08:00Z and 08:30Z, so the order lives in the queue. If it is not started by 08:42Z it expires and I re-mint it.

## 3. A crash I found and fixed

`resource_map.py snap` uses `parse_amount`, which understands only K and M suffixes (line 21). The HUD shows iron as 1.1G, and my 18 growth briefs said to enter values as shown. Tested without writing state: `1.1G` raises a ValueError; `1100M`, `732.3M`, `565.1K` and plain integers work. I patched the guidance in all 18 growth units (all still unclaimed) and wrote it into the two new units: write 1.1G as 1100M.

Breakdown keys such as `power_hero` are not in `resources.json`, so `snap` prints an unknown-resource warning for each. The values are still saved.

## 4. Proposals

- **Toolsmith:** accept a G suffix in `parse_amount`, and add `power_hero`, `power_drone`, `power_building`, `power_tech` and `power_troop` to `resources.json`.
- If the operator's 07:43Z assignment already ran `snap` with a G value, it will have printed a traceback and saved nothing; the coach should check `resources.jsonl` for that run.
