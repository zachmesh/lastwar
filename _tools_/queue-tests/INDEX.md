---
title: Queue Tests
created: 2026-11-23T07:50:00Z
modified: 2026-11-23T09:11:27Z
version: 1.2.0
description: Tests for the queue unit serves key, run against throwaway pools in temporary git repositories
---

# Queue tests

Tests for the `serves` key of a queue unit (planner finding, A-20261123-0746). `queue.py` used to write only the keys
listed in `FM_ORDER`, so a `serves:` line added to a unit was dropped at the next claim.

They cover: `enqueue --serves` writes the key and a `Serves:` body line; the key survives claim, release, claim again
and complete; a hand-added line is no longer dropped; a multi-line value folds to one line and an empty one is refused;
`validate` warns, never errors, for an upgrade-type unit (activity building-queues, research-queue or troop-training, or
an activity, regular or unit id containing upgrade or growth-fill) in inbox or claimed without `serves`, also at a git ref.

Each pool is a throwaway repository under /tmp with the tool's temp-dir and currency guards bypassed through the
`LASTWAR_QUEUE_ALLOW_*` variables, so nothing touches the live pool.

`test_next_expired.py`: `next` never names a unit whose window has closed (pick_key sorts by expiry first, so an expired unit used to lead the list), and `claim` refuses one by name.

Run: `python3 -m unittest discover -s _tools_/queue-tests`.
