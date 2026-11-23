---
title: Second play hold and a near collision - 2026-11-22 21:44 PT
created: 2026-11-22T21:44:00-08:00
modified: 2026-11-22T21:46:00-08:00
level: L3
version: 0.1.0
description: The Steward opened a fixed-end hold for the owner's GitHub login one minute after a unit was dispatched; the run was stopped after one navigation click, and the coordinator's first all-clear misreported the click
status: done
activity: team-operations
run_id: team-operations-2026-11-22-2144-hold-incident
trigger: Steward hold 2026-11-23T05:44Z, hard end 05:58Z
started_at: 2026-11-22T21:44:00-08:00
finished_at: 2026-11-22T21:46:00-08:00
duration_seconds: 120
verified: bridge status of run 20261123T054400Z-f957de read at 05:44:31Z; operator reply with exact stop time; claimed folder and unit state read
---

# Second play hold and a near collision

## Timeline (UTC)

- 05:43:32 `A-20261123-0443-operator` (scout-midday) delivered.
- 05:43:59 the operator claims the unit; 05:44:00 desktop run `20261123T054400Z-f957de` starts.
- 05:44 the Steward's hold arrives: no desktop unit until 05:58Z; it asked to be told at once of any dispatch in the last minute.
- 05:44:03 I steered the operator to stop; 05:44:05 its one click, the Events icon (navigation only); 05:44:09.8 stop; 05:44:12 unit and token released.
- 05:44:25 I told the Steward not to open the window; 05:44:31 all-clear sent.

## Reading

- The run was cancelled after 1 step, 1 click, no claim, nothing priced, no scout record. The unit is in the inbox, attempts 1 of 3. The game was left on the Events hub, not the base.
- **My error:** the all-clear said no game input was sent. The bridge showed one action done; I read its "looked at app" step line as an observation. The operator's reply and the bridge counter say one click. Corrected to the Steward at 05:45Z.
- **Cause:** I dispatched one minute before the hold; neither side could have known. The cost was a live run that had to be stopped.

## Rule going forward

Before any dispatch, read the bridge and the last Steward message; after a stop, report the bridge's action counter and the operator's own account, not a step label. A hold with a fixed end is obeyed to the minute.

## Follow-up

Release comes from the Steward by 05:58Z. Then the 1-hour Secret Missions claim (overdue, plunder risk) goes first, then the scout replay.
