---
title: Changelog part 2
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 56
description: 0.34.0, 2026-11-22 - section 11 gains rule R23 (missed-VIP-days count, issue 742) - the count comes
---
- 0.34.0, 2026-11-22 - section 11 gains rule R23 (missed-VIP-days count, issue #742): the count comes from the pool via new `_tools_/vip_missed.py`, keyed on the unit-id slot date with only the 1800 slot defining a day, and a day is missed when its 1800 unit expired/failed or closed done/partial with claimed_count 0; the ticker's hand count of seven vs the ruled eight is the live instance (the Nov 13 unit's finished_at fell on Nov 15).
- 0.33.0, 2026-11-22 - section 11 gains rule R22 (slot coverage, issue #743): every scheduled ticker slot leaves a record or a missed-fire marker; `_tools_/slot_coverage.py check` reports the recordless past-window slots on the :04/:34 grid and `mark` writes a marker, refusing a slot a record already covers; coverage is read from the record title, never the file name alone, so a late-starting pass serves the slot its title states.
- 0.32.0, 2026-11-22 - section 3 specifies the `_queue_/completed/` completion markers (issue #726): the marker's purpose (issue #438), its four fields, the validity rule, the readers that treat a marker like a local done record, the live-only status, and the sync reaping rule (168 hours, lost closings reported per issue #563). No tool change: `queue.py` already implements all of it; the design document never mentioned the directory.
