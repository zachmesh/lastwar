---
title: Test T1 - does a tap from a live 1/30 count land
created: 2026-11-23T01:50:00-08:00
modified: 2026-11-23T01:50:00-08:00
level: L0
version: 1.0.0
description: One-unit falsification test for alliance-donations card rule R1 and digest rule 5, the stop-at-1/30 premise
status: unverified
grounded_in:
  - source: donation records of 2026-10-31 0220, 11-04 1046, 11-08 0920, 11-10 0747 and 0815, 11-11 0434, 11-22 0554 under _records_/
  - source: alliance-donations card and rule digest in the scribe pilot worktree, commits 893b9090 and 0db1a219
---

# T1 - a tap from a live 1/30

**Rule tested:** card R1 and digest 5, "a tap from 1/30 does not land, so stop at 1/30" (status tested).

**Why doubtful.** Five EXP-verified landings from 1/30: 10-31 0220, 11-04 1046, 11-10 0747, 11-11 0434 (tap 4), 11-22 0554. Two EXP non-landings: 11-10 0815, 11-11 0434 (tap 3). The 11-08 "eaten" verdicts rest on a count re-read after the timer, which a regeneration also produces. Quick Construction's bar (3.6M of 8.0M) moves in 0.1M steps and cannot show a landing; Rallied Attack's moves in 0.1K steps.

**Do (about 11 steps; about 8 if entry is 1/30).**
1. Confirm LastWar is frontmost; screenshot the base.
2. Alliance shield (ground fresh), Techs, War tab, Rallied Attack (800 coin).
3. Read count N, Tech EXP, top-bar badge item, cost. Run only if N is 1 or 2 and no timer hides it.
4. If N is 2: tap Donate once and read 1/30, EXP, badge. Each should rise 0.1K, which calibrates both witnesses.
5. At live 1/30: ONE tap. No second tap, no long-press.
6. Screenshots at once, +4 s, +10 s. Leave the panel open.

**Record:** N, seconds since the previous tap, EXP and badge before and after, button state and timer per shot.

**Refuted** (the tap lands): EXP or badge rises 0.1K in any shot after the tap. **Supported for the trial:** neither moves by +10 s. Stage two units an hour apart: one landing refutes R1; one landing plus one miss means intermittent, and the unit reports what differed.

**Risk and spend.** Coin only: 800 per landed tap, two at most. Contribution points are earned, not spent. Diamonds never. An eaten tap loses nothing.
