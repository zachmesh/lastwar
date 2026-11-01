---
unit: survivors-diagnostic-001
regular: survivors
activity: survivor-intake
segment: 1
priority: 1
created_at: 2026-11-01T05:48:06Z
expires_at: 2026-11-01T18:10:00Z
planned_for:
not_before:
window: method-change diagnostic - owner M5 decision 2026-10-31
est_minutes: 15
chain_id: diagnostic
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: ticker-1004
claimed_at: 2026-11-01T18:05:35Z
lease_until: 2026-11-01T18:25:35Z
result:
  status: partial
  started_at: 2026-11-01T18:05:35Z
  finished_at: 2026-11-01T18:16:20Z
  duration_seconds: 645
  executor: ticker-1004
  summary: Diagnostic partial: gate not located, Quick Dispatch not located; Titanium Alloy Factory panel verified with no Quick Dispatch
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-01/survivor-intake/1017-queue-run.md
  follow_up: none
  stats:
    target: complete verified map from base to Quick Dispatch, gate line verbatim
    achieved: 0
    resources_gained: none claimed as survivor work
    costs: about 12 minutes, no items consumed
    verified: no
    blocker_category: c
    survivors_recruited: 0
    question_bubbles_found: 0
    live_quick_dispatch_completed: no
    gate_located: no
    quick_dispatch_located: no
---

# survivors - DIAGNOSTIC / method-change unit (not a regular intake unit)

Owner decision 2026-10-31 (retro item M5): change the survivor method,
keep doing Survivors. Queue-era survivor units closed 22 of 22 partial
because the Quick Dispatch gate line was repeatedly not found or not
verified. This unit exists to fix that by mapping the flow once,
properly, before regular survivor units rely on it again.

## Success standard for THIS unit

Success is NOT completing a dispatch. Success is a complete, verified
map of the flow, written into this unit's result. A unit that dispatches
nobody but returns the full map below is done; a unit that dispatches
but returns no map is partial.

## What to do

1. Read _activities_/survivor-intake/INDEX.md first (current method,
   including the E1 gate-start rule), then open the survivor interface
   from the base screen, observing twice after each tap before
   concluding anything.
2. Locate where new survivors appear - the gate position. Record which
   screen shows them, what the gate area looks like, and the exact
   on-screen text of the gate line, read verbatim (copy the line as
   displayed; if no new survivor is present, record what the gate area
   shows instead and say so - do not reconstruct the line from memory).
3. Find the Quick Dispatch entry: starting from the gate / survivor
   screen, walk the path control by control. For EVERY control on the
   path, measure it fresh in this unit and record (a) the screen it is
   on, (b) its label or icon description, (c) its measured center
   coordinates. No coordinate may be copied from an earlier unit.
4. If a new survivor is actually present during this unit, complete one
   real Quick Dispatch through the mapped path, step by step, recording
   each screen change; this both proves the map and honours the
   standing rule (new survivors are always Quick Dispatched
   autonomously). If none is present, leave the map as the deliverable
   and state that no dispatch was available to prove it with.

## Closing requirements (result block)

The result must contain, in its evidence/stats:
- entry path: the ordered list of screens from the base screen to the
  Quick Dispatch control, one line per step;
- every control on that path with its screen, label/icon and measured
  center coordinates from THIS unit;
- the gate line text read verbatim this unit, or an explicit statement
  that the gate was empty and what it showed instead;
- whether a live Quick Dispatch was completed through the map (yes/no,
  and the survivor count before/after if yes).
Any step of the flow that could not be located is written as
"not located" for that step - never inferred, never filled in from an
older unit. Red lines unchanged: no diamonds, no paid buttons, no
price-tagged taps.
