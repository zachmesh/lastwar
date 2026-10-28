---
unit: <regular-id>-<yyyy-mm-dd>-<hhmm>
regular: <regular-id from tools/regulars.json>
activity: <activity type folder name>
segment: <1, 2 or 3>
priority: <1 expiry-critical, 2 windowed, 3 standard>
created_at: <ISO 8601 UTC>
expires_at: <ISO 8601 UTC or empty>
window: <phase or posture constraint or empty>
est_minutes: <producer estimate>
claimed_by: <empty until claimed>
claimed_at: <empty until claimed>
lease_until: <empty until claimed>
---

# <Regular name>

What to do, in the regular's own terms. The executor also reads the
activity metadata in `_activities_/<activity>/` and the standing rules
in the recording rules before acting.

On completion the executor appends the result block defined in the
[task unit queue design](../_conventions_/local-conventions/task-unit-queue-design.md)
and moves this file to `done`.
