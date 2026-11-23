---
title: Repository Tools
created: 2026-11-01T07:58:31Z
modified: 2026-11-23T09:20:47Z
version: 2.7.0
description: Executable helpers, configuration and runtime state, with each tool described in a linked article
---

# Repository tools

Python 3 helpers for the play loop, plus their configuration and runtime state in [state](state/INDEX.md). Run them from the
repository root; they use the standard library and find their data relative to the script. `_tools_/` is the canonical
path and the root `tools` link only keeps old commands working.

Find a tool in the table. Its article holds purpose, data and issue history. The [tool details](tool-details/INDEX.md)
list every article, and [usage notes](tool-details/usage-and-compatibility.md) cover examples, the compatibility link
and staging runtime state.

| Tool | Does | Article |
|---|---|---|
| [queue.py](queue.py) | work-unit queue; a unit may carry a `serves` line (`enqueue --serves`, kept through claim and complete; `validate` warns when an upgrade-type unit has none) | [queue](tool-details/queue-part-1.md) |
| [queue-guard-tests](queue-guard-tests/INDEX.md) | stale-tool guard tests (issue 694) | [own index](queue-guard-tests/INDEX.md) |
| [regulars.py](regulars.py) | recurring activities | [planning](tool-details/planning-and-scouting-tools.md) |
| [duel.py](duel.py) | duel day and advice | [planning](tool-details/planning-and-scouting-tools.md) |
| [resource_map.py](resource_map.py) | resource snapshots | [planning](tool-details/planning-and-scouting-tools.md) |
| [spawn-seat](spawn-seat/INDEX.md) | the only way to spawn a roster seat: model fixed from TEAM.yaml, read back | [own index](spawn-seat/INDEX.md) |
| [model-guard](model-guard/INDEX.md) | quiet check that every roster seat runs the approved model | [own index](model-guard/INDEX.md) |
| [scout_diff.py](scout_diff.py) | observations to work | [planning](tool-details/planning-and-scouting-tools.md) |
| [observation.py](observation.py) | observation file writer | [records](tool-details/records-and-worktree-tools.md) |
| [observation-tests](observation-tests/INDEX.md) | observation.py rollover tests | [own index](observation-tests/INDEX.md) |
| [retro_report.py](retro_report.py) | retro metrics | [records](tool-details/records-and-worktree-tools.md) |
| [log_append.py](log_append.py) | JSONL log append | [records](tool-details/records-and-worktree-tools.md) |
| [log-append-tests](log-append-tests/INDEX.md) | log_append.py gate tests | [own index](log-append-tests/INDEX.md) |
| [live_checkout_check.py](live_checkout_check.py) | live tool drift | [records](tool-details/records-and-worktree-tools.md) |
| [pass_worktree.py](pass_worktree.py) | pass worktrees | [records](tool-details/records-and-worktree-tools.md) |
| [branch_guard.py](branch_guard.py) | records branch guard | [delivery](tool-details/delivery-and-coverage-tools.md) |
| [tree_check.py](tree_check.py) | top-level entries | [delivery](tool-details/delivery-and-coverage-tools.md) |
| [held_patches.py](held_patches.py) | held patch check | [delivery](tool-details/delivery-and-coverage-tools.md) |
| [slot_coverage.py](slot_coverage.py) | ticker slot coverage | [delivery](tool-details/delivery-and-coverage-tools.md) |
| [vip_missed.py](vip_missed.py) | missed VIP days | [delivery](tool-details/delivery-and-coverage-tools.md) |
| [tapcal.py](tapcal.py) | tap calibration | [tap-mac](tool-details/tap-and-mac-tools.md) |
| [mac_capture_probe.py](mac_capture_probe.py) | capture failure diagnosis | [tap-mac](tool-details/tap-and-mac-tools.md) |
| [mac_window_open.py](mac_window_open.py) | window open step | [tap-mac](tool-details/tap-and-mac-tools.md) |
| [harvest_verify.py](harvest_verify.py) | harvest tap check | [harvest](tool-details/harvest-and-pool-tools.md) |
| [pool_gap.py](pool_gap.py) | pool gap | [harvest](tool-details/harvest-and-pool-tools.md) |
| [records_batch.py](records_batch.py) | records batch cadence | [batch](tool-details/batch-and-bridge-tools.md) |
| [cu_bridge.py](cu_bridge.py) | computer-use bridge | [batch](tool-details/batch-and-bridge-tools.md) |
| [lint-gate](lint-gate/INDEX.md) | commit gate and size watch | [gate](tool-details/lint-gate-summary.md) |
| [board-check](board-check/INDEX.md) | project board drift check | [own index](board-check/INDEX.md) |
| [split-doc](split-doc/INDEX.md) | verbatim document splitter | [own index](split-doc/INDEX.md) |
| [cu-bridge-tests](cu-bridge-tests/INDEX.md) | bridge daemon lifecycle tests | [own index](cu-bridge-tests/INDEX.md) |
| [queue-tests](queue-tests/INDEX.md) | queue unit serves-key tests | [own index](queue-tests/INDEX.md) |
| [resource-map-tests](resource-map-tests/INDEX.md) | resource_map.py amount and power-key tests | [own index](resource-map-tests/INDEX.md) |
