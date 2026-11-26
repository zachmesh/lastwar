---
title: Home Glob Check
created: 2026-11-26T15:53:42Z
modified: 2026-11-26T15:53:42Z
version: 1.0.0
description: home_glob_check.py, the read-only finder of code that globs, lists or walks from the home folder, with its tests and the guard over this tree
---

# Home glob check

On 2026-11-26 a shared tool's `glob(~/*/*/TEAM.yaml)` walked Desktop, Documents, Music and Library and made macOS ask for them: the same breach as `ls ~`
(`~/.dsh/AGENTS.md`). `home_glob_check.py` reads source and never runs it.

`python3 _tools_/home-glob-check/home_glob_check.py [--root DIR] [--staged] [PATH...]`: default scan `_tools_`; exit 0 clean, 1 findings, 2 unreadable.

It flags, in Python (read with `ast`: docstrings and comments never count), shell and Node:
- a path pattern whose first component under the home folder is a wildcard (`Path.home() / "*"`, `~/*/x`, `$HOME/*`);
- a listing, glob or walk whose base is the home folder, Library itself, or Desktop, Documents, Downloads, Music, Movies, Pictures, Public;
- shell `ls ~`, `find ~`, `for f in ~/*`.

Named roots pass (`~/.dsh/sessions/*/x`, `~/.computer-use`). `home-glob: ok <reason>` on the line or the one above allows one. A name set from the home
folder is followed inside its own function; a parameter is whatever the caller passes, so a home handed in from elsewhere is not seen.

Tests (`test_home_glob_check.py`) hold the cases and a guard: no file under `_tools_` may trip the check. Run:
`python3 -m unittest discover -s _tools_/home-glob-check`. The Planner or the Coach can wire `--staged` as a lint rule.
