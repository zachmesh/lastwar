---
title: Survivor Intake Queue Run
created: 2026-11-05T01:07:00Z
modified: 2026-11-05T01:07:00Z
---

# Survivor intake, ticker-1704, 17:04 to 17:07 local

Unit survivors-2026-11-04-1403, status failed. No survivor was
recruited, no card was opened, Quick Dispatch did not run, and
the regulars tracker is untouched.

## What was verified live

- The Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd) was
  online and the LastWar window was running fullscreen
  (pid 59735, 1920x1080, window "Last War").
- Every screen-capture attempt failed with the same device-channel
  error: "Failed to start stream due to audio/video capture
  failure". Five attempts across two computer sessions
  (cc-471: activate, observe, activate again; cc-472: activate,
  observe in image mode), all with the same error.
- No blind taps were made: without a single screenshot the gate
  line could not be grounded, so no game input was sent and no
  game state was changed.

## Blocker

- This is the device-channel fault already tracked as GitHub
  Issue #284 (Mac screen capture failure blocks ticker passes),
  not a tap failure, not a game-state blocker, and not a
  red-line miss. The ticker-1704 pass commented Issue #284
  with this pass's evidence (comment 6646759476).
- Counting from the records branch day INDEX, the ticker-1634
  pass was the ninth consecutive ticker pass to fail this way,
  so this pass is the tenth consecutive capture-failure pass.
- The pass stopped after this unit rather than failing further
  units identically: every further unit needs the same capture
  channel, so repeating the attempt across more units would only
  add failed units, not progress. The next pass should retry
  capture first; if it recovers, the survivors unit is
  re-produced by the tracker as a fresh unit (tracker untouched).

## Pass-level notes (ticker-1704)

- Own PRs checked first: open records PRs 286 (2026-11-04),
  265 (2026-11-02), 256 (2026-11-03) and 187 (2026-11-01) all
  name Owner lastwar-pr-integrator, none names this job, and
  PR 286 carries no comments, so nothing was owed on them.
- Sync reaped nothing and produced nothing new - all due
  regulars were already queued (21 due, all already_queued).
- Zombie Invasion was not seeded: the chain zombie-2026-10-28
  closed with unit 066 on 2026-10-30, the Events hub has no
  Zombie Invasion tab since, and the activity metadata forbids
  seeding a fresh chain until such a tab is seen live again.
- No diamonds, money, price tags, paid buttons, speedups,
  research, buildings, assembly or teleport were touched.
  Nothing was claimed.
