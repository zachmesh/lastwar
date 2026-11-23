---
title: Queue Guard Tests
created: 2026-11-23T08:24:14Z
modified: 2026-11-23T08:24:14Z
version: 1.0.0
description: Tests for the stale-tool guard of queue.py, issue 694, on a fake remote
---

# Queue guard tests

Tests for the stale-tool guard of `queue.py` (issue 694). It byte-compared the live copy with origin's and so refused a
copy that was AHEAD of origin for 15 minutes. Now only a copy that is behind main or has diverged from it refuses; a copy
ahead runs, with a warning naming both blobs.

Each case is a bare repository as the remote, a live clone, and a second clone that plays the other author. They cover:
equal, ahead by a commit and by an uncommitted edit, behind, diverged, pulling the newer main, an unreadable origin, no
remote, the environment escape, a shallow live clone, the `version` command's currency, and that the guard's fetch leaves
the clone whole and `origin/main` alone (a depth-1 fetch had made the live clone shallow and grafted `origin/main`).

Run: `python3 -m unittest discover -s _tools_/queue-guard-tests`.
