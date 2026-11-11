---
title: Donations queue run 2350
created: 2026-11-09T08:01:00Z
modified: 2026-11-09T08:01:00Z
level: L0
version: 1.0.0
description: Ticker-2334 donations unit, 9 coin donations to Rallied Attack, close unverified, count last read live 1/30
status: unverified
---

# 2350 queue run - Alliance donations

Executor: ticker-2334. Unit: donations-2026-11-08-2203.
Session window about 23:51 to 00:01 America/Los_Angeles.

## Performed

- Alliance menu entered via the shield icon at a fresh measured
  centre, norm 934,710 (magnified crop of the right icon column;
  the 2026-11-02 measured centre 903,787 is stale in the current
  base framing, and the 934,747 grounding point that failed on
  2026-11-02 sits just below the tile on map terrain - the entry
  route rule is satisfied by the fresh measurement). Alliance Techs
  tile tapped; Development tab shown by default with Tech Donation
  Today 1300.
- War tab tree read in full (drag-scrolled): Unit Load Capacity
  2/10, Quick Training 1/10, Expert Trainer 2/10, World
  Interception 5/10, Rapid Siege 5/10, Quick Garrison 5/10, Troop
  Movement 5/10, Rallied HP 7/10, Rallied Attack 7/10, Rallied
  Defense 7/10, Expert Nurse 1/10.
- Target: Rallied Attack 7/10, "Increased Hero Attack in Rallies
  for Allies". It carries the recommended marker - the small round
  red-panda badge on its tile, the only tile with one. The red
  thumbs-up icon sits fixed above the Development tab and does not
  move with the tree scroll, so it is not a node marker.
- Donation panel read live at entry: Tech EXP Required 23.6K/4.5M,
  Current +7%, Next Level +8%, Donation Reward EXP 50 plus 50,
  Donation Count 9/30 (remaining), Donate buttons yellow 2 diamonds
  (never touched) and green 800 coin.
- Donated 9 times with the green 800-coin button (7,200 coin total;
  HUD coin 25.2M, unchanged at displayed precision). Count read
  live through the unit: 9/30 at entry, 4/30 after the first batch
  of 5, 1/30 after the second batch of 4 clicks (only 3 landed -
  one click in the batch did not register), then the final 1
  donation landed (Tech EXP 24.4K to 24.5K). The coin button then
  greyed with a 00:18:26 timer, hiding the count label.
- Closing verification (hard rule): the coin button greyed with a
  00:18:26 timer after the last donation and the timer hides the
  count label, and the 18:26 cooldown exceeds the unit budget, so
  no live 0/30 read exists. The Tech Donation Today footer was
  re-read (1300 at entry to 2200 at close, +900) but the footer
  is NOT a closing count: the ticker-2004 pass found it falling
  6900 to 1800 while donations were being made, and its
  knowledge-gap Issue states it must never be used as a donations
  closing count until understood (see also open Issues #417,
  #423, #450). The +900 is recorded here as an unexplained
  observation only, not as proof of 9 donations.
- The count was last read live at 1/30; one further donation
  demonstrably landed after that read (Tech EXP 24.4K to 24.5K).
  Under the hard rule the unit therefore closes UNVERIFIED, the
  tracker is left untouched (the done mark made at 00:00:57 was
  reverted in this same pass), and the re-read unit already in
  the inbox (donations-2026-11-09-0441, enqueued by ticker-2004)
  re-reads the count at its opening read.
- Fresh replenishment evidence (commented on Issue #423 in this
  pass): the count stood at 8/30 at the ticker-2004 exit (20:44)
  and 9/30 at this unit's entry (23:50), with no donations unit
  running between - the count rose with no donations in between,
  a fresh instance of Issues #423 and #160. Reaching 0 on a
  single node does not settle the day; the closing model needs
  the replenishment rule (Issue #174).
- Returned to the base screen afterwards. No diamonds, money,
  speedups or other spending. No alliance diplomacy, no assembly,
  no teleport.

## Closing reads

- Donation Count last read live 1/30, then 1 final donation landed;
  footer 1300 to 2200 (+900); Tech EXP 23.6K/4.5M to 24.5K/4.5M;
  Rallied Attack still 7/10, +7% toward +8%; coin spent 7,200;
  button greyed with 00:18:26 cooldown at close.

## Outcome

Partial (unverified close). Nine coin donations landed on Rallied
Attack (count read live 9/30, 4/30, 1/30, then one more after the
last live read), but the 00:18:26 timer hid the count before a
0/30 read, and the footer is not a closing count (Issues #417,
#423, #450, #174). The tracker is untouched and the re-read unit
in the inbox re-reads the count. This pass first closed the unit
as done on the footer and reverted that close in the same pass
after reading the ticker-2004 record and the open Issues; the
revert is recorded here and in the day INDEX correction, not
hidden.

## Result stats

- target 1, achieved 0, resources_gained 9 coin donations to
  Rallied Attack, costs 7200 coin, verified no,
  blocker_category unverified-close,
  donations_made 9, donation_count_at_entry 9,
  donation_count_last_read_live 1,
  contribution_before 1300, contribution_after 2200,
  tech_exp_before 23.6K, tech_exp_after 24.5K,
  device_takeovers 0
