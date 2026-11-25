---
title: Operator run recipe and hazards 0054
created: 2026-11-23T16:12:00Z
modified: 2026-11-25T01:03:00Z
version: 2.3.0
description: Operator sidecar page - the run recipe and hazard rules, including the hung-screen relaunch rule; the measured rows (times, frames, counts) are in the CSV beside it
status: handover
grounded_in:
  - source: handover 0.9.0 section Run recipe and hazards, moved 2026-11-23T15:12Z into the sidecar detail page and split out 2026-11-23T16:12Z
  - source: sidecar rows Run shape (records alliance-donations 1441, resource-collection 1445) and Never (shop-claims 1528-t3-focus-incident.md)
  - source: measured rows in 0054-run-hazards.csv; the hung-screen rule from Steer A's standing rule of 2026-11-24T20:26Z, relayed by the Scribe and the Coordinator
---

# Run recipe and hazards

Part of [the sidecar](0054-operator-handover-detail.md); measured rows: [0054-run-hazards.csv](0054-run-hazards.csv).

## Run recipe

- Claim BY NAME (stale read receipt: `queue.py read`), `killall -9 UserNotificationCenter NotificationCenter`, `lsappinfo front` names LastWar, `cu_bridge.py start --app com.lastwar.ios`; turn 1 a NO-CLICK frame, last turn a report.
- Desktop gate: `cu_bridge.py lock`; on a refusal wait and log a waits row.

## Never

- The Thanksgiving Lottery tab: never opened again; the Gift of Thanks and the draw button stay unread.
- Backpack Resources opens with the 5,000 Diamonds tile SELECTED and a live Use: never press Use.
- The Go button on the check-in banner opens Chrome; a consent request is human-only.
- A macOS alert (UserNotificationCenter): hold; the standing killall only on the coordinator's word; "Google Chrome for Testing": hold.

## Hung screen: controlled relaunch

A HUNG SCREEN (a full-window loading screen or an unresponsive window with no HUD, 15 MINUTES with no progress, one back-arrow tap that changed nothing) is repaired by a controlled relaunch, authorized in advance for the Operator: (1) the app menu Quit, never a key chord, Escape or force quit; (2) the standing front script reopens it; (3) read the first frame after the login: TIPS 'Enable notifications': Cancel only; 'active on a different device': ONE Confirm, never a second within 30 minutes; (4) re-read the HUD and the builders' and labs' timers against the last known ends: a mismatch goes to the Coordinator; (5) the 300 s owner-idle gate applies; (6) ONE UNIT, cap 0.60 USD, dispatched by the Coordinator without waiting for Steer A.

## Pans and drags

- A clipped page moves only by the composed pan, in ONE message: mouse_move to the start on the blank right margin, left_mouse_down, wait 1 s, ONE move of 175 px, wait 1 s, left_mouse_up, then the screenshot; a malformed wait refuses the batch. 
- The Backpack grid and the Store list: a margin pan moves 0 px; a pan from a gap between tiles inside the grid moves it.
- A wait over 10 s is refused: three 10 s waits do 30 s.

## Badges and upgrades

- A stale tram dot: ONE WORLD tap and ONE BASE tap (no icon tapped) refresh it; the tram icon is not drawn while no truck waits.

## Profile and VIP

The avatar opens the profile: never tap it. If the profile like dialog 'You're very popular!' is open, tap its one 'Awesome!' button once, then the profile's X once to the base, nothing else on the profile. The VIP lines are read from the VIP panel (the VIP entry in the left column or the HUD, read-only) or stay unreadable. The profile shows the owner's in-game name: no record carries it, not in a summary, a frame description or a state_read: write 'the profile page' only.
