---
title: Correction to Arms Race queue run 0004
created: 2026-11-05T00:12:00-08:00
modified: 2026-11-05T00:12:00-08:00
level: L0
version: 1.0.0
description: Correction of two figures in 0004-queue-run.md - consecutive-pass count and session window
status: unverified
---

# Correction to 0004 queue run - Arms Race

This file corrects 0004-queue-run.md. The original entry stands
unchanged, per the append-only rule.

## Corrections

- Consecutive-pass count: the record, the day INDEX, the Issue
  284 comment and the PR body say twenty-second. The count is
  twenty-third. Recount from Issue 284: the issue was filed on
  the third consecutive pass (ticker-1340); the comments run
  ticker-1404 (4th), 1434 (5th), 1504 (6th), 1534 (7th), 1604
  (8th), 1634 (9th), 1704 (10th), 1734 (11th), 1804 (12th),
  1834 (13th), 1904 (14th), 1934 (15th), 2034 (16th), 2104
  (17th), 2134 (18th), 2204 (19th), 2234 (20th), 2304 (21st),
  2334 (22nd) - so ticker-0004 is the 23rd consecutive
  ticker pass with this blocker. The earlier count dropped
  one pass in the 2104 to 2134 step.
- Session window: the record says about 00:04 to 00:22
  America/Los_Angeles. The measured window is about 00:04 to
  00:10: the device token was taken at 08:07 UTC, the last
  device observation was about 08:09 UTC, and the token was
  released at 08:10 UTC. The 00:22 figure was an estimate
  written from memory, not a measured time.
- Nothing else in the record changes: five capture attempts
  across sessions cc-499 and cc-500, Chrome observation
  succeeding in the same session, no screen read, no input
  dispatched, unit failed, tracker untouched.
