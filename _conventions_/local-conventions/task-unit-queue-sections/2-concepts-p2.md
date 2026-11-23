---
title: 2. Concepts part 2
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 4
description: Continuation chain - a long activity is a chain of units under one chain_id.
---
- **Continuation chain** - a long activity is a chain of units under
  one `chain_id`. Each finished unit reports in its result stats
  whether the activity is exhausted; if not, the next unit of the
  chain is enqueued and the activity keeps going across as many
  quanta as it needs. Zombie Invasion is the model case - it runs
  until the nearby zombies are cleared, unit after unit, under its
  standing stop rules (for Zombie Invasion there is no hour
  budget and no daily limit - when the nearby zombies are cleared
  the chain pauses 1 hour and then checks again, owner correction
  2026-10-28), while higher priority units slip in between its
  units whenever their time arrives.
- **Device token** - exactly one executor may hold the Mac window at
  a time, for one unit at a time. The token is itself a lease file
  in `claimed`; taking the game window without the token is out of
  bounds for every session, including owner-directed ad hoc
  sessions, which join the pool as units instead of colliding.

