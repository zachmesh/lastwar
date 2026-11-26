---
title: Handover to the new harness
created: 2026-11-26T20:29:20Z
modified: 2026-11-26T20:44:32Z
version: 0.2.0
description: State of the game and the team at the owner's stop order of 2026-11-26T20:26Z, the standing rulings, the open owner items, the schedules that existed and how to restart them - counts only, no identifiers
---

# Handover to the new harness

Scribe, at the owner's stop order, 2026-11-26 20:30Z, edited 20:45Z. Nothing runs. Live state after 17:40Z: the Coordinator's [handover](../coordinator/handover.md). Measured state and schedule names: [state rows](new-harness-state.csv).

## Standing rules (Steer A)

- Different-device dialog: one tap on its exact text; a return within 30 minutes doubles the wait before the next Confirm (2, 4, 8 hours); a 2-hour hold resets it.
- Promotion (Lv.27 barracks, Lv.8 to Lv.9, 726 a batch, 887.6K food and iron, no coin): each visit with the queue row idle, food at least 35M, iron at least 150M, start the next batch whether or not the last return fitted; if the full ground blocked it, collect at the Lv.27 tent's pistol right after the new Promote press; the last batch is 237, the Lv.7 troops follow after a cost read; Promote only, never Finish Now; no disband without the owner's word.
- Room conveyor: after a batch start frees places, plain collects by power per place: Lv.30 pistol, Hospital Collect, Lv.27 tent pistol, Lv.24, Lv.20; stop at the "Drill Ground Full" toast; read total power and the Lv.7 to Lv.10 counts before and after each; read the Hospital free room before the siege (it wounds 1,000 about one night in three; wounded beyond the free room die).
- Help: press the white round helmet bubble over an upgrading building once right after every build start (alliance help; 30 helps cut about 14 percent, a flat 21.6 minutes each under 2.99 days left).
- Floors: HQ 31 coin bill about 2.15B (the Researcher's); the R5 choice-chest reserve stays untouched without the owner's word; before every build press drag the cost list and check iron 100M, food 30M, coin 10M against all three costs; an unseen row means no press.
- Front and windows: another app in front, nobody at the Mac (idle 300 s or more), not a consent window: `bash _tools_/mac_lastwar_front.sh` once, front recorded before and after, nothing touched; a repeat within 10 minutes: stop. UserNotificationCenter: one `killall -9` per window (the owner's own step); first read `pgrep -f 'Python.app'` and ps names only; kill one python only if a hung session-inbox.py over 60 s, never the DSH host, bridge daemon or release-watch. Apple Follow Up notice: the front script, never a kill. We never answer a consent window; the owner does (Python and a protected folder: Don't Allow; cu helper and Screen Recording: Allow).
- Red lines: no purchases, no PvP beyond truck plunder, never Go on the check-in banner, diamonds never spent.

## Open owner items

Board option rename; a home-folder-glob line for the owner's agent rules; the upstream roster fix; the owner's A, B or C choice (OD-20261126-02); the zombie siege of 2026-11-27T01:15Z, never cancelled.

## Restart

Recreate the scheduled wakes in the new scheduler, each prompt pointing at the seat's duties page; read `AGENTS.md` and each seat's handover first.
