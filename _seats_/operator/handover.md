---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-24T13:10:00Z
level: L2
version: 0.17.0
description: The operator's live recipe - run recipe and hazards, research and plunder rules, stat names, gates, open items, links to the route card and the detail sidecar
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT
  - source: operator runs 2026-11-23T06:48Z to 14:30Z, cited in the day INDEX
  - source: coordinator assignments A-20261123-0648-operator to A-20261123-1329-operator and the second-device records 2715 and 2738
  - source: operator runs 2026-11-24T08:08Z to 12:12Z on the new bridge tree, cited in the day INDEX, and the scribe's note of 12:26Z (CU-721)
  - source: successor session f364ec2c runs 20261123T143827Z-dc51cf to 20261123T144558Z-65ae31, records alliance-donations 1441 and resource-collection 1445
---

# Handover - operator

Updated 2026-11-24 12:30Z. Lessons and task-text kit: `_records_/2026-11-22/growth/0054-session-lessons.md`. Detail: `_records_/2026-11-22/growth/0054-operator-handover-detail.md`, `0054-run-hazards.md`. Routes: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. Kit in the same folder: `0054-run-unit.sh` (new-tree runner), `0054-mk-record.py`, `0054-task-texts.csv`. Research: `0054-research-rules.md`; plunder: `0054-plunder-notes.md`; second device: `_records_/2026-11-22/team-operations/2715-second-device.md`.

## Holder

Only the operator holds the device token and sends game input. Reply in four lines (STATUS, ARTIFACT, MEASUREMENT, NEXT), 120 words at most, context percent last. Write scope: queue, `_records_/<date>/`, `_tools_/state/`; never stage.

## Run recipe

- ONE unit, one run, one claim at a time, each BY NAME, its own `queue.py complete` and a record of 350 words or fewer plus a CSV. token-acquire; claim (stale receipt: `queue.py read --record PATH --executor operator`); `cu_bridge.py lock` must read free (a cu run: wait, log a waits row); `killall -9 UserNotificationCenter NotificationCenter`; `lsappinfo` names LastWar; `cu_bridge.py start --app com.lastwar.ios --model claude-gateway/claude-sonnet-5-5`; poll `status --run-id`. 16 steps or fewer (19 screenshots end `context_full`); EXACTLY ONE action per turn; the scrolling top banner is ordinary text.
- Owner-idle wait: restored 20:04Z (OD-23), 0 from the restart after 21:25Z (OD-27), 300 s again from 2026-11-24T08:36:10Z when the bridge moved to the computer-use worktree (CU-720's carry): waits are 0 s on every run since; the cost is cu gate runs holding the lock about 2.4 min.
- Dialogs: TIPS "Enable notifications": Cancel only, never Enable Now. Radar Claim All confirm ("will not grant Alliance Duel points"): Confirm. Consent requests are human-only. "Active on a different device": stop, never Confirm.
- STANDING RULE: a foreground switch stops the run: press nothing, `lsappinfo front` by name, tell the coordinator. A macOS alert: the standing killall only on the coordinator's word. The owner's "Google Chrome for Testing" job: hold, no killall.
- Drags: taps first; a clipped page moves only by the composed pan (hazards page, shop-claims 1301); count written. Never Go, Obtain, a spending Train, Heal or Collect in the Hospital, the gold trophy bubble.

## Trucks and trains

The tram icon (107,580): no badge, no tap (it only pans the camera to the station); with a red badge it opens Intercity Trade (Others' Trucks is the plunder list: read only; Your Truck holds the slots). Own dispatch: rule 2 (SR or above Let's Go once; below SR the free dice, then Trade Contract refreshes through the dice tag); no Mega Mode. A carriage plus bubble plays a cinematic into the Station Platform; boarding: carriage 2, quantity 3, Gift Contract once.

## Game facts

A finished upgrade shows a gift box: one tap is the Complete. Every upgrade runs 23,520 s under the preview time. Barracks Lv.24 and Lv.20 read "Drill Ground Full"; the Lv.30 batch ended 11:18:24Z. Donation grid: 03:57:57.397Z plus k x 1,200 s.

## Open

Oil Well Lv.23 ends 2026-11-24T17:27:28Z; labs 17:30Z and 2026-11-25T02:39Z; the S1 Drone Parts Claim was claimed 13:02Z by the composed pan (next daily pickup after the 18:00 reset).
