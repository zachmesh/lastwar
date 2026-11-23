---
title: Ghost Ops
created: 2026-10-26T04:02:00Z
modified: 2026-11-23T07:43:59Z
level: L1
version: 1.2.0
description: Weekly Ghost Ops event missions at the Secret Command Post, one activity folder for ghost ops knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: in-game instructions No.2487 Ghost Ops Guide, read 2026-10-25
  - source: owner direction to register each learned task type as metadata, 2026-10-25
  - source: ghost-ops execution record 2026-11-05 2303 queue run (ticker-2303 unit, failed, Mac device offline, sixty-second consecutive pass, Issue 284)
---

# Ghost Ops

Read rule-digest.md first.

Weekly Ghost Ops event missions at the Secret Command Post, one activity folder for ghost ops knowledge. This document was split verbatim into 6 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Ghost ops](ghost-ops.md)
- [What this activity is and 1 more](what-this-activity.md) - what-this-activity, how-to-enter - A weekly event run from the third tab of the Secret Command Post.
- [How it is played](how-it-is.md) - how-it-is - From the in-game guide (No.2487 Ghost Ops Guide), read 2026-10-25.
- [Cadence and 3 more](cadence-section.md) - cadence-section, scope-and-availability, day-20261025, open-questions - Weekly, Thursdays only, inside the four server time windows.
- [What the 2026-11-05 2303 unit added - Mac](run-20261105-2303-p1.md) - run-20261105-2303 - Unit ghost-ops-2026-11-05-0000 by ticker-2303, about 23:10 to 23:14 local, status failed.
- [What the 2026-11-05 2303 unit added - Mac](run-20261105-2303-p2.md) - run-20261105-2303 - Tracker untouched, per the failed-unit rule; the next tick re-produces the ghost-ops unit.

## Changelog

- 1.2.0, 2026-11-23 - The `lint_gate.py redact` dry run found 0 matches, so no text was replaced; split verbatim by `split_doc.py` from an 86-line, 866-word body into 6 key-named articles and 0 catalog pages, and added `rule-digest.md`; no word rewritten otherwise. `--verify` PASS and `--check` EQUAL against the original, body sha256 70efd7efb5ff; the unsplit 1.1.0 file is commit 1f0610cb.
