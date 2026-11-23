---
title: Repository Tools
created: 2026-11-01T07:58:31Z
modified: 2026-11-23T16:17:54Z
version: 2.9.0
description: Executable helpers, configuration and runtime state, with each tool described in a linked article
---

# Repository tools

Python 3 helpers for the play loop, with their configuration and runtime state in [state](state/INDEX.md). Run them from the
repository root; they use the standard library. `_tools_/` is the canonical path; the root `tools` link keeps old commands working.

One row per kind. Each article holds purpose, data and issue history; [tool details](tool-details/INDEX.md) lists every article and
[usage notes](tool-details/usage-and-compatibility.md) cover examples and staging runtime state.

| Kind | Tools | Article |
|---|---|---|
| Queue | [queue.py](queue.py), [queue-tests](queue-tests/INDEX.md), [queue-guard-tests](queue-guard-tests/INDEX.md) | [queue](tool-details/queue-part-1.md) |
| Planning | [regulars.py](regulars.py), [duel.py](duel.py), [resource_map.py](resource_map.py), [resource-map-tests](resource-map-tests/INDEX.md), [scout_diff.py](scout_diff.py) | [planning](tool-details/planning-and-scouting-tools.md) |
| Records | [observation.py](observation.py), [observation-tests](observation-tests/INDEX.md), [retro_report.py](retro_report.py), [log_append.py](log_append.py), [log-append-tests](log-append-tests/INDEX.md), [live_checkout_check.py](live_checkout_check.py), [pass_worktree.py](pass_worktree.py) | [records](tool-details/records-and-worktree-tools.md) |
| Delivery | [branch_guard.py](branch_guard.py), [tree_check.py](tree_check.py), [held_patches.py](held_patches.py), [slot_coverage.py](slot_coverage.py), [vip_missed.py](vip_missed.py) | [delivery](tool-details/delivery-and-coverage-tools.md) |
| Tap and Mac | [tapcal.py](tapcal.py), [mac_capture_probe.py](mac_capture_probe.py), [mac_window_open.py](mac_window_open.py) | [tap-mac](tool-details/tap-and-mac-tools.md) |
| Harvest and pool | [harvest_verify.py](harvest_verify.py), [pool_gap.py](pool_gap.py) | [harvest](tool-details/harvest-and-pool-tools.md) |
| Batch and bridge | [records_batch.py](records_batch.py), [cu_bridge.py](cu_bridge.py), [cu-bridge-tests](cu-bridge-tests/INDEX.md) | [batch](tool-details/batch-and-bridge-tools.md) |
| Gate and landing | [lint-gate](lint-gate/INDEX.md), [integrator](integrator/INDEX.md), [tool-sync](tool-sync/INDEX.md), [board-check](board-check/INDEX.md), [split-doc](split-doc/INDEX.md) | [gate](tool-details/lint-gate-summary.md) |
| Team guards | [spawn-seat](spawn-seat/INDEX.md), [model-guard](model-guard/INDEX.md), [strategy-conformance](strategy-conformance/INDEX.md), [strategist-health](strategist-health/INDEX.md) | each own index |
