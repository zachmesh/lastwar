---
title: Queue Tests
created: 2026-11-23T07:50:00Z
modified: 2026-11-23T09:45:00Z
version: 1.3.0
description: Tests for the queue unit serves key, run against throwaway pools in temporary git repositories
---

# Queue tests

Tests for the `serves` tag of a queue unit (planner finding, then the Steward's enforcement). `queue.py` used to write only the
keys in `FM_ORDER`, so a `serves:` line added to a unit was dropped at the next claim.

They cover: `enqueue --serves` writes the key and a `Serves:` body line, folded to one line, empty refused; the key survives
claim, release and complete; `enqueue` REFUSES a unit with no serves unless the roster gives one (a roster regular inherits its
`regulars.json` serves, default `upkeep`; a custom roster file decides; an unreadable roster lets nothing through);
`regulars.json` gives every entry `serves`, and `plan`, `sync` and `sweep` copy it into the units they mint, so a full sync
mints only tagged units; `validate` and `validate --ref` report a live inbox unit without it as an ERROR, a claimed
upgrade-type one as a warning, done units not at all; `sync` only warns, so an untagged unit never stops the tick. Upgrade-type:
activity building-queues, research-queue or troop-training, or an activity, regular or unit id containing upgrade or growth-fill.

Each pool is a throwaway repository under /tmp with the tool's temp-dir and currency guards bypassed through the
`LASTWAR_QUEUE_ALLOW_*` variables, so nothing touches the live pool.

`test_next_expired.py`: `next` never names a unit whose window has closed (pick_key sorts by expiry first, so an expired unit used to lead the list), and `claim` refuses one by name.

Run: `python3 -m unittest discover -s _tools_/queue-tests`.
