---
title: Survivors 2026-11-05 ticker-0504 queue run
created: 2026-11-05T05:12:00-08:00
executor: ticker-0504
unit: survivors-2026-11-05-0203
regular: survivors
activity: survivor-intake
status: failed
---

# Survivors queue run ticker-0504

Session window: 2026-11-05 about 05:12 to 05:20 America/Los_Angeles.
Unit: survivors-2026-11-05-0203 (planned for 2026-11-05T10:03:00Z,
expires 2026-11-05T14:03:00Z).

## Own PRs first

- Open records PRs checked before any game work: PR 310
  (records/2026-11-05, this job's live branch) is OPEN, MERGEABLE,
  CLEAN, 0 comments, 0 reviews - nothing owed. PRs 309, 301, 265
  and 256 (records/2026-11-01 to 2026-11-04) were all CONFLICTING
  with integrator notes awaiting branch-side reconciliation.
- Reconciled all four from their remote heads this pass:
  - PR 309 (records/2026-11-01): merged main 65e12ecf, union
    action-log.jsonl (861 lines) - commit 22274ed91, pushed,
    ls-remote verified.
  - PR 265 (records/2026-11-02): same, 861 lines - commit
    e9effc346, pushed, verified.
  - PR 256 (records/2026-11-03): same, 867 lines - commit
    f960817d1, pushed, verified.
  - PR 301 (records/2026-11-04): three conflicts - action-log
    union (864 lines) plus the two add/add queue files
    donations-2026-11-04-2203.md and radar-2026-11-04-2203.md,
    kept the BRANCH copies: they record the true outcomes
    (claimed and failed by ticker-2304 / ticker-2334, evidence
    files in _records_/2026-11-04/), while main's copies record
    both as expired with 0 attempts - a stale re-creation by a
    later sync pass working from a worktree where the units still
    looked unclaimed. Commit ace4f02bf, pushed, verified.
  - Commented on each PR with the reconciliation note. GitHub
    mergeable status still recomputing (UNKNOWN) at comment time;
    local test merges are clean (main is an ancestor of each new
    head). A first attempt at 301 from the local branch tip
    instead of the remote head was caught and redone correctly;
    the local branch tips had already landed on main through
    other branches, so they were the wrong base.
- No zombie chain seeded: the Zombie Invasion event ended at
  about the 19:00 reset on 2026-10-30 (unit 066 chain close);
  seeding stays forbidden until a Zombie Invasion tab is seen
  live again.

## What was done

- Queue sync: reaped 0, expired 0, produced nothing new - 21
  regulars already queued. No zombie seeding (see above).
- Device token acquired by ticker-0504. Next unit picked:
  survivors-2026-11-05-0203, claimed.
- Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd) online.
  Computer session cc-521 opened for the probe.

## Outcome: failed, no game input dispatched

- Probe per _tools_/mac_capture_probe.py --probe-checklist
  (Issue 284), one cheap probe instead of re-proving the failure:
  - list_windows LastWar: 1 window, 1920x1080, pid 59735,
    window_id 160366, x 0 y 0.
  - activate LastWar: brought_to_front false,
    window_on_screen false, evidence_error "Failed to start
    stream due to audio/video capture failure"; frontmost app
    Keychain Access.
  - inspect_menu View: stale_observation - the app menu is not
    bound to the selected main window, observe required first.
  - computer.observe compact: screen_failed, same capture error.
  - Chrome window in the same session observes normally (full
    element tree, evidence available) - the channel itself works.
- Classifier result: diagnosis OFF_SCREEN_WINDOW (high
  confidence), stop_pass yes, exit 10. The View-menu inspect is
  the only missing probe step (blocked by the same failure).
- No game screen was ever read, so the gate line could not be
  verified and no tap was dispatched while blind. No survivor
  was recruited, no Quick Dispatch was run, no figure was read.
- This is the same blocker as GitHub Issue 284 (open, tooling);
  commented there with this pass's probe classification instead
  of filing a duplicate. Recovery remains the one owner step on
  the Mac mini: click the LastWar Dock icon once (or run
  _tools_/mac_lastwar_front.sh in Terminal), then re-probe.
- Tracker untouched (failed units do not mark the tracker); the
  next tick re-produces the survivors unit. No other unit was
  attempted: the probe says stop the pass, and the blocker is
  channel-wide - failing further units would only burn their
  attempts. This pass therefore ends after this single unit.

## Stats

- target: 1 (gate line cleared)
- achieved: 0
- resources_gained: none
- costs: probe_only_no_game_input
- verified: no
- blocker_category: e (repeated blocker)
