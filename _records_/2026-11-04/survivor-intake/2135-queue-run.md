---
title: Survivors 2026-11-04 ticker-2134 queue run
created: 2026-11-04T21:35:00-08:00
executor: ticker-2134
unit: survivors-2026-11-04-1803
regular: survivors
activity: survivor-intake
status: failed
---

# Survivors queue run ticker-2134

Session window: 2026-11-04 about 21:35 to 21:36 America/Los_Angeles.
Unit: survivors-2026-11-04-1803 (planned for 2026-11-05T02:03:00Z,
expires 2026-11-05T06:03:00Z).

## What was done

- Own PRs checked first: open records PR 293 for records/2026-11-04
  is clean and mergeable per gh, carries no comments and no question
  addressed to this job, and names Owner lastwar-pr-integrator, not
  this job. No own-PR work was owed.
- Queue sync: reaped 0, expired 0, produced nothing new - 21
  regulars already queued. No zombie chain was seeded: the Zombie
  Invasion event ended at about the 19:00 reset on 2026-10-30, and
  the seeding rule forbids a fresh chain until a Zombie Invasion
  tab is seen live again.
- Device token acquired by ticker-2134. Next unit picked:
  survivors-2026-11-04-1803, claimed.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) was online and
  LastWar was running fullscreen 1920x1080 (pid 59735), with Google
  Chrome frontmost.

## Outcome: failed, no game input dispatched

- Every screen-capture attempt failed with the same error:
  "Failed to start stream due to audio/video capture failure".
- Attempts: computer.observe compact (twice), computer.observe
  image (once), computer.control activate (twice), across two
  computer sessions (cc-488, cc-489). A session restart did not
  clear it - the same failure returned on the fresh session.
- No game screen was ever read, so the gate line could not be
  verified and no tap was dispatched while blind. No survivor was
  recruited, no Quick Dispatch was run, no figure was read.
- This is the same blocker as GitHub Issue 284 (open, tooling),
  commented instead of filing a duplicate. It is the next
  consecutive ticker pass to fail on it after ticker-2104.
- Tracker untouched (failed units do not mark the tracker); the
  next tick re-produces the survivors unit. No other unit was
  attempted: the blocker is channel-wide, proven across two
  sessions, and failing further units would only burn their
  attempts.

## Stats

- target: gate line cleared (1 line)
- achieved: 0
- resources_gained: none
- costs: about 2 minutes of pass time, no game input, no items spent
- verified: no
- blocker_category: e (repeated blocker)
