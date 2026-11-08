---
title: Zombie Invasion Execution 2026-10-28 0407 Queue Run
created: 2026-10-28T11:10:00Z
modified: 2026-10-28T11:10:00Z
level: L0
version: 0.1.0
description: Zombie-invasion chain unit 004 - coin panel read at 35488573, then the device-access error blocked all input after three reopen attempts, no kill and no collection, chain continues
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, and the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
---

# Zombie Invasion — execution, 2026-10-28 04:07 queue unit 004

A single task unit, executed by executor ticker-0407 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-004,
chain zombie-2026-10-28, chain sequence 4, priority 4. Session
window 04:07 to about 04:10 America/Los_Angeles. Status — not
performed; access failed after the opening read.

## What was observed

- The game stood open on the base with the COIN panel open,
  left by the previous unit. The panel read Owned 35,488,573
  exactly (35.4M), Resource Items 86.1M, Optional resource
  items 892.3M. That is coin_before 35488573 for this unit,
  unchanged from unit 003's coin_after.
- Sessions cc-46 and cc-47 were started, LastWar was activated
  and the coin panel screenshot was captured as evidence.

## Access failure

- The first click (closing the coin panel) returned the known
  unreliable device-access error claiming this schedule lacks
  owner-authorized device access. Per the recording rules the
  session was reopened and the attempt repeated at least 3
  times in total - a fresh computer.session start and a fresh
  activate both returned the same error.
- No in-game input landed after the opening screenshot, so no
  zombie was attacked, no LOOT collection was tapped, and no
  stamina was spent. zombies_killed 0, cleared false,
  coin_after 35488573, coins_collected 0.
- The unit is completed as failed, the tracker is left
  untouched, and the chain successor is enqueued to start now
  under the chain rule (cleared is false), so the next tick
  retries the work.
- Nothing bought, no diamond spent, no item used.
