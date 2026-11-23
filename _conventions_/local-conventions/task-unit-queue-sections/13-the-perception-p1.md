---
title: 13. The perception layer (scout) part 1
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 43
description: The day work set is no longer defined by the static regulars alone.
---
## 13. The perception layer (scout)

The day work set is no longer defined by the static regulars
alone. Under the owner direction of 2026-10-31, a perception
layer sits in front of production - scout units walk the game
interface first, record what is actually available to do, and
the pool is then diffed and filled from that observation. The
full design - the traversal checklist, the observed items
schema, the diff rules, the tool design and the phased roadmap -
is [perception-driven queue](perception-driven-queue.md). This
section fixes the queue-level contract.

- **Scout unit type.** The regular is `scout` (the post-reset
  full pass, daily-reset cadence anchored at the trade-day reset
  (absolute 02:00 UTC, about 18:00 PST in winter, 19:00 PDT in summer)) and `scout-midday` (the midday pass, daily-reset cadence
  anchored at 07:00 local, the middle of the reset day). Both
  name the activity `perception-scout`. Scout units are windowed
  work - priority 2; the production priority table carries
  their entries since the Phase 2 change (SYNC_PRIORITY and the
  SYNC_EST_MINUTES seeds of 10 minutes in `_tools_/queue.py`). A
  scout unit observes and records only - it never claims,
  fights, dispatches or buys. The work it finds belongs to the
  owning regular own unit.
