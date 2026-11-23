---
unit: building-queues-2026-11-22-1803
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-22T16:41:46Z
expires_at: 2026-11-23T06:03:00Z
planned_for: 2026-11-23T02:03:00Z
not_before: 2026-11-23T02:03:00Z
window:
est_minutes: 5
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T04:24:06Z
lease_until: 2026-11-23T04:44:06Z
result:
  status: partial
  started_at: 2026-11-23T04:24:06Z
  finished_at: 2026-11-23T04:25:07Z
  duration_seconds: 61
  executor: operator
  summary: Run 20261123T042406Z-ff5098 (claude-gateway/claude-sonnet-5-5, max-steps 8) closed the Research Queue panel left open, opened the BUILDING QUEUE panel and read all four builder slots live: all Idle (0/4), each with an untouched Construct button; banner quest 'Build: Oil Well (0/1)'. No build started: starting an upgrade is owner-only per the profile and OD-20261109-02 (Issue #517) is unanswered; the assignment cited no owner approval, so that half is needs-owner. 4 steps, 9 actions done, 0 refused, 3.37 s model time per step, 0.050798 USD. No takeover. Base screen left clean.
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2024-queue-run.md; run 20261123T042406Z-ff5098 step-0002.png (panel) and step-0003.png (close), final frame _tools_/state/cu_buildq_2024.png
  follow_up: owner decision needed on what the four idle builders build (OD-20261109-02, Issue #517); Oil Well build likely gated by the Unlock Oil Well research finishing about 11:43Z (inference); until then building-queues units are reads
  stats:
    target: read the four builder slots and start the profile's next build with resources only
    achieved: all four builder slots read live and Idle (0/4); 0 builds started because starting a build is owner-only (needs-owner); Research Queue panel closed
    resources_gained: none
    points: 0
    costs: model 0.050798 USD; no resources, diamonds, speedups or items spent
    verified: yes
    blocker_category: g
    builders_busy: 0
    builders_idle: 4
    builds_started: 0
    needs_owner: start a build (OD-20261109-02, Issue 517)
    banner_quest: Build: Oil Well (0/1)
    run_id: 20261123T042406Z-ff5098
    run_steps: 4
    actions_done: 9
    actions_refused: 0
    model_s_per_step: 3.37
    cost_usd: 0.050798
    device_takeovers: 0
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.
