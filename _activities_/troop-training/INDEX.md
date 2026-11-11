---
title: Troop Training
created: 2026-10-25T20:12:00Z
modified: 2026-11-11T14:32:17Z
level: L1
version: 1.43.0
description: Training new troops in the barracks, tier by tier, one activity folder for training knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner task request naming a train task, 2026-10-25
  - source: web guides on barracks and troop tiers, read 2026-10-25
  - source: troop training execution record 2026-11-01 1216 queue run
  - source: troop training execution record 2026-11-01 1651 queue run
  - source: troop-training execution record 2026-11-01 2120 queue run (ticker-2104 unit, partial, barracks tents not located after north and south pans)
  - source: troop-training execution record 2026-11-02 0322 queue run (ticker-0308 unit, partial, pistol tap opened upgrade panel)
  - source: troop-training execution record 2026-11-02 0811 queue run (ticker-0804 unit, partial, action-row taps switched to the world map)
  - source: troop-training execution record 2026-11-02 1146 queue run (ticker-1134 unit, partial, Lv.24 batch queued, Lv.20 pistol route retired)
  - source: troop-training execution record 2026-11-02 1723 queue run (ticker-1703 unit, partial, Lv.24 panel not opened from inherited points)
  - source: troop-training execution record 2026-11-02 1949 queue run (ticker-1934 unit, partial, drag blocked by open radial)
  - source: troop training execution record 2026-11-02 2255 queue run
  - source: ticker-0234 troop-training execution record 2026-11-03 0252 queue run (partial, road drag pans, centre drag does not, no tent)
  - source: ticker-0634 troop-training execution record 2026-11-03 0647 queue run (partial, no tent in four framings, road drags pan)
  - source: ticker-1034 troop-training execution record 2026-11-03 1051 queue run (partial, three framings no tent, road drag pans where centre drag does not, Issue 150)
  - source: ticker-1534 troop-training execution record 2026-11-03 1552 queue run (partial, Lv.27 T9 batch queued and HUD-verified, tent blocker breakthrough, Issue 150)
  - source: ticker-2134 troop-training execution record 2026-11-03 2144 queue run (partial, production grid is factories not tents, 1552 point selects Factory No.3 in this framing, Issue 150)
  - source: ticker-0134 troop-training execution record 2026-11-04 0143 queue run (partial, factories confirmed again, 1552 tent point not re-tried, Tank Base Lv.28 to 29 upgrade in progress, Issue 150)
  - source: ticker-0434 troop-training execution record 2026-11-04 0440 queue run (partial, tent point 585,548 selects Barracks Lv.24, Drill Ground Full confirmed live again, Training Count +666, Issue 150)
  - source: ticker-0804 troop-training execution record 2026-11-04 0814 queue run (partial, 0440 tent point selects Arena in this framing, Lv.20 verified via Details, framing instability measured, Drill Ground Full neither reconfirmed nor cleared, Issue #150 comment deferred)
  - source: ticker-1134 troop-training execution record 2026-11-04 1147 queue run (partial, fullscreen framing mismatch, four grounded tent taps opened no panel, centre drag moved no view, session drop reopened, Issue 150)
  - source: ticker-1734 troop-training execution record 2026-11-04 1734 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, eleventh consecutive ticker pass to fail this way, Issue 284)
  - source: ticker-0534 troop-training execution record 2026-11-05 0534 queue run (failed, Mac screen-capture failure on every attempt, no game screen read, no input dispatched, thirty-fourth consecutive pass, probe classification OFF_SCREEN_WINDOW, Chrome observes normally in the same session, Issue 284)
  - source: ticker-1655 troop-training execution record 2026-11-07 1655 queue run (partial, Lv.27 T9 x726 and Lv.30 T10 x793 requeued at cap, 9.6M food plus 9.6M iron, two upper-right barracks unchecked, Drill Ground Full not seen; record commit 514e333e5b on records/2026-11-07)
  - source: ticker-2006 troop-training execution record 2026-11-07 2026 queue run (partial, Lv.27 verified busy 1d 07:03:33 by panel read, Lv.30 busy by timer bubble only, two upper-right barracks unlocated, south and east pans ruled out; record commit e9bf320c92 on records/2026-11-07)
  - source: ticker-2034 troop-training execution record 2026-11-07 2050 queue run (partial, Lv.30 busy T10 x793 1d 13:41:04, Lv.24 idle but blocked by Drill Ground Full toast, Drill Ground Lv.25 read live Unit Count +7812 Officers Joe/Marcus/Karen/John Quick Dispatch present not tapped, tent-body taps missed twice, no_change_observed flag unreliable; record commit 7a4a104930 on records/2026-11-07)
  - source: ticker-1317 troop-training execution record 2026-11-08 1350 queue run (partial, Lv.30 barracks re-verified busy, Lv.10 batch 793 with 20:47:28 left, tent tap (459,457) opens TRAIN UNITS directly, tent tap (564,510) misses, no batch queued; record commit d272dd711 on records/2026-11-08)
  - source: ticker-2058 troop-training execution record 2026-11-08 2119 queue run (partial, Lv.27 busy, Lv.20 Drill Ground Full re-confirmed live, paw Details route works, long-press retired, T9 stats corrected; record commit 023fb42b6 on records/2026-11-08)
  - source: ticker-0019 troop-training execution record 2026-11-09 0039 queue run (partial, Drill Ground Lv.30 read live, Unit Count +10080, officers Samantha/William/Chloe/Catherine, Quick Dispatch not tapped, fenced structure resolves to Aircraft Center Lv.29, no barracks verified; record commit f99faa9744 on records/2026-11-09)
  - source: ticker-0034 arms-race execution record 2026-11-09 0058 queue run (partial, Unit Progression phase read live 0 points, Events entry (672,132), orange medal is Wall of Honor, back arrow centre (355,944), fill not executed, barracks state carried forward; record commit 77db994162 on records/2026-11-09)
  - source: ticker-0113 arms-race execution record 2026-11-09 0129 queue run (partial, Unit Progression phase read live again 0 points, third consecutive tent-grounding failure, red troop formation resolves to Drill Ground Lv.30, entry route must change, phase ends about 02:00; record commit c0ebf0c4f0 on records/2026-11-09)
  - source: ticker-0404 troop-training execution record 2026-11-09 0413 queue run (partial, fullscreen zoom-out variant tried, no barracks tent verified, View-menu fullscreen exit measured; record commit 9fdcc4c9ee on records/2026-11-09)
  - source: ticker-1304 troop-training execution record 2026-11-09 1330 queue run (partial, Lv.27 idle and blocked by Drill Ground Full, tents grounded by a fresh route, blue-roofed tents are Material Workshops; record commit 5108be8d7 on records/2026-11-09)
  - source: ticker-2040 troop-training execution record 2026-11-09 2103 queue run (partial, barracks tent tap no-change x3, no TRAIN UNITS panel, Drill Ground not read, next unit must change entry route per R2; record commit ca96fa0c9 on records/2026-11-09)
  - source: ticker-0034 troop-training execution record 2026-11-10 0034 queue run (partial, formation-yard taps resolve to squads and the Wall, Drill Ground selection route does not reproduce; record commit d3c648601 on records/2026-11-10)
  - source: ticker-0334 troop-training execution record 2026-11-10 0337 queue run (partial, fourth consecutive training partial with the same blocker, R2 process failure, wide-zoom and panned-down tent taps select nothing, Duel screen live read UR truck dispatch +300,000; record commit b7e79a62 on records/2026-11-10)
  - source: ticker-0834 troop-training execution record 2026-11-10 0850 queue run (partial, fifth consecutive training partial, R2 process failure, game found on TECH screen by unexplained navigation, slot-1 timer discrepancy, no barracks requeued; record commit 5473d6845 on records/2026-11-10)
  - source: ticker-1204 troop-training execution record 2026-11-10 1229 queue run (partial, Lv.24 requeued T8 x666 verified running, Drill Ground Full did not block it, R2 five-partial run broken, T8/T10 stats corrected live; record commit 88e51ae5d on records/2026-11-10)
  - source: ticker-1634 troop-training execution record 2026-11-10 1649 queue run (partial, verified no, no barracks tent located after three camera pans, blind-pan method retired under R2, Lv.24 T8 batch still running to about 2026-11-11 16:49; record commit 986c1877 on records/2026-11-10)
  - source: ticker-1503 perception-scout execution record 2026-11-10 1521 queue run (partial, Drill Ground level-up to Lv.27 live, upgrade to Lv.28 available with costs met, not started; record commit f530c19b7 on records/2026-11-10)
  - source: ticker-2122 troop-training execution record 2026-11-10 2146 queue run (partial, Lv.27 finished batch of 313 Lv.9 collected, power +423,176, requeue blocked by Drill Ground Full live toast, tents re-grounded fresh, 1229 point stale for current framing; record commit ccb00e883 on records/2026-11-10)
  - source: ticker-0155 troop-training execution record 2026-11-11 0213 queue run (partial, Lv.30 pistol x2 and paw x1 close the button row with no panel, Drill Ground screen still not read live, fourth consecutive unit on the same blocker, changed entry route needed; record commit 72b82b0e3 on records/2026-11-11)
  - source: ticker-0534 troop-training execution record 2026-11-11 0548 queue run (partial, Lv.24 barracks busy 11:01:26, 1 of 4 checked, radar-entrance wrong turn, Drill Ground live read not done, duration corrected to about 4 minutes; record commit a3ef6b276 on records/2026-11-11)
---

# Troop training

## What this activity is

Training new troops in the four base Barracks. Each barracks trains one
batch at a time, up to its Training Count, at the highest tier its own
level unlocks. This folder accumulates training knowledge - entry,
costs, timers and tier rules. Executions are recorded in
`_records_/<date>/troop-training/`, one file per execution.

Naming note - the owner named this the train task on 2026-10-25. In
game there is also a separate alliance train at the station, registered
on its own as [`alliance-train`](../alliance-train/INDEX.md). Training
troops and riding the train are different systems and are kept apart.

## How to enter

- On the base screen, tap a Barracks tent. The four tents stand in the
  lower middle of the base in this layout. The tent row's screen
  position is camera-dependent: measure it fresh in the unit's
  own view, never from a pinned coordinate - a reused point has
  selected a wrong building (0917 unit, below).
- CORRECTION 2026-11-09 1330: the diagonal row of blue-roofed tents in the upper base is NOT barracks - it is Material Workshops (a tap at norm (267,365) selected Material Workshop Lv.20, a tap at norm (460,290) selected Eternal Pyramid Lv.3). The barracks are the beige tents with blue zigzag markings at the base lower-right edge, each with an instructor portrait circle overlapping the tent body - tap the body, not the circle, as the 1655 unit already noted. The 'lower middle' wording above is refined for the current camera view: the tents sit at the lower-right edge, and the second beige tent sits half off the bottom edge and needs the camera panned down first. (Update 2026-11-10 0337: the beige tents at the base right edge did not select at wide zoom or in the panned-down view either - (890,500) and (919,530) on the tent bodies at wide zoom and (841,116) in the panned-down view, all no-change; the top-right corner points open the radar map (903,468) and the Alliance Duel screen (903,198) instead. The next unit needs a new grounding route, not another tap on these tent points.)
- A row of round buttons appears under the selected tent: paw,
  pistol and green up arrow. The green up arrow is the upgrade
  shortcut - do not tap it. The paw-to-Details and pistol-to-TRAIN-UNITS mapping is camera-position dependent, not dead: the 0811 suspension is LIFTED IN PART 2026-11-02 (1146 unit), which re-grounded the Lv.24 row fresh (paw about 670,584; pistol 794,605; green up arrow 930,584) and opened TRAIN UNITS with the pistol tap. The 0811 world-map result and the 0322 upgrade-panel result do not carry across camera views. The standing rule is fresh grounding of the whole row in every unit's own view, never inherited coordinates. (Update 2026-11-09 2103: a freshly grounded tent tap can still fail to open the panel - the 2103 unit's three tent taps produced no TRAIN UNITS panel; the next unit must change the entry route before tapping a tent again, per queue rule R2 - try click_element on the tent control, a foreground click with the window truly frontmost, or a different barracks tent; the same background-click point must not be repeated. See the 2103 section.) The 1552 unit extends the lifted-in-part pistol route to Lv.27 in its view: tent grounded at norm (630,592), pistol re-grounded at norm (612,608) before tapping, TRAIN UNITS opened with Lv.9 preselected. QUALIFIED 2026-11-03 (2144 unit): that same tent point (630,592), re-tried after a rightward drag re-framing, selected Titanium Alloy Factory No.3 Lv.30 in the 2144 framing, not a barracks tent - so the point is framing-bound, not a portable tent coordinate. Re-grounding in the unit's own view is mandatory, and a factory selection must never be re-tapped as if it were a tent. The Lv.20 pistol route is separately RETIRED 2026-11-02 (1146 unit): two fresh pistol points (818,584 and 829,575) both only cleared the selection, so the next Lv.20 attempt tries a different entry route (a long-press variant on the selected tent, or the paw Details route with freshly grounded coordinates).
  QUALIFIED 2026-11-08 (2119 unit): the paw Details route WORKS for Lv.20 (Training Count +613, instructors Alexis, Joe, Jolene and Anthony; the Details panel shows no batch timer, so busy/idle is not readable from it; Quick Dispatch NOT tapped, owner decision) and the pistol tap in the 2119 framing REACHED the train attempt (live toast "Drill Ground Full: Unable to add more units"), so the 1146 pistol retirement is framing-bound, not a dead route. The long-press variant is RETIRED by the same unit: a 1-second long-press on the selected Lv.20 tent body entered building-move mode (red X and green check at screen centre), cancelled at once with the red X, no building moved - do not repeat.
- In TRAIN UNITS, the tier cards run left to right with the highest
  unlocked tier preselected, the count slider sits at the Training
  Count cap, and the blue Train button starts the batch. The yellow
  Finish Now button is never used, under the recording rules on
  spending.
- Entry, 2026-11-10 1229: a tap on the tent carrying the gold face bubble (norm 374,526) selected the Lv.24 barracks and raised the toast 'Training complete: 666 Lv.8 units are ready' - the gold-bubble tent is a working entry point for Lv.24 in that framing. Re-ground fresh in the unit's own view; the point is framing-bound, not portable. (2026-11-10 1649 update: the blind-pan method is RETIRED under rule R2 - three pans in this unit (down overshot into full fog, right barely moved the view, long right overshot past the base edge into fog with a mountain peak) never landed on a tent. The next training unit re-grounds from the 1229 record's successful entry - read troop-training/1229-queue-run.md for the measured tent point that opened TRAIN UNITS that day - and goes straight to that point before any pan. If the tents still cannot be located from that grounding, the blocker is filed as a GitHub issue instead of a third identical partial.) (2026-11-10 2146 CORRECTION: the 1229 point (374,526) no longer matches the current camera framing - the 2146 unit re-grounded the tents fresh from the current screenshot instead (lower-middle tent bbox 549-688, 533-614; lower-right tent bbox 653-814, 580-675) and located both with no pan. Do NOT go straight to 374,526; re-ground the tents fresh from the current screenshot every unit. The issue-filing trigger did not fire - the tents were located.)
- Entry, 2026-11-11 0548: the 2146 groundings (tent at norm 374,526 / 618,573) no longer match this camera framing - a tap on the tent at norm (763,584) opened the radar world map (12 Radar Tasks to restore in 05:49:38, 1/40 stored, Quick Execute offered) instead of a barracks; that structure is the radar entrance in this framing, not a barracks tent, and no radar action was taken. The tap on the tent at norm (864,610) opened TRAIN UNITS for the Lv.24 barracks. Tents must be re-grounded fresh every unit. The visual grounding tool returned two boxes for both "Drill Ground" and "barracks tent" (553-652, 638-710 and 658-781, 688-758) without distinguishing them; those boxes do not match the tents visible in this framing and were not used as tap points. Grounding points must be verified against the live screenshot, not trusted blindly.

## How it is done

- Keep every barracks busy. One batch per barracks at its highest
  unlocked tier, count left at the cap, then press Train.
- Busy/idle is read from the 'Training in progress' line in the TRAIN UNITS panel, not from the button time: the 1d 17:14:37 shown on the Lv.30 panel's buttons is the prospective batch duration (2026-11-10 1229 lesson); a barracks showing only the button time is state-unverified. (2026-11-10 1649 update: the Lv.24 T8 x666 batch queued at 12:29 for 1d 04:19:43 is still running and is not due for requeue until about 16:49 on 2026-11-11; Lv.30, Lv.27 and the fourth barracks are state-unverified in this unit.) (2026-11-10 2146 update: Lv.27 is now checked - its finished batch of 313 Lv.9 was collected (power +423,176, exactly 313 x 1,352) and it is idle, but its requeue is blocked by the Drill Ground Full toast live; Lv.24 still running to about 2026-11-11 16:49; Lv.30 and the fourth barracks are still unchecked.) (2026-11-11 0548 update: Lv.24 checked live - T8 x666, "Training in progress 11:01:26", busy until about 16:58 today, no action possible; matches the 2146 note (queued 12:29 for 1d 04:19:43). The other three barracks were not checked. The Lv.27 barracks was idle and requeue-blocked by Drill Ground Full at 21:46 yesterday (unit 2146); its state today is unverified - carried, not re-read.)
- Queueing a batch costs food and iron only, paid up front. No diamond
  use, no instant finish.
- Training finishing also feeds VS Unit Progression and Arms Race
  points, per the web guides - unverified on this account.

## Cadence

- Continuous. A batch runs from about 23 hours to about 1 day 17 hours
  at this account, so in practice requeue each barracks as its batch
  finishes - check once per daily round and requeue any idle barracks.

## Scope and availability

- Always available, not season specific.
- Four barracks, one batch each. Barracks level gates the tier -
  observed Lv.24 trains up to T8, Lv.27 up to T9, Lv.30 up to T10.
  Guide tables agree (T8 at Lv.24 to 26, T9 at Lv.27 to 29, T10 at
  Lv.30 with Special Forces research), unverified beyond the observed
  three.
- Promotion of lower tier troops exists from Barracks Lv.10 per the
  guides. The promote arrow in the panel did nothing on the observed
  barracks, so its exact conditions are unconfirmed.

## What is known from 2026-10-25

Observed in game on this account, first execution 2026-10-25.

- Lv.30 barracks - T10, count 793, cost 5.5M food and 5.5M iron, time
  1 day 17 hours 14 minutes. T10 panel stats - power 1647, morale
  750.0, load 2200, HP 4726.34, attack 38.45, defense 7.79 (2026-11-10 1224 live read, superseding the 2026-10-25 baseline 720.01 / 38.03 / 7.55; the 1655, 2050 and 1350 units already read morale 750.0 and attack 38.45 live, and defense 7.7, the same figure at lower precision - the baseline section was never updated for those reads, corrected here).
- Lv.27 barracks - T9, count 726, cost 4.1M food and 4.1M iron, time
  1 day 10 hours 19 minutes. T9 stats - power 1352, morale 625.0 (2026-11-08 2119 live panel read, superseding 600.01),
  load 2000, HP 4121.49, attack 33.5, defense 6.74 (2026-11-08 2119 live panel read, superseding 33.13 / 6.67).
- Lv.24 barracks - T8, count 666, cost 2.9M food and 2.9M iron, time
  1 day 4 hours 20 minutes. T8 stats - power 1063 in game (one web
  table says 800 - the in-game figure governs), morale 531.25, load 1800, HP 3527.4, attack 28.69, defense 5.84 (2026-11-10 1229 live read, superseding the 2026-11-02 read 520.63 / 28.37 / 5.72).
- Fourth barracks - highest tier T7, count 613, cost 2.0M food and
  2.0M iron, time 23 hours 11 minutes. T7 stats - power 779, morale
  444.01, load 1600, HP 2942.73, attack 23.75, defense 4.7. Its own
  level was not read this round.
- Instructor survivors are assigned per barracks in Building Details.
  Quick Dispatch was not used.
- Guide strategies noted but not adopted - staggered barracks levels
  (the waterfall) and training T1 then promoting up to save resources.
  This account already runs staggered barracks levels by accident of
  its upgrade history.

## Limits

- Never tap Finish Now or the green upgrade shortcut while training.
- Training spends food and iron from stock. The 2026-10-25 round spent
  14.5M of each across four batches, small against roughly 290M stocks.

## Standing blocker recorded by the retro of 2026-10-31

- Queue era 2026-10-28 to 2026-10-31 - 21 of 22 training units
  closed non-done, 19 partial and 2 failed, 1 done. The dominant
  late-window blocker is Drill Ground Full, reading 39,460 of
  39,460, which blocked both collection and requeue in every
  2026-10-31 unit that reached a barracks.
- How a full Drill Ground is cleared is not yet known from a
  live read, and no clearing method is claimed here. The next
  unit reads the Drill Ground screen live first, records what
  controls it actually shows, and spends itself on the nearest
  allowed preparatory action instead of closing as a bare
  blocked read. This is a third-strike blocker under queue
  rule R2.
- Update 2026-11-07 2050: the Drill Ground screen was read live,
  as this section required - Drill Ground Lv.25, Building Details
  panel reads Unit Count +7812, Survivors Officers Joe, Marcus,
  Karen and John, and a single action button Quick Dispatch at the
  panel bottom. Quick Dispatch was NOT tapped: its effect is
  unverified and it may march troops out, so it is left for an
  owner decision or a learn-first exploration unit, not pressed
  blind inside a training unit. No 39,460 of 39,460 figure appears
  on this screen; that figure comes from earlier units and was not
  re-read live here, so its provenance is the 2026-10-31-era reads.
  The clearing method for a full Drill Ground is still unknown from
  a live read; Quick Dispatch is the only candidate control seen,
  untested.
- Update 2026-11-09 0039: the Drill Ground screen was read live
  again - Drill Ground Lv.30 (the 2050 unit read Lv.25 on
  2026-11-07, level risen since, not reconciled), Building Details
  panel reads Unit Count +10080 (up from +7812), Survivors
  Officers Samantha, William, Chloe and Catherine (roster rotated
  since Joe, Marcus, Karen and John), single action button Quick
  Dispatch at the panel bottom, NOT tapped (effect unverified, may
  march troops out, left for an owner decision or a learn-first
  exploration unit). No capacity denominator appears on this
  screen; the 39,460 of 39,460 figure was not re-read live. The
  clearing method for a full Drill Ground is still unknown from
  a live read; Quick Dispatch is the only candidate control seen,
  untested.
- Update 2026-11-09 0129 (arms-race unit, R2 metadata write): the barracks tents were not located for a third consecutive unit (0039 troop-training, 0058 arms-race, 0129 arms-race) - a third strike under queue rule R2. The red troop formation at the base's lower middle, tapped from a fresh route in the 0129 unit, resolved to Drill Ground Lv.30 again (paw, train-hat and green upgrade buttons), not a barracks tent. Both failed routes are now retired: the yellow-green fenced structure (Aircraft Center Lv.29) and the red troop formation (Drill Ground Lv.30). The entry route must change before any further training or arms-race fill unit runs - the next attempt must not re-tap either structure. Drill Ground Lv.30 re-confirmed live by the 0129 unit. The phase ends about 02:00 local, before the Lv.27 batch ends about 03:27, so even a located idle barracks may still be blocked by Drill Ground Full.
- Update 2026-11-09 1330: Drill Ground Full re-confirmed live on a second barracks - Lv.27 is idle and blocked, the pistol tap producing the toast 'Drill Ground Full: Unable to add more units' (read live by OCR), no TRAIN UNITS panel opened. The 2050 unit read the same blocker for Lv.24 on 2026-11-07, so the blocker now spans two barracks two days apart. No timer bubble stands above the Lv.27 tent, consistent with idle. The clearing method is still unknown from a live read; Quick Dispatch is still the only candidate control seen, untested. Grounding drift: the building at norm (435,518) is the ICU hospital, not a barracks - the 2050 grounding point no longer maps to a barracks in the current camera view.
- Update 2026-11-10 0337: fourth consecutive training partial with the same blocker (0039, 1330, 0034, this unit), each with a changed method and none requeuing a barracks - per queue rule R2 a fourth identical partial is a process failure, not a result, and it was reported as one on Issue #150 by the ticker pass (comment 2026-11-10T11:42:26Z). The beige tents at the base right edge do not select at wide zoom or in the panned-down view; the top-right corner hotspots belong to the VS and radar entries. The Drill Ground screen was NOT re-read live; the Drill Ground Full toast (39,460 of 39,460, last read live 2026-10-31) stays carried forward unverified. The next unit needs a new grounding route, not another tap on these tent points. (Update 2026-11-10 0850: fifth consecutive partial with the same blocker - 0039, 1330, 0034, 0337, this unit - R2 process failure stands, and this unit added its evidence comment to Issue #150 as well. The untried routes named for the next unit are the full-observe accessibility tree with click_element on the tent control, and a fullscreen reframe via the green zoom button (never Ctrl-Cmd-F or Escape, both crash the app). The right-edge tent points (0337) and the formation-yard points (0034) are retired and must not be re-tapped.)
- Update 2026-11-10 1229: the five-consecutive-partial R2 process failure is BROKEN - the 1229 unit requeued the Lv.24 barracks (T8 x666) and verified it running ('Training in progress 1d 04:19:43'), the first requeue since the 0850 unit. The Drill Ground Full blocker (39,460 of 39,460, last read live 2026-10-31) did NOT block this collection or requeue: the finished batch counted into power on the tent tap (+707,958, exactly 666 x 1,063) with no Drill Ground visit, no toast appeared, and the new batch is running. The standing claim that Drill Ground Full 'blocked both collection and requeue' is contradicted by this live requeue and is now qualified - the toast appeared in earlier units (2050 for Lv.24, 1330 for Lv.27), but it did not stop this unit. Whether the Drill Ground is still full is unverified (not re-read live); the clearing method remains unknown from a live read, and Quick Dispatch stays untapped (owner decision). Commented on Issue #150 by this run. The unit is still partial (1 of 4 barracks requeued, 2 unchecked), so the done-streak metric is unchanged - only the same-blocker partial run is broken. (2026-11-10 2146 QUALIFICATION: Drill Ground Full is live again for requeue - the 2146 unit's Lv.27 requeue attempt raised the toast 'Drill Ground Full: Unable to add more units' and no panel opened, while the Lv.27 finished batch still collected into power on the tap (+423,176) with no Drill Ground visit. Collection and requeue are DECOUPLED: collecting never needed the Drill Ground, requeueing does. The 1229 'did not block' reading stands for that unit only; whether the Drill Ground refilled between 1229 and 2146 or the block is per-barracks is unverified - the Drill Ground screen itself was not read live in either unit. How a full Drill Ground is cleared is still not known from a live read; the next training unit's first action is to read the Drill Ground screen live. Commented on Issue #150 by this run.) (2026-11-11 0213 update: still not read live - the 0213 unit could not locate the Drill Ground building on the base screen and the barracks button row never opened a panel from which it could be reached; two pistol taps plus one paw tap on Lv.30 all closed the row with no panel, so the pistol method ends for this barracks per R2. The next training unit must locate the Drill Ground building FIRST - by name on the base screen or via a troop overview entry - before tapping any barracks button again. This is the fourth consecutive unit closing on the same blocker; the blocker now needs a changed entry route, not another pistol tap. Commented on Issue #150 by this run.) (2026-11-11 0548 update: still not read live - the 0548 unit checked the Lv.24 barracks (busy 11:01:26) and the pass budget ended at the Lv.24 panel, so the Drill Ground read did not happen. How a full Drill Ground is cleared is still unknown from a live read. The next training unit's first action remains: locate the Drill Ground building on the base, open it, and record what controls it actually shows (deploy, dispatch, dismiss, collect). Commented on Issue #150 by this run.)
- Update 2026-11-10 1521 (scout cross-read): the Drill Ground levelled up live to Lv.27 (Power 118,600 to 140,200, Unit Count +7,200 to +7,400, +21,600 total power verified) - this supersedes the standing Lv.30 reads (0039, 0129), now treated as misidentifications, not deleted. Upgrade to Lv.28 is available with all costs met and was NOT started (red line, owner-initiative); the 24.0M EXP reward card was not tapped. The Full state is still unverified (not re-read live); Quick Dispatch stays untapped (owner decision).

## What the 2026-11-01 0045 unit added

- Inherited points went stale after camera drift: a tap at norm
  708,602 (the pinned Drill Ground / Lv.30 point from the
  2026-10-31 03:04 and 07:04 units) selected nothing visible in
  this camera view, and a tap at norm 617,570 (the pinned Lv.27
  tent point from the 15:44 unit) likewise selected nothing -
  no label, no button row. The camera had drifted through the
  preceding survivors unit's pans. This is the queue rule R2
  failure mode in miniature: points must be measured fresh in
  the unit's own camera view, never inherited, and this unit
  recorded the miss instead of repeating the taps.
- No ungrounded tap followed: an enlarged crop of the base
  centre in this view showed production houses carrying 59.6K
  resource bubbles, a helicopter pad and a green military
  vehicle, but no barracks tent row that could be grounded
  with confidence, so no TRAIN UNITS panel opened, no Drill
  Ground panel opened, and no toast (including Drill Ground
  Full) was read live in this unit.
- Full-block status carried forward unverified: the standing
  Drill Ground Full block from 2026-10-31 (39,460 of 39,460)
  is carried forward unverified by this unit, not
  re-confirmed and not cleared, because the unit never reached
  a barracks.
- Focus note, shared with the survivors unit in the same pass:
  pans stopped moving the view after a focus loss and resumed
  only after a title-bar left-segment tap at norm 274,18.
- Not attempted: no batch collected or started, no troops
  deployed or dismissed to free drill-ground space (an
  owner-side decision, outside this unit), no Finish Now, no
  green upgrade shortcut, no purchase, no diamond spend, no
  speedup item burned. The game was left on the base screen.

## What the 2026-11-01 0917 unit added

- Pinned-point failure escalated from a miss to a wrong
  building: in this camera position, norm 617,570 (the
  pinned Lv.27 tent point from the 2026-10-31 15:44 unit,
  which merely missed in the 0045 unit) positively
  selected Missile Vehicle Base Lv.10. The other two taps
  in this pan selected Titanium Alloy Factory No.1 Lv.30
  at norm 405,475 and Titanium Alloy Factory No.2 Lv.30
  at norm 330,540 - so the unit was searching a factory
  pan, not the tent row. A reused coordinate therefore
  does not just miss across camera positions; it can
  select a wrong building. Leave any wrongly selected
  building untouched (no upgrade shortcut, no Finish
  Now, no Train pressed) and pan to the tent row first
  rather than repeating taps in the same pan - the
  record's own next-unit instruction.
- Drill Ground Full carried forward unverified a second
  consecutive unit: 0045 and 0917 both never reached a
  barracks, and the Drill Ground panel was not re-read in
  0917, so the 39,460 of 39,460 block remains a
  2026-10-31 read, not a 2026-11-01 re-confirmation, and
  no clearing method is claimed.
- Control-channel recovery: the computer session dropped
  mid-unit; a new session re-selected Last War with no
  game state lost, no different-device dialog, and no
  login demanded.


## What the 2026-11-01 1216 unit added

- Changed method per queue rule R2: instead of repeating
  taps in the factory pan, this unit panned the base view
  in four directions looking for the tent row. The opening
  pan showed the Titanium Alloy Factory cluster in the
  walled compound; one tap at norm 400,535 selected
  Titanium Alloy Factory No.4 Lv.30 and was left untouched
  (no upgrade shortcut, no Train, no Finish Now). Four
  drags then swept the view - up, right, diagonal
  down-left, and up again - showing the HQ and furnace
  sector, the vehicle Formation 2 and 3 parking sector,
  and empty snowfield to the south and east. No barracks
  tent row appeared in any swept pan, so no TRAIN UNITS
  panel was reached, no batch was collected or started,
  and the Drill Ground panel was not re-read in this unit.
- Drill Ground Full carried forward unverified a third
  consecutive unit: 0045, 0917 and now 1216 all never
  reached a barracks, so the 39,460 of 39,460 block
  remains a 2026-10-31 read, not a 2026-11-01
  re-confirmation, and no clearing method is claimed.
- Next-unit instruction, from the record itself: try a
  zoomed-out whole-base view first (the current pans
  cover the compound and the surrounding snowfield but
  never show a tent row), and ground the Drill Ground
  building itself before any further tent taps, since the
  drill-ground gate is the standing blocker and its panel
  has not been read live since 2026-10-31. This is the
  same zoom-out-first variant the 1159 survivors unit
  names for its own gate search - the two searches share
  the method, not the target.
- Not a live read: the chat line visible during the unit,
  "thorsey: need to lose some troops", is consistent with
  a full drill ground but is not a live read of the Drill
  Ground panel and is not used as one. The red target icon
  with a countdown seen at the right edge of the closing
  pan was left untouched: it belongs to another task type,
  not this unit.
- HUD at open: food 289.2M, iron 477.2M, coin 10.6M,
  total power 148,957,193, unchanged at close. No
  diamonds, money, speedups or paid buttons used; the
  tracker is untouched, so the next tick re-produces
  this regular.

## What the 2026-11-01 1651 unit added

- Status partial: unit training-2026-11-01-1403 by
  ticker-1638, session about 16:45 to 16:51. No barracks
  panel opened, no batch queued, no Drill Ground screen
  read, nothing claimed. Tracker untouched; the next
  tick re-produces the regular.
- Centre view, no tent verified: the base screen in the
  642 by 951 window showed the resource-house row, the
  signed front gate and the vehicle formation lots; no
  barracks tent was verified in this view. The profile's
  "four tents stand in the lower middle of the base"
  line is therefore not confirmed in this camera
  framing - it stands as the 2026-10-25 layout
  description, not as a verified point in this unit,
  and no tent point is claimed from it.
- Grounding points NOT tapped: fresh visual grounding
  for a barracks tent returned points that sat on the
  gate road area, not on a verified tent. Those points
  were not tapped: tapping the gate would have repeated
  the survivors unit, a different task type. Ungrounded
  or wrong-target points are not tapped - the same
  discipline as the 0045 and 0917 pinned-point failures.
- South ruled out to the map edge: changed method
  versus earlier units - two upward pans to walk the
  view south. The first pan reached the vehicle depot
  and the Season 2 structures at the map edge; the
  second pan reached the map south edge itself (Season
  2 house cluster, a tank, a STOP sign, formation lots
  2 and 3 at the top of the view). No barracks tent
  appeared in either panned view. Barracks tents are NOT
  south of the vehicle formation lots down to the map
  south edge.
- Next-unit instruction, from the record itself (rule
  R2): start from a zoomed-out full-base view and
  locate the four tents first, or find a building-list
  entry, rather than panning south again or tapping
  grounding points that sit on the gate road. This is
  the zoom-out-first variant the 1216 unit already
  named - still untried, now with the south route
  closed.
- Drill Ground Full carried forward unverified a fourth
  consecutive unit: 0045, 0917, 1216 and now 1651 all
  never reached a barracks, so the 39,460 of 39,460
  block remains a 2026-10-31 read, not a 2026-11-01
  re-confirmation, and no clearing method is claimed.
  This unit differs from the 2026-10-31 Drill Ground
  Full partials: no barracks was reached at all, so the
  blocker was neither confirmed nor cleared here, and
  no Drill Ground figure is claimed.

## What the 2026-11-01 2120 unit added

- Partial, barracks tents still not located: unit
  training-2026-11-01-1803 by ticker-2104, session about
  21:07 to 21:20. No barracks panel was opened, no batch
  was queued, no Drill Ground screen was read, and
  nothing was claimed. Tracker untouched, so the next
  tick re-produces the regular.
- Device takeover handled under the owner rule: the
  "active on a different device" dialog appeared
  mid-unit, Confirm was tapped once, the app exited as
  expected, and it was relaunched and back at the base
  screen with no login or verification demanded. No
  second dialog appeared. HUD after the relaunch read
  food 359.5M, iron 550.3M, coin 34.2M, diamonds 2,416,
  same power 149,288,895 as the unit-start read (food
  353.1M, iron 543.9M, coin 30.1M, diamonds 2,396) -
  production ticks only, no claim made.
- Grounding discipline, measured: a visual-grounding call
  for a barracks tent timed out at 3 minutes with no
  result and was abandoned, not retried - do not repeat
  a grounding call inside a 15-minute unit after a
  timeout. Scroll gestures did nothing to the game view;
  drag pans are the working move, and their mapping is
  now measured: a drag from norm y 300 to y 700 moves
  the view south, the reverse moves it north, and a
  full-length drag crosses most of the base.
- Pan results, both edges ruled out at this zoom level:
  the south pan reached the map south edge again - the
  Season 2 house cluster, a tank, a STOP sign, formation
  lots 2 and 3 at the top - repeating the 1651 south
  route and adding nothing new; the houses there are
  not verified barracks. The north pan reached the map
  north edge - the same house cluster at the top and
  empty snow below, no barracks tent in either edge
  view. A half-length drag back south landed near the
  start view (house cluster top left, cannon and tank,
  empty snow below); the dense red-roofed formation of
  the unit's very first screenshot was not in this view
  either, so it lies further east or north-east of the
  start view, unreached in this unit.
- Next-unit rule, from the record under rule R2: change
  the route again before repeating this work - pan east
  from the start view toward the dense red-roofed
  formation seen in the first screenshot, and only tap
  a tent that is visually verified as a tent, never a
  point that sits on the gate road or the house cluster.
  Do not repeat the south or north pans, and do not
  spend a grounding call inside the unit budget after a
  timeout.
- Drill Ground Full status, fifth consecutive carry
  without a live read: the 2026-10-31 Drill Ground Full
  blocker was neither confirmed nor cleared in this
  unit - no barracks was reached, so no Drill Ground
  figure is claimed here. The profile therefore still
  carries it unverified, now a fifth consecutive unit
  without a live Drill Ground read (1651 was the fourth).
  No diamonds or money spent, no Finish Now, no upgrade
  shortcut. Evidence in
  `_records_/2026-11-01/troop-training/2120-queue-run.md`.


## What the 2026-11-02 0017 unit added

- Unit training-2026-11-01-2203 by ticker-0004, session
  about 00:16 to 00:17, status partial. No barracks panel
  was opened, no batch was queued, no Drill Ground screen
  was read, and nothing was claimed. The tracker is left
  untouched, so the next tick re-produces the regular
  and the work resumes as a fresh unit.
- Changed route taken, per queue rule R2 and the 2120
  next-unit rule: one east pan (drag norm 320,450 to
  120,450) from the opening base view. The resulting view
  shows formation lots 2 and 3, parked tanks and a blue
  structure at the top, and production buildings at the
  left edge - no row of four barracks tents, and no tent
  was visually verified, so no tent was tapped on a
  guess. The east-pan formation-lot view is ruled out as
  the barracks tent row at this camera position.
- Next-unit rule, from the record under rule R2: change
  the route again - pan from the opening view toward the
  lower-middle base area where the pinned coordinates
  were measured (Lv.30 tent at norm 708,602, Lv.27 tent
  at 617,570), and only tap a tent visually verified as
  a tent. Do not repeat the east pan to the formation
  lots, nor the south or north pans.
- Drill Ground Full status, sixth consecutive carry
  without a live read: the 2026-10-31 Drill Ground Full
  blocker was neither confirmed nor cleared in this
  unit - no barracks was reached, so no Drill Ground
  figure is claimed here. The profile therefore still
  carries it unverified, now a sixth consecutive unit
  without a live Drill Ground read (2120 was the fifth).
  This recurrence is the failure open Issue #150 tracks
  (barracks tent rows not located, Drill Ground never
  re-read); the recurrence is commented onto #150, not
  filed as a new issue.
- Base screen read live at unit start: food 362.4M, iron
  555.0M, coin 36.7M, diamonds 2,476, total power
  149,198,310. No different-device dialog, no login or
  verification demanded. No diamonds or money spent, no
  paid button tapped, no Finish Now, no upgrade
  shortcut. Evidence in
  `_records_/2026-11-02/troop-training/0017-queue-run.md`.

## What the 2026-11-02 0322 unit added

- Unit training-2026-11-02-0203 by ticker-0308, session about
  03:22 to 03:30, status partial. No batch was queued and no
  training state was verified. The tracker is left untouched,
  so the next tick re-produces the regular and the work
  resumes as a fresh unit. Evidence in
  `_records_/2026-11-02/troop-training/0322-queue-run.md`.
- Barracks tents grounded on the live base screenshot: norm
  (308, 552), (409, 606), (546, 544), (608, 518). This locates
  the tent rows that Issue #150 records as not located.
- First tent tapped and selection confirmed: Barracks Lv.27
  with the three-button action row - paw (details), pistol
  (train per this profile), green up arrow (upgrade). The
  pistol button tapped at norm (405, 568) opened the Lv.27
  to 28 UPGRADE panel, not TRAIN UNITS: Unit Training Cap
  540 to 550, Unit Training Level 9 to 9, cost coins 43.7M
  of 127.5M and iron 565.3M of 314.5M, Upgrade timer 19d
  14:30:46, Finish Now 187,490. It was closed with the panel
  X. No Upgrade, no Finish Now, no Obtain, no building
  started. Whether the pistol mapping is stale or the tap
  landed on a neighbouring control is unresolved - the
  profile's pistol-to-TRAIN-UNITS claim is therefore
  qualified as disputed above, not silently kept and not
  silently erased.
- Paw button tapped at norm (311, 552) on the re-selected
  tent: no panel opened. Deselected with a tap on empty
  ground, leaving the game on the base screen.
- TRAIN UNITS was not reached, so no barracks queue state
  was read, no idle barracks was requeued, and the Drill
  Ground state was not read. The other three barracks were
  not inspected. Drill Ground Full is therefore carried
  forward unverified a seventh consecutive unit (0017 was
  the sixth). The record commented on Issue #150 with the
  located tent rows and the unresolved TRAIN UNITS entry,
  so the next unit re-grounds the action row before
  tapping; no new issue is filed here.


## What the 2026-11-02 0811 unit added

- Unit training-2026-11-02-0603 by ticker-0804, session 08:05
  to 08:11, status partial. No batch was queued and no
  training state was verified. The tracker is left untouched,
  so the next tick re-produces the regular and the work
  resumes as a fresh unit. Evidence in
  `_records_/2026-11-02/troop-training/0811-queue-run.md`.
- Barracks located in this unit's camera view by visual
  inspection of a cropped lower band: three tents in the
  lower-middle base area. Tapping the upper-right tent at
  norm (825, 578) selected Barracks Lv.24, with the
  three-button action row under its label: blue paw circle
  at about norm (623, 499), orange pistol circle at about
  norm (763, 510), green up-arrow circle at about norm
  (903, 494). The green arrow was not tapped, per the red
  lines.
- Entry failure, both routes: the pistol tap switched to the
  world map (radar fan, Radar Task restore countdown), not
  TRAIN UNITS and not an upgrade panel; Home at norm
  (903, 941) returned to base. The paw tap on the
  re-selected tent gave the same world-map switch, not
  Building Details. Re-tapping the tent body only re-showed
  the same action row; no panel opened. The action-row
  mapping is therefore suspended in How to enter above -
  it is unstable across camera positions, not merely stale
  in one direction, since the 0322 pistol tap opened the
  upgrade panel instead.
- TRAIN UNITS was not reached, so no barracks queue state
  was read, no idle barracks was requeued, and the Drill
  Ground state was not read. The other three barracks were
  not inspected. Drill Ground Full is therefore carried
  forward unverified an eighth consecutive unit (0322 was
  the seventh). The record commented on Issue #150 with
  the measured tent coordinate, action-row coordinates and
  the world-map result for both taps, so the next unit does
  not repeat the action-row route; no new issue is filed
  here.
- One different-device takeover, handled under the owner
  rule: the dialog appeared at unit start, Confirm was
  tapped once, the app exited as expected, and it was
  relaunched and back at the base screen with no login or
  verification demanded. No second dialog appeared.


## What the 2026-11-02 1146 unit added

- Unit training-2026-11-02-1003 by ticker-1134, session 11:36
  to 11:46, status partial: 1 of 4 barracks queued (Lv.24),
  Lv.20 selected only, Lv.27 and Lv.30 not inspected. The
  tracker is left untouched, so the next tick re-produces
  the regular. Evidence in
  `_records_/2026-11-02/troop-training/1146-queue-run.md`.
- Entry mapping re-established for Lv.24, suspension
  lifted in part: the Lv.24 tent was selected at norm
  (806,581) and its action row re-grounded fresh (paw
  about 670,584; pistol 794,605; green up arrow 930,584)
  - the row sits about 90 pixels lower than the 0811
  row, so the 0811 world-map result does not carry to
  this camera view. The pistol tap opened TRAIN UNITS.
  The 0811 suspension's own condition is therefore met
  for Lv.24: a fresh, verified mapping reproduced a
  panel opening. The standing rule is now fresh
  grounding in every unit's own view, never inherited
  coordinates - the mapping is camera-position
  dependent, not dead.
- Lv.20 pistol route retired inside the unit per queue
  rule R2: the Lv.20 tent was selected at norm (857,531)
  and its row re-grounded (paw about 704,552; pistol
  829,575; green 942,549), but two pistol taps - the
  visual-grounding point (818,584) and the crop-measured
  centre (829,575) - both only cleared the selection and
  returned to the base screen; neither opened TRAIN
  UNITS. The next Lv.20 attempt tries a different entry
  route (a long-press variant on the selected tent, or
  the paw Details route with freshly grounded
  coordinates) and does not repeat the pistol taps. A
  clock badge above the Lv.20 tents was visible but not
  read, so no claim is made that Lv.20 is already
  training.
- Train button lesson, measured: taps at the estimated
  centre (561,715), (561,720) and (561,740), plus a
  1-second long-press at (561,715), all produced no
  change; visual grounding put the blue Train button at
  norm (628,793), about 70 pixels below the estimate.
  Never estimate the Train button centre from panel
  proportions - ground it fresh before tapping. The
  (628,793) tap queued the batch.
- Batch queued, verified by the live resource drop: Lv.24,
  T8 x666, 2.9M food and 2.9M iron, 1d 04:20:26, matching
  the profile cost and time; food 390.2M to 387.2M and
  iron 580.0M to 577.0M at HUD rounding. The panel shows
  no Drill Ground figure and no queue-progress line.
- Drill Ground Full, ninth consecutive unit without a
  live read, but now with counter-evidence: no Drill
  Ground Full toast appeared on the successful Train
  tap, no Drill Ground figure was read live, and the
  successful Lv.24 queue is evidence against a
  universal block - but it is not a Drill Ground read,
  so the 39,460 of 39,460 figure remains a 2026-10-31
  read, neither confirmed nor cleared here. The next
  unit still reads the Drill Ground screen live first
  if a panel route to it is found.
- The recurrence was commented onto Issue #150 by the
  executor (Lv.24 success coordinates, the Train-button
  mis-estimate lesson, the Lv.20 pistol failure), so no
  duplicate comment is filed here.


## What the 2026-11-02 1723 unit added

- Unit training-2026-11-02-1403 by ticker-1703, session
  about 17:19 to 17:23, inside the pass budget, status
  partial. No batch was queued. The tracker is left
  untouched, so the next tick re-produces the regular.
  Evidence in
  `_records_/2026-11-02/troop-training/1723-queue-run.md`.
- Inherited 1146 points did not reproduce in this camera
  view: the Lv.24 tent point from the 1146 unit, norm
  806,581, was tapped and no selection label or action
  row was visible on the next screenshot; the Lv.24
  pistol point from the 1146 unit, norm 794,605, was
  tapped and the control reported only a small visual
  change in the tent area, with no TRAIN UNITS panel
  opened and the base screen otherwise unchanged. This
  is the standing fresh-grounding rule cutting both
  ways: the 1146 pistol entry was verified only in the
  1146 camera view, and its coordinates are not a
  reusable shortcut in any later view. The next unit
  re-grounds the tent and the whole action row fresh
  before tapping either point, and does not re-tap the
  1146 points on a guess.
- No training state was verified: Lv.24 was queued at
  11:34 today for T8 x666 with a 1 day 4 hour timer, so
  it is expected to still be busy, but its panel was
  not read live in this unit and that is not claimed
  as a verified state. Lv.27 and Lv.30 were not
  inspected. No Drill Ground figure was read live in
  this unit.
- Drill Ground Full carried forward unverified a tenth
  consecutive unit without a live read (1146 was the
  ninth): no barracks was reached, so the 39,460 of
  39,460 figure remains a 2026-10-31 read, neither
  confirmed nor cleared here, and the 1146 successful
  queue remains the counter-evidence against a
  universal block, not a Drill Ground read.
- HUD measured 2026-11-02 in this unit: food 387.7M,
  iron 577.5M, coins 54.0M - matching the 1520 harvest
  unit's HUD snapshot the same day, a consistent
  stock picture, not a unit result. Base screen
  confirmed live at entry; game left safe on the base
  screen. No diamonds or money spent, no Finish Now,
  no upgrade shortcut. The recurrence is a further
  data point for open Issue #150, commented there by
  the executor, so no duplicate comment is filed here.

## What the 2026-11-02 1949 unit added

- Unit training-2026-11-02-1803 by ticker-1934, session
  about 19:48 to 19:49, inside the pass budget, status
  partial. No batch was queued. The tracker is left
  untouched, so the next tick re-produces the regular.
  Evidence in
  `_records_/2026-11-02/troop-training/1949-queue-run.md`.
- Entry state: the squad-vehicle selection radial left
  open by the previous survivors unit was still showing
  on the base view at entry - a cross-unit handover
  confirmed on screen.
- New failure mode: an upward drag (norm 500,600 to
  500,300) to expose the lower-middle barracks tents
  did not pan the view at all; the screenshot after
  the drag was unchanged, so no barracks tent was
  brought into view and no tent point was tapped in
  this unit. The drag may have been intercepted by
  the open selection radial. Next-unit rule: close or
  deselect any open selection radial before attempting
  a pan drag; a drag that leaves the screenshot
  unchanged is a blocked drag, not a "no tents here"
  result.
- No training state was verified: 0 barracks checked,
  no TRAIN UNITS panel opened, no Drill Ground figure
  read live in this unit. Lv.24 queued at 11:34 today
  for T8 x666 per the 1723 record is carried as
  expectation only, not a live read here.
- Drill Ground Full carried forward unverified an
  eleventh consecutive unit without a live read (1146
  was the ninth, 1723 the tenth): no barracks was
  reached, so the 39,460 of 39,460 figure remains a
  2026-10-31 read, neither confirmed nor cleared here,
  and the 1146 successful queue remains the
  counter-evidence against a universal block, not a
  Drill Ground read.
- HUD measured in this unit: food 227.1M, iron 561.8M,
  coins 5.9M - matching the 1945 harvest snapshot in
  the same pass, a consistent stock picture, not a
  unit result. Base screen confirmed live at entry;
  game left safe on the base screen with the squad
  radial still open; no action was taken from it.
- The recurrence is a further data point for open
  Issue #150, commented there by the executor, so no
  duplicate comment is filed here.


## What the 2026-11-02 2255 unit added

- Unit training-2026-11-02-2203 by ticker-2234,
  session about 22:52 to 22:55, status partial: 0
  barracks verified, 0 batches queued, tracker
  untouched, so the next tick re-produces this
  regular. Evidence in
  `_records_/2026-11-02/troop-training/2255-queue-run.md`.
- Base screen confirmed live at entry; HUD food
  230.0M, second top-bar 564.7M, coins 5.9M,
  second-row first resource 18.7M, matching the
  2247 harvest close. An "Alliance Gifts received!"
  toast was visible at entry; it belongs to the
  gifts regular and was not acted on from this
  training unit.
- Dragged the base view upward (500,700 to 500,400)
  to expose the lower-middle barracks tents, per the
  1949 unit's attempt. Unlike 1949, the drag did move
  the view this time: the central cluster shifted to
  the top of the screen and the lower area showed
  empty snow, with no barracks tent brought into
  view. No tent point was therefore tapped, and no
  TRAIN UNITS panel was opened. Dragged back
  (500,400 to 500,700) to restore the starting view.
  Game left safe on the base screen.
- No Drill Ground figure was read live in this unit,
  and no Drill Ground Full state is claimed. The
  2026-10-31 Drill Ground blocker in the activity
  metadata is therefore neither confirmed nor
  cleared here, and is carried unverified a twelfth
  consecutive unit. The Lv.24 batch queued at 11:34
  today (T8 x666, 1 day 4 hours, per the 1146 and
  1723 records) is not a live read in this unit and
  is not claimed as a verified busy state.
- Why partial, not done: no barracks queue was
  verified and no idle barracks was requeued, so the
  "keep every barracks busy" standard is unmet. The
  matching open issue is #150; this unit's
  drag-moved-but-no-tent result is a further data
  point for that issue, not a new issue.


## What the 2026-11-03 0252 unit added - road drags pan, centre drags sometimes do not, still no tent

- Unit training-2026-11-03-0203 by ticker-0234, about
  02:52 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/0252-queue-run.md`.
- Entered from the survivors unit's top-edge panned view
  (gate and formation slots 1/2/3 in frame). A centre
  vertical drag (500,650 to 500,300), intended to return
  to the central view, moved nothing: the next screenshot
  kept the identical top-edge framing. A second vertical
  drag on the left road surface (200,600 to 200,300) did
  move the view, restoring the central cluster framing
  (furnace centre, houses, same as the harvest unit's
  start view). Drag-pan responsiveness therefore varies
  by start surface: road drags pan, centre drags over
  buildings or fields sometimes do not. This is a
  further data point for Issue #150, not a new issue,
  and it is commented onto #150 by this run.
- The restored central view shows no barracks tent: the
  lower-middle area holds the furnace and the house
  cluster, with snow below. No tent point was therefore
  tapped, and no TRAIN UNITS panel was opened.
- No Drill Ground figure was read live in this unit,
  and no Drill Ground Full state is claimed. The
  2026-10-31 Drill Ground blocker in the activity
  metadata is therefore neither confirmed nor cleared
  here, now a thirteenth consecutive unit without a live
  Drill Ground read.
- The pass budget (about 25 minutes from the 02:35
  token) ended during this unit, so the search for the
  tents stops here rather than consuming another unit's
  budget.
- Result stats: target 4, achieved 0, verified no,
  blocker category c. Partial: 0 barracks verified, 0
  batches queued, tracker untouched, so the next tick
  re-produces this regular.

## What the 2026-11-03 0647 unit added - four framings, no tent, road drags pan again

- Ticker-0634, unit training-2026-11-03-0603, about
  06:47 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/0647-queue-run.md`.
- Tent search, four framings, no tent tapped: from the
  survivors unit's upper view, a left-road drag
  (200,600 to 200,300) restored the central view; a road
  drag down (200,300 to 200,650) returned to the upper
  view; two more road drags up (200,600 to 200,300,
  twice) returned to the central view; a horizontal drag
  (300,500 to 700,500) reached the right-side view (own
  blue-roofed buildings on the left, neighbouring bases
  on the right). No barracks tent was identified in any
  framing: the central lower-middle holds the furnace
  and the house cluster, the upper view holds the
  Capitol pyramid and pink buildings, and the right-side
  view holds tower and house buildings - none presented
  as a barracks tent, and no TRAIN UNITS panel was
  opened.
- Drag-surface distinction re-confirmed, consistent
  with the 0252 unit: road drags pan while centre
  drags over buildings sometimes do not. This is a
  further data point for Issue #150, commented onto
  #150 by this run.
- The 2026-10-25 "lower middle" tent description does
  not match the current framings: the central
  lower-middle now reads as furnace and house cluster,
  not tents. The description is marked stale for the
  current layout as of 2026-11-03, not deleted from
  history; the next unit re-grounds the four tent
  positions on the current base layout before any tap.
- No batch was queued, no barracks queue state was
  verified, and no Drill Ground figure was read live in
  this unit, so the 2026-10-31 Drill Ground Full blocker
  is neither confirmed nor cleared here, now a
  fourteenth consecutive unit without a live Drill
  Ground read.
- Result stats: target 4, achieved 0, verified no.
  Partial: 0 barracks verified, 0 batches queued,
  tracker untouched, so the next tick re-produces this
  regular. Follow-up: re-ground the four tent positions
  on the current base layout before any tap, and read
  the Drill Ground screen live first if a panel opens.

## Open questions

- The fourth barracks level, and whether raising it to Lv.27 or Lv.30
  is worth a build slot.
- How promotion actually engages, and its cost against training fresh.
- Whether the Lv.30 barracks button row differs - its pistol position
  opened Details twice before the panel opened from another button.

## Changelog

- 1.43.0 (2026-11-11): 0548 training unit folded (partial, Lv.24 barracks checked live - T8 x666, 'Training in progress 11:01:26', busy until about 16:58 today, no action possible, matches the 2146 note; tent (864,610) opened TRAIN UNITS; wrong turn - tent (763,584) opened the radar world map instead of a barracks, that structure is the radar entrance in this framing; 2146 groundings no longer match this framing, re-ground fresh every unit; visual grounding boxes do not distinguish Drill Ground from barracks tent and were not used; Drill Ground screen still NOT read live, next unit's first action remains the live Drill Ground read; Lv.27 state carried from 2146, not re-read; duration corrected to about 4 minutes (record said about 12); commented on Issue #150 by this run).
- 1.42.0 (2026-11-11): 0213 training unit folded (partial, Lv.30 barracks: two pistol taps at (318,885) and one paw tap at (263,850) all close the button row with no panel and no power change - R2 pistol method ends for this barracks after two no-change taps; Drill Ground screen still NOT read live, fourth consecutive unit closing on the same blocker, third-strike R2 already triggered in 2146 - the blocker now needs a changed entry route (locate the Drill Ground building first, by name or via a troop overview entry) not another pistol tap; Lv.24 T8 x666 batch still running to about 2026-11-11 16:49; Lv.27 batch collected 21:46 on 2026-11-10, requeue blocked then; tents re-grounded fresh (399,815), (523,853), (664,781), (740,726); train boarding banner seen 00:02:51; power 149,218,973 unchanged; commented on Issue #150 by this run).
- 1.41.0 (2026-11-10): 2146 training unit folded (partial, Lv.27 finished batch of 313 Lv.9 collected - power +423,176, exactly 313 x 1,352, no Drill Ground visit needed; requeue blocked by the Drill Ground Full toast live ('Drill Ground Full: Unable to add more units', no panel opened) - collection and requeue are DECOUPLED, the 1229 'did not block' reading is qualified to that unit only; tents re-grounded fresh from the current screenshot (lower-middle bbox 549-688, 533-614; lower-right 653-814, 580-675), no pan needed - the 1229 point (374,526) no longer matches the current framing, do NOT go straight to it; Lv.24 T8 x666 batch still running to about 2026-11-11 16:49; Lv.30 and the fourth barracks still unchecked; Drill Ground screen still not read live, next unit's first action is to read it live; commented on Issue #150 by this run).
- 1.40.0 (2026-11-10): 1649 training unit folded (partial, verified no - no barracks tent located after three camera pans: down overshot into full fog, right barely moved the view, long right overshot past the base edge into fog; blind-pan method RETIRED under rule R2, next unit re-grounds from the 1229 record's successful tent point and goes straight to it before any pan, and files a GitHub issue if the tents still cannot be located; Lv.24 T8 x666 batch queued 12:29 for 1d 04:19:43 still running, not due for requeue until about 2026-11-11 16:49; Lv.30 '1d 17:14:37' is a batch duration, not a remaining timer; skull badge moved 1 to 4 to 2 with countdown 00:00:24 to 00:00:52 inside the unit - same-unit evidence for Issue #498; blocker_category e).

- 1.39.0 (2026-11-10): 1521 scout cross-read folded (partial, Drill Ground levelled up live to Lv.27 - Power 118,600 to 140,200, Unit Count +7,200 to +7,400, +21,600 total power verified; CORRECTION the standing Lv.30 reads (0039, 0129) are superseded as misidentifications, not deleted; upgrade to Lv.28 available with costs met, NOT started - red line, owner-initiative; 24.0M EXP reward card untapped; Full state still unverified, Quick Dispatch still untapped, owner decision; next unit reads the Lv.30 "Training in progress" line and the Drill Ground screen live).

- 1.2.0 (2026-11-01): inherited-point staleness after camera
  drift (708,602 and 617,570 both missed), the no-ungrounded-tap
  rule applied to a crop with no groundable barracks row, the
  Drill Ground Full block carried forward unverified, and the
  shared 274,18 focus fix, folded from the 0045 training unit.

- 1.3.0 (2026-11-01): pinned-point failure escalated to a
  wrong-building selection (617,570 selected Missile
  Vehicle Base Lv.10; factory-pan landmarks Factory No.1
  and No.2 Lv.30 measured), the pan-to-the-tent-row-first
  next-unit rule, Drill Ground Full carried forward
  unverified a second consecutive unit, and the mid-unit
  session-drop recovery, folded from the 0917 training
  unit.

- 1.4.0 (2026-11-01): four-direction pan sweep with no tent
  row (factory cluster, HQ and furnace sector, Formation
  2 and 3 parking, snowfield south and east), Drill Ground
  Full carried forward unverified a third consecutive
  unit, the zoomed-out whole-base view plus ground-the-
  Drill-Ground-first next-unit instruction, and the chat
  line explicitly not a live Drill Ground read, folded
  from the 1216 training unit.

- 1.5.0 (2026-11-01): south of the vehicle lots ruled
  out to the map south edge, gate-road grounding points
  correctly not tapped, the zoom-out-or-building-list
  next-unit rule, and Drill Ground Full carried forward
  unverified a fourth consecutive unit, folded from the
  1651 training unit.

- 1.6.0 (2026-11-01): north and south map edges ruled out at this zoom level, the measured drag mapping (y 300 to 700 moves south, reverse north), the 3-minute grounding timeout abandoned not retried, the device-takeover Confirm once with clean relaunch, the east-toward-the-red-roofed-formation next-unit rule, and Drill Ground Full still carried unverified a fifth consecutive unit, folded from the 2120 training unit.

- 1.7.0 (2026-11-02): east pan to the formation lots ruled out as the barracks tent row, the lower-middle-base next-unit rule, Drill Ground Full carried unverified a sixth consecutive unit, and the recurrence commented onto Issue #150, folded from the 0017 training unit.

- 1.8.0 (2026-11-02): barracks tent rows grounded at four measured points, the pistol tap opening the Lv.27 to 28 upgrade panel instead of TRAIN UNITS so the pistol mapping is now disputed, Drill Ground Full carried unverified a seventh consecutive unit, and the recurrence commented onto Issue #150, folded from the 0322 training unit.

- 1.9.0 (2026-11-02): Lv.24 tent selected at 825,578 with the action row measured (paw 623,499, pistol 763,510, up arrow 903,494), both action-row taps switching to the world map so the pistol/paw mapping is suspended, not merely disputed, Drill Ground Full carried unverified an eighth consecutive unit, and the recurrence commented onto Issue #150, folded from the 0811 training unit; the How to enter pistol-to-TRAIN-UNITS claim is corrected to suspended, not silently kept.

- 1.10.0 (2026-11-02): Lv.24 pistol entry re-established with a fresh-grounded row (tent 806,581; pistol 794,605) so the 0811 suspension is lifted in part for Lv.24, the Lv.20 pistol route retired after two fresh-point failures, the Train button grounded at 628,793 against a 70-pixel-low estimate, the Lv.24 T8 batch queued and verified by the live resource drop, and Drill Ground Full carried unverified a ninth consecutive unit with a successful queue as counter-evidence, folded from the 1146 training unit.

- 1.11.0 (2026-11-02): inherited 1146 Lv.24 points (tent 806,581, pistol 794,605) failing to open any panel in this camera view, so the fresh-grounding rule is re-affirmed against reusing a verified entry, Lv.24 busy status carried as expectation only with no live panel read, Lv.27 and Lv.30 not inspected, Drill Ground Full carried unverified a tenth consecutive unit without a live read, and the HUD stock snapshot (food 387.7M, iron 577.5M, coins 54.0M) matching the 1520 harvest read, folded from the 1723 training record.

- 1.12.0 (2026-11-02): upward drag (500,600 to 500,300) not panning at all with the screenshot unchanged, so the drag was likely intercepted by the squad-vehicle radial left open by the previous survivors unit, close-or-deselect-before-drag next-unit rule, 0 barracks checked with no TRAIN UNITS panel, Drill Ground Full carried unverified an eleventh consecutive unit, Lv.24 busy carried as expectation only, HUD matching the 1945 harvest snapshot, and the recurrence commented onto Issue #150 by the executor, folded from the 1949 training unit.

- 1.13.0 (2026-11-02): upward drag (500,700 to 500,400) moved the view this time unlike 1949 but brought no barracks tent into view, only empty snow below the shifted central cluster, so 0 barracks checked with no TRAIN UNITS panel, Drill Ground Full carried unverified a twelfth consecutive unit, Lv.24 busy carried as expectation only with no live panel read, HUD matching the 2247 harvest close, and the recurrence commented onto Issue #150 by this run, folded from the 2255 training unit.

- 1.14.0 (2026-11-03): centre vertical drag (500,650 to 500,300) moving nothing while the left-road drag (200,600 to 200,300) restored the central cluster, so drag-pan responsiveness varies by start surface, no barracks tent in the restored central view with no TRAIN UNITS panel, Drill Ground Full carried unverified a thirteenth consecutive unit, pass budget ending mid-unit, and the recurrence commented onto Issue #150 by this run, folded from the 0252 training unit.

- 1.15.0 (2026-11-03): no barracks tent in four framings (central, upper, right-side) with no TRAIN UNITS panel, road drags panning again consistent with 0252 as a further Issue #150 data point commented by this run, 2026-10-25 "lower middle" tent description marked stale for the current layout (furnace and house cluster, not tents) without deleting history, Drill Ground Full carried unverified a fourteenth consecutive unit, 0 barracks verified and 0 batches queued, folded from the 0647 training unit.


- 1.17.0 (2026-11-03): tent-blocker breakthrough (1552 unit, fresh grounding returning three tent points, Lv.27 tent tap at (630,592) selecting Barracks Lv.27 with its label and button row confirmed, pistol re-grounded at (612,608) opening TRAIN UNITS, Lv.9 batch of 726 queued and verified by the live food and iron drop, Drill Ground Full block not presenting at this barracks, other three barracks not reached so partial), T9 defense corrected 6.6 to 6.67 per the live panel read, and the breakthrough commented onto Issue #150 by this run, folded from the 1552 training record.

- 1.18.0 (2026-11-03): production-grid buildings tapped building by building are Titanium Alloy Factories No.1, No.2 and No.3 (all Lv.30), each showing only an info button and small icons, never a TRAIN UNITS row; green military structures on the grid's right side are not selectable (three direct taps, no selection, no panel); the 1552 tent point (630,592) QUALIFIED as framing-bound after it selected Factory No.3 Lv.30 in the 2144 framing, so the How to enter proven-entry claim now carries the framing bound; a centre double-click produced no zoom change; Drill Ground Full neither confirmed nor cleared (no barracks reached, no Drill Ground figure read live); HUD stock snapshot (food 275.0M, iron 612.5M, coins 34.2M, power 149,948,901); the next-unit rule (different base area or pinch-zoom framing before tapping, never re-tap the factory row as tents) and the recurrence commented onto Issue #150, folded from the 2144 training unit.

- 1.24.0 (2026-11-05): 0534 training unit folded (failed, thirty-fourth consecutive screen-capture failure, no game screen read, no input dispatched, probe OFF_SCREEN_WINDOW, Chrome observes normally in the same session, inbox 70, tracker untouched); CORRECTION - the 1734 "running fullscreen 1920x1080" wording and the 1147 "fullscreen framing" wording are superseded, the window is windowed on an inactive Space (0134 View-menu read, re-confirmed by 0204, agreed by the 0534 probe), and the unblock is getting the window back onto the active Space (owner Dock-icon click); the thirty-fourth occurrence commented onto Issue #282 by this run. (1.19.0 through 1.23.0 carry sections without changelog lines; the numbering is preserved, not rewritten.)

- 1.25.0 (2026-11-07): 1655 training unit folded (partial, Lv.27 T9 x726 at cap and Lv.30 T10 x793 at cap requeued and HUD-verified, 9.6M food plus 9.6M iron spent, two upper-right barracks unchecked so the keep-every-barracks-busy aim is not fully met, Drill Ground Full not seen but not closed with no live Drill Ground read, Lv.30 tap-the-body-not-the-circle entry lesson, white '?' bubble at (113,582) handed to the next survivors unit), folded from the 1655 training record.

- 1.26.0 (2026-11-07): 2026 training unit folded (partial, Lv.27 verified busy by a live panel read - TRAIN UNITS, Lv.9 selected, count 726, "Training in progress 1d 07:03:33", consistent with the 1655 requeue; Lv.30 busy by its clock timer bubble only, not panel-read; two upper-right barracks unlocated, south and east pans ruled out as the direction to them, north and west pans and the zoomed-out whole-base view remain untried; upward drag moves the view south re-confirmed; no Drill Ground read live so the Drill Ground Full blocker is neither confirmed nor cleared; white "?" bubble at about norm 505,790 in the eastern framing handed to the next survivors unit; footer side read for donations - Tech Donation Today 1150 at about 20:22, up from 750 with no own donation in between).

- 1.27.0 (2026-11-07): 2050 training unit folded (partial, Lv.30 busy by panel read - T10 count 793, "Training in progress 1d 13:41:04", consistent with the 1655 requeue; Lv.24 idle but blocked by the Drill Ground Full toast on the pistol tap, no panel stayed open, no batch started; Drill Ground Lv.25 read live as the standing blocker required - Unit Count +7812, Officers Joe, Marcus, Karen and John, single action Quick Dispatch at the panel bottom, not tapped, effect unverified, left for an owner decision or a learn-first exploration; CORRECTION - no 39,460 of 39,460 figure appears on the live Drill Ground screen, that figure's provenance is the 2026-10-31-era reads and it was not re-read live here; tent-body direct taps missed twice (norm 393,600 and 511,557), visual-grounding point (435,518) selected Lv.24 and the pistol grounded at (425,581), and the no_change_observed flag proved unreliable twice so the next units screenshot to verify after every tap instead of trusting that flag; Lv.27 not re-verified live in this unit).

- 1.31.0 (2026-11-09): 0129 arms-race unit folded as the R2 metadata write (third consecutive tent-grounding failure - 0039, 0058, 0129 - red troop formation resolves to Drill Ground Lv.30 again, both failed routes retired, entry route must change before any further training or fill unit runs; Drill Ground Lv.30 re-confirmed live; phase ends about 02:00 before the Lv.27 batch ends about 03:27, so a located idle barracks may still be Drill Ground Full blocked; carried state Lv.30 busy until about 10:22, Lv.27 busy until about 03:27, Lv.24 idle but blocked, fourth barracks unknown).

- 1.32.0 (2026-11-09): 0413 training unit folded (partial, fullscreen zoom-out variant tried for the first time - green zoom button to native fullscreen, 1280x720 capture, wider base view, one tent candidate at (445,665) produced no change, R2 ends; fullscreen exit MEASURED via the View menu - inspect_menu lists "Exit Full Screen" enabled and the menu action returns to the 642x951 window with no crash, pointer-to-top-edge does not drop the menu bar, never Ctrl-Cmd-F or Escape; west road drag blocked with no view change; retired routes not re-tapped; Drill Ground 39,460 of 39,460 stays a 2026-10-31 read; barracks verified 0, batches queued 0).

- 1.34.0 (2026-11-09): 2103 training unit folded (partial, barracks tent tap no-change x3 - one barracks tent grounded fresh on the live screenshot (top-row blue tent, 283,230), first tap showed a "+45" float and a small portrait marker at the tent (200,215) but no row of round buttons and no TRAIN UNITS panel, second tap at (283,245) and third at (283,230) after a title-bar click both no-change; control guidance on the second tap says background clicks do not reach some controls and suggests click_element or the keyboard; session cc-343 dropped mid-pass, cc-344 started, window came up covered (brought_to_front false); Drill Ground not read live, the standing Drill Ground Full blocker (39,460 of 39,460) neither confirmed nor cleared, no batch requeued; next unit must change the entry route before tapping a tent again per R2; the tap-method failure here is distinct from the Drill Ground Full blocker; blocker category c).

- 1.35.0 (2026-11-10): 0034 training unit folded (partial, camera panned down to the formation yard per the 1330 handover - three fresh grounding taps inside the yard resolve to parked squads or the Wall, never to a Drill Ground building: green truck (413,541) no selection, red car (592,547) selects 2nd Squad Lv.20, FORMATION sign (545,421) selects Wall Lv.26, empty pavement (670,736) selects 2nd Squad Lv.20 again; the 0039 unit's Drill Ground Lv.30 tap does not reproduce from these points, so the next unit needs a different selection route - formation ground at a wider zoom, or the Drill Ground entry from a building list - not another tap on a vehicle, a sign or the fence; Drill Ground screen not re-read live, no barracks requeued, carried state Lv.30 batch due about 10:22 on 2026-11-09 unverified, Lv.27 idle and blocked at the 1330 read, Lv.24 and the fourth barracks not checked, Drill Ground Full (39,460 of 39,460, last read live 2026-10-31) carried unverified; Quick Dispatch stays untapped, owner decision; power 146,751,949 matches the 2121 gifts close, second corroboration of the levelled power figure; blocker category e).

- 1.38.0 (2026-11-10): 1229 training unit folded (partial, Lv.24 requeued T8 x666 and verified running - BREAKS the five-consecutive-partial R2 process-failure run (0039, 1330, 0034, 0337, 0850); finished T8 batch of 666 collected on the tent tap, +707,958 power (666 x 1,063), no Drill Ground visit needed; Drill Ground Full (39,460 of 39,460, last read live 2026-10-31) did NOT block this collection or requeue - the 'blocks requeue' claim is qualified, commented on Issue #150; cost 2.9M food + 2.9M iron, duration 1d 04:20:26, 'Training in progress 1d 04:19:43' on reopen; T8 stats corrected live (Morale 531.25, Attack 28.69, Defense 5.84, superseding 520.63/28.37/5.72) and T10 stats corrected (Morale 750.0, Attack 38.45, Defense 7.79, superseding the 2026-10-25 baseline 720.01/38.03/7.55); Lv.8 owned 1,998 cross-checks the 1224 read of 1,332 + 666 collected; Lv.30 busy/idle still unverified - the 1d 17:14:37 on its buttons is the prospective batch duration, not a remaining timer, next unit reads the 'Training in progress' line; two further barracks unchecked; blocker_category h).

- 1.37.0 (2026-11-10): 0850 training unit folded (partial, fifth consecutive training partial with the same blocker, R2 process failure stands - this unit added its evidence comment to Issue #150 as well; game found on the TECH screen by unexplained navigation after a session restart, no game input sent between the 08:46 base screenshot and the 08:49 TECH screenshot except the restart and window activate, navigation flagged not attributed; slot-1 timer discrepancy - research unit read 1d 01:35:27 at 08:46, TECH screen read 1d 01:51:59 at about 08:49, one read is misread, neither claimed as true without a re-read; back arrow at 129,928 returned to base; no barracks tent tapped, token lease expired 08:51:29 inside the pass budget; next unit must use a new grounding route - full-observe accessibility tree with click_element, or fullscreen reframe via the green zoom button, never Ctrl-Cmd-F or Escape - and must not re-tap the retired right-edge tent points (0337) or formation-yard points (0034); Drill Ground screen NOT re-read live, Drill Ground Full (39,460 of 39,460, last read live 2026-10-31) carried unverified; Quick Dispatch stays untapped, owner decision; blocker category e).

- 1.36.0 (2026-11-10): 0337 training unit folded (partial, fourth consecutive training partial with the same blocker, R2 process failure reported on Issue #150 by the ticker pass; wide-zoom tent taps (890,500) and (919,530) and panned-down tap (841,116) select nothing, top-right corner points open the radar map (903,468) and the Alliance Duel screen (903,198); Duel screen live read - Base Expansion, 14:18:29 remaining, alliance target 1,650,000, UR truck dispatch +300,000 (superseding the 100,000 Handbook rate, corrected in truck-plunder 1.38.0), UR secret task +225,000; power 146,751,949 rising to 148,058,020 during the unit, cause not established, not attributed; Drill Ground Full (39,460 of 39,460, last read live 2026-10-31) carried unverified; Quick Dispatch stays untapped, owner decision; blocker category e).

- 1.33.0 (2026-11-09): 1330 training unit folded (partial, Lv.27 idle and blocked by Drill Ground Full - pistol tap produced the toast live by OCR, no TRAIN UNITS panel opened, no timer bubble above the tent, consistent with idle; same blocker the 2050 unit read for Lv.24 on 2026-11-07, now re-confirmed on a second barracks two days later; CORRECTION - the diagonal row of blue-roofed tents in the upper base is Material Workshops, not barracks (tap (267,365) selected Material Workshop Lv.20, tap (460,290) selected Eternal Pyramid Lv.3); the barracks are the beige tents with blue zigzag markings at the base lower-right edge, instructor portrait circle overlapping the tent body, tap the body not the circle; Lv.27 selected live at (799,871), pistol TRAIN UNITS grounded at (787,931); (435,518) is the ICU hospital, not a barracks - the 2050 grounding point no longer maps to a barracks in the current camera view; gold-mine timer bubble 97 to 94min is a mine production timer, unrelated to training; Lv.30, Lv.24 and the fourth barracks not checked, second beige tent half off the bottom edge, camera must be panned down first; Quick Dispatch still untapped, owner decision; session cc-277 dropped mid-unit, cc-278 restarted with no game state lost).

- 1.30.0 (2026-11-09): 0039 training unit folded (partial, Drill Ground Lv.30 read live with Unit Count +10080 and officers Samantha, William, Chloe and Catherine - the roster rotated since Joe, Marcus, Karen and John on 2026-11-07, level risen since the 2050 Lv.25 read, not reconciled; Quick Dispatch the only button, not tapped, owner decision; the yellow-green fenced structure with soldiers, a tank and a 3d 01:53 countdown resolves to Aircraft Center Lv.29 on two taps, not a barracks, so the four tents were not located and that grounding method ends per R2; no barracks verified live, no requeue - carried state Lv.30 busy until about 10:22, Lv.27 busy until about 03:27, Lv.24 idle but Drill Ground Full blocked, fourth barracks unknown; no 39,460 of 39,460 figure re-read live; same session cc-192 held for both units of the pass with no drop).

- 1.29.0 (2026-11-08): 2119 training unit folded (partial, Lv.27 busy by live panel read with a Lv.9 batch of 726 and 06:26:20 left, Lv.20 Drill Ground Full toast live re-confirmed for the first time since 2026-10-31, paw Details route works for Lv.20 with Training Count +613 and instructors Alexis, Joe, Jolene and Anthony, Quick Dispatch not tapped, owner decision; CORRECTIONS - T9 stats corrected to Morale 625.0 / Attack 33.5 / Defense 6.74 per the live panel read, the Lv.20 long-press variant RETIRED after it entered building-move mode, the 1146 Lv.20 pistol retirement qualified as framing-bound since the 2119 pistol tap reached the train attempt; session cc-167 dropped mid-unit with cc-168 recovery and no state lost; HUD power 149,209,253 corroborates Issue #482; Lv.30 and Lv.24 not reached). (1.28.0 carries the 1350 section without a changelog line; the numbering is preserved, not rewritten.)

## What the 2026-11-03 1051 unit added - three framings, still no tent, road drag pans where centre drag does not

- Ticker-1034, unit training-2026-11-03-1003, about
  10:50 to 10:51 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/1051-queue-run.md`.
- Tent search, three framings, no tent tapped: from
  the survivors unit upper view, a reverse centre
  drag (500,700 to 500,300) produced no visible view
  change; a road drag (200,600 to 200,300) restored
  the central view. The central lower-middle holds
  the furnace and the house cluster, the upper view
  holds the Capitol pyramid and pink buildings -
  neither framing presented a barracks tent, and no
  TRAIN UNITS panel was opened. The drag contrast
  matches the 0647 unit: road drags pan, centre
  drags sometimes do not.
- No batch was queued, no barracks queue state was
  verified, and no Drill Ground figure was read live
  in this unit, so the 2026-10-31 Drill Ground Full
  blocker is neither confirmed nor cleared here.
  No new Issue was filed: this is the known tent
  and Drill Ground blocker already tracked as Issue
  150; this unit adds only the framing data point
  above.
- Why partial, not done: 0 of 4 barracks verified and
  0 batches queued, so the keep-every-barracks-busy
  standard is unmet. Tracker untouched, per the rule
  for partial units.
- Follow-up for the next training unit: re-ground
  the four tent positions on the current base layout
  before any tap, rather than working from the
  2026-10-25 lower-middle description, which does
  not match the current framings; read the Drill
  Ground screen live first if a panel opens. No
  earlier claim superseded.

## What the 2026-11-03 1552 unit added - tent blocker broken, Lv.27 T9 batch queued and HUD-verified

- Ticker-1534, unit training-2026-11-03-1403, about
  15:43 to 15:52 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/1552-queue-run.md`.
- Breakthrough on the standing tent blocker (Issue
  150): fresh visual grounding on the live central
  base frame returned three barracks tent points, and
  the tap at norm (630,592) selected Barracks Lv.27,
  confirmed by its on-screen label and button row
  (paw Details, orange pistol Train, green upgrade
  arrow untouched). The Lv.27 tent point (630,592)
  is a proven entry but must still be re-grounded,
  never inherited blindly.
- The pistol button was re-grounded at norm
  (612,608) before tapping, so the green upgrade
  shortcut was never at risk. TRAIN UNITS opened
  with Lv.9 preselected, count slider at the cap
  726, cost 4.1M food and 4.1M iron, time 1d
  10:19:35 - matching the Lv.27 T9 archive (power
  1352, HP 4121.49, attack 33.13, defense 6.67, Lv.10
  locked). The profile's T9 defense figure is
  corrected 6.6 to 6.67 on this live panel read.
- Train tapped (blue button, norm (630,778)).
  Finish Now was never tapped. The panel closed with
  no error and no Drill Ground block shown, so the
  2026-10-31 Drill Ground Full blocker did not
  present at this barracks. This is counter-evidence
  against the carried block, not a clearance claim:
  the other barracks were not reached and no Drill
  Ground panel was read live.
- Queue verified live from the HUD, not assumed
  from the panel close: food 251.1M to 247.0M (minus
  4.1M) and iron 592.7M to 588.5M (minus about 4.1M
  at displayed 0.1M precision). One T9 batch of 726
  is now training in the Lv.27 barracks.
- Why partial, not done: the other three barracks
  were not reached in this unit, so the
  keep-every-barracks-busy standard is unmet.
  Tracker untouched for the unreached barracks.
- Follow-up for the next training unit: the tent
  grounding works - re-ground the tents on the live
  frame and work the remaining three barracks the
  same way (tent tap, pistol tap, Train tap, HUD
  verification). Issue #150 is commented with this
  breakthrough by this run, not closed here -
  closure belongs to the daily retro.

## What the 2026-11-03 2144 unit added - production grid is factories, 1552 point does not transfer across framings

- Ticker-2134, unit training-2026-11-03-1803, about
  21:34 to 21:44 local, status partial. Evidence in
  `_records_/2026-11-03/troop-training/2144-queue-run.md`.
- Changed method versus the 0252, 0647 and 1051 units
  (queue rule R2): instead of only re-framing, this
  unit systematically tapped the production grid
  building by building on the live frame, and
  re-tried the proven 1552 point after re-framing.
- Results on the live frame: the dark-roofed
  buildings in the grid are Titanium Alloy
  Factories, not barracks - taps selected Factory
  No.1 Lv.30, No.2 Lv.30 and No.3 Lv.30 in turn,
  each showing only its info button and small
  icons, never a TRAIN UNITS button row. The
  green military structures on the right side of
  the grid are not selectable: direct taps on
  three of them produced no selection and no
  panel. The barracks tents are not in the
  production grid reached here.
- CONTRADICTION RESOLVED, in favour of the newest
  verified record, by QUALIFICATION (not erasure):
  the proven 1552 point norm (630,592), re-tried
  after a rightward drag re-framing, selected
  Factory No.3 Lv.30 in this framing, not a
  barracks tent. The 1552 frame therefore used a
  different zoom or a different base area than
  the framing reached here; its point does not
  transfer to this framing. The 1552 event stands
  as history - a Lv.27 T9 batch was queued and
  HUD-verified in that frame - but the point is
  now framing-bound, and the How to enter section
  carries that bound. A double-click at the grid
  centre produced no zoom change.
- Drag-pan notes, consistent with earlier units:
  road and open-snow drags pan; centre drags
  over buildings sometimes do not. Drags used:
  down, up, rightward and leftward, all
  dispatched.
- HUD resources at start: food 275.0M, iron
  612.5M, coins 34.2M, power 149,948,901 - read
  from the base screen, unchanged by this unit.
- No batch was queued, no barracks queue state
  was verified, and no Drill Ground figure was
  read live in this unit, so the 2026-10-31
  Drill Ground Full blocker is neither confirmed
  nor cleared here.
- Why partial, not done: 0 of 4 barracks verified
  and 0 batches queued, so the
  keep-every-barracks-busy standard is unmet.
  Tracker untouched, per the rule for partial
  units; the next tick re-produces training and
  resumes the search.
- Follow-up for the next training unit, from the
  record under rule R2: the barracks tents are
  not in the production grid reached here. Try
  a different base area or a pinch-zoom framing
  before tapping, and do not re-tap the factory
  row as if it were tents. No new issue filed:
  this is the known tent blocker already tracked
  as Issue #150; this run comments the recurrence
  onto #150.

## What the 2026-11-04 0143 unit added - factories confirmed again, 1552 tent point not re-tried, Tank Base upgrade in progress

- Unit training-2026-11-03-2203 by ticker-0134,
  about 01:43 local, status partial. The "active on
  a different device" dialog appeared on entry;
  Confirm was tapped once per the owner rule (kick
  1 of this pass), the app exited as usual, and it
  was reopened and reached the base screen.
- Tank Base Lv.28 selected on the central frame
  (607,468): its button row shows the green upgrade
  arrow (never tapped) and a red-panda Details
  button. The Details panel confirms an upgrade
  Lv.28 to 29 in progress with 21:17:49 remaining,
  cost line iron 922,228/1.7M, and a Finish Now
  price of 2,032 diamonds - none of these were
  tapped. Panel closed with X.
- Tent search: fresh visual grounding on the live
  central frame returned points that selected
  Titanium Alloy Factories, not barracks - norm
  (389,463) gave Factory No.1 Lv.30, norm (504,626)
  gave Factory (Weekly Pass) Lv.30. This confirms
  2144: the dark-roofed grid buildings are
  factories. Grounding on the upper-base frame
  converged on norm (938,240) at the far right
  edge; the tap produced only an Alliance Gifts
  toast, no selection.
- Pans used: one upward drag reached empty snow
  below the grid, one downward drag reached the
  formation parking areas above, one upward drag
  returned the view to the central frame. Game left
  on the central base view.
- Not re-tried: the 1552 tent point (630,592) was
  not re-tried in this unit's framings. Follow-up
  stands: re-ground the tents on the live frame
  first, and do not re-tap the factory row as if it
  were tents. Known blocker Issue #150; this run
  comments the recurrence onto #150.
- HUD resources at end, unchanged by this unit:
  food 391.8M, iron 727.5M, coins 548.9K, power
  150,028,269. No batch was queued, 0 of 4 barracks
  verified, and no Drill Ground figure was read
  live in this unit, so the 2026-10-31 Drill Ground
  Full blocker is neither confirmed nor cleared
  here.

## What the 2026-11-04 0440 unit added - tent point resolved for Lv.24, Drill Ground Full confirmed live again, clearing method still open

- Unit training-2026-11-04-0203 by ticker-0434, about 04:40 local, status partial. No "active on a different device" dialog appeared.
- Tent search resolved on this framing: visual grounding on the live central frame returned a tent point at norm (585,548), and the tap selected Barracks Lv.24 with its button row (paw Details, pistol Train Units, green upgrade arrow never tapped). This point is distinct from the factory-row points that misled the 0143 unit and from the 1552 point (630,592). The next unit starts from (585,548). (2026-11-04 0814 correction: (585,548) selected Arena Lv.1 in the 0814 framing, not a barracks - the point is framing-bound like the 1552 point and must not be carried as a standing tent coordinate; re-ground the tent on the live frame in every unit.)
- Train attempt: the pistol button, grounded on the live frame at norm (544,580), was tapped and the game answered with the toast "Drill Ground Full: Unable to add more units" - no Train Units panel opened. The 2026-10-31 Drill Ground Full blocker is therefore CONFIRMED live again at this barracks, by the Train tap itself, not assumed from an earlier unit. An earlier mis-aimed tap at norm (465,505) landed on the world map instead of the button row; it was undone with the home button and no world action was taken. Do not re-aim at (465,505).
- Preparatory read, per the activity metadata: the Lv.24 barracks Details panel was opened (paw button, norm (468,580) by offset from the grounded pistol point). It reads Training Count +666, matching the T8 count in the activity metadata, with instructors Maria, Hannah, James and Christopher assigned, and no training timer shown in Details. The panel was closed with X; nothing was queued, dispatched or spent.
- HUD resources at end, unchanged by this unit: food 397.0M, iron 732.0M, coins 3.1M, power 150,028,269 - consistent with the 0413 harvest and 0416 reads, not a contradiction. 0 of 4 barracks queued, 1 of 4 verified (Lv.24, blocked by Drill Ground Full); the other three barracks remain unverified this unit. Tracker untouched, per the rule for partial units.
- Open question carried, not closed: the clearing method for a full Drill Ground is still unknown - no clearing method was found or claimed in this unit. The 0143 follow-up (re-ground the tents first) is satisfied for Lv.24 on this framing by the (585,548) point; the blocker that remains is the Drill Ground itself. Evidence commented onto Issue #150 by the ticker unit, fold noted here.

## What the 2026-11-04 0814 unit added - 0440 tent point selects Arena in this framing, Lv.20 verified via Details, framing instability, Drill Ground Full neither reconfirmed nor cleared, partial

- Unit training-2026-11-04-0603 by ticker-0804, about 08:14 local, status partial. Sessions cc-435 and cc-436 (the first session closed mid-unit and was restarted; no device contention). No 'active on a different device' dialog appeared on entry; no takeover was needed. Evidence in `_records_/2026-11-04/troop-training/0814-queue-run.md`.
- Method changed versus the 0440 unit (queue rule R2): inherited points were NOT trusted. The 0440 tent point (585,548) was tried once and selected Arena Lv.1 in this framing, not a barracks, proving again that tent points do not transfer across camera framings (see the correction in the 0440 section). The grounded Drill Ground candidate (722,610) produced no panel. Every later tap was grounded fresh on the live frame of that moment.
- Barracks verified, 1 of 4: after a drag-pan down (drag from (300,500) to (300,300) on the base screen, which moved the view down to the tent row), a fresh-grounded tent tap selected Barracks Lv.20 with its button row (paw, pistol, green upgrade arrow never tapped). Its middle button opened the Building Details panel, not a Train Units panel: Training Count +613, matching the T7 count in the activity metadata for the fourth barracks, instructors Alexis, Joe, Jolene and Anthony, no training timer shown in Details. This button mapping differs from the 0440 record (paw Details, pistol Train Units); in this frame the middle button behaved as Details. The panel was closed with its X; nothing was queued, dispatched or spent.
- Framing instability, measured: closing the Details panel returned the camera to a different framing, so re-tapping the same tent point (660,893) opened the chat panel instead of the tent. The chat panel was closed at once with its back arrow; nothing was typed, sent, opened or acted on there, and no chat content is recorded here. A second drag-pan down restored the tent row, but two further fresh taps on tent candidates ((467,727) grounded, and (592,831) read off the live frame) selected nothing, and the unit's time was then spent.
- HUD resources at end, unchanged by this unit: food 415.2M, iron 745.8M, coins 15.2M, power 150,028,269 - consistent with the 0755 harvest gains, not a contradiction. No batch was queued and no Train Units panel was reached, so the Drill Ground Full toast was neither reconfirmed nor cleared in this unit; the 0440 live confirmation still stands as the latest Drill Ground read. 0 of 4 barracks queued, 1 of 4 verified (Lv.20 Details only), so the 'keep every barracks busy' standard is unmet. Tracker untouched, per the rule for partial units; the next tick re-produces training and resumes from the findings below.
- Follow-up for the next training unit, in order: (1) which button in the current framing actually opens Train Units, since the middle button opened Details here; (2) the Drill Ground clearing method, still unknown. This is the known tent / Drill Ground blocker already tracked as Issue #150; no new issue filed. The framing-instability comment onto #150 is DEFERRED by this run: the 0814 record names it as a comment only if the next unit confirms it again, so no #150 comment is made here.
- Red lines: nothing spent at all; no Train button completed a queue, no Finish Now, no green upgrade shortcut, no building started, no squad dispatched, no other activity's work done, no chat message sent.

## What the 2026-11-04 1147 unit added - fullscreen framing mismatch, four grounded tent taps no panel, centre drag no view move, Issue 150 repeat, partial

- Unit training-2026-11-04-1003 by ticker-1134, about 11:47 local, status partial. Sessions cc-453 then cc-454 (the first session dropped mid-unit and was reopened; no data was lost - a control-channel recovery repeat of the 0917 and 0814 pattern, not a game-state event). No "active on a different device" dialog appeared. Chrome was the frontmost app on the Mac during this unit; background input to the Last War window still dispatched.
- Tent search, no panel reached: four grounded taps on the live fullscreen base frame - norm (368,545), norm (435,465), norm (555,460) and norm (438,545) - each dispatched, but no building label and no button row (paw Details, pistol Train, green upgrade arrow) appeared in the following screenshots, so no TRAIN UNITS panel was ever reached. One drag (norm start (450,550) to (650,350)) did not move the base view; the framing stayed identical across screenshots. The centre-drag no-move is consistent with the 0252 and 0647 reads (road drags pan, centre drags do not), not a new drag rule.
- Framing mismatch, qualified not contradicted: the fullscreen 1920x1080 framing does not match the 2026-11-03 success frame, where a grounded tap at norm (630,592) selected Barracks Lv.27. This does not contradict the standing rule - the 2144 section already qualified (630,592) as framing-bound (it selected Titanium Alloy Factory No.3 in the 2144 framing) - so the mismatch is the framing-bound rule playing out again in a fullscreen framing, not a portable coordinate failing.
- Focus refusals, retried not recorded as access failures: one early click was refused for focus reasons ("user working in another window") and one click was refused for a stale observation; both were retried and the following taps dispatched. Neither refusal is an access failure.
- Follow-up from the record itself: the next unit re-grounds on its own live frame rather than reusing any point from this unit, and tries the windowed (non-fullscreen) Last War window if the fullscreen frame keeps refusing to select a tent.
- No barracks queue state was verified, no batch was queued, and no Drill Ground figure was read live in this unit, so the 0440 live Drill Ground Full confirmation still stands as the latest Drill Ground read - neither reconfirmed nor cleared here. This is the known tent blocker already tracked as Issue #150; no new issue was filed, and this run comments the fullscreen-framing recurrence onto #150.

## What the 2026-11-04 1734 unit added - screen-capture failure, eleventh consecutive pass, nothing read

- Unit training-2026-11-04-1403 by ticker-1734, about 17:34 to 17:46 local, status failed. Evidence in `_records_/2026-11-04/troop-training/1734-queue-run.md`. No barracks was opened, no batch was collected or requeued, and no training count was verified.
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt across two computer sessions: session cc-473 open_app LastWar returned outcome_unknown, then computer.observe (compact) failed; session cc-474 observe (compact) failed, computer.control activate selected the LastWar window for background input but captured no observation, observe (compact) failed again, observe (image) failed, and a final observe (compact) failed after a healthy connection repair check, all with "Failed to start stream due to audio/video capture failure". The control channel itself was reachable (computer.control list_apps confirmed LastWar running and selected as target); the capture stream was not. The device connection health was healthy on both native and web transports, LastWar (com.lastwar.ios, pid 59735) was running fullscreen 1920x1080, and Google Chrome was frontmost. Screen-recording permission is granted on the device.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. The pass stopped after this unit rather than failing further units identically, since every further unit needs the same capture channel.
- Recurrence, not a new failure class: this is the eleventh consecutive ticker pass to fail on this exact blocker (ticker-1224 help 1235, ticker-1327 mail 1333, ticker-1340 star-ceremony 1344, ticker-1404 train 1404, ticker-1434 passes 1434, ticker-1504 donations 1504, ticker-1534 radar 1534, ticker-1604 arms-race 1604, ticker-1634 harvest 1634, ticker-1704 survivors 1707, ticker-1734 training 1734), now across eleven activities. The blocker is filed as Issue #284 (tooling, filed by the ticker-1340 pass) alongside the knowledge Issue #282 filed by the 1332 organizer run; this pass commented on #284 (comment 6647208826) instead of filing a duplicate, and this run comments the eleventh and twelfth occurrences onto #282.
- Reading warning: this failed unit gives zero evidence about training state. It must NOT be read as "no batch due" or as a queue state - the 0440 live Drill Ground Full confirmation still stands as the latest Drill Ground read, and the 1147 framing findings stand; this unit rests on no read at all. The Drill Ground clearing method remains unknown, carried forward from Issue #150, not closed.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## Correction 2026-11-05 - the game window is windowed on an inactive Space, not in native fullscreen

- Source: the 0134 survivors record (`_records_/2026-11-05/survivor-intake/0134-queue-run.md`, ticker-0134, twenty-sixth consecutive capture failure), re-confirmed by the 0204 gifts record (`_records_/2026-11-05/alliance-gifts/0204-queue-run.md`, ticker-0204, twenty-seventh). The View menu lists "Enter Full Screen" (read from the menu-action error listing in session cc-505, repeated probe in cc-508 with the menu unchanged), so the app is NOT in native fullscreen: it is a windowed window on an inactive Space, and the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission (Chrome windows observe normally in the same sessions). The 0534 troop-training pass agrees: its probe classifies OFF_SCREEN_WINDOW at high confidence, and the window is listed as 2560x1440 at (0,360) - a windowed geometry, not a fullscreen frame.
- Superseded in this profile: the "running fullscreen 1920x1080" wording in the 1734 section above, and the "fullscreen framing" wording in the 1147 section above. The 1147 framing findings stand unchanged - the tent points are framing-bound, and the mismatch is the framing-bound rule playing out, not a portable coordinate failing. The 1147 follow-up (try the windowed Last War window) already points at the corrected model.
- Follow-up set: no unblock was stated in the 1734 section; the standing unblock is now getting the window back onto the active Space, and the owner clicking the LastWar Dock icon once is the known reliable step (or run `_tools_/mac_lastwar_front.sh` in Terminal, then re-probe). Background-sent Space keys do not switch Spaces, set_window_frame is gated by the stale-observation rule, Cmd+Tab is blocked by the tool, and list_windows needs the exact app name "LastWar". Never use Control-Command-F or Escape on this app (both crash it).
- This correction does not change the training state: the 0440 live Drill Ground Full confirmation still stands as the latest Drill Ground read; no barracks, batch or Drill Ground figure was read in the failed passes and none is asserted here. The thirty-fourth occurrence is commented onto Issue #282 by this run; Issue #284 already tracks the blocker.

## What the 2026-11-05 0534 unit added - screen-capture failure, thirty-fourth consecutive pass, nothing read

- Unit training-2026-11-05-0203 by ticker-0534, about 05:34 to 05:45 local, status failed. Evidence in `_records_/2026-11-05/troop-training/0534-queue-run.md`. No barracks was opened, no batch was collected or requeued, and no training count was verified. On a working screen this unit would have checked the four barracks and requeued any idle batch, and would have read the Drill Ground screen live first under the standing third-strike blocker note (Drill Ground Full, 39,460 of 39,460).
- No game screen was ever read and no game input was dispatched. The Mac screen-capture stream failed on every attempt in computer session cc-522: computer.control activate selected the LastWar window for background input but captured no observation, computer.observe (compact) failed three times with the same error (a 10 second wait between attempts 1 and 2 changed nothing), and computer.control open_app LastWar returned outcome_unknown with no verifiable launch result and the window still listed under the same pid, all with "Failed to start stream due to audio/video capture failure". The capture pipeline itself works: a Chrome window observed normally in the same session (the Coordinator harness tab, full accessibility tree), so the fault is specific to the LastWar window. LastWar (bundle com.lastwar.ios, pid 59735) is running, a 2560x1440 window at (0,360) on an inactive Space, window_id 160366; Google Chrome was frontmost at session start, Keychain Access frontmost at the close of the probe. `activate` reports `window_on_screen: false` and `brought_to_front: false`.
- Probe classification: `_tools_/mac_capture_probe.py` (tool version 1.0.0) classifies OFF_SCREEN_WINDOW (high confidence), stop_pass yes, exit code 10. The LastWar window sits on an inactive Space, so its pixel stream cannot start.
- Recovery still needs the one owner step: click the LastWar Dock icon once on the Mac mini (or run `_tools_/mac_lastwar_front.sh` in Terminal), then re-probe. No background control route moves the window - Space keys sent in the background do not switch Spaces, open_app returns outcome_unknown, and set_window_frame needs a fresh observation, which is exactly what the failure prevents. Never use Control-Command-F or Escape on this app (both crash it).
- Recurrence, not a new failure class: this is the thirty-fourth consecutive ticker pass to fail on this exact blocker (ticker-0504 the thirty-third). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 (comment IC_kwDOVXE0ls8AAAABjO5-yA) instead of filing a duplicate, and this run comments the thirty-fourth occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about training state. It must NOT be read as "no batch due" or as a queue state - the 0440 live Drill Ground Full confirmation still stands as the latest Drill Ground read, and the 1147 framing findings stand; this unit rests on no read at all. The Drill Ground clearing method remains unknown, carried forward from Issue #150, not closed.
- The pass stopped after this one unit - every further unit needs the same game screen, and the probe says to stop. The inbox held 70 units at this pass. No other unit was attempted. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 1655 unit added - Lv.27 T9 and Lv.30 T10 requeued, two barracks unchecked, Drill Ground Full not seen, partial

- Unit training-2026-11-07-1403 by ticker-1655, about 17:08 to 17:12 local, status partial. Evidence in `_records_/2026-11-07/troop-training/1655-queue-run.md` (commit 514e333e5b on records/2026-11-07). Computer session cc-19, LastWar already running on the Mac mini.
- Lv.27 barracks (center tent, timer bubble now above it): TRAIN UNITS panel read Power 1352, Morale 625.0, Squad Load 2000, Unit HP 4121.49, Attack 33.5, Defense 6.74; Lv.9 selected, count 726 at cap, cost 4.1M food plus 4.1M iron, time 1d 10:19:35. Train tapped; panel closed and the HUD moved food 486.5M to 482.3M and iron 810.0M to 805.9M. Batch started. (726 at cap matches the 1552 batch - the cap is stable.)
- Lv.30 barracks (tent below-right of the first; its portrait circle overlaps the tent body - tap the body, not the circle): TRAIN UNITS panel read Power 1647, Morale 750.0, Squad Load 2200, Unit HP 4726.34, Attack 38.45, Defense 7.7; Lv.10 selected, count 793 at cap, cost 5.5M food plus 5.5M iron, time 1d 17:14:37. Train tapped; panel closed and the HUD moved food 482.3M to 476.8M and iron 805.9M to 800.4M. Batch started.
- Total spent in this unit: 9.6M food and 9.6M iron for 726 T9 plus 793 T10 troops. Both requeued barracks now carry a clock timer bubble. Finish Now was never tapped.
- The other two barracks (upper-right tents) were not checked in this unit, so the "keep every barracks busy" aim is not fully met. The next training unit starts with those two. Tracker untouched, per the partial rule; the next tick re-produces the training regular.
- The Drill Ground Full blocker from the 2026-10-31 retro was not seen: both Train taps succeeded and no capacity message appeared. No Drill Ground screen was read live in this unit, so the blocker is not closed, only not encountered - it is carried forward, not cleared.
- Handover observation for the next survivors unit: a white "?" speech bubble stands at the left edge near the front gate (norm about 113,582) in the closing screenshots of this unit - a waiting survivor may have arrived after the survivors unit closed unverified minutes earlier.
- Figures read live: food 486.5M at entry, 482.3M after the first batch, 476.8M at close; iron 810.0M, 805.9M, 800.4M; coin 5.7M; stone 25.0M; 922.2K; power 149,850,353. No diamonds, money, speedups or paid buttons were used. No login or verification was demanded, and no different-device dialog appeared.

## What the 2026-11-07 2026 unit added - Lv.27 verified busy by panel read, Lv.30 busy by timer bubble, two barracks unlocated, partial

- Unit training-2026-11-07-1803 by ticker-2006, about 20:19 to 20:26 local, status partial. Evidence in `_records_/2026-11-07/troop-training/2026-queue-run.md` (commit e9bf320c92 on records/2026-11-07). Computer session cc-43, LastWar already running on the Mac mini.
- Entry from the donations panel left open by the previous unit of this pass: closed the ALLIANCE TECH panel with its X (norm 815,200), the ALLIANCE TECHS tree with its X (norm 818,152), and the Alliance menu with its back arrow (norm 185,932), returning to the base screen. Side read on the way out, for the donations profile: the ALLIANCE TECHS footer read Tech Donation Today 1150 at about 20:22, up from 750 at the 2018 donations unit's close about six minutes earlier, with no donation made by me in between. The footer moves independently of this unit's donations; recorded as observed only, no mechanism claimed. The 1924 2700-to-750 drop remains unexplained.
- Base screen, opening view: two barracks tents with clock timer bubbles, grounded at norm (577,546) and (671,597) - the Lv.27 and Lv.30 pair requeued by the ticker-1655 unit at about 17:10 today.
- South pan, changed route per rule R2: an upward drag (norm 500,650 to 500,350) moved the view south - Formation 2 and 3 lots, parked vehicles, snowfield at the map edge. No additional barracks tent in this framing. Drag mapping re-confirmed: an upward finger drag moves the view south (1651 unit), the reverse drag returns north.
- East pan: a leftward drag (norm 650,500 to 300,500) moved the view east - Capitol and Big Ben, the VS tower at 02:23, gold buildings, the red-roofed troop formation. The same two timer-bubble tents shifted left (grounded (192,543) and (298,587)); no additional barracks tent in this framing.
- Lv.27 tent tap at norm (192,543) selected Barracks Lv.27 with its three-button action row (blue paw, orange pistol, green up arrow - the green arrow was not tapped). The pistol grounded at norm (201,585) opened TRAIN UNITS on the first try: Power 1352, Morale 625.0, Squad Load Capacity 2000, Unit HP 4121.49, Unit Attack 33.5, Unit Defense 6.74; Lv.9 selected, count 726, "Training in progress 1d 07:03:33". The batch is busy, verified by panel read, consistent with the 1655 requeue (1d 10:19:35 at about 17:10). The Speed Up button was not tapped. Lv.10 shows locked. Panel closed with its X.
- Lv.30: busy by its clock timer bubble only, not panel-read in this unit.
- Not done: the other two barracks (upper-right tents per the 1655 unit) were not located in this unit. The south and east pans from the opening view are now ruled out as the direction to them; the north and west pans and the zoomed-out whole-base view remain untried for this search.
- No batch was queued and no idle barracks was found. No Drill Ground figure was read live in this unit, so the 2026-10-31 Drill Ground Full blocker is neither confirmed nor cleared here.
- Handover observation for the next survivors unit: a white "?" speech bubble stands at about norm (505,790) in the eastern framing - not acted on from this training unit.
- Figures read live: food 478.7M, iron 802.1M, coin 6.9M, power 149,850,353 at entry and close. No diamonds, money, speedups or paid buttons were used. No Finish Now, no upgrade shortcut. Game left on the base screen in the eastern framing.
- Tracker untouched (partial close); the next tick re-produces the training regular.

## What the 2026-11-07 2050 unit added - Lv.30 busy by panel read, Lv.24 idle but blocked by Drill Ground Full, Drill Ground screen read live, partial

- Unit training-2026-11-07-1803 by ticker-2034, about 20:43 to 20:50 local, status partial. Evidence in `_records_/2026-11-07/troop-training/2050-queue-run.md` (commit 7a4a104930 on records/2026-11-07). Computer session cc-47, LastWar already running on the Mac mini.
- Lv.30 barracks: TRAIN UNITS panel read Power 1647, Morale 750.0, Squad Load 2200, Unit HP 4726.34, Attack 38.45, Defense 7.7; Lv.10 selected, count 793, "Training in progress 1d 13:41:04" at about 20:47. This is the batch requeued by the 1655 unit at about 17:08 today (1d 17:14:37 at start), so the remaining time is consistent. Busy; Speed Up was never tapped.
- Lv.24 barracks: selected (label "Barracks Lv.24" with the paw, pistol and green up-arrow button row). Tapping the pistol TRAIN UNITS button produced the toast "Drill Ground Full: Unable to add more units" (read live by OCR); no TRAIN UNITS panel stayed open and no batch was started. This barracks is idle and blocked, not busy.
- Drill Ground screen read live, as the standing blocker requires: tapping the troop formation selected "Drill Ground Lv.25"; its Building Details panel (paw button) reads Unit Count +7812, Survivors Officers Joe, Marcus, Karen and John, and a single action button "Quick Dispatch" at the panel bottom. No 39,460 of 39,460 figure appears on this screen; that figure comes from earlier units and was not re-read live here. Quick Dispatch was NOT tapped: its effect is unverified and it may march troops out, so it is left for an owner decision or a learn-first exploration unit, not pressed blind inside a training unit.
- No barracks was requeued in this unit: one confirmed busy, one idle but blocked by the full Drill Ground, two not checked. The Lv.27 barracks was requeued by the 1655 unit at about 17:08 today and should still be busy, but that was not re-verified live in this unit. Tracker untouched, per the partial rule; the next tick re-produces the training regular.
- The clearing method for a full Drill Ground is still unknown from a live read. The only candidate control seen is Quick Dispatch on the Drill Ground Details panel, untested.
- Tap method note (rule R2): direct coordinate taps on tent bodies missed twice (norm 393,600 and 511,557, both no panel). The visual-grounding point (435,518) selected the Lv.24 barracks, and the pistol button grounded at (425,581). The observation "no_change_observed" flag proved unreliable twice: the view had in fact changed after the tap. Next units should screenshot to verify after every tap instead of trusting that flag.
- Figures read live on screen: food 478.8M, iron 802.1M, coin 6.9M, stone 25.0M, 922.2K, power 149,850,353, diamonds 4,217, energy 118 at entry rising to 119 during the unit. No diamonds, money, speedups or paid buttons were used. No other task type was executed in this unit. No login or verification was demanded, and no different-device dialog appeared.
- Result statistics: target 4, achieved 0, resources_gained none, costs about 7 minutes play, verified yes, blocker_category e, device_takeovers 0.

## What the 2026-11-08 1350 unit added - Lv.30 barracks re-verified busy, tent tap (459,457) opens TRAIN UNITS directly, no batch queued

- Unit training-2026-11-08-1003 by ticker-1317, about 13:37 to 13:40
  local, status partial - 1 of 4 barracks verified (Lv.30 busy), 0
  batches queued, the other three barracks not reached inside the
  unit cap. Evidence in
  `_records_/2026-11-08/troop-training/1350-queue-run.md` (commit
  d272dd711 on records/2026-11-08). Tracker untouched.
- Session: computer session cc-126 on the owner Mac mini (session
  cc-125 had dropped between units and was restarted). No
  device-access error, no different-device dialog, no login demanded.
  Nothing bought, no speedup used, no Finish Now tapped.
- Session window: 13:37-13:40 local, about 3 minutes. Base HUD at
  entry: food 489.5M, wood 811.9M, iron 25.0M, stone 922.2K, coin
  12.3M, power 149,850,353, diamonds 4,397, gold 13.22K. Stamina 88
  at the lightning icon.
- Tent tap 1 at norm (564, 510), on the second white-blue chevron
  tent in the middle of the base: no change, no selection label, no
  action row. A miss, not a tent selection (rule R2: that point ends
  here).
- Tent tap 2 at norm (459, 457), on the first white-blue chevron
  tent: opened TRAIN UNITS directly, with no action row seen in this
  framing. Panel read live: Power 1647, Morale 750.0, Squad Load
  Capacity 2200, Unit HP 4726.34, Unit Attack 38.45, Unit Defense
  7.7, Lv.10 selected at 36.5K, a Lv.10 batch of 793 already training
  with 20:47:28 left. This is the same Lv.30 barracks the arms-race
  unit read at 21:01:06 left about 13:27 - busy, cannot queue more.
  No Train was tapped and no Speed Up was tapped; the panel was
  closed with its X, returning to the base.
- Tap-method lesson: a single tap on a verified tent can open TRAIN
  UNITS directly in this framing, while a neighbouring tent point
  missed outright - re-ground fresh in the unit's own view; the
  (564, 510) point is a miss, not a tent.
- The other three barracks (Lv.27, Lv.24, fourth T7) were not
  reached in this unit. The Drill Ground Full state was not re-read
  live, and Quick Dispatch was not tapped (unverified effect, left
  for an owner decision per the activity metadata).
- Arms Race implication: no Lv.10 batch was queued in this unit, so
  the Unit Progression phase score stays at 0. The priority-1
  successor arms-race-2026-11-08-2127 follows in this pass to
  re-read the score and close the phase verdict before the phase end
  (see arms-race 1.59.0).
- Observed, not acted on: a top banner reading "5000 Diamonds from
  Alliance Star Thank You Gift. The rumor turns out to be true!" - a
  system/chat banner, not a claim by this unit; any gift claim
  belongs to the gifts regular, not this unit.
- Result stats: target 4 barracks, achieved 0 batches queued (1
  barracks state verified live), verified yes for the Lv.30 busy
  read.
- Follow-up: the next training unit resumes the barracks check from
  the unchecked barracks (Lv.27, Lv.24, fourth T7 - three by live
  read; the 1333 and 1350 follow-ups' "two remain" counts the
  2026-11-01 Lv.8-only carry as checked). Re-ground fresh in its own
  view.

## What the 2026-11-08 2119 unit added - Lv.27 busy, Lv.20 Drill Ground Full re-confirmed live, paw Details works, long-press retired, T9 stats corrected

- Unit training-2026-11-08-1803 by ticker-2058, about 21:01 to 21:19
  local, status partial - 2 of 4 barracks verified live (Lv.27 busy,
  Lv.20 blocked by Drill Ground Full), 0 batches queued, the other
  two barracks not reached inside the unit cap. Evidence in
  `_records_/2026-11-08/troop-training/2119-queue-run.md`
  (commit 023fb42b6 on records/2026-11-08). Tracker untouched.
- Session: computer session cc-167 on the owner Mac mini, dropped
  mid-unit (observe returned observation_unavailable with no session
  open); session cc-168 was started, LastWar re-selected, and no
  game state was lost. No device-access error, no different-device
  dialog, no login demanded. Nothing bought, no speedup used, no
  Finish Now tapped. Session window about 18 minutes, over the 15
  minute unit cap by about 3 minutes; the closing pistol tap and its
  toast read ran past the cap and the unit was closed immediately
  after. The cc-167 drop is new evidence for Issue #282.
- Base HUD at entry: food 499.1M, iron 821.2M, coin 15.8M, total
  power 149,209,253, diamonds 4,467 (gold 13.22K per the 1350 unit),
  unchanged at close. Stamina 120 at the lightning icon. The power
  figure corroborates Issue #482: the third live read of the
  stepped-down 149,209,253 (after the 17:06-17:12 step-down from
  149,850,353), still with no named cause.
- Barracks Lv.27, verified busy live: tent tap at norm (610, 580)
  selected Barracks Lv.27 with its three-button action row; the
  pistol tap at freshly grounded norm (602, 632) opened TRAIN UNITS.
  Panel read live: Power 1352, Morale 625.0, Squad Load Capacity
  2000, Unit HP 4121.49, Unit Attack 33.5, Unit Defense 6.74, Lv.9
  selected (1,152), Lv.10 locked (36.5K), a Lv.9 batch of 726
  already training with 06:26:20 left. No Train was tapped and no
  Speed Up was tapped; the panel was closed with its X.
- CORRECTION - T9 stats: Morale 625.0 (profile said 600.01),
  Attack 33.5 (profile said 33.13), Defense 6.74 (profile said
  6.67) - the live values govern and the standing T9 line is
  corrected in this fold.
- Barracks Lv.20, two findings: (a) the paw Details route WORKS for
  Lv.20 - tent tap at norm (362, 588) selected Barracks Lv.20, the
  paw tap at freshly grounded norm (285, 606) opened Building
  Details, read live: Training Count +613, Survivors Instructors
  Alexis, Joe, Jolene and Anthony, Quick Dispatch button at the
  panel bottom NOT tapped (unverified effect, left for an owner
  decision per the activity metadata). The Details panel shows no
  batch timer, so busy/idle is not readable from it. (b) The pistol
  tap at freshly grounded norm (396, 634) in the same framing
  produced the live toast "Drill Ground Full: Unable to add more
  units" - the first live re-confirmation of the standing Drill
  Ground Full blocker since the 2026-10-31 read, and proof the
  Lv.20 pistol route reaches the train attempt in this framing (it
  neither cleared the selection as in 1146 nor opened the upgrade
  panel as in 0322). No batch was queued: the game refused on the
  full Drill Ground, not on an idle barracks. The toast is transient
  and had cleared by the next screenshot; the game was left on the
  base screen with the selection cleared.
- Lv.20 long-press variant, DANGEROUS, RETIRED on this evidence: a
  1-second long-press on the selected Lv.20 tent body at norm
  (848, 453) entered building-move mode (red X and green check
  buttons at the screen centre, view panned) instead of opening
  TRAIN UNITS. It was cancelled at once with the red X at norm
  (413, 610); no building was moved and the HUD was unchanged after.
  Do not repeat. The standing Lv.20 rule is updated above.
- Wrong-building tap: a visual-grounding point for a tent at norm
  (535, 455) in the panned framing selected Hospital Lv.20 instead;
  it was left untouched (no button tapped) and deselected with a tap
  on empty ground. Grounding points for tents must be verified
  against the selection label before any action-row tap.
- Lv.30 and Lv.24 were not reached in this unit. Lv.30 was verified
  busy by the 1350 unit (Lv.10 batch 793 with 20:47:28 left at
  13:37) and is still expected busy; that is expectation, not a live
  read here.
- The Drill Ground panel itself was not opened and no 39,460 of
  39,460 figure was read live; the toast is the live re-confirmation,
  not a count.
- Result stats: target 4 barracks, achieved 0 batches queued (2
  barracks states verified live), blocker category e (repeated
  blocker, Drill Ground Full re-confirmed live).
- Commented on Issue #150 by the unit itself; this run comments the
  fold. The session drop is commented onto Issue #282 by this run.
- Game left safe: base screen, no purchase, no diamond spent, no
  speedup used.
- Follow-up: the next training unit resumes from Lv.27 busy until
  about 03:27, Lv.20 blocked by Drill Ground Full, Lv.30 and Lv.24
  still to check. Re-ground fresh in its own view. It falls to the
  next run.

## What the 2026-11-09 0039 unit added - Drill Ground Lv.30 read live, Unit Count +10080, officers rotated, Quick Dispatch not tapped, no barracks requeued

- Unit training-2026-11-08-2203 by ticker-0019, about 00:25 to 00:39 local, status partial - no barracks verified live, no batch requeued. Evidence in `_records_/2026-11-09/troop-training/0039-queue-run.md` (commit f99faa9744 on records/2026-11-09). Tracker untouched; the next tick re-produces the training regular.
- Drill Ground screen read live, as the activity's third-strike instruction requires. Tapping the red troop formation at the base's lower edge selected Drill Ground Lv.30 (the 2050 unit read Lv.25 on 2026-11-07 - the level has risen since, noted as a live read, not reconciled here). Its Building Details panel (paw button) reads Unit Count +10080 (up from +7812 on 2026-11-07), Survivors Officers Samantha, William, Chloe and Catherine (the roster has rotated since Joe, Marcus, Karen and John on 2026-11-07), and a single action button, Quick Dispatch, at the panel bottom. No capacity denominator appears on this screen either - the 39,460 of 39,460 figure from earlier units was not re-read live on any screen in this unit.
- Quick Dispatch was NOT tapped: its effect is still unverified and it may march troops out, so it stays left for an owner decision or a learn-first exploration unit, as the 2050 unit decided. No diamonds, money, speedups or paid buttons were used.
- The yellow-green fenced structure with soldiers, a tank and a 3d 01:53 countdown was tapped twice to identify it as a barracks candidate. Both taps resolved to the Aircraft Center Lv.29 selection with a medal button and a green fast-forward button, so the structure is not verifiably a barracks and the four tents were not located in this unit. Per queue rule R2 that grounding method ends here - the next unit must ground the tents from a fresh route, not re-tap this structure.
- No barracks was requeued: no barracks state was verified live in this unit. Carried-forward state (not re-verified): Lv.30 busy (batch requeued 2026-11-07 about 17:08, 1d 17h, ends about 10:22 today), Lv.27 busy (ends about 03:27 today), Lv.24 idle but blocked by the Drill Ground Full toast in the 2050 unit, fourth barracks unknown.
- Figures read live on screen: food 513.8M, iron 838.3M, coin 25.2M, power 149,209,253, diamonds 6,027, energy 43 at entry rising to 45 during the unit. No login or verification was demanded, and no different-device dialog appeared.
- Result stats: target 4, achieved 0, resources_gained none, costs about 14 minutes play, verified yes, blocker_category e, device_takeovers 0.
- Commented on Issue #150 by this run with the fold. The 2119 session drop is not repeated here - same session cc-192 held for both units of this pass with no drop.
- Game left safe: base screen, no purchase, no diamond spent, no speedup used.
- Follow-up: the next training unit re-grounds the four tents from a fresh route (never re-tap the yellow-green fenced structure - it resolves to Aircraft Center Lv.29), and re-checks Lv.27 (busy until about 03:27), Lv.30 (busy until about 10:22) and Lv.24 (idle but Drill Ground Full blocked) live. It falls to the next run.

## What the 2026-11-09 0129 arms-race unit added - third-strike tent grounding failure, entry route must change

- Unit arms-race-2026-11-09-0855 by ticker-0113, about 01:14 to 01:29 local, status partial - the barracks fill was not executed. Evidence in `_records_/2026-11-09/arms-race/0129-queue-run.md` (commit c0ebf0c4f0 on records/2026-11-09). This section is the R2 metadata write the 0129 record directs to this profile; the arms-race fold (1.62.0) carries the phase read itself.
- Fresh-route attempt at the barracks tents (R2): the base view was panned toward the lower middle and the red troop formation there was tapped. It resolved to Drill Ground Lv.30 again, not a barracks tent. The four tents were not located in this unit either.
- Third strike under queue rule R2: this is the third consecutive unit failing to ground the tents (0039 troop-training, 0058 arms-race, this unit). The blocker and the failed routes (Aircraft Center structure, red troop formation = Drill Ground) are written into this profile's metadata here, and the entry route must change before any further unit of this type runs - the next attempt must not re-tap either structure.
- Drill Ground re-confirmed live: the red troop formation in the lower middle selects Drill Ground Lv.30 (label read on screen), with the paw (Building Details), train-hat and green upgrade buttons. The upgrade button was not tapped.
- Carried-forward barracks state (not re-verified live): Lv.30 busy (batch ends about 10:22 today), Lv.27 busy (ends about 03:27 today), Lv.24 idle but blocked by the Drill Ground Full toast, fourth barracks unknown. The phase ends about 02:00 local, before either busy batch ends, so even a located idle barracks may still be blocked by Drill Ground Full - the successor must judge that live.
- No successor was manually enqueued by the 0129 unit: the tracker still shows arms-race due (partial leaves it untouched), so the next tick re-produces it; the arms-race-2026-11-09-1003 unit already sits in the inbox for the next phase window.
- Follow-up: the next training unit must ground the four tents from a changed route (never re-tap the yellow-green fenced structure or the red troop formation), and re-checks Lv.27 (busy until about 03:27), Lv.30 (busy until about 10:22) and Lv.24 (idle but Drill Ground Full blocked) live. It falls to the next run.

## What the 2026-11-09 0413 unit added - fullscreen zoom-out variant tried, no barracks tent verified, View-menu fullscreen exit measured

- Unit training-2026-11-09-0203 by ticker-0404, about 04:10 to 04:13 local, status partial. Evidence in `_records_/2026-11-09/troop-training/0413-queue-run.md` (commit 9fdcc4c9ee on records/2026-11-09). Computer session cc-217 on the owner Mac mini.
- Entry snapshot, read live on the opening base screen: food 540.1M, iron 864.9M, coin 42.9M, diamonds 13.22K, total power 149,217,331, window 642 by 951. LastWar already frontmost; no different-device dialog, no login or verification demanded.
- Fresh grounding for a barracks tent on the opening windowed frame returned no tent. The tents are not in this framing.
- Changed method one, per queue rule R2: a west road drag (norm 500,700 to 150,700) along the bottom road produced no view change. A blocked drag, not a "no tents here" result; the method ends here.
- Changed method two, per queue rule R2 and the zoom-out-first variant named by the 1216 and 1651 units and still untried until now: native fullscreen via the green zoom button. The fullscreen frame (1280 by 720 capture) shows a wider base view. Fresh grounding found one tent candidate at norm 445,665; the tap on the fresh frame produced no change - no building label, no action row, no panel. The point did not resolve to a tappable tent, so per rule R2 the method ends after the one no-change tap and the point was not tapped again. The zoom-out-first variant is now TRIED and did not locate a tent in this framing; it is not a standing solution, and the next unit still re-grounds on its own live frame.
- FULLSCREEN EXIT, MEASURED: the menu bar did not drop from a pointer move to the top edge (the control channel delivers the pointer to the window only, not the system cursor), but computer.control inspect_menu with path ["View"] lists "Exit Full Screen" enabled, and the menu action with path ["View", "Exit Full Screen"] returned the game to the 642 by 951 window with no crash and no login demanded. This is the working exit route for this control channel; never use Ctrl-Cmd-F or Escape. NOTE: this is a deliberate-entry measurement (green zoom button in, View menu out) and does not contradict the 2026-11-05 correction that the 0134/0204 sessions were windowed on an inactive Space, not in native fullscreen - those sessions never entered fullscreen.
- No barracks panel opened, no batch state verified, no batch queued. The retired routes were not re-tapped: the yellow-green fenced structure (Aircraft Center Lv.29) and the red troop formation (Drill Ground Lv.30). The Drill Ground screen was therefore not re-read in this unit, and the 39,460 of 39,460 figure stays a 2026-10-31 read, neither confirmed nor cleared here.
- "Violet's Gift received!" toast seen in the fullscreen frame; it belongs to the gifts regular and was not acted on from this training unit. No diamonds or money spent, no Finish Now, no upgrade shortcut, no speedup burned.
- Closing reads: barracks verified 0, batches queued 0. Training state unverified; the game was left on the base screen in its normal windowed framing.
- Result stats: target 4, achieved 0, resources_gained none, costs 10m_wall_no_stamina, verified no, blocker_category c, barracks_verified 0, batches_queued 0, device_takeovers 0.

## What the 2026-11-09 1330 unit added - Lv.27 idle and blocked by Drill Ground Full, tents grounded by a fresh route

- Unit training-2026-11-09-1003 by ticker-1304, about 13:13 to 13:30 local, status partial - Lv.27 barracks idle and blocked by Drill Ground Full, no batch requeued. Evidence in `_records_/2026-11-09/troop-training/1330-queue-run.md` (commit 5108be8d7 on records/2026-11-09). Tracker untouched; the next tick re-produces the training regular.
- Computer sessions cc-277 then cc-278 on the owner Mac mini (cc-277 dropped mid-unit, observation_unavailable; cc-278 restarted, LastWar re-selected, no game state lost).
- Tents grounded by a fresh route, as the 0039 unit required under queue rule R2 (the yellow-green fenced structure method ended there). CORRECTION: the diagonal row of blue-roofed tents in the upper base is Material Workshops, not barracks - a tap at norm (267,365) selected Material Workshop Lv.20, and a tap at norm (460,290) selected Eternal Pyramid Lv.3. The barracks are the beige tents with blue zigzag markings at the base lower-right edge, each with an instructor portrait circle overlapping the tent body - tap the body, not the circle, as the 1655 unit already noted.
- Barracks Lv.27 selected live (label read on screen, norm tap (799,871) on the tent body; the earlier tap at (748,910) hit the tent's left edge and selected nothing). Its button row reads paw, pistol, green up-arrow; the pistol TRAIN UNITS button grounds at norm (787,931) for this screen position.
- Pistol tap produced the toast "Drill Ground Full: Unable to add more units" (read live by OCR), and no TRAIN UNITS panel opened. Lv.27 is idle and blocked - the same blocker the 2050 unit read for Lv.24 on 2026-11-07, now re-confirmed live on a second barracks two days later. No timer bubble stands above the Lv.27 tent, consistent with idle. No diamonds, money, speedups or paid buttons were used, and no other task type was executed in this unit.
- The building at norm (435,518) is the ICU hospital, not a barracks - the 2050 grounding point no longer maps to a barracks in the current camera view. A gold-mine timer bubble read 97min then 94min during the unit; it is a mine production timer, unrelated to training.
- What was not done: no barracks was requeued - Lv.27 is idle but blocked by the full Drill Ground. Lv.30 (batch requeued 2026-11-07 about 17:08, 1d 17h, due about 10:22 today), Lv.24 and the fourth barracks were not checked in this unit - the second beige tent sits half off the bottom edge and needs the camera panned down first. The Drill Ground screen was not re-read live in this unit; the 0039 unit read it this morning (Lv.30, Unit Count +10080, officers Samantha, William, Chloe and Catherine, single action Quick Dispatch, untapped). Quick Dispatch stays untapped: its effect is still unverified and it may march troops out, left for an owner decision or a learn-first exploration unit.
- Figures read live on screen: food 553.9M, iron 879.2M, coin 51.9M, power 149,217,331, diamonds 13.22K, energy 68 at entry. No login or verification was demanded, and no different-device dialog appeared.
- Result stats: target 4, achieved 0, resources_gained none, costs about 17 minutes play, verified yes, blocker_category e, device_takeovers 0.
- Follow-up: the next unit pans the camera down to find the red troop formation at the base lower edge, re-reads the Drill Ground screen live, and checks Lv.30, Lv.24 and the fourth barracks. It falls to the next run.

## What the 2026-11-09 2103 unit added - barracks tent tap no-change x3, no TRAIN UNITS panel, Drill Ground not read, entry route must change (R2), partial

- Unit training-2026-11-09-1803 by ticker-2040, about 20:56 to 21:03 local, status partial. Evidence in `_records_/2026-11-09/troop-training/2103-queue-run.md` (commit ca96fa0c9 on records/2026-11-09).
- Session: computer session cc-343 dropped mid-pass (observation unavailable); cc-344 started, LastWar re-selected. The window came up covered - activate reported brought_to_front false.
- One barracks tent was grounded fresh on the live screenshot (top-row blue tent, 283,230) and tapped three times: the first tap showed a "+45" float and a small portrait marker at the tent (200,215), but no row of round buttons and no TRAIN UNITS panel appeared; the second tap at (283,245) and a third at (283,230) after a title-bar click to bring the window forward both reported no change. The control's own guidance on the second tap says background clicks do not reach some controls and suggests click_element or the keyboard instead.
- Drill Ground not read live in this unit: no barracks panel opened, so the standing Drill Ground Full blocker (39,460 of 39,460) could neither be confirmed nor cleared, and no batch was requeued.
- No diamonds or money spent. No Train, Finish Now or upgrade shortcut tapped. Nothing bought, nothing deleted.
- Next unit of this type must change the entry route before tapping a tent again (R2): try click_element on the tent control, a foreground click with the window truly frontmost, or a different barracks tent - the same background-click point must not be repeated. The tap-method failure here is distinct from the Drill Ground Full blocker recorded by the retro. The 1330 section's follow-up (pan down, re-read the Drill Ground screen, check Lv.30/Lv.24/the fourth barracks) was not executed in this unit - entry failed first - and still falls to the next unit, after the entry route changes.
- Result stats: target requeue idle barracks, achieved 0 of 4 barracks checked, resources gained none, verified yes (no-change reads are live reads), blocker_category c (tap method).

## What the 2026-11-10 0034 unit added - formation-yard taps resolve to squads and the Wall, Drill Ground selection route does not reproduce, partial

- Unit training-2026-11-09-2203 by ticker-0034, about 00:34 to 00:50 local, status partial - Drill Ground screen not re-read live, no barracks requeued. Evidence in `_records_/2026-11-10/troop-training/0034-queue-run.md` (commit d3c648601 on records/2026-11-10). Tracker untouched; the next tick re-produces the training regular. Computer session cc-370, started and ended cleanly, no drops, no different-device dialog.
- Camera panned down to the base lower edge, exposing the fenced troop formation yard (Formation 1, 2 and 3 signs, parked squads). Three fresh grounding taps were tried for the Drill Ground, per the 1330 unit's handover to re-read its screen live:
  - Tap at norm (413,541) on the green truck at the yard's left edge: no selection, only an alliance announcement banner scrolled across the top.
  - Tap at norm (592,547) on the red car: selected 2nd Squad Lv.20 (label read live; an earlier compact read showed Lv.2, an OCR misread of Lv.20), with a speech bubble "The truck is full, waiting for your command" and a tank-icon button plus a green up arrow. No squad button was tapped: dispatching a squad is truck-type work and must not merge into this unit.
  - Tap at norm (545,421) on the wooden FORMATION sign on the fence: selected Wall Lv.26, with a house-icon button and a green up arrow. The green arrow was not tapped: no upgrades on the agent's initiative.
  - Tap at norm (670,736) on empty pavement inside the fence: selected 2nd Squad Lv.20 again (the blue tank).
- Negative grounding result: at this camera view, taps inside the formation yard resolve to the individual squads parked there or to the Wall, never to a Drill Ground building. The 0039 unit's tap that selected Drill Ground Lv.30 does not reproduce from these points; the next unit needs a different selection route (for example the formation ground at a wider zoom, or the Drill Ground entry from a building list), not another tap on a vehicle, a sign or the fence. The 1330 follow-up (pan down, re-read the Drill Ground screen, check Lv.30/Lv.24/the fourth barracks) was attempted by this route and is still owed, now with the route changed.
- A green truck at the yard's left edge read "Collecting supplies, ready to depart again" - a full truck waiting, truck-type work for its own unit, left untouched. The squad selection was cleared by tapping empty snow before the session ended.
- No barracks was requeued: no barracks state was verified live in this unit, and every barracks remains blocked in the carried-forward state by the Drill Ground Full toast (39,460 of 39,460, last read live 2026-10-31). Lv.30's batch (requeued 2026-11-07 about 17:08, 1d 17h) was due about 10:22 on 2026-11-09 and its state is unverified; Lv.27 was idle and blocked at the 1330 read on 2026-11-09; Lv.24 and the fourth barracks were not checked.
- Quick Dispatch stays untapped: its effect is still unverified and it may march troops out, left for an owner decision or a learn-first exploration unit.
- Figures read live: food 598.9M, iron 922.5M, coin 80.6M, power 146,751,949, diamonds 6,207, energy 81 at entry. Build slot in use: Oil Well (0/1), 1/4 hammer icon. The power figure 146,751,949 matches the 2121 gifts unit's closing read - a second corroboration of the levelled power figure (Issue #482).
- No diamonds, money, speedups or paid buttons were used, and no other task type was executed in this unit.
- Result stats: target 4, achieved 0, resources_gained none, costs about 15 minutes play, verified yes, blocker_category e, device_takeovers 0.

## What the 2026-11-10 0337 unit added - fourth consecutive partial, R2 process failure, wide-zoom and panned-down tent taps select nothing, Duel screen live read

- Unit training-2026-11-10-0203 by ticker-0334, about 03:37 to 03:42 local, status partial - no barracks requeued. Evidence in `_records_/2026-11-10/troop-training/0337-queue-run.md` (commit b7e79a62 on records/2026-11-10). Computer session cc-390 on the owner Mac mini, started and ended cleanly, no drops, no different-device dialog.
- Changed method per queue rule R2 and the 0034 handover: the camera was zoomed out with a scroll to a wide base view and the beige tents with blue zigzag markings at the base right edge were tried fresh. Three fresh grounding taps on those tents selected nothing: (890,500) on the upper tent body, (919,530) on the lower tent body, and (841,116) on the upper tent in the panned-down view (Formation 2 and 3 signs, parked squads). Two of the points misfired into other entries: (903,468) opened the world/radar map ("12 Radar Task(s) will be restored in 01:59:55", "9 task rewards can be claimed", Claim All NOT tapped - radar work belongs to its own unit), and (903,198) opened the Alliance Duel screen. The truck bubble beside the yard changed to "Supplies are fully loaded, please claim them" during the step; the truck was left untouched (truck-type work for its own unit).
- Fourth consecutive training partial with the same blocker (0039, 1330, 0034, this unit), each with a changed method and none requeuing a barracks. Per queue rule R2 a fourth identical partial is a process failure, not a result, and it was reported as one on Issue #150 by the ticker pass (comment 2026-11-10T11:42:26Z). The next unit needs a new grounding route, not another tap on these tent points: the tents at the base right edge do not select at wide zoom or in the panned-down view, and the top-right corner hotspots belong to the VS and radar entries.
- Alliance Duel read live on that screen (duel-type context, no duel action taken): Today's Theme Base Expansion, 14:18:29 remaining, alliance target 1,650,000 points; reward chests 8,020 / 9,530 / 18,100 with progress bars 40,000 / 150,000 / 540,000; scoring actions include Dispatch UR Trade Truck 1 time +300,000.0 and Perform 1 UR Secret Task +225,000.0. Today is a duel UR day for trucks. The +300,000 live rate supersedes the 100,000 Handbook rate - see the truck-plunder correction (1.38.0) and the duel cross-read section. Folded into the alliance-duel profile by this run.
- Power read live twice: 146,751,949 at entry, then 148,058,020 from the wide view onward (+1,306,071 during the unit; no cause established - no training batch was observed completing and no claim was made in this unit). The rise is recorded as a live read, not attributed.
- No barracks was requeued: no barracks state was verified live in this unit, and the Drill Ground screen was NOT re-read live either. The Drill Ground Full toast (39,460 of 39,460, last read live 2026-10-31) stays carried forward unverified. Carried-forward state (not re-verified): Lv.30 batch requeued 2026-11-07 about 17:08 (1d 17h) was due about 10:22 on 2026-11-09; Lv.27 idle and blocked at the 1330 read on 2026-11-09; Lv.24 and the fourth barracks not checked. Tracker untouched, per the partial rule; the next tick re-produces the training regular.
- Quick Dispatch stays untapped: its effect is still unverified and it may march troops out, left for an owner decision or a learn-first exploration unit.
- Figures read live on screen: food 610.2M, iron 933.6M, coin 82.7M, power 146,751,949 at entry rising to 148,058,020 during the unit, diamonds 6,207, energy 117 at entry. Build slot in use: Oil Well (0/1), 1/4 hammer icon, 1/2 flask icon. Radar: 12 task(s) restore in 01:59:55, 9 task rewards claimable (not claimed in this unit).
- No diamonds, money, speedups or paid buttons were used, and no other task type was executed in this unit. No squad was dispatched, no truck claimed, no radar reward claimed. The game was left on the base screen with nothing selected.
- Result stats: target 4, achieved 0, resources_gained none, costs about 5 minutes play, verified yes, blocker_category e, device_takeovers 0.

## What the 2026-11-10 0850 unit added - fifth consecutive partial, R2 process failure, TECH-screen navigation unexplained, slot-1 timer discrepancy, partial

- Unit training-2026-11-10-0603 by ticker-0834, about 08:47 to 08:50 local, status partial - no barracks requeued. Evidence in `_records_/2026-11-10/troop-training/0850-queue-run.md` (commit 5473d6845 on records/2026-11-10). Tracker untouched; the next tick re-produces the training regular. Computer session cc-424 dropped mid-pass (a full observe failed with observation_unavailable, no active session); session cc-426 started to recover, no game state lost, no different-device dialog.
- On re-activating the game window after the session restart, the game was found on the TECH screen (research category list: Development 84%, Economy 98%, Hero 68%, Units 77%, Squad 1 Max Level, Squad 2 11%, Squad 4 0%, Alliance Duel Max Level, Intercity Truck 95%), not on the base screen where the previous unit left it. No game input was sent by this pass between the base screenshot at 08:46 and the TECH screenshot at about 08:49 except the session restart and the window activate, neither of which taps the game. The navigation is unexplained and is not attributed to any cause - it may be a delayed effect of the earlier back-arrow tap, a window-focus artefact, or another session's input. Flagged, not asserted.
- Slot-1 timer discrepancy, flagged unverified: the research unit in this same pass read slot 1 as 1d 01:35:27 at 08:46; the TECH screen at about 08:49 reads slot 1 as 1d 01:51:59. A countdown cannot gain 16 minutes over 3 minutes of wall time, so one of the two reads is misread. Neither figure is claimed as the true timer without a re-read; the 1d 01:35:27 coherence argument in the 0846 research record (matching the 0116 read) is now weakened by this second read. Slot 2 reads Idle on both screens.
- The back arrow at norm 129,928 was tapped once and the base screen returned (Build: Oil Well banner, HEROES and WORLD buttons, power 148,058,020, iron 939.3M, coin 84.1M read live). The game was left on the base screen with nothing selected.
- No barracks tent was tapped in this unit: the token lease expired at 08:51:29, inside the pass budget, and the unit closed before a new grounding route could be tried. The untried routes named for the next unit are the full-observe accessibility tree with click_element on the tent control, and a fullscreen reframe via the green zoom button (never Ctrl-Cmd-F or Escape, both crash the app). The retired points must not be re-tapped: the right-edge tent points (0337) and the formation-yard points (0034).
- No barracks was requeued: no barracks state was verified live in this unit, and the Drill Ground screen was NOT re-read live either. The Drill Ground Full toast (39,460 of 39,460, last read live 2026-10-31) stays carried forward unverified. Carried-forward state (not re-verified): Lv.30 batch requeued 2026-11-07 about 17:08 (1d 17h) was due about 10:22 on 2026-11-09; Lv.27 idle and blocked at the 1330 read on 2026-11-09; Lv.24 and the fourth barracks not checked. Tracker untouched, per the partial rule; the next tick re-produces the training regular.
- Quick Dispatch stays untapped: its effect is still unverified and it may march troops out, left for an owner decision or a learn-first exploration unit.
- R2 process failure: this is the fifth consecutive training partial with the same blocker (0039, 1330, 0034, 0337, this unit), each with a changed method and none requeuing a barracks. Per queue rule R2 a fourth identical partial is a process failure, not a result; the 0337 pass already reported it as one and commented the blocker on issue #150. This unit adds its evidence comment to #150 as well. The next unit must use a new grounding route, not another tap on the retired points.
- Figures read live on screen: food 612.5M, iron 939.3M, coin 84.1M, power 148,058,020, diamonds 13.22K at close. Build slot in use: Oil Well (0/1), 1/4 hammer icon. No login or verification was demanded, and no different-device dialog appeared.
- Result stats: target 4, achieved 0, resources_gained none, costs about 3 minutes play, verified yes, blocker_category e, device_takeovers 0.

## What the 2026-11-10 1229 unit added - Lv.24 requeued T8 x666 verified running, Drill Ground Full did NOT block it, R2 five-partial run broken, T8/T10 stats corrected, partial

- Unit training-2026-11-10-1003 by ticker-1204, about 12:29 to 12:33 local, status partial. Evidence in `_records_/2026-11-10/troop-training/1229-queue-run.md` (commit 88e51ae5d on records/2026-11-10).
- Lv.24 barracks: tapping the tent (gold face bubble, norm 374,526) raised the toast "Training complete: 666 Lv.8 units are ready". Total power moved 148,058,020 to 148,765,978, +707,958, exactly 666 times 1,063 (the T8 unit power), so the finished batch counted into power on the tap, with no Drill Ground visit needed.
- TRAIN UNITS panel: Lv.8 preselected as highest unlocked (Lv.9 and Lv.10 padlocked), count slider at the 666 cap, cost 2.9M food and 2.9M iron, duration 1d 04:20:26. Stats read live: Power 1063, Morale 531.25, Squad Load Capacity 1800, Unit HP 3527.4, Unit Attack 28.69, Unit Defense 5.84. Owned counts: Lv.7 715, Lv.8 1,998, Lv.9 1,152, Lv.10 35.8K. Train tapped (blue button, never Finish Now): food 618.9M to 615.9M and iron 941.8M to 938.8M, the 2.9M each charged. Reopened panel reads "Training in progress 1d 04:19:43", counting down, so the batch is running.
- BREAKTHROUGH - the five-consecutive-partial R2 process failure is broken: this is the first barracks requeued since the 0850 unit (0039, 1330, 0034, 0337, 0850 all closed with no requeue). The Drill Ground Full blocker (39,460 of 39,460, last read live 2026-10-31) did NOT block this collection or requeue: no Drill Ground visit was needed, no toast appeared, and the batch is verified running. The standing claim that Drill Ground Full "blocked both collection and requeue" is contradicted by this live requeue and is now qualified - the toast appeared in earlier units, but it did not stop this unit. Whether the Drill Ground is still full is unverified (not re-read live); the clearing method remains unknown, and Quick Dispatch stays untapped (owner decision). Issue #150 commented by this run. See the updated standing blocker.
- Cross-check with the 1224 survivors-unit panel read: that unit read Lv.8 owned 1,332 before this collection; 1,332 + 666 collected = 1,998, matching this unit's Lv.8 owned count exactly. The two records cohere.
- Lv.30 barracks (white-bubble tent): the panel read during the survivors unit showed T10 selected with 1d 17:14:37 on the buttons. That figure is the prospective batch duration, NOT a remaining timer, so whether that barracks is busy or idle is still unverified; the next training unit must read its "Training in progress" line, not the button time. See the new lesson in How it is done.
- T10 panel stats from the same survivors-unit read: Power 1647, Morale 750.0, Squad Load 2200, Unit HP 4726.34, Unit Attack 38.45, Unit Defense 7.79, counts Lv.7 715, Lv.8 1,332, Lv.9 1,152, Lv.10 35.8K, slider 793, cost 5.5M food plus 5.5M iron. See the corrected baseline stats above.
- Not checked: two further barracks unchecked; the four-barracks sweep did not finish inside this unit's window.
- Result stats: target keep all four barracks busy, requeue any idle one at highest tier and cap count; achieved 1 of 4 barracks requeued (Lv.24, T8 x666, verified running); 1 known panel read but state unverified; 2 unchecked; resources_gained 666 Lv.8 units counted (+707,958 power); points 0; costs about 4 minutes, 2.9M food and 2.9M iron for the new batch, no items spent; verified yes (power delta, cost delta and running timer all read live in-unit); blocker_category h (by-design partial - unit window ended mid-sweep).

## What the 2026-11-10 1521 scout read added - Drill Ground level-up to Lv.27, upgrade to Lv.28 available with costs met, Lv.30 reads superseded, partial

- Cross-read, not a training unit: the ticker-1503 perception-scout pass (scout-2026-11-09-1800, about 15:12 to 15:21 local, status partial) observed the Drill Ground level up live. Evidence in `_records_/2026-11-10/perception-scout/1521-queue-run.md` (commit f530c19b7 on records/2026-11-10). Computer session cc-474 on the owner Mac mini.
- Level-up observed 15:13: the "DRILL GROUND LEVEL UP!" celebration surfaced after the scout's first Inventory tap; Power 118,600 to 140,200, Unit Count +7,200 to +7,400; the 24.0M EXP reward card was not tapped. Total power re-read live after dismissal at 148,787,578, confirming +21,600. Building now reads Drill Ground Lv.27.
- CORRECTION - Drill Ground level: this live level-up read supersedes the profile's standing Lv.30 reads (0039 unit on 2026-11-09, re-confirmed by the 0129 arms-race unit) - a building cannot fall from Lv.30 to Lv.27, so those reads are now treated as misidentifications of the structure, not deleted. The 2050 unit's Lv.25 read (2026-11-07, Unit Count +7812) is likewise not reconciled with the +7,200/+7,400 figures here; the Unit Count series (+7812 at Lv.25, +10080 at the Lv.30 read, +7,200 to +7,400 at Lv.26 to 27) does not progress monotonically and is not explained from these reads. The newest verified on-screen figures stand: Drill Ground Lv.27, Power 140,200, Unit Count +7,400. The next training unit re-reads the Drill Ground screen live to confirm.
- Upgrade panel, inspected only by the scout: Lv.27 to 28, Hero EXP 26.0M, Unit Count +7,400 to +7,600, Power 140,200 to 165,800; costs all met (Lv.28 Headquarters, iron 952.1M/102.0M, food 629.3M/314.5M); Original Time 30d 01:27:10, Upgrade button 14d 07:32:57. "Finish Now 33,887" diamonds and "Upgrade" both untouched (red lines) - starting a building upgrade is owner-only, not a training-unit action. No issue filed; the upgrade availability is routed through the scout diff (no building-upgrade regular exists).
- Drill Ground Full state: still unverified - the level-up celebration is not a Full-state read, and the Drill Ground screen was not re-read live in this pass. The 1229 qualification stands (Full did not block the Lv.24 requeue); the clearing method remains unknown, and Quick Dispatch stays untapped (owner decision).
- No barracks was requeued by this read; the Lv.24 batch (requeued 1229, 1d 04:20:26) runs to about 2026-11-11 16:50. The next training unit's standing work is unchanged: read the Lv.30 "Training in progress" line (not the button time), check the two unchecked barracks, re-read the Drill Ground screen live.

## What the 2026-11-10 1649 unit added - no barracks tent located after three pans, blind-pan method retired, partial

- Unit training-2026-11-10-1403 by ticker-1634, about 16:45 to 16:49 local, status partial, unverified. Evidence in `_records_/2026-11-10/troop-training/1649-queue-run.md` (commit 986c1877 on records/2026-11-10). Tracker untouched for partial, per the queue rules.
- Entry: base view at entry shows only the top-left corner of the base; the four barracks tents (lower middle of the base per the activity metadata) are not in frame, and the lower two thirds of the screen are fog. Base HUD read live: power 148,787,578; food 631.3M; iron 954.1M; coin 97.8M; diamonds 6,267; stamina 120; level 30. VS timer 01:13:28 at entry, 01:10:39 at close; Season II 3d 01:23:28; third timer 5d 01:13:28 (meaning unverified).
- Three pans tried, none located a tent: pan 1 down (drag norm 320,700 to 320,250, the 1615 survivors grounding) overshot into full fog; pan 2 right (drag norm 500,500 to 200,500) moved the view only slightly, top edge of the base stayed in frame, no tent appeared; pan 3 right long (drag norm 550,450 to 100,450) overshot past the right edge of the base into fog with a mountain peak at the top. Restore drag (norm 200,450 to 500,450) returned the view to the base's top edge, where the game was left. No TRAIN UNITS panel was opened and no batch was queued. No Finish Now button and no upgrade shortcut were tapped.
- METHOD CHANGE under rule R2: the blind-pan method is retired inside this unit after the three no-locate pans - the drags either barely move the view or overshoot the base edge into fog, and they never land on the tents. The next training unit must re-ground from the 12:29 record's successful entry - read troop-training/1229-queue-run.md for the measured tent point that opened TRAIN UNITS that day - and go straight to that point before any pan. If the tents still cannot be located from that grounding, the blocker is filed as a GitHub issue instead of a third identical partial. See the updated How to enter entry.
- Known state, not re-verified in this unit: Lv.24 barracks - a fresh T8 batch x666 was queued at 12:29 for 1d 04:19:43, so it is still running and is not due for requeue until about 16:49 on 2026-11-11. The 12:29 unit also showed Drill Ground Full did not block that requeue. Lv.30, Lv.27 and the fourth barracks: states unverified; the Lv.30 "1d 17:14:37" seen at 12:24 is a batch duration, not a remaining timer. See the updated How it is done entry.
- Cross-reads: skull badge on the base right edge moved 1 to 4 to 2 with a 00:00:24 to 00:00:52 countdown inside this unit - same-unit evidence that the badge count and countdown change between reads, for Issue #498 (folded in radar-tasks). Toasts seen: "Violet's Gift received!" (the gifts regular owns it) and "Important: President HawksMav appointed..." (truncated, unread).
- Result stats: target check all 4 barracks, requeue any finished batch at its highest tier; achieved 0 barracks checked, 0 batches requeued; resources_gained none; points 0; costs 5min-device-session; verified no (no barracks state read live in this unit); blocker_category e (repeated blocker - barracks tents not located; training units have closed partial on location since the 2026-10-28 to 2026-10-31 queue era).

## What the 2026-11-10 2146 unit added - Lv.27 batch of 313 Lv.9 collected, requeue blocked by Drill Ground Full live toast, tents re-grounded fresh, partial

- Unit training-2026-11-10-1803 by ticker-2122, about 21:37 to 21:46 local, status partial. Evidence in `_records_/2026-11-10/troop-training/2146-queue-run.md` (commit ccb00e883 on records/2026-11-10). Computer session cc-512 on the owner Mac mini. Tracker untouched for partial, per the queue rules.
- Entry - tents located from a fresh grounding, no pans: the game was left on the Alliance Techs screen by the donations unit of this pass. Closed the Techs panel (X) to the Alliance menu, then the back arrow to the base screen. Base screen at entry: food 644.3M, iron 967.4M, coin 105.9M, gold 13.22K, Total Power 148,787,578, stamina 46, diamonds 6,267. VS timer 20:23:46, Season II 2d 20:33:46. The 1649 unit retired the blind-pan method and the 1229 grounding (tent at norm 374,526) no longer matches this camera framing. Two tents were re-grounded fresh from the current screenshot (visual grounding): lower-middle tent bbox 549-688, 533-614 and lower-right tent bbox 653-814, 580-675. No pan was needed. Tapping the lower-middle tent at its centre (618,573) selected it: 'Barracks Lv.27' label with the button row (blue paw, orange pistol, green up arrow - the upgrade shortcut, never tapped). See the How to enter correction above: do NOT go straight to 374,526; re-ground fresh every unit.
- Lv.27 barracks - finished batch collected: tapping the orange pistol button (619,648; bbox 568-670, 615-682) raised the toast 'Training complete: 313 Lv.9 units are ready' and the button row closed without opening TRAIN UNITS. Total Power moved 148,787,578 to 149,210,754 on the tap: +423,176, exactly 313 times 1,352 (the T9 unit power), so the finished batch counted into power on the tap, with no Drill Ground visit needed - the same mechanism the 1229 unit verified for the Lv.24 barracks (666 x 1,063). The Lv.24 barracks batch (T8 x666, queued 12:29 for 1d 04:19:43) is still running and is not due for requeue until about 16:49 on 2026-11-11. The Lv.30 and fourth barracks were not checked in this unit.
- Requeue blocked - Drill Ground Full (live toast): the Lv.27 barracks is now idle. Re-tapping the tent and then the pistol to open TRAIN UNITS instead raised the toast 'Drill Ground Full: Unable to add more units.' and no panel opened. The Drill Ground Full blocker is therefore live in this unit, not inferred: the drill ground cap (39,460 of 39,460 per the retro) blocks the requeue even though the finished batch was collected without a Drill Ground visit. Collection and requeue are decoupled - collecting never needed the Drill Ground, requeueing does. The Drill Ground screen itself was not read live in this unit: the pass budget ended at the toast. The next training unit's first action is to read the Drill Ground screen live - locate the Drill Ground building on the base, open it, and record what controls it actually shows (what a full drill ground offers: deploy, dispatch, dismiss or collect) - and to spend itself on the nearest allowed preparatory action toward clearing it. How a full Drill Ground is cleared is still not known from a live read. See the 1229-update qualification above. Commented on Issue #150 by this run.
- Close: partial. One barracks checked, its finished batch of 313 Lv.9 collected and verified by the exact power delta; its requeue blocked by Drill Ground Full; the other three barracks unchecked (Lv.24 known running from 1229). The tracker stays untouched, so the next tick re-produces the training regular and the work resumes as a fresh unit. No diamonds or money spent. No Finish Now button and no upgrade shortcut tapped. No login or verification demanded. No 'active on a different device' dialog appeared.
- Result stats: target check all 4 barracks, requeue any idle one at its highest tier; achieved 1 of 4 barracks checked (Lv.27); finished batch of 313 Lv.9 collected; requeue blocked by Drill Ground Full; 3 unchecked; resources_gained 313 Lv.9 units counted (+423,176 Total Power); points 0; costs about 9 minutes, no items spent, no food or iron spent (no batch queued); verified yes (power delta 313 x 1352 read live in-unit); blocker_category e; barracks_checked 1, batches_collected 1, units_collected 313, batches_requeued 0, drill_ground_full yes (live toast), power_before 148787578, power_after 149210754.

## What the 2026-11-11 0213 unit added - Lv.30 pistol x2 and paw x1 close the button row with no panel, Drill Ground screen still not read live, fourth consecutive unit on the same blocker, partial

- Unit training-2026-11-10-2203 by ticker-0155, 01:56 to 02:13 local, status partial. Evidence in `_records_/2026-11-11/troop-training/0213-queue-run.md` (commit 72b82b0e3 on records/2026-11-11). Computer session cc-536 on the owner Mac mini. Tracker untouched for partial, per the queue rules.
- Entry: the game was left on the Alliance Techs screen by the donations unit of this pass (Tech Donation Today 2600, Quick Construction 8/10). Closed the Techs panel (X) to the Alliance menu, then the back arrow to the base screen. Base screen at entry: food 666.0M, iron 988.7M, coin 117.4M, gold 13.22K, diamonds 6,287, Total Power 149,218,973, stamina 26, VS timer 16:02:28.
- Lv.30 barracks - two pistol taps, one paw tap, no panel: the four tents were re-grounded fresh from the current screenshot (visual grounding points): (399,815), (523,853), (664,781), (740,726). A first tap at (505,857) selected "Barracks Lv.30" with the button row (blue paw, orange pistol, green up arrow). Pistol tap 1 at (318,885): the button row closed, no TRAIN UNITS panel opened, no toast captured in the screenshot after the tap, Total Power unchanged at 149,218,973. No finished batch collected. A re-tap at (607,857) missed between tents (no selection); re-grounded and re-tapped the tent at (523,853), which selected Lv.30 again. Pistol tap 2 at (318,885): identical outcome - the button row closed, no panel, no toast captured, Total Power still 149,218,973. Per queue rule R2 the pistol method ends for this barracks after two no-change taps. Pivot to the paw button (Building Details): re-selected the tent, tapped the paw at (263,850). The button row closed again with no Details panel opening. No live read of the barracks training timer was obtained from any of the three taps.
- Drill Ground screen - still not read live: the standing instruction from the 2146 unit was that this unit's first action is to read the Drill Ground screen live. That read was not achieved: the Drill Ground building was not located on the base screen in this unit, and the barracks button row - the only entry tried - never opened a panel from which the Drill Ground could be reached. The two pistol taps behaving exactly as the 2146 unit's Drill Ground Full toast case (row closes, no panel) is consistent with the blocker still being live, but the toast itself was not captured live in this unit, so that is an inference, not a live read, and is not claimed as one. The next training unit must locate the Drill Ground building first - by name on the base screen or via a troop overview entry - before tapping any barracks button again. This is the fourth consecutive unit closing on the same blocker (third-strike rule R2 already triggered in 2146); the blocker now needs a changed entry route, not another pistol tap. See the Standing blocker update.
- Other barracks - unchecked: Lv.24: not checked in this unit; known running from the 1229 unit, due for requeue about 16:49 on 2026-11-11. Lv.27: not checked; its batch was collected at 21:46 on 2026-11-10 and its requeue was blocked by Drill Ground Full then. Fourth barracks: not checked. Side observation during this unit: a "Boarding closes in" banner appeared at the top of the base screen (00:02:51 at first sight, 00:02:38 at the paw tap) - the alliance train is boarding now. That is the train regular's work, not this unit's; it is noted here so the next unit in this pass can pick the train unit up.
- Close: partial. One barracks checked (Lv.30); no batch collected, no batch requeued, no TRAIN UNITS or Details panel opened, Drill Ground screen not read live. The tracker stays untouched, so the next tick re-produces the training regular and the work resumes as a fresh unit. No diamonds or money spent. No Finish Now button and no upgrade shortcut tapped. No login or verification demanded. No "active on a different device" dialog appeared. The game was left on the base screen.
- Result stats: target check all 4 barracks, requeue any idle one at its highest tier; achieved 1 of 4 barracks checked (Lv.30); no batch collected; no batch requeued; Drill Ground screen not read live; resources_gained none; points 0; costs about 17 minutes, no items spent, no food or iron spent (no batch queued); verified yes (power 149,218,973 read live before and after; no change); blocker_category e; barracks_checked 1, batches_collected 0, batches_requeued 0, drill_ground_full inferred-not-read, drill_ground_screen_read no, power_before 149218973, power_after 149218973, train_boarding_seen yes (closes 00:02:51 at first sight), device_takeovers 0.

## What the 2026-11-11 0548 unit added - Lv.24 barracks busy 11:01:26, 1 of 4 checked, Drill Ground live read not done, radar-entrance wrong turn, partial

- Unit training-2026-11-11-0203 by ticker-0534, about 05:48 to 05:52 local, status partial. Evidence in `_records_/2026-11-11/troop-training/0548-queue-run.md` (commit a3ef6b276 on records/2026-11-11). Computer session cc-565 on the owner Mac mini.
- Entry: the game was left on the Alliance Techs panel by the donations unit of this pass. Closed the Techs panel (X) to the Alliance menu, then the back arrow to the base screen.
- Wrong turn, recorded: tapping the tent at norm (763,584) opened the radar world map (12 Radar Tasks to restore in 05:49:38, 1/40 stored, Quick Execute offered) instead of a barracks. No radar action was taken - this unit is training only - and the Home button returned to base. That structure is the radar entrance in this framing, not a barracks tent. The 2146 grounding (tent at norm 374,526 / 618,573) no longer matches this camera framing; tents must be re-grounded fresh every unit. See the updated Entry entry.
- One barracks checked: tapping the tent at norm (864,610) opened TRAIN UNITS for the Lv.24 barracks - T8 selected (Power 1063, Morale 531.25, Squad Load Capacity 1800, Unit HP 3527.4, Unit Attack 28.69, Unit Defense 5.84; Lv.9 and Lv.10 locked). Current batch Lv.8 x666, "Training in progress 11:01:26" - busy until about 16:58 today, no action possible. The Speed Up button was not tapped (red line). This matches the 2146 note (queued 12:29 for 1d 04:19:43).
- Not done - stated plainly: the other three barracks were not checked. The Lv.27 barracks was idle and requeue-blocked by Drill Ground Full at 21:46 yesterday (unit 2146); its state today is unverified - carried, not re-read. The Drill Ground live read that unit 2146 assigned as this unit's first action did NOT happen: the pass budget ended at the Lv.24 panel. How a full Drill Ground is cleared is still unknown from a live read. The next training unit's first action remains: locate the Drill Ground building on the base, open it, and record what controls it actually shows (deploy, dispatch, dismiss, collect). See the updated Standing blocker entry.
- Grounding-tool warning: the visual grounding tool returned two boxes for both "Drill Ground" and "barracks tent" (553-652, 638-710 and 658-781, 688-758) without distinguishing them; those boxes do not match the tents visible in this framing and were not used as tap points. Grounding points must be verified against the live screenshot, not trusted blindly.
- Correction (appended 05:53, same pass): the duration stated in the record is withdrawn - the unit ran about 4 minutes (claimed 05:48:15, completed 05:52:27), not "about 12 minutes", and the window was 05:48-05:52 PT, not 05:48-06:00. Durations are read from the tool timestamps, never estimated from perceived effort - the second wall-time misjudgement in this pass (the donations 0541 record needed the same correction).
- Close: partial. 1 of 4 barracks checked (Lv.24, busy); no batch collected, no batch queued, no resources spent. The tracker stays untouched, so the next tick re-produces the training regular and the work resumes as a fresh unit.
- Result stats: target check all 4 barracks, requeue any idle one at its highest tier; achieved 1 of 4 barracks checked (Lv.24, T8 x666, 11:01:26 remaining, busy); 3 unchecked; Drill Ground live read not done; resources_gained none; points 0; costs about 4 minutes; verified yes (Lv.24 panel read live in-unit; the Lv.27 and Drill Ground states are carried from 2146, not re-read); blocker_category e; barracks_checked 1, batches_collected 0, batches_requeued 0, drill_ground_read no, device_takeovers 0.
- No diamonds or money spent. No Finish Now button and no upgrade shortcut tapped. No login or verification demanded. No "active on a different device" dialog appeared.
