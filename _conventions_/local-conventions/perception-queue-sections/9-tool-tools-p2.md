---
title: 9. Tool - _tools_/scout_diff.py (Phase 2, implemented) part 2
created: 2026-11-23T08:37:03Z
modified: 2026-11-23T08:37:03Z
version: 0.1.0
sequence: 21
description: The enqueue plan - one entry per unit to create or raise, in the exact field
---
1. **The enqueue plan** - one entry per unit to create or raise,
   in the exact field shape `_tools_/queue.py enqueue` consumes -
   regular, activity, priority computed by the formula of
   section 5, expires_at from the item deadline, not_before,
   window text naming the observation and the trigger it came
   from, and a chain id `scout-followup-<date>` for exploration
   units. Known items map to their regular when one of their
   profile triggers fired.
2. **The unknown items list** - every observed item with no
   owning model, with its surface, label and state, formatted
   for the round summary naming rule R5 requires.
3. **The coverage report** - the perception scoreboard for the
   day - items observed, items queued, items already done, red
   dots seen, red dots explained, unexplained red dots, and the
   day `unmatched_labels` list printed in full - totalled and
   split by surface. Narrative observations also carry
   their per-pass red-dot accounting sections, reconciled
   section total against frontmatter counter in the same
   report, so a narrative-only day's dots are checked,
   not just carried. The unexplained count is the headline -
   the day perception is judged by it reaching zero.
4. **The candidate filings and exploration plan** - one entry
   per unmatched label not already in the candidate register -
   the provisional profile to file under `_activities_` (surface,
   transcribed text, clues in hand) and the exploration unit to
   enqueue for it at priority 2 under chain id
   `scout-discovery-<date>`. Candidates already exploring get
   their next exploration unit here instead of a duplicate
   filing; candidates whose exploration completed get their
   promotion or rejection recorded as a proposed metadata edit,
   never applied silently.

**Idempotency** - the tool obeys the pool invariant it feeds.
Produced units dedupe on (regular, planned_for) exactly as sync
and plan do. Dynamic units carry their source in their window
text and chain id, and the tool checks the pool for an existing
unit from the same observation item - same date, surface and
label - before enqueueing. A second run over the same
observation produces an empty enqueue plan and an unchanged
pool. The tool never completes, claims or deletes a unit - it
only proposes and, with `--enqueue`, enqueues.

**Priority support from the queue tool** - produced scout units
stage at priority 2, windowed work. The queue tool takes
production priority from its SYNC_PRIORITY table; the Phase 2
change landed `scout` and `scout-midday` there at priority 2,
with SYNC_EST_MINUTES seeds of 10 minutes each until the pool
learns better, instead of silently defaulting scout production
to priority 3. The tool reads its expected durations through
the queue tool learned estimates, so its priority formula and
the planner seeds never drift apart.

