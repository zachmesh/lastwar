---
title: Glittering Market
created: 2026-11-01T05:00:00Z
modified: 2026-11-23T07:42:02Z
level: L1
version: 1.2.0
description: The Glittering Market - locating its entry, recording its daily free, refresh and exchange rules, and working it daily
status: unlocated
grounded_in:
  - source: mail records of 2026-10-27, 2026-10-29 and 2026-10-30 in _records_
  - source: owner direction of 2026-10-31 - collect daily and maximize
  - source: miss audit fix pass of 2026-10-31
  - source: glittering-market execution record 2026-11-02 0508 queue run
---

# Glittering Market

Read rule-digest.md first.

The Glittering Market - locating its entry, recording its daily free, refresh and exchange rules, and working it daily. This document was split verbatim into 6 articles in reading order; nothing was rewritten, and `split_doc.py --check` rebuilds the original body from them. Find a section by its key (an entry id, a unit key such as run-20261107-1824, or a day) or heading; each line gives the title, the keys the article holds and its first sentence.

- [Glittering Market](glittering-market.md)
- [What this activity is and 1 more](what-this-activity.md) - what-this-activity, what-is-known - A market the game calls Glittering Market.
- [The job](the-job.md) - the-job - Locate the entry.
- [Cadence](cadence-section.md) - cadence-section - Until located - attempted or reported by name under rule R5 of the task...
- [What the 2026-11-02 0508 first attempt added](run-20261102-0508.md) - run-20261102-0508 - Unit glittering-market-2026-11-01-0501 by ticker-0504, session 05:05 to 05:08, status partial, first execution attempt.
- [Open questions](open-questions.md) - open-questions - Entry point, currency, daily free claim, refresh rule and exchange list - none recorded...

## Changelog

- 1.2.0, 2026-11-23 - The `lint_gate.py redact` dry run matched 0 of 1 files (0 matches), so nothing was replaced and `--apply` was skipped; the body was split verbatim by `split_doc.py` from a 117-line, 700-word body into 6 key-named articles and 0 catalog pages, and `rule-digest.md` was added; no word rewritten otherwise. `--verify` PASS and `--check` EQUAL against the redacted original (byte-identical to the unsplit file), body sha256 b62da6e50ea8; the unsplit 1.1.0 file is commit 1f0610cb.
