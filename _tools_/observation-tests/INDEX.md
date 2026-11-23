---
title: Observation Tests
created: 2026-11-23T08:45:00Z
modified: 2026-11-23T08:45:00Z
version: 1.0.0
description: Tests for the day observation file rollover of observation.py
---

# Observation tests

Tests for the rollover of `observation.py`. The day observation file kept growing (760 words, over the hard limit, blocking
every commit that staged it). Now a section that would take the day file past 400 words goes into the next key-named
part, `observation-p2.md` and on, each under 450 words; the earlier files stay byte-identical (records are immutable),
the new part carries the cumulative counters, and the folder `INDEX.md` lists it.

They cover: a fitting section still appends; a rollover leaves the old file untouched; counters across parts; a day file
already over the limit; parts filling and rolling; a section too long for any part is refused; headings unique across
parts; reference healing; the index; other file names never roll; `check` across parts; the official word counter.

Run: `python3 -m unittest discover -s _tools_/observation-tests`.
