---
title: Planning and scouting tools
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim index rows for regulars.py, duel.py, resource_map.py, scout_diff.py
---

# Planning and scouting tools

Moved verbatim from the former `_tools_/INDEX.md` table; only link destinations are adjusted for this folder. Back to the [tool index](../INDEX.md).

| Tool | Purpose | Data |
|---|---|---|
| [regulars.py](../regulars.py) | Track recurring activities; tracker state resolves to the main checkout's state dir when this copy runs from a linked worktree (issue #598) | [regulars.json](../regulars.json) and [state](../state/INDEX.md) |
| [duel.py](../duel.py) | Calculate the active duel day and advice | [duel_schedule.json](../duel_schedule.json) |
| [resource_map.py](../resource_map.py) | Record resource snapshots and check floors | [resources.json](../resources.json) and [state](../state/INDEX.md) |
| [scout_diff.py](../scout_diff.py) | Compare observations with activities and plan work; `--root` accepts a repository root, resolved to its `_queue_` folder, or a pool directory directly, and `--apply` refuses a root holding no pool state directory, so a wrong root fails loudly instead of writing units into a fresh empty directory (issue #510); a dry run against a root holding no pool state directory prints the pool_root_warning, so its counts never silently describe an empty pool (issue #537); --apply prints the pool_root_warning too, so a stray pool beside the resolved pool is named on the write path as well (issue #539); the diff consults today's delivered records branch before enqueueing, so a unit already closed on the branch - or an exploration already closed on the branch today - is reported already-queued instead of re-enqueued (issue #466); unmatched-label lines that are the prose form of an empty list (`- none (...)` block lines, `unmatched_labels: none (...)` scalars and `none  # ...` trailing comments) are skipped instead of filed as exploration candidates (issue #527); the diff also reads the shared main-checkout pool's done/ records before enqueueing, so a slot the ticker already closed in the live pool - whose delivery has not landed on the branch yet - is reported already-queued instead of re-enqueued (issue #533); the none-/empty- slug family is never filed as a candidate, so a marker form the parser misses (``none.``) still cannot mint an exploration unit (issue #536); a per-pass accounting heading that carries its own counts (``Red dots - 8 seen, 6 explained, 2 unexplained``) starts a narrative accounting section with those counts, and its ``- Unexplained:`` bullet names the dots against the heading count, so a narrative-only day no longer reads zero unexplained (issue #149); a Coverage heading's prose red-dot statement (``Red dots seen this unit: 7, explained 6, unexplained 1 (the 99+ chest badge).`` as its own bullet or embedded in the Surfaces-walked bullet) starts a narrative accounting section too, its numbers must add up or the section reads as unstated, and the parenthetical after the unexplained count names the dots, so a Coverage-written day no longer reads zero unexplained (issue #800) | `../_activities_/` and `../_queue_/` |
