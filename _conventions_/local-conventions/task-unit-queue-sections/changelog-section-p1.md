---
title: Changelog part 1
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 55
description: 0.37.0, 2026-11-22 - section 11 gains rule R26 (reaped-marker reasons, issue 826) - sync reports completion_markers_reaped_by_reason
---
## Changelog

- 0.37.0, 2026-11-22 - section 11 gains rule R26 (reaped-marker reasons, issue #826): `sync` reports `completion_markers_reaped_by_reason` in its JSON, splitting every reaped completion marker into done-landed, aged-out and invalid, and the ticker's sync section quotes the aged-out subset as lost, so a lost closing is named as lost in the run record that reaped it instead of folding into the bare reaped count; the aged-out warning moves to stderr, so stdout stays one parseable JSON object even when markers are lost.
- 0.36.0, 2026-11-22 - section 11 gains rule R25 (claim-before-read gate, issue #737): `queue.py read` records that a pass read the newest queue-ticker record into a shared live-pool receipt, and `claim` refuses until the receipt names the newest record, carries its sha256, names the claiming executor and is at most 120 minutes old, so the standing route change (re-read the newest queue-ticker record before any claim) is enforced by the tool instead of the pass's pre-step prose; with no queue-ticker record in the tree the claim proceeds.

- 0.35.0, 2026-11-22 - section 11 gains rule R24 (stale scout chains, issue #818): `enqueue` refuses a scout chain successor after the chain's reset day ended and `next` skips units whose scout chain day is past, so a Nov-20 chain stops minting on Nov-22 instead of seeding units that write observations to the wrong day's file; the day end comes from the chain id's trailing date against the roster's 02:00 UTC reset (post-reset chains end at the following local date's reset, midday chains at their own date's reset), and zombie, sweep and discovery chains are untouched.

