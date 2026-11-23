---
title: 6. The ticker and the executor loop part 2
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 10
description: Take the device token.
---
1. Take the device token. No token, no game input - whoever holds
   it finishes their unit first (at most 15 minutes). Contention
   becomes a short wait, never a collision or a stand-down.
2. Pick the inbox unit with the earliest `expires_at`, ties broken
   by priority then by age. Claim it by atomic rename `inbox` to
   `claimed`, stamping `claimed_by`, `claimed_at`, `lease_until`
   (default lease 20 minutes - longer than the unit cap, so a unit
   is never requeued out from under a live executor) and
   incrementing `attempts`. The claim is gated by rule R25: the
   pass must first record its read of the newest queue-ticker
   record, so a claim on unread state fails loudly instead of
   executing.
3. Run the unit, at most 15 minutes. On time, finish the current
   atomic in-game action, write the `_records_` file, and complete
   the unit with a `partial` result noting the remaining work. The
   partial unit is an attempt record in `done`; the tracker still
   shows the regular as due, so the next tick re-produces it and
   the work resumes as a fresh unit - and the attempt stays in the
   statistics instead of vanishing.
4. On completion, write the `_records_` file, complete the unit
   (the result section lands in its frontmatter), rename `claimed`
   to `done`, and update the regulars tracker exactly as segment
   runs do today. If the unit belongs to a chain and its result
   stats say the activity is not exhausted, enqueue the next unit
   of the chain. A chain ends only when its activity ends. For
   Zombie Invasion a unit whose stats say cleared does not end
   the chain - its successor is enqueued with `not_before` 1 hour
   later, because new zombies may appear (waves arrive about
   hourly); there is no daily limit and no hour budget (owner
   correction 2026-10-28).
5. Release the token and go back to step 1. Every unit boundary is
   a scheduling point - a VIP unit that lands while a background
   chain is mid-run waits at most for the current unit to end.
6. A reaper pass (part of the producer job) returns any `claimed`
   unit whose `lease_until` has passed to `inbox`, clearing the
   claim stamps. A crashed executor therefore strands at most one
   unit for at most one lease period - the direct fix for the
   2026-10-26 lock failure mode at the work level.
7. Dead letters - a unit whose `attempts` reach `max_attempts` is
   not requeued again. It moves to `done` with result status
   `failed`, and the stats report surfaces it, so a poison unit
   cannot spin the loop forever.

