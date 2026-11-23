---
title: Scope and availability part 2
created: 2026-11-23T06:53:20Z
modified: 2026-11-23T06:53:20Z
version: 0.1.0
sequence: 13
description: Server maintenance windows (2026-11-10 2340) - a maintenance shutdown is announced by a server banner about
---
- Server maintenance windows (2026-11-10 2340) - a maintenance
  shutdown is announced by a server banner about 7 minutes
  ahead (seen 23:14 in the 2319 donations unit) and, once it
  lands, the game shows "Server disconnected. Please restart
  the game." - click_element on Confirm does nothing, a
  coordinate tap at 501,545 exits the app (the restart itself,
  not a crash). Relaunch shows a SYSTEM ANNOUNCEMENT "Update
  complete, please restart the game." (Confirm 502,568 -
  click_element no-change, coordinate tap dismisses and the
  game restarts). Then "The server is under maintenance.
  Please wait a moment, we'll be back with you shortly."
  with Cancel / Confirm, plus "Login failed. Please retry or
  contact Support" at the bottom - one Confirm tap at 634,568
  retries the login and the game loads to the base screen.
  The maintenance came back on its own; no "active on a
  different device" dialog appeared. Do not treat the
  disconnect as a crash - recover through the dialog
  sequence and keep the unit going.

