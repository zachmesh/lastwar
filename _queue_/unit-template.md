---
unit: <regular-id>-<yyyy-mm-dd>-<hhmm>
regular: <regular-id from tools/regulars.json>
activity: <activity type folder name>
segment: <1, 2 or 3>
priority: <1 expiry-critical, 2 windowed, 3 standard>
created_at: <ISO 8601 UTC>
expires_at: <ISO 8601 UTC or empty>
planned_for: <cadence window this unit serves, ISO 8601 UTC>
not_before: <claim not allowed before this time, or empty>
window: <phase or posture constraint or empty>
est_minutes: <producer estimate, never above 15>
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

On completion the executor runs `tools/queue.py complete`, which
writes the result section into this file's frontmatter - status,
start and finish times, duration, claimed items and the activity's
result statistics - and moves the file to `done`. The result shape is
defined in the
[task unit queue design](../_conventions_/local-conventions/task-unit-queue-design.md).
