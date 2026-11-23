---
title: Changelog part 4
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 58
description: 0.27.0, 2026-11-21 - section 11 gains rule R19 (already_present counts only genuine dedupe hits, issue 744)
---
- 0.27.0, 2026-11-21 - section 11 gains rule R19 (already_present counts only genuine dedupe hits, issue #744): `plan` and `sweep` report a refused window (expired, duplicate chain step, stale roster) under its own skip list instead of counting it as already present, so already_present equals the units the pool actually holds for the staged windows; the roster-freshness refusal now carries the refused window's unit id so callers can classify it.
- 0.26.0, 2026-11-21 - section 11 gains rule R18 (chain event-end guard, issue #745): `enqueue` refuses a chain successor when the chain's latest recorded `event_ends_at` is past, so a dead event's chain stops minting instead of seeding units for it; no reading recorded means no signal and the mint proceeds as before.
- 0.25.0, 2026-11-21 - section 11 gains rule R17 (doomed-probe zombie preference, issue #746): `next --probe` hands out a queued zombie chain unit ahead of the overlay steering and the normal pick, so a probe pass burns the re-minted chain unit instead of a scout unit; with no zombie unit queued, actionable and inside budget, the probe falls through to the normal pick.
- 0.24.0, 2026-11-21 - section 11 gains rule R16 (enqueue chain-seq reconciliation, issue #750): `enqueue` takes the next chain seq from the highest seq named by the live pool, its completion markers, or the given root's snapshot pool, so a finished seq the live pool forgot is never re-minted. 0.23.0 is now claimed by the merged R15 change (PR #715); the competing R15 branch PR #751 stands superseded, and the geometry fold (PR #761) still claims 0.23.0 per issue #739 and must renumber on rebase, so this change takes the next free number.
