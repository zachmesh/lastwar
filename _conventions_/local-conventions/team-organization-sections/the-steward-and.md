---
title: The Steward and the Coordinator
created: 2026-11-23T07:02:07Z
modified: 2026-11-23T07:02:07Z
version: 0.1.0
sequence: 4
description: The owner's root session is the Steward, session-eb024f72-e661-4a77-9303-66af95dbcfd1, titled lastwar Steward.
---
### The Steward and the Coordinator

The owner's root session is the **Steward**, `session-eb024f72-e661-4a77-9303-66af95dbcfd1`,
titled `[lastwar] Steward`. It is the owner gateway, not a seat: it holds
no write scope, takes no assignment, and runs no loop schedule. It
relays owner instructions and approvals to the Coordinator and receives
`needs-owner` escalations.

By the reflection convention every team has exactly one **Coordinator**.
The Coordinator is a separate top-level seat
(`session-4b4cb08d-fb77-419a-be34-14a72a3b73d1`) that owns the 900-second
loop clock, dispatches the other seats and keeps `TEAM.yaml`. The
Coordinator seat was moved from the Steward to its own session on
2026-11-23T04:04Z; the Steward deleted its old 900-second schedule in the
same turn, so there is exactly one clock.

