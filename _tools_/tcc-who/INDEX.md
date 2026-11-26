---
title: Tcc Who
created: 2026-11-26T17:13:05Z
modified: 2026-11-26T17:13:05Z
version: 1.0.0
description: tcc_who.py, the read-only names-only reader of who asked macOS for a protected folder and which Python is running, with its tests
---

# Tcc who

A macOS window that names Python and the Desktop, Documents, Music, All Files or Media Library is a hung process walking the home folder; dismissing
the window lets it ask for the next folder (2026-11-26, 16:58Z then 17:01Z). Steer A's 17:11Z rule: read first, stop that Python first, then the one
`killall -9 UserNotificationCenter`. This tool reads and prints names only, never a path or an argument, and writes nothing.

`python3 _tools_/tcc-who/tcc_who.py pythons [--min-age SECONDS]`: each Python of this user with pid, script file name, elapsed time, parent names up
to the DSH host, and whether the kill rule allows stopping it: named `session-inbox.py`, alive over 60 seconds, not the DSH host, the bridge daemon or
`release-watch.py`. It prints `kill <pid>` only for an eligible one; none means only the one `killall`.

`python3 _tools_/tcc-who/tcc_who.py window START END [--all]`: the tccd requests between two UTC times (`HH:MM:SSZ` today or a full stamp, at most ten
minutes) by requester: time, responsible process, services (`(access)` is an actual access, not a preflight). Apple's own requesters are left out
unless `--all`. It reads the unified log with `log show`; times print in the Mac's local time.

Exit 0 for a read, 2 when `ps` or `log` cannot run or a time is wrong. Tests (`TCC_WHO_PS_FILE` and `TCC_WHO_LOG_FILE` feed recorded output):
`python3 -m unittest discover -s _tools_/tcc-who`.
