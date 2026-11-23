---
title: 13. The perception layer (scout) part 5
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 47
description: Perception points are a floor, not a ceiling.
---
- **Perception points are a floor, not a ceiling.** The two
  anchored scout passes (post-reset and midday) are the
  guaranteed minimum perception of a day. A full pass also
  fires on a detected state change, and partitioned perception
  of the volatile surface groups rolls with every ticker
  heartbeat, appending to the same day observation file - so a
  trigger is seen when it fires, not at the next anchor.
- **New task discovery (perception document section 6).** Every
  scout traversal roster-matches the labels it meets; an
  unmatched label is filed the same session as a provisional
  candidate profile under `_activities_`, and system mail and
  update notices are discovery signals in their own right (the
  Crystal Shop was announced by the maintenance mail of
  2026-10-21 before any pass found it). Candidates move
  candidate, exploring, then active or rejected with the reason
  kept. Exploration units learn a candidate read-only first -
  entry, mechanism, rewards, cost, cycle, deadline, scoring -
  and anything touching a price, diamonds, a red line or an
  unclear rule stays learn-only and is named to the owner in
  that day round summary. A candidate whose mechanism is clear
  and inside the free and safe envelope is completed as a
  profile with trigger conditions and turns active - from then
  on the trigger scheduler produces its execution units with no
  per-item owner approval. Every full pass closes with the
  `unmatched_labels` roster-out list as part of its coverage
  report, printed even when empty.
