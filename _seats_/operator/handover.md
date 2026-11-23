---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-23T18:16:00Z
level: L2
version: 0.14.0
description: The operator's live recipe - run recipe and hazards, research and plunder rules, stat names, gates, open items, links to the route card and the detail sidecar
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT
  - source: operator runs 2026-11-23T06:48Z to 14:30Z, cited in the day INDEX
  - source: coordinator assignments A-20261123-0648-operator to A-20261123-1329-operator and the second-device records 2715 and 2738
  - source: successor session f364ec2c runs 20261123T143827Z-dc51cf to 20261123T144558Z-65ae31, records alliance-donations 1441 and resource-collection 1445
---

# Handover - operator

Updated 2026-11-23 16:05Z. Detail (commands, coordinates, routes, long rules): `_records_/2026-11-22/growth/0054-operator-handover-detail.md`, `tag-index.csv`. Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`, `2700-routes.csv`. Second device: `_records_/2026-11-22/team-operations/2715-second-device.md`, `2738-owner-orders-and-takeover.md`.

## Holder

Only the operator holds the device token and sends game input. Reply to the coordinator in four lines (STATUS, ARTIFACT, MEASUREMENT, NEXT) plus context percent. Write scope: queue, `_records_/<date>/`, `_tools_/state/`.

## Run recipe and hazards

- token-acquire; claim BY NAME (stale receipt: `queue.py read --record PATH --executor operator`); in one shell `killall -9 UserNotificationCenter NotificationCenter`, `lsappinfo` names LastWar, `cu_bridge.py start --app com.lastwar.ios --model claude-gateway/claude-sonnet-5-5 --max-steps 8 --max-cost 0.5`. Task text: never ask, never zoom or Escape, turn 1 NO-CLICK, last turn a report. Release the token after a unit.
- (400,640) is safe only on a fresh camera: WORLD then BASE (660,940) first with no menu open, or tap a bare spot such as (310,660); never (200,610) (a Gold Mine); no bubble taps.
- Read `run-lock.mjs status` before each run; a cu run there means wait. After a `local_input` pause or a `gateway_unreachable` run: retry once.
- STANDING RULE (Steer A, 15:28Z): an action that may open another app, browser, store or payment surface needs Steer A's approval first, with an exit plan; never click Go on the check-in banner (web store in Chrome). An unexpected foreground switch STOPS the run: press nothing, answer nothing, touch nothing there, tell the coordinator in minutes. Consent requests are human-only. TIPS "active on a different device": same stop; never Confirm.
- Exclusive lease: in a cu quiet window (today 16:10Z to 16:35Z, 17:10Z to 17:25Z, 18:35Z to 18:50Z) `token-acquire` and `claim` are refused (exit 1): record the text and time, wait, tell the coordinator; never `--ignore-token`; finish by 16:09Z, 17:09Z, 18:34Z.

## Research and plunder

- Research: read the Finish Now clock (M 3.678); tech speed-up items only, name and quantity read before each press; reserves in the sidecar.
- Trade trucks only (OD-20261123-20): hospital first (tag Hospital, orange middle button; free room = 7,999 minus Completed minus wounded; stop under 1,000 or after two fights each wounding over 100); the opened card decides: UR or SSR, guard below 24.96M, a UR shard stack in either half, arrival over 30 minutes; Quick Plunder and Battle once; never Collect.
- Blocked training closes with `--stat slots_blocked_by_capacity=N --stat capacity_blocker="Drill Ground Full"`.

## Open

Labs busy until 2026-11-24T17:30Z and 2026-11-25T02:39Z; builders free 2026-11-23T23:20:12Z (four Training Base upgrades, read 18:07Z); Lv.27 batch about 19:56Z; HQ 31 needs Base Expansion, 433.5M coin, 1.3G iron, food. Plunder count 4/4 today, shard payout varies. Donation refill: 20-minute grid (14:57:57.397Z plus k x 1,200 s; record alliance-donations 1745). Trade icon (107,580) absent since 16:39Z.

Oil: collect via the OIL panel (231,115; Collect 553,501; X 612,209) every 8 hours, next about 23:30Z. Oil Well Lv.20 is at the north-east wall (pan route in the sidecar); Lv.20 to 21 costs iron 8.5M, 09:20:18; Details is not approved: never.
