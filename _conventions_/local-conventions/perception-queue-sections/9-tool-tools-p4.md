---
title: 9. Tool - _tools_/scout_diff.py (Phase 2, implemented) part 4
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T13:46:17Z
version: 0.2.0
sequence: 29
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

2026-11-23: with coordination.queue.require_forecast on, enqueue, plan, sweep and sync refuse a unit whose serves is not a ledger plan item or one of upkeep, snapshot, baseline, fill idle slot; --no-require-forecast is the emergency override.
