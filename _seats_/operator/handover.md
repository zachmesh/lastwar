---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-26T04:17:00Z
level: L2
version: 0.19.0
description: The operator's live recipe - run recipe and hazards, research and plunder rules, stat names, gates, open items, links to the route card and the detail sidecar
status: unverified
grounded_in:
  - source: team establishment 2026-11-22 19:12 PT
  - source: operator runs 2026-11-23T06:48Z to 14:30Z, cited in the day INDEX
  - source: coordinator assignments A-20261123-0648-operator to A-20261123-1329-operator and the second-device records 2715 and 2738
  - source: operator runs 2026-11-24T08:08Z to 12:12Z on the new bridge tree, cited in the day INDEX, and the scribe's note of 12:26Z (CU-721)
  - source: operator session 2026-11-24T16:00Z to 2026-11-26T04:15Z (records 0025 to 0525, coordinator orders of 06:33Z and 04:15Z)
  - source: successor session f364ec2c runs 20261123T143827Z-dc51cf to 20261123T144558Z-65ae31, records alliance-donations 1441 and resource-collection 1445
---

# Handover - operator

Updated 2026-11-26 04:17Z. Lessons and kit: `_records_/2026-11-22/growth/0054-session-lessons.md`, `0054-operator-handover-detail.md`, `0054-run-hazards.md`, `0054-task-texts.csv`. Routes: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. Second device: `_records_/2026-11-22/team-operations/2715-second-device.md`.

## Holder

Only the operator holds the device token and sends game input. Reply in four lines (STATUS, ARTIFACT, MEASUREMENT, NEXT), 120 words at most, context percent last. Never stage.

## Run recipe

- ONE unit, one run, one claim at a time, each BY NAME, its own `queue.py complete`, a record of 350 words or fewer plus a CSV. token-acquire; claim (stale receipt: `queue.py read --record PATH --executor operator`); `cu_bridge.py lock` free; `lsappinfo` names LastWar; start `--app com.lastwar.ios`; poll. 16 steps or fewer (18 screenshots end `context_full`: read the saved frames yourself); EXACTLY ONE action per turn.
- Owner-idle gate 300 s: `cu_bridge.py lock` shows `owner_idle_seconds`. A person at the Mac (idle near 0) means HOLD, poll read-only, send one line when he leaves; never input over him.
- Dialogs: TIPS "Enable notifications": Cancel only. Radar Claim All confirm ("will not grant Alliance Duel points"): Confirm. Consent requests are human-only. "Active on a different device": the owner's standing approval (OD-20261123-05 and -17: take the session, kick the other device out) is run ONLY by the takeover unit `scout-midday-takeover-session-2026-11-26-001`: ONE Confirm, a 30-minute guard (the dialog returning means someone plays), at most two Confirms in two hours. Steer A withdrew the no-press ruling at 04:05Z (OD-20261126-01); "nobody Confirms without the owner" was the Steers' resume procedure of 11-23 (record 2738), not the owner's.
- Foreground: a switch stops the run: press nothing, `lsappinfo front`, tell the coordinator. The front script does NOT lift LastWar over a UserNotificationCenter window (04:07Z, still in front at 04:08Z): the coordinator asked Steer A about one killall; never read or click that window. Chrome for Testing: hold. `out_of_scope` refusals: stop and tell.
- Map moves: plain drags only (a 1 s hold on a building starts move mode: the red X cancels); the composed pan with its hold only from blank ground 60 px or more from any building. The avatar is never tapped (the VIP unit used its one named exception).
- Privacy: 'the profile page' only; never the owner's name.

## Trucks and trains

The tram icon (107,580): bare icon taps only pan the camera; a badge counts empty slots and opens Intercity Trade. Rule 2 dispatch: SR or above Let's Go once, below SR the free dice then contract refreshes; no Mega Mode. Plunder: Squad 1 25.61M, one Quick Plunder and one Battle each; read the Hospital after.

## Closing rule (Steer A 16:03Z)

DONE: the staged claim was taken (`state_change: yes`) or a verified nothing-to-do quoted (`state_change: no` plus `state_read: <quoted> | <frame> | <HH:MM:SSZ>`); unread state or clipped claim: PARTIAL. Never close DONE to lower the partial rate.

## Open

The Oil Well hand-off `building-queues-oil-well-2026-11-24-005` waits (one builder idle, Lv.24 finished before 05:25Z on 11-25); the takeover retry follows Steer A's answer on the killall.
