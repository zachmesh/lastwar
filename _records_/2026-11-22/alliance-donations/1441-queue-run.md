---
title: Donations run 1441
created: 2026-11-23T14:42:00Z
modified: 2026-11-23T14:42:00Z
version: 1.0.0
description: Unit donations-2026-11-23-0603 - eight coin donations to Quick Construction in two runs, count 8/30 to spent, grey Donate timer 00:16:59 at 14:40:58Z, diamond button never pressed; the timer fits a refill every 35 minutes (unverified)
status: done
grounded_in:
  - source: cu_bridge runs 20261123T143827Z-dc51cf and 20261123T144015Z-df60cd, events and frames step-0004, step-0007 and step-0004, step-0005, 2026-11-23T14:38Z to 14:41Z
  - source: unit brief donations-2026-11-23-0603, tracker policy 2532 and the alliance-donations closing standard
---

# Donations run 1441

Rows in [1441-queue-run.csv](1441-queue-run.csv); one ledger row in [ledger.csv](../growth/ledger.csv).

- **Entry (policy 2532).** Quick Construction 9/10, count **8/30** read at **14:39:00.956Z**, no timer, coin cost 1,000, no different-device dialog. The last tap before it was 10:12:44.209Z (T1).
- **Taps.** Run 1 landed three (8 to 5/30) and ended at `max_steps` with the panel open. The operator ran a continuation because the count was live and the panel still open (the 1002 and 1010 part-two precedent): five more, 5 to 1/30 read after each tap, then one tap from **1/30** at **14:40:53.005Z**. The model's closing text says six taps; the event log shows five clicks, and 3 plus 5 equals the entry count of 8.
- **Close.** Green coin Donate turned grey with the cooldown timer **00:16:59**, read 14:40:58.397Z; the badge rose 98.8K to 99.7K (the Tech EXP bar is blind at 4.4M/8.0M). Count spent: **8 witnessed landed taps, 8,000 coins**. The entry count was above 1, so the close is not flagged uncalibrated. Diamond Donate never pressed.
- **Refill datum (unverified).** The T1 timer (5:10 from 10:12:47.107Z) ends at 10:17:57; this timer ends at about 14:57:57, 16,800 s, which is 8 times 2,100 s, and the entry count was 8. One refill per **35 minutes** fits both reads, against the profile's 20 minutes [G]. It assumes 0/30 after T1 and no tap between (the T2 record shows none). Test: the count reads 1/30 at 14:57:57Z, 3/30 at 16:30Z, 6/30 at 18:03Z.
- **Cost.** 0.096291 and 0.064796 USD, 0.161087 in all, against a stated cap of 0.5 each; 0 refused, no `local_input` pause.
- **Closing state.** The Alliance Tech panel is open over the base (not closed yet); the harvest unit opens next.
- **Rules.** Digest rules 1, 2, 3, 4, 5, 6 and 8 helped; the 20-minute refill in rule 8 is the gap.
