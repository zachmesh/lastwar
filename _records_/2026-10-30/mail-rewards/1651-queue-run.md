---
title: Mail rewards queue run
created: 2026-10-30T23:51:00Z
modified: 2026-10-30T23:51:00Z
version: 1.0.0
description: Queue unit mail-2026-10-30-1430 execution
status: partial
---

# Mail rewards - 2026-10-30 about 16:48 to 16:51 PDT queue run

Unit: mail-2026-10-30-1430, executor ticker-1634, computer
session cc-546.
Status partial: no mail category was opened or claimed in
this unit; the work resumes as a fresh unit next tick.
Tracker untouched.

## What happened

- Entry screen was the Alliance page, left over from the
  help unit in the same pass. The mail regular needs the
  base screen, so the Alliance back arrow had to be used
  first.
- Back-arrow taps at norm 53,953, 86,952, 93,952, 70,945
  and a double-click at 93,952 all dispatched with no
  change; the screen stayed on the Alliance page in every
  closing screenshot. The system twice flagged these as
  background clicks not reaching the control, the same
  intermittent background-click failure seen with the
  Help button earlier in this pass (which did register
  on a re-grounded tap at 732,491).
- No Claim All, no Delete All, no other button was
  touched. In particular Delete All was never pressed.
- The game is left on the Alliance page; the successor
  mail unit should re-ground the back arrow on its own
  screenshot before tapping, rather than reusing these
  points blindly.

## Close

- Partial, not failed: the mail check itself was never
  reached, and the regular remains due for the next tick.
