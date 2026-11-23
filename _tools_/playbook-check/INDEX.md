---
title: Playbook Check
created: 2026-11-23T09:48:36Z
modified: 2026-11-23T09:48:36Z
version: 1.0.0
description: playbook_check.py, the read-only counts-only validator of the activity playbook cards, with its template and tests
---

# Playbook check

OD-20261123-15 turns each activity `INDEX.md` into a playbook card of 300 words or fewer. `playbook_check.py` checks the shape
(`card-template.md`), that every cited path resolves, and flags unverified rules older than 14 days. It writes nothing and prints
counts and finding codes with the activity name, never a rule or a number from a card.

| Command | Use |
|---|---|
| `check PATH...` | each file as a card; exit 1 on a shape or citation error, stale is a warning (`--stale-fail` fails it) |
| `changed --staged` or `--base REV` | at commit: changed cards are checked in full, a card that lost its shape is an error, a page that was never a card is skipped |
| `daily` | for the coach: cards, passes, findings by code, rules verified and stale, the verified share, citations by how they resolve; exit 1 on a failing card or a stale rule |

Findings: card over 300 words; a missing, misordered or extra (Errata) section; more than 8 steps, 5 rules, 3 failures, 3 questions
or 5 links; a rule line without id, status, date and evidence; a superseded rule left in; evidence that is not a `_records_/`
path (never a run note or run article); a question without `test:`; no Numbers line with a digit and a record path; an unresolved
path. A path that resolves only through `_run_notes_/moved-paths/moved-paths.csv` is a warning to update.

Wiring is the coordinator's: the hook runs `changed --staged`, the coach runs `daily`. Tests: `python3 -m unittest discover -s _tools_/playbook-check`.
