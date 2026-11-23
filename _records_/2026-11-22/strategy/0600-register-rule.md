---
title: Register date rule
created: 2026-11-23T15:17:00Z
modified: 2026-11-23T15:17:00Z
version: 1.0.0
level: L3
description: The four rules for open hypothesis claims so their read dates stop arriving in lumps the operator cannot read, written after the 15:15Z alarm
status: proposed
grounded_in:
  - source: Steer A round message of 2026-11-23 15:15Z on 18 overdue claims
  - source: _records_/2026-11-22/strategy/hypothesis-register.csv
---

# Register date rule

The register carries two columns beside the claim, `decision` and `decision_due_utc`, and a status of open, confirmed, retired, superseded, adopted or DEFERRED.

1. **Every open claim names the decision it would change** and the first date that decision falls due: a node start, a builder slot, the 00:00Z flip, the weekly review.
2. **A claim whose answer changes no action in the next 7 days is DEFERRED** with a review date, not an open date it will miss. On 2026-11-23 38 claims moved to DEFERRED (boxes, Black Market details, season, store resets, HQ 32 and above, the six panel reads of the slot-arrival protocol, which become one pre-arrival unit on 11-28).
3. **`read_by_utc` comes from the planner's real queue slot,** never from a wish. The dates written on 2026-11-23 15:17Z are proposals sized to about 5 operator units an hour; the planner confirms or moves them.
4. **At most about 12 open claims fall due in any 6-hour window.** Beyond that the lower-value claims queue behind. After this pass the largest window holds 8.

## Closed in the same pass

H99 and H91 (superseded by the clean research reads), H83 and H92 (the panel marks match the graph), H84 (split into H103 and H112), H88 (retired after the first plunder fight), H47 and H78 (confirmed).
