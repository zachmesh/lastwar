---
title: Open questions part 1
created: 2026-11-23T06:19:33Z
modified: 2026-11-23T06:19:33Z
version: 0.1.0
sequence: 35
description: The capacity cap per building, and how long until output stops accumulating when bubbles are left
---
## Open questions

- The capacity cap per building, and how long until output stops
  accumulating when bubbles are left uncollected.
- The drone component bubble's spot: still unidentified after
  the 1534 pass (the 164,116 top-left-corner candidate is
  unverified); the next harvest pass must locate it on screen
  rather than assuming the candidate.
- Why HUD food and iron totals rise between harvest units with no
  harvest record between: the 1935 unit flagged food +3.2M and
  iron +3.1M for 18:00-19:50, and the 2310 unit measured food
  +2.8M, iron +2.8M, coin -0.1M for 19:50-23:12 with no
  intervening harvest record. Tracked as GitHub Issue #490
  (labels records). Until resolved, HUD deltas across units are
  not clean harvest measurements. (Added 2026-11-08 2310.)

- Whether bubble collection is per-type (one tap clears every standing bubble of that resource type) or per-bubble, and under what standing conditions the 1935 one-tap-one-bubble read occurs: the 0340 unit cleared all visible bubbles of each type in one tap per type (iron 4, coin 3, EXP 4, food), contradicting the 1935 iron one-by-one re-confirmation, with HUD deltas exceeding the visible sums. Tracked as knowledge Issue #502 (labels knowledge). (Added 2026-11-09 0340. 2026-11-09 0636 update: second independent confirmation - one tap per type cleared all bubbles of each type again; the profile now treats one-tap-per-type as the standing rule with the 1935 read as the single outlier; Issue #502 stays open, closure belongs to the daily retro.) (2026-11-09 1623 update: fourth confirmation - iron 5 bubbles, coin 8 bubbles, food 4 bubbles, each type cleared by one tap, all HUD-verified in-unit; the iron HUD delta again exceeds the visible sum, so the base-wide-collection candidate is still NOT verified. Issue #502 stays open, closure belongs to the daily retro.) (2026-11-09 retro A-2026-11-09-04 specifies one-tap-per-type as the standing rule, grounded in five verified units (0340, 0636, 1220, 1623, 2030); Issue #502 stays open pending the retro's closure decision.) (2026-11-09 2326 update: iron one-by-one read a second time - one tap, +1.8M, 5 mature iron bubbles about 1.30M each still standing; the 1935 read is no longer a lone outlier. Iron stands 5 per-type clears against 2 one-by-one reads; the mechanism is unsettled. Next test: the next harvest unit reads all standing iron bubbles before the tap, taps once, and re-reads - if bubbles remain, one-by-one is a real mode, and the discriminator (bubble age, cluster, grounding) is the open question. Issue #502.) (2026-11-10 0257 update: seventh confirmation - food +2.4M, iron +2.2M, coin +1.5M HUD-verified, field clear after three taps; iron now 6 per-type clears vs 2 one-by-one; the 2326 next-test was not run and is still owed.