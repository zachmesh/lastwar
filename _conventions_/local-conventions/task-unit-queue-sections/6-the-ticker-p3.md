---
title: 6. The ticker and the executor loop part 3
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 14
description: Pick the inbox unit with the earliest expires_at, ties broken by priority then by age.
---
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
