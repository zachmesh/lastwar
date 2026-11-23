---
title: Operator handover 0054 detail
created: 2026-11-23T09:10:00Z
modified: 2026-11-23T12:20:00Z
version: 1.1.0
description: Sidecar of the operator handover - commands, screen coordinates, inventory map, ledger and record paths; the base map and the tag index moved out to their own records
status: handover
grounded_in:
  - source: operator session work 2026-11-23T05:30Z to 12:20Z and the runs cited in the day INDEX
---

# Detail for operator handover 0054

Companion to [0054-operator-handover.md](0054-operator-handover.md). Pixel points are in the 1920x1080 screen
frame, game window at about x 73-715, y 62-980.

## Commands

| Need | Command |
|---|---|
| token | `python3 _tools_/queue.py token-acquire --executor operator`, `token-release` |
| claim, complete | `queue.py claim --unit U --executor operator`, `complete --unit U --status done` with `--summary --evidence --follow-up --stat --rules-used --rule-failed --rule-gap` |
| read receipt | `queue.py read --record PATH --executor operator` when a claim is refused |
| poll, stop a run | `cu_bridge.py status`, `control --run-id ID --command stop`; final text in `run.json` |
| desktop gate | `node /Users/zhenchen/dtadpole/computer-use/_environments_/macos-desktop/run-lock.mjs status` |
| record gate | `python3 _tools_/lint-gate/lint_gate.py record-check FILE` |
| send reply | `DSH_WEB_URL=http://localhost:8080 SESSION_RELAY_JAR=/tmp/dsh-gate.cj python3 ~/dtadpole/reflection/_tools_/session-relay/session-relay.py send --runtime dsh --session session-4b4cb08d-fb77-419a-be34-14a72a3b73d1 --text "$(cat FILE)"` |

## Coordinates

| Target | Point |
|---|---|
| Right column | Alliance 670,708; Mail 670,787; Inventory 670,852; Events 673,165 |
| Left column | hammer (builders) 108,200; flask (research) 110,258; trade or train shortcut 107,580 |
| Camera restore | WORLD 660,940, then the same button (BASE); never with a menu open |
| Backpack tabs | Special 137,154; Resources 240,154; Speed-up 342,154; Heroes 445,154; Gear 548,154; Gift 651,154 |
| Backpack quantity | minus 180,823; slider handle right end 456,825, left 200,825; plus 494,823; number field 573,823 (a tap does nothing) |
| Backpack buttons | Use 400,920 (never by default); back arrow 112,914 |
| Panel X | 609,217 (upgrade panels), 611,222 (tech node), 611,281 (TRAIN UNITS) |
| Empty ground | 400,640 (the old 200,610 is a Gold Mine Lv.28) |

## Inventory map (Resources tab)

- The tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use; the Resource Chest (20,862) defaults to its
  full stock. Row 3: Resource Choice Chest UR 552; row 4: SSR 587, SR 1,522, Resource Chest, Food Chest UR.
- One drag of 260 px scrolls the grid; coin chests UR 87 (2.43M each, max per Use = stock), SSR 71, SR 122 sit lower.

## Paths and links

- Ledger `_records_/2026-11-22/growth/ledger.csv`; records in `_records_/2026-11-22/`.
- Base map and hazards: [1030-base-map.md](1030-base-map.md); Drill Grounds: [1047-f1b-drill-ground.md](1047-f1b-drill-ground.md),
  [1054-f1c-drill-grounds.md](1054-f1c-drill-grounds.md); building tags: [tag-index.csv](tag-index.csv).
