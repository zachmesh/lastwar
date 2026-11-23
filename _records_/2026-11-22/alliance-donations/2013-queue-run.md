---
title: Alliance donations queue run 2013
created: 2026-11-23T04:17:00Z
modified: 2026-11-23T04:17:00Z
version: 1.0.0
description: Donations unit donations-2026-11-22-1803, stopped by coordinator order after local input from a Screen Sharing viewer
status: run-failure
grounded_in:
  - source: cu_bridge status and control stop on run 20261123T041338Z-3b2b98, 2026-11-23T04:15Z
  - source: run trajectory events.jsonl and final screenshot step-0003.png under /Users/zhenchen/.computer-use/runs/20261123T041338Z-3b2b98
  - source: queue claimed pool reads and the device-token lease file, 2026-11-23T04:13Z and 04:16Z
---

# Alliance donations queue run 2013

- Executor: operator seat, unit donations-2026-11-22-1803, est 7 minutes,
  attempts 1, token and claim lease both taken at 04:13:17Z.
- Status: partial, and stopped on the coordinator's instruction. Local input
  from a Screen Sharing viewer was being delivered to this Mac, so the run was
  paused at step 3 and could not be trusted to act where the executor intended.
- Run: `20261123T041338Z-3b2b98`, desktop, apps `com.lastwar.ios`,
  model `model-a`. Started 04:13:39Z, stopped 04:15:06Z (15.1 s active,
  10.5 s model). Steps 3, actions done 6, failed 1, skipped 2, refused 0,
  blocked 0. Cost 0.081707 USD.
- What the run actually did, from its trajectory: three planned clicks at
  (606,252), (669,708) and (513,676), each with a 1-2 s wait and a screenshot.
  The first two landed (`frontmostBundleId: com.lastwar.ios`); the third
  recorded `failed` with no effect, and the run then sat at step 3 until I
  stopped it.
- Screen state at close (final screenshot step-0003.png): the ALLIANCE hub,
  `[tag] the owner alliance`, overall rating 5.0, leader Abjss the owner alliance, power
  14,645,705,598, members 99/100, with red dots on Help, Gifts, Store, Techs
  and Events. The Alliance Techs donation tree was never opened, so the
  Donation Count was NEVER read and no donation is claimed.
- Result: 0 donations. No count delta, no Tech Donation Today footer read, no
  cooldown timer observed. Nothing to attribute.
- Cause, as measured: the Mac's pointer was being driven from an observer's
  Screen Sharing viewer, which delivers the viewer's mouse moves as local
  input to this machine. From inside a run that is indistinguishable from the
  owner using the Mac, so the run paused and any further clicks would have
  gone wherever the remote pointer was, not to the grounded point.
- Blocker category: recorded `e` (repeated blocker). The coordinator asked for
  `c`, but in `_tools_/queue.py` (mirroring the design doc) `c` is the tap
  method class; the cause here is not the tap method. This is the third
  desktop-input interference event in the hour - `excluded:terminal` (iTerm2
  in front) on the 1955 harvest unit, `excluded_front:os_security`
  (UserNotificationCenter) on the 2000 radar unit, and now remote local input -
  so `e` fits; `f` (missing precondition) is the alternative reading, since
  the missing precondition was exclusive operator input.
- Model baseline for the comparison the coordinator asked for: this run's
  model was `model-a`, 3.51 s of model time per step and 0.0272 USD per step
  (0.081707 USD / 3 steps). The 2003 survivors run on the same model was
  5.90 s and 0.0223 USD per step (0.133481 USD / 6 steps). The next run is to
  carry `--model claude-gateway/claude-sonnet-5-5` (or a local alias if that id
  is refused) with `--max-steps 8`.
- Not retired: no further run started, per instruction, until the owner
  switches Screen Sharing to View Only or uses the watch-only URL. The token
  was released at close and the unit handed back to the queue.
- Red lines: nothing purchased, no diamonds, no attack, no diplomacy action
  beyond opening the Alliance hub, no pin tapped.
