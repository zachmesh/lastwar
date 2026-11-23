---
title: Open link 4 - no capacity feedback, no aging guarantee
created: 2026-11-23T09:06:14Z
modified: 2026-11-23T09:06:14Z
version: 0.1.0
sequence: 3
description: Discovery and scout triggers expand unit demand, while execution bandwidth is fixed (one device, 30-minute ticker,
---
## Open link 4 - no capacity feedback, no aging guarantee

Discovery and scout triggers expand unit demand, while execution
bandwidth is fixed (one device, 30-minute ticker, 15-minute unit
cap). Two missing pieces:

- The retro spec has no queue-depth or oldest-unit-age metric, so
  structural overload is not measured. Add both to the retro
  aggregation spec (section 14) when retro_report.py is next
  revised.
- queue.py next picks by expires_at, then priority, then age as
  tiebreak only. There is no aging boost, so a no-expiry
  low-priority chain can still starve (the 2026-10-30 zombie chain
  stall is the precedent). scout_diff can raise priority for
  observed items, but chained units are not observed items. An
  aging boost in queue.py (effective priority rises with wait
  time) is a tooling candidate for the backlog.

