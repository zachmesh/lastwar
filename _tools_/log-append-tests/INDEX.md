---
title: Log Append Tests
created: 2026-11-23T07:21:58Z
modified: 2026-11-23T07:21:58Z
version: 1.0.0
description: Fixture tests for the log_append.py pre-delivery gate on made-up JSONL files
---

# Log append tests

Tests for the `gate` command of `log_append.py` (PR 425, issue 422): it checks a JSONL log, repairs in place what is
repairable (concatenated objects split onto their own lines, blank lines dropped) and exits 0 only when the file is
clean. Every file is made up in a temporary folder; no real log is read or written.

They cover the stale tail shape of issue 422, a clean file left byte-identical, an unrepairable line (exit 1, file
untouched), an unreadable file (exit 2), several files with JSON output, and that no object is lost or altered.

Run: `python3 -m unittest discover -s _tools_/log-append-tests`.
