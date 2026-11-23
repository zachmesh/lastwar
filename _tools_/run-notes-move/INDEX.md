---
title: Run Notes Move
created: 2026-11-23T09:28:30Z
modified: 2026-11-23T09:28:30Z
version: 1.0.0
description: run_notes_move.py, the tool that marks superseded run articles and moves them to the run notes type, with tests
---

# Run notes move

OD-20261123-14 / IMP-20261123-13: the run articles that duplicate a dated record (class a of the coach's audit) are marked
superseded, then moved from `_activities_/<activity>/` to `_run_notes_/<activity>/`. Class b and c stay.

`python3 _tools_/run-notes-move/run_notes_move.py [--root R] plan | apply --activities a,b,c --reviewed a,b,c | verify --base REV`

- `plan` is the dry run: counts per activity, the digest state, catalog pages, links to rewrite, references outside `_activities_`,
  and `--sample N` diffs (frontmatter and changelog only). It writes nothing.
- `apply` takes one block of at most three activities. Per file: `status: superseded`, `superseded_by` the record, version up one
  minor, `modified` now, one changelog line; the original body stays byte for byte; `git mv`; a proof. Then the folder INDEX and
  catalogs (300 words or fewer each), the links inside `_activities_` rewritten, and `_run_notes_/moved-paths/moved-paths.csv`
  (a folder, because the gate blocks a loose file in a type folder). Resumable; a second run changes nothing.
- It REFUSES a file whose class is not a, whose record is missing, whose activity has no reviewed digest, that lacks version or
  modified, or that would reach 500 words. It writes only under `_activities_` and `_run_notes_`: no record is edited.
- `verify` proves each row of the table against the originals at REV.

Tests: `python3 -m unittest discover -s _tools_/run-notes-move`.
