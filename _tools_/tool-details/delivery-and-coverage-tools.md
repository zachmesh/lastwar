---
title: Delivery and coverage tools
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index rows for branch_guard.py, tree_check.py, held_patches.py, slot_coverage.py, vip_missed.py
---

# Delivery and coverage tools

Moved verbatim from the former `_tools_/INDEX.md` table; only link destinations are adjusted for this folder. Back to the [tool index](../INDEX.md).

| Tool | Purpose | Data |
|---|---|---|
| [branch_guard.py](../branch_guard.py) | Verify a records-branch tip is a fast-forward over the previous tip before a reconcile merge or push (issue #485); sweep the merged tree for unresolved conflict-marker lines before the push (issue #441); verify a branch descends from its base by merge-base before calling it orphan (issue #605) | `refs/remotes/branch-guard/` |
| [tree_check.py](../tree_check.py) | Verify the ten expected top-level entries (AGENTS.md, README.md, `_activities_`, `_conventions_`, `_knowledge_`, `_logs_`, `_queue_`, `_records_`, `_tools_`, `tools`) are present in the git index and working tree before a delivery commit, or in a committed tree (`--tree REF`) before a push, so a sparse-checkout worktree whose index holds only `_records_` can never push a poisoned tree (issue #541); exit 0 complete, 1 entries missing, 2 cannot verify | the repository root being delivered |
| [held_patches.py](../held_patches.py) | Step-2 in-flight check for held patches (issue #809): `check <issue>` reports HELD (exit 1, do not re-implement), SUPERSEDED or no held patch (exit 0); `list` lists the register; exit 2 when the register cannot be read or a row is malformed | [held-patches.md](../../_conventions_/local-conventions/held-patches.md) |
| [slot_coverage.py](../slot_coverage.py) | Slot-coverage check for queue-ticker records (issue #743): `check` reports the recordless past-window slots on the :04/:34 grid (exit 0 covered, 1 recordless, 2 unreadable or malformed), `list` lists every slot with its status, and `mark` writes a missed-fire marker for a past-window slot, refusing a slot a record already covers; coverage is read from the record title, never the file name alone, so a late-starting record serves the slot its title states | `_records_/<date>/queue-ticker/` |
| [vip_missed.py](../vip_missed.py) | Missed-VIP-days count from the queue pool (issue #742): `count` reports the missed days in a window and the consecutive missed run ending at --to, `list` lists every day with its unit, outcome and verdict; a day is keyed on the unit-id slot date, only the 1800 slot defines a day, and a day is missed when its 1800 unit expired/failed or closed done/partial with claimed_count 0; exit 0 determined, 1 unknown days present, 2 unreadable or malformed | `../_queue_/done/` and `../_queue_/completed/` |
