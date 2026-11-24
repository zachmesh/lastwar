---
title: Operator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-24T16:12:00Z
level: L2
version: 0.18.0
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

Updated 2026-11-24 16:12Z. Lessons and kit: `_records_/2026-11-22/growth/0054-session-lessons.md`, `0054-operator-handover-detail.md`, `0054-run-hazards.md`, `0054-run-unit.sh`, `0054-mk-record.py`, `0054-task-texts.csv`. Routes: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`. Research: `0054-research-rules.md`; plunder: `0054-plunder-notes.md`; second device: `_records_/2026-11-22/team-operations/2715-second-device.md`.

## Holder

Only the operator holds the device token and sends game input. Reply in four lines (STATUS, ARTIFACT, MEASUREMENT, NEXT), 120 words at most, context percent last. Write scope: queue, `_records_/<date>/`, `_tools_/state/`; never stage.

## Run recipe

- ONE unit, one run, one claim at a time, each BY NAME, its own `queue.py complete` and a record of 350 words or fewer plus a CSV. token-acquire; claim (stale receipt: `queue.py read --record PATH --executor operator`); `cu_bridge.py lock` free (else wait, log a waits row); pre-start killall; `lsappinfo` names LastWar; `cu_bridge.py start --app com.lastwar.ios --model claude-gateway/claude-sonnet-5-5`; poll `status --run-id`. 16 steps or fewer (19 screenshots end `context_full`); EXACTLY ONE action per turn; the scrolling banner is ordinary text.
- Owner-idle wait: 300 s since 2026-11-24T08:36:10Z (CU-720's carry); waits are 0 s on every run; the cost is cu gate runs holding the lock about 2.4 min (log a waits row, note OTHER).
- Dialogs: TIPS "Enable notifications": Cancel only. Radar Claim All confirm ("will not grant Alliance Duel points"): Confirm. Consent requests are human-only. "Active on a different device": stop.
- STANDING RULE: a foreground switch stops the run: press nothing, `lsappinfo front` by name, tell the coordinator. A macOS alert (the owner's Screen Recording prompt, recurs about 22:07Z): only after the coordinator's restore word, `killall -9 UserNotificationCenter NotificationCenter`, `lsappinfo front`; respawn: wait 30 s, once more; still in front: stop. Never open or read the window. Chrome for Testing: hold.
- Drags: taps first; a clipped page moves only by the composed pan (hazards page); the Backpack grid did not move under it (1601). Never Go, Obtain, a spending Train, Heal or Collect in the Hospital, the gold trophy bubble.

## Trucks and trains

The tram icon (107,580): no badge, no tap (a truck unit; the train read may tap it: a camera pan only); a badge opens Intercity Trade on Your Truck. A lone returned truck lights the badge; an empty slot at 5/5 does not; one slot tap settles and puts it out. Rule 2 dispatch: SR or above Let's Go once, below SR the free dice then contract refreshes (more by the coordinator's word); no Mega Mode. Boarding: carriage 2, quantity 3.

## Closing rule (Steer A 16:03Z)

DONE: the staged claim was taken, or a verified nothing-to-do state quoted as `state_read: <quoted> | <frame> | <HH:MM:SSZ>`; no evidence line: PARTIAL; unread state, alert, absent badge or clipped claim: PARTIAL. Never close DONE to lower the partial rate.

## Game facts

A finished upgrade shows a gift box: one tap is the Complete. Upgrades run 23,520 s under the preview time. Barracks Lv.24, Lv.20 and Lv.30 read "Drill Ground Full". Donation grid: 03:57:57.397Z plus k x 1,200 s.

## Open

Oil Well Lv.23 ends 17:27:28Z; labs 17:30Z and 11-25T02:39Z; the Weekly Pass page: five composed pans from the top reach the Coin card (pickups reset 18:00 server time).
