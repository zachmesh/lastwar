---
title: Device access
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 7
description: Retry the device-access error at least 3 times (owner rule, 2026-10-26).
---
## Device access

- **Retry the device-access error at least 3 times** (owner rule,
  2026-10-26). The error reporting that a run lacks owner-authorized
  device access is unreliable - runs have held access for minutes
  and then hit it mid-run (2026-10-26, the 0435, 0448 and 0456
  runs). When it appears, do not abandon the run at once - reopen
  the computer session and try again, at least 3 attempts, before
  recording the run as access-failed. The owner has confirmed the
  authorization stands and is not to be asked about again.

- **Kick the other device out** (owner rule, 2026-10-27). When the
  game shows the "active on a different device" dialog, the agent
  is authorized to click Confirm and take the session over on the
  Mac, kicking the other device - every time the dialog appears.
  The app exits; reopen it and continue. The dialog alone never
  ends a run. Only after two takeovers in the same run, if the
  dialog still returns, record the run as contested - the owner
  is likely playing on his phone at that moment - and stop.

