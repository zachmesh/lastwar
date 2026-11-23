---
title: Integrator clean-worktree procedure
created: 2026-11-23T07:32:21Z
modified: 2026-11-23T07:32:21Z
level: L3
version: 0.1.0
description: How the Integrator scans a landing branch in a clean worktree, the controls that make a zero count mean something, and the decision rules; counts only
status: unverified
activity: integration
run_id: integration-2026-11-22-procedure
verified: dry runs on origin/main and on two throwaway snapshots, none pushed
---

# Clean-worktree procedure

The working prototype is /private/tmp/lw-integrator/integrator.py (310 lines, sha1 f59d6e74136b), outside the repository because the seat holds no _tools_ scope; it is offered to the toolsmith as the base of _tools_/integrator/. Subcommands: scan, control, readback, clean. It uses detached worktrees only and prints counts.

## Controls

- Positive control on origin/main 43c088d8f8: git grep -P -i -f finds 169 files; the whole-file census finds 171 (two wrapped names); metadata 1 of 4855. A branch zero counts only while this control is live.
- Silent-zero traps: macOS grep has no -P; the pattern list goes to git grep through stdin with comment lines removed.
- The head's own gate predates --privacy, so a pinned copy exported from local main (0467e3ef1b) runs the census. watch --privacy --worktree records nothing; --accept is never used.

## Rules applied

- Push only when file contents, file names, new-commit metadata and the census are all 0, no binary, symlink or ignored file was added, and no inherited metadata count rose.
- The full lint with --base has no redaction exemption (98 blocking findings on a clean redaction). The verdict is the author's-hook replay: the branch diff staged on the merge-base, then check --staged, plus redact --verify-diff for a redaction branch.
- A test failure blocks only when it is new against the same test on the merge-base (the lint-gate suite has 2 failures on origin/main today).
- Rehearsal on a throwaway snapshot made by the redact tool: 171 files changed, all privacy counts 0, replay rc 0, 171 of 171 redaction-only, 0 new test failures. Nothing pushed.
