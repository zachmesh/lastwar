---
title: Loop review 2026-10-31 - open links in the feedback and improvement loop
version: 1.0.0
status: active
created: 2026-10-31
---

# Loop review - 2026-10-31

Owner asked whether the feedback and improvement loop is actually
closed. Verdict: the loop is closed in design and most machinery is
live (perception design + scout_diff, ticker execution, retro spec +
daily retro job, improvement backlog with closure rule, standing
tool-developer and knowledge-organizer jobs). The open links below
are filed for the first retro (2026-11-01) to take as improvement
tasks; they are recorded here so they cannot be lost.

## Open link 1 - scout_diff auto-invocation (highest priority)

scout_diff.py exists and is validated, but nothing runs it
automatically after scout units produce an observation. The wiring
step is a planner cron body change (after plan: read the newest
observation, run scout_diff dry-run, then --apply against the live
pool root). Pending owner approval in chat on 2026-10-31. Until it
lands, the perception-to-queue link works only when an operator
runs the tool by hand.

## Open link 2 - pre-reset sweep production is manual

The 17:30 / 18:30 zero-sweep pair is not produced by the planner
(it cannot express fixed time slots; queue design section 12 notes
the interface as pending). The 2026-11-02 pair was hand-enqueued
again on 2026-10-31 (chain pre-reset-sweep-2026-11-02). Structural
fixes, either acceptable: planner fixed-slot production, or a
pre-reset scout anchor in regulars whose observation feeds
scout_diff fix-up enqueueing (depends on open link 1).

## Open link 3 - measurement is detected, not enforced

Unit result stats (queue design section 14) are filled by executor
discipline. The retro counts closings with missing or unverified
stats, so the loop detects bad data, but queue.py complete does
not yet validate required fields. Validation is tooling backlog
item (b) in the tool-developer job. retro_report.py (backlog item
(a), in build on 2026-10-31) covers the aggregation half.

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

## Notes

- Retro loop-health has a one-day blind spot: if the retro job
  itself fails, the gap is only visible at the next retro (plus
  cron failure notices). Accepted for now; recorded so the
  acceptance is explicit.
- Owner-decision items (skipped-needs-owner units) resurface via
  round summaries and the retro; there is no separate aging digest
  for them. Rule R5 covers owner-named tasks. Accepted for now.
