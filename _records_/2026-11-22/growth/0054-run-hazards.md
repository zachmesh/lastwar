---
title: Operator run recipe and hazards 0054
created: 2026-11-23T16:12:00Z
modified: 2026-11-24T20:47:00Z
version: 2.2.0
description: Operator sidecar page - the run recipe and hazard rules, including the hung-screen relaunch rule; the measured rows (times, frames, counts) are in the CSV beside it
status: handover
grounded_in:
  - source: handover 0.9.0 section Run recipe and hazards, moved 2026-11-23T15:12Z into the sidecar detail page and split out 2026-11-23T16:12Z
  - source: sidecar rows Run shape (records alliance-donations 1441, resource-collection 1445) and Never (shop-claims 1528-t3-focus-incident.md)
  - source: measured rows in 0054-run-hazards.csv; the hung-screen rule from Steer A's standing rule of 2026-11-24T20:26Z, relayed by the Scribe and the Coordinator
---

# Run recipe and hazards

Part of [the sidecar](0054-operator-handover-detail.md); the short form is in `_seats_/operator/handover.md`; measured rows: [0054-run-hazards.csv](0054-run-hazards.csv).

## Run recipe

- Claim BY NAME (stale read receipt: `queue.py read --record PATH --executor operator`), `killall -9 UserNotificationCenter NotificationCenter`, `lsappinfo front` names LastWar, `cu_bridge.py start --app com.lastwar.ios`; turn 1 a NO-CLICK frame, last turn a report.
- Safe point for menus: the bare spot (310,660) after WORLD then BASE (never (400,640) after a camera shift); no bubble taps.
- Desktop gate: `cu_bridge.py lock`; on a refusal wait and log a waits row.

## Never

- The Thanksgiving Lottery tab: never opened again; the Gift of Thanks and the draw button stay unread.
- Backpack Resources opens with the 5,000 Diamonds tile SELECTED and a live Use: never press Use.
- The Go button on the check-in banner opens Chrome ([1528-t3-focus-incident.md](../shop-claims/1528-t3-focus-incident.md)); a consent request is human-only.
- A macOS alert (UserNotificationCenter): hold; the standing killall only on the coordinator's word; "Google Chrome for Testing": hold, no killall.

## Hung screen: controlled relaunch

A HUNG SCREEN (a full-window loading screen or an unresponsive window with no HUD, 15 MINUTES with no progress, one back-arrow tap that changed nothing) is repaired by a controlled relaunch, authorized in advance for the Operator: (1) the app menu Quit, never a key chord, Escape or force quit; (2) the standing front script reopens it; (3) read the first frame after the login: TIPS 'Enable notifications': Cancel only; 'active on a different device': ONE Confirm (the owner's standing order), never a second within 30 minutes; (4) re-read the HUD and the builders' and labs' timers against the last known ends: a mismatch goes to the Coordinator; (5) the 300 s owner-idle gate applies; (6) ONE UNIT, cap 0.60 USD, dispatched by the Coordinator without waiting for Steer A (he is told after). Evidence and the first-frame state: the CSV row hung_screen_relaunch.

## Pans and drags

- A clipped page moves only by the composed pan, in ONE message: mouse_move to the start on the blank right margin, left_mouse_down, wait 1 s, ONE move of 175 px, wait 1 s, left_mouse_up, then the screenshot; a malformed or missing wait refuses the whole batch. A single drag event moves nothing or flings.
- The Backpack grid and the Thanksgiving Store list: the margin pan moves 0 px (stop at one try).
- A wait over 10 s is refused: three 10 s waits do 30 s. One drag per turn.

## Badges and upgrades

- A stale tram dot: ONE WORLD tap and ONE BASE tap (no icon tapped) refresh it; the tram icon is not drawn while no truck waits.
- A finished upgrade shows a wrapped gift box; one tap on its body is the Complete.
- Cu gate runs hold the lock about 2.4 min: poll `cu_bridge.py lock`.
