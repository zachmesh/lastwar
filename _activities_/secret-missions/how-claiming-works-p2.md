---
title: How claiming works part 2
created: 2026-11-23T07:15:45Z
modified: 2026-11-23T07:15:45Z
version: 0.1.0
sequence: 7
description: Blocker status, R2 metadata write 2026-11-04 0847 (third consecutive Claim-blocker partial - 0248, 0545, 0847) -
---
- Blocker status, R2 metadata write 2026-11-04 0847 (third consecutive Claim-blocker partial: 0248, 0545, 0847): the Claim buttons have now failed in three consecutive units, so under queue rule R2 as corrected in the 0545 section this blocker is written into the activity metadata here, the entry route changes before any further unit of this type runs, and the streak is named in that day's round summary. Entry-route change owed: attempt a genuine foreground activation (Dock or app-icon activation) before any Claim tap - background taps failed in all three units, and a true foreground tap was never actually achieved (the 0545 title-bar click did not raise the window; click_foreground is unavailable for this game). A fourth identical partial is a process failure reported to the owner. (2026-11-08 1114 update: the blocker is discharged in practice - the Claim tap worked on the first try and collected all four finished tasks at once; see the 1114 section. No genuine foreground activation is recorded in that unit, so the foreground hypothesis stays untested and the session-dependence note stands - buttons responded here as they did in session cc-441 per the 0914 daily-missions unit. The entry-route change this blocker owed is moot for now; if Claim buttons fail again, the R2 sequence restarts from the first partial.)
  (2026-11-22 0244 update: the blocker RECURRED - occurrence 1
  of a new streak. Five variants tried, all verified no-change
  by screenshot: single tap Claim 1, single tap Claim 2,
  1-second long-press, exit + fresh re-entry, and a genuine
  foreground raise (raise=true, brought_to_front true) plus
  double-tap. The 2026-11-04 hypothesis that background taps
  were the cause is now TESTED and DISCHARGED - the window was
  raised to the front and the Claim buttons still did not
  respond. Follow-up per R2: the next unit changes method; a
  2nd consecutive failure files a GitHub Issue (play); a 3rd
  writes the blocker into the activity metadata. Candidate
  next methods: the Claim button via its OCR/click_element
  route, the task row first to open its detail card and claim
  from there, or a fresh computer session. The two finished UR
  tasks (Rescue Test Subject, Capture the Oil Depot) stayed
  unclaimed. The 1104 unit the same morning claimed both
  finished UR tasks with one tap, so the streak stands at 1
  occurrence, not 2 - no Issue filed.)
- Morning batch claimed - UR Rescue Officer, UR Rescue Missing
  Agent, SSR Search for Missing Refugees, SSR Protect Refugee Camp.
  Rewards included Treasure Map Fragments number 7, 4 and 1, a full
  Treasure Map, a Resource Chest, Upgrade Ore and a 5 minute
  Research Speed-up.
