---
title: Usage and compatibility notes
created: 2026-11-23T04:53:59Z
modified: 2026-11-23T04:53:59Z
version: 1.0.0
description: Verbatim usage, compatibility link and payload notes from the former tool index
---

# Usage and compatibility notes

Moved verbatim from the former `_tools_/INDEX.md`; only link destinations are adjusted. Back to the [tool index](../INDEX.md).

Run commands from the repository root with Python 3. These helpers use the
standard library and locate their data relative to their script or repository.

For example, run `python3 _tools_/regulars.py todo --json` or
`python3 _tools_/queue.py next --budget-minutes 15`.

`_tools_/` is the canonical directory. The root `tools` symlink keeps existing
external job commands and historical paths working during migration. It shares
all configuration and state with `_tools_/`; it is not a second installation.
New job commands, stage pathspecs and documentation use `_tools_/`. Keep the
compatibility link until external callers have been verified to use that path.
Git cannot stage files through a directory symlink. Records writers must use
`git add -- _tools_/state/` for runtime state; update any external job stage
pathspecs before relying on them to publish state.

This executable payload retains its existing Python and JSON filenames as
specified in the [type registry](../../_conventions_/local-conventions/typed-folder-adoption.md).
Validate write operations against an isolated pool and output directory.
