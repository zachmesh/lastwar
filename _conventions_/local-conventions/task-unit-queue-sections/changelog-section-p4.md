---
title: Changelog part 4
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 44
description: 0.20.0, 2026-11-12 - section 11 gains rule R12 (live-pool handout, issue 694) - next resolves the
---
- 0.20.0, 2026-11-12 - section 11 gains rule R12 (live-pool handout, issue #694): `next` resolves the given root through the live pool before listing candidates, so a worktree-root `next` reads the live inbox instead of the snapshot, and `claim` claims the live-pool copy into the pass root, so a unit handed out from the live pool is claimable even when the snapshot never held it.
- 0.19.0, 2026-11-12 - section 11 gains rule R11 (worktree-location guard, issue #429): the decision commands refuse when this copy of queue.py - or the pool it would decide on - sits under the system temp directory, so a pass whose worktree was created under /tmp fails loudly at its first decision instead of losing its records to the runtime's /tmp sweep mid-pass; pass_worktree.py (PR #432) already refuses /tmp targets at creation, and this guard covers passes that never call it.
- 0.18.0, 2026-11-12 - section 11 gains rule R10 (tool-currency guard, issue #694): the decision commands refuse when this copy of queue.py differs from main's _tools_/queue.py, so a pass can no longer decide from a stale main-tree checkout; the worktree-tool rule is now enforced by the tool, not just documented.
- 0.17.0, 2026-11-12 - section 11 gains rule R9 (control-lock pause, issue #689): a unit that meets the outcome_unknown control lock closes failed naming blocker_overlay=control-lock, queue.py records a pool-level blocker that pauses next until it ages out after 4 hours or a closing that sent input lifts it, so a locked night burns no failed units.
- 0.16.0, 2026-11-07 - the four 19:00 mentions flagged as follow-up on #147 in 0.15.0 are rewritten to the absolute reset instant 02:00 UTC (about 18:00 PST in winter, 19:00 PDT in summer): VIP expiry (section 4), the scout anchor and the deadline list (section 13), and the quota checkpoints (rule R3). The dated 19:00 mentions in sections 1 and 9 stay: both describe the PDT era, when the reset was 19:00 local.
- 0.14.0, 2026-11-01 - section 14 gains a cross-reference to
  the ops execution records standard: the loop's own
  activities are executions and record themselves in the
  repository, and the retro measures them from those records.
- 0.13.0, 2026-11-01 - a cross-reference to the new push and
  PR policy: the queue's own outputs are tier-1 direct pushes,
  and changes to the design and tools are tier-2 pull requests
  under the audit of section 14's loop-health check.
- 0.12.0, 2026-11-01 - section 14 gains a cross-reference to
  the new evaluation metrics specification - the system-level
  companion that measures execution efficiency, perception,
  discovery, retro effectiveness and the impact of the tool
  developer and the knowledge organiser, with its computation
  extending _tools_/retro_report.py.
