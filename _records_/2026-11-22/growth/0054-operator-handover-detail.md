---
title: Operator handover 0054 detail
created: 2026-11-23T09:10:00Z
modified: 2026-11-23T09:10:00Z
version: 1.0.0
description: Sidecar of the operator handover - commands, screen coordinates, inventory map, ledger and record paths
status: handover
grounded_in:
  - source: operator session work 2026-11-23T05:30Z to 09:10Z and the runs cited in the day INDEX
---

# Detail for operator handover 0054

Companion to [0054-operator-handover.md](0054-operator-handover.md). Pixel points are in the
1920x1080 screen frame, game window at about x 73-715, y 62-980.

## Commands

| Need | Command |
|---|---|
| token | `python3 _tools_/queue.py token-acquire --executor operator`, `token-release` |
| claim, complete | `queue.py claim --unit U --executor operator`, `complete --unit U --status done` with `--summary --evidence --follow-up --stat` |
| read receipt | `queue.py read --record PATH --executor operator` when a claim is refused |
| poll a run | `cu_bridge.py status --run-id ID`, final text in `run.json` result.finalMessage |
| stop a run | `cu_bridge.py control --run-id ID --command stop` |
| snapshot | `resource_map.py snap food=641.3M iron=1000M coin=9.7M diamonds_red=11136 total_power=150211809 stamina=195` |
| record gate | `python3 _tools_/lint-gate/lint_gate.py record-check FILE` |
| send reply | `DSH_WEB_URL=http://localhost:8080 SESSION_RELAY_JAR=/tmp/dsh-gate.cj python3 ~/dtadpole/reflection/_tools_/session-relay/session-relay.py send --runtime dsh --session session-4b4cb08d-fb77-419a-be34-14a72a3b73d1 --text "$(cat FILE)"` |

## Coordinates

| Target | Point |
|---|---|
| Inventory button | 670,850 |
| Backpack tabs | Special 137,154; Resources 240,154; Speed-up 342,154; Heroes 445,154; Gear 548,154; Gift 651,154 |
| Backpack grid | y 190 to 650, a drag starts inside it, one drag scrolls about 3 to 4 rows |
| Backpack quantity | minus 180,823; slider handle right end 456,825, left end 200,825; plus 494,823; number field 573,823 |
| Backpack buttons | Use 400,920; back arrow 112,914 |
| Jeep, Secret Command Post | 107,647; Claim button about 575,489 |
| Panel X (upgrade panels) | 609,217; TRAIN UNITS X 611,281 |
| Empty ground spot | 250,650 |

## Inventory map (Resources tab, scrolled one drag)

- Special tab: Mystery Supply Box (3rd row, 2nd tile, 365 left), Violet's Loot 139.
- Resources tab, top: diamond items (5,000 x16 selected by default), Resource Choice Chest UR
  552 (3rd row, 4th tile), row 4 tiles: SSR 587, SR 1,523, Resource Chest 20,753, Food Chest UR.
- After one drag: iron chests, coin chests UR 87, SSR 71, SR 122 (3rd row, 574,467 is SR).

## Paths

- Ledger `_records_/2026-11-22/growth/ledger.csv`; records in `_records_/2026-11-22/`.
- Records read before this: 0054-box-chest-read.md, 0009-inventory-read.md, 0030-capacity-read.md.
