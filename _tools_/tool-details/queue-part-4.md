---
title: queue.py, part 4 of 4
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index text for queue.py
---

# queue.py, part 4 of 4

Moved verbatim from the former `_tools_/INDEX.md` row for [queue.py](../queue.py); only link destinations are adjusted. Back to the [tool index](../INDEX.md). Continues [part 3](queue-part-3.md).

Purpose, continued: `next --probe` hands out a queued zombie chain unit ahead of the overlay steering and the normal pick, so a doomed probe burns the re-minted chain unit instead of a perception unit (issue #746); `enqueue` refuses a chain successor after the chain's recorded event end (result.stats event_ends_at in the past, latest reading by finished_at across live and snapshot done), so a dead event's chain stops minting instead of seeding units for it (issue #745); `plan` and `sweep` report a refused window (expired, duplicate chain step, stale roster) under its own skip list instead of counting it as already present, so already_present counts only units the pool actually holds (issue #744); the production path appends the standing ledger-walk task section to a pre-reset sweep pair body (first/final pass by chain_seq, slot and reset times from the unit's own fields, ledger line count read live) so a staged pair carries its walk instructions instead of the generic body ; `enqueue` refuses a scout chain successor after the chain's reset day ended and `next` skips inbox units whose scout chain day is past, naming the skipped units on stderr, so a stale scout chain stops minting and its units are never handed out (issue #818); `read` records that a pass read the newest queue-ticker record and `claim` refuses without a receipt naming the newest record, its sha256, the claiming executor and a read within 120 minutes, so the standing route change (re-read the newest queue-ticker record before any claim) is enforced by the tool instead of the pass's pre-step prose (issue #737); `enqueue` refuses a future `--not-before` with no `--expires-at` and any timestamp it cannot parse, because an empty `expires_at` is the design's no-deadline marker that no expiry pass can reach, and `complete --status expired` retires a unit whose empty expiry left it unretirable - it needs a `--summary`, refuses a unit with a done record or a live future expiry, and writes no completion marker (issue #859)

Data: `../_queue_/`
