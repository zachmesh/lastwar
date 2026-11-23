---
title: Queue Planning The Amended Donation Close Rule In The Passes 2990 2026-11-23
created: 2026-11-23T10:05:00-08:00
modified: 2026-11-23T10:05:00-08:00
level: L0
version: 1.0.0
description: Planner pass putting the Researcher's amended close rule, a grey timer ending on the 20 minute refill grid, into the four donation passes and removing the stale uncalibrated clause
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1005-close-amended
trigger: Researcher amendment donation-close-amendment
started_at: 2026-11-23T09:58:00-08:00
finished_at: 2026-11-23T10:05:00-08:00
verified: the donation units searched for the old wording before and after; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/research/donation-close-amendment.md
---

# The amended donation close rule, 2990

The four donation passes (`donations-pass-2026-11-23-002`, `-003`, `-004` and `donations-2026-11-23-1630`) now close by the amended rule: a count needs a live read in the same unit and is hidden after the last tap; the pass closes DONE when the live count before the last tap was 1/30, the Donate turned from green to grey with a timer, and the timer's end (read time plus timer) lies on the 20-minute refill grid within 3 seconds. A 0.1K rise of the badge item or Tech EXP corroborates when it is in the same frame and is not required, since the Tech EXP bar at Quick Construction cannot move. The pass writes the timer, its read time and the UTC time of the last tap; an off-grid or unread end closes unverified unless a witness rose; a count is never written after the last tap, derived by arithmetic or taken from the footer. The sentence that an entry at 1/30 closes flagged uncalibrated is struck, and so is a stale paragraph in the 00:30Z unit that still called the refill a guess. The units keep the logging of the first timer with its read time and the entry-count prediction; pass 002 states its first timer end (21:17:57) and that an entry after it gives 11. The digest rules 4 and 6, card R2 and closing-standard.md are the scribe's: I do not edit them.
