---
unit: <regular-id>-<yyyy-mm-dd>-<hhmm>
regular: <regular-id from _tools_/regulars.json>
activity: <activity type folder name>
segment: <1, 2 or 3>
priority: <1 expiry-critical, 2 windowed, 3 standard>
created_at: <ISO 8601 UTC>
expires_at: <ISO 8601 UTC or empty>
planned_for: <cadence window this unit serves, ISO 8601 UTC>
not_before: <claim not allowed before this time, or empty>
window: <phase or posture constraint or empty>
est_minutes: <producer estimate, never above 15>
serves: <exactly one of: upkeep, snapshot, baseline, fill idle slot, or a plan item id that has a row in the forecast ledger (PL-nn, comma separated if more than one); free text fails the validate check>
chain_id: <continuation chain id or empty>
chain_seq: <position inside the chain or empty>
attempts: 0
max_attempts: 3
claimed_by: <empty until claimed>
claimed_at: <empty until claimed>
lease_until: <empty until claimed>
---

# <Regular name>

What to do, in the regular's own terms. The executor also reads the
activity metadata in `_activities_/<activity>/` and the standing rules
in the recording rules before acting.

Units minted after the forecast refusal switches on (2026-11-24T00:05Z), chain follow-ups
included, are refused unless serves is a plan item id with a row in the forecast ledger or an
exempt word: write the ledger row before the unit.

A brief that can reach a banner, a Go, a Buy, a link, a web, a share or an
external-app button carries one line: 'may open another app: needs Steer A's
approval first; if it opens, STOP' (standing rule, Steer A, 2026-11-23).

A brief that taps buildings or menus points at the route card,
`_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`,
writes a precondition first (what must be true; if not, stop), records the
tag text beside every number taken from a building panel, and stops with
one named reason: blocked by capacity, by the owner on another device, by
cost, by prerequisite, by route or by window.

On completion the executor runs `_tools_/queue.py complete`, which
writes the result section into this file's frontmatter - status,
start and finish times, duration, claimed items and the activity's
result statistics - and moves the file to `done`. The result shape is
defined in the
[task unit queue design](../_conventions_/local-conventions/task-unit-queue-design.md).
