---
title: Zombie Invasion Execution 2026-10-28 0347 Queue Run
created: 2026-10-28T10:55:00Z
modified: 2026-10-28T10:55:00Z
level: L0
version: 0.1.0
description: Zombie-invasion chain unit 002 - claimed and session opened, then the device channel returned the known unreliable authorization error on every further call; recorded access-failed after 3 retries, chain continues
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, and the task unit queue ticker
  - source: recording rules - the device-access error is unreliable and a run is recorded access-failed only after at least 3 attempts
---

# Zombie Invasion — execution, 2026-10-28 03:47 queue unit 002

A single task unit, executed by executor ticker-0334 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-002,
chain zombie-2026-10-28, priority 4. Status — not performed;
access-failed as defined below. Metadata for this type lives in
[`_activities_/zombie-invasion/`](../../../_activities_/zombie-invasion/INDEX.md).

## What happened

- The unit was claimed after unit 001 closed partial with
  cleared false, and the device token was re-acquired (held
  to 11:01 UTC). A computer session opened and the game was
  activated; the world map near the home base was visible.
- The screen then showed the Mail index (the game had been
  left or landed there; no mail was opened, claimed or
  deleted by this unit - mail is a different task type).
  The plan was to read only the Battle Report list to verify
  unit 001's zombie march, which is evidence for this chain.
- Every further device call - a click, a session end, and a
  fresh session start, 3 attempts in all - returned the
  error claiming this schedule lacks owner-authorized device
  access. That claim is false under the owner authorization
  of 2026-10-26, extended to the queue on 2026-10-28, and
  the recording rules name this exact error unreliable;
  after the required 3 attempts the unit is recorded
  access-failed and the pass stops here. Unit 001 in this
  same pass played normally, so the channel worked minutes
  earlier in this same schedule.
- No zombie was fought in this unit (zombies_killed 0),
  cleared stays false, the tracker is untouched for a
  failed unit, and the next chain unit was enqueued so a
  later pass resumes the chain. Nothing bought, no diamond
  spent, no item used.
