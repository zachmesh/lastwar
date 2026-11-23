---
title: Operator handover 0054 detail
created: 2026-11-23T09:10:00Z
modified: 2026-11-23T16:12:00Z
version: 1.8.0
description: Sidecar of the operator handover - the commands, the standing hazards and the links to the route, coordinate, inventory and plunder files and the four topic pages split out of it
status: handover
grounded_in:
  - source: operator session work 2026-11-23T05:30Z to 12:20Z and the runs cited in the day INDEX
  - source: coordinator order to split the page under the 500-word limit, sent in the quiet window of 2026-11-23
---

# Detail for operator handover 0054

Companion to [0054-operator-handover.md](0054-operator-handover.md) and the seat page [handover.md](../../../_seats_/operator/handover.md). Pixel points are in the 1920x1080 screen frame, game window about x 73-715, y 62-980.

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

## Standing hazards

Never press Go on the check-in banner, Details, Buy or a link; a foreground switch or a TIPS different-device dialog stops the run. Close menus at the bare spot (310,660), never (200,610). Full text: [run hazards](0054-run-hazards.md).

## Where the rest is

| File | Holds |
|---|---|
| [0054-coordinates.csv](0054-coordinates.csv) | columns, Backpack tabs and buttons, panel X points |
| [0054-routes.csv](0054-routes.csv) | donations, harvest, plunder, camera, oil, trucks settle, Oil Well taps |
| [0054-inventory-map.csv](0054-inventory-map.csv) | Backpack Resources tab map |
| [0054-plunder-fights.csv](0054-plunder-fights.csv) | one row per plunder fight |
| [0054-run-hazards.md](0054-run-hazards.md), [0054-research-rules.md](0054-research-rules.md), [0054-plunder-notes.md](0054-plunder-notes.md), [0054-oil-well.md](0054-oil-well.md) | the rules and findings by topic |
| [2700-routes.csv](../queue-planning/2700-routes.csv), [tag-index.csv](tag-index.csv) | planner routes, building tags |

Also: records in `_records_/2026-11-22/`; ledger [ledger.csv](ledger.csv); base map [1030-base-map.md](1030-base-map.md); Drill Grounds [1047-f1b-drill-ground.md](1047-f1b-drill-ground.md), [1054-f1c-drill-grounds.md](1054-f1c-drill-grounds.md).

## Changelog

- 1.8.0, 2026-11-23T16:12Z - split from 1,353 body words: coordinates, inventory map, route tables and the plunder results moved to four CSV files, the rules and findings to four topic pages; no fact deleted, the Empty ground point now carries its supersession note.
