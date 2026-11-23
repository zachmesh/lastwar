---
title: Radar queue run 2000
created: 2026-11-23T04:06:00Z
modified: 2026-11-23T04:06:00Z
version: 1.0.0
description: Radar unit radar-2026-11-22-1803, operator seat, second consecutive run blocked by the desktop frontmost gate
status: run-failure
grounded_in:
  - source: cu_bridge start, status and control on run 20261123T040058Z-74e835, 2026-11-23T04:00Z to 04:02Z
  - source: run trajectory events.jsonl and screenshot step-0001.png under /Users/zhenchen/.computer-use/runs/20261123T040058Z-74e835
  - source: lsappinfo front and lsappinfo list readings, 2026-11-23T03:5xZ and 04:05Z
  - source: queue.py version, token-acquire and claim on the live pool, 2026-11-23T03:59Z to 04:01Z
---

# Radar queue run 2000

- Executor: operator seat, unit radar-2026-11-22-1803, priority 2, window
  label "duel day 7 - radar stack" (minted 18:03 PT; the live posture rolled
  to duel day 1 Radar Training release before this unit ran - see below).
  Token held 04:15:52Z lease, claim lease 04:20:53Z.
- Status: failed. Zero game input dispatched, zero claims, zero tasks
  executed. Second consecutive operator run blocked before any click landed.
- Run: `20261123T040058Z-74e835`, desktop, apps `com.lastwar.ios`,
  max-steps 20, max-minutes 15, max-cost 1.0 USD. Started 04:00:58Z, ended
  04:01:58Z. Steps 2, actions done 1 (a screenshot) / skipped 3 / blocked 0,
  cost 0.060881 USD. View URL at start
  `http://127.0.0.1:62539/?token=2a0444e230a592571d98130b87bd6084` (human-only
  control link, now closed).
- What blocked it, measured from the run's own events:
  - Step 0 and step 1 observations both carried url
    `app:com.apple.UserNotificationCenter`, not `com.lastwar.ios`.
  - Step 2 planned a left click at screen (106,713), the model's grounded
    radar-dish point, with its note "Radar dish icon is at ~(106, 713).
    Stamina before: 120." The action record: decision `handoff`, rule
    `excluded_front:os_security`, app `com.apple.UserNotificationCenter`,
    target `{"origin": "com.lastwar.ios", "role": "AXGenericElement"}`,
    status `skipped`, attempted false, completed false. The click
    hit-tested into the GAME window at that point and was still refused
    because a system surface held the front slot.
  - The run ended itself at 04:01:58Z (`cancelled`); I sent no input and
    did not start a second run.
- The screen itself is clear. Run screenshot step-0001.png (1920x1080) shows
  only the Last War window (about 64,32 to 634,992) on a black desktop - no
  dialog, banner or notification is visible over the game. The base view is
  live: food 732.3M, iron 1.1G, gold 35.3M, diamonds 8,336, power 150,080,120,
  stamina 120, builders 0/4, research 2/2, harvest bubbles standing
  uncollected, Warriors Duel timer 21:58:58.
- Foreground readings, the finding of this unit:
  - `lsappinfo front` at about 03:59Z returned the ASN of `LastWar`
    (`0x0-0x1486e85a`), which is what the coordinator's check saw.
  - `lsappinfo front` again at 04:05Z returned `ASN:0x0-0x147126fe`, and
    `lsappinfo list` names that process `UserNotificationCenter`
    (`com.apple.UserNotificationCenter`, `/System/Library/CoreServices/...`)
    marked `(in front)`, checked in 2026-11-17 03:37, i.e. resident for over
    five days and taking the front slot intermittently.
  - So the front slot flipped away from LastWar within about a minute of the
    check, and the computer-use policy's `excluded_front:os_security` rule
    then refuses every click on the desktop - even when the click point
    resolves into the game window - for as long as that process holds front.
- Live posture check, same unit: `_tools_/duel.py` reports "Alliance Duel -
  Day 1: Radar Training (win points 1, ends 2026-11-23T18:00:00-08:00)" and
  "RADAR: release day - complete and claim everything, early in the day."
  The unit's window label says day 7 stack, which is the label it was minted
  with - stale. The live posture is release, so claiming would have been
  correct today; the unit never got the chance.
- What the next attempt needs, in order: Last War frontmost AND
  UserNotificationCenter not holding the front slot at the moment the run
  clicks (a one-shot `killall NotificationCenter` immediately before the
  start, or Focus/Do Not Disturb on, or an owner-side fix to the policy so
  `excluded_front` is judged on the click's hit-test target rather than the
  global front app). Re-checking `lsappinfo front` once is not enough - it
  flips.
- Disclosure: at about 03:5xZ, before this unit, I ran one
  `osascript -e 'tell application "System Events" to get name of first
  application process whose frontmost is true'` to confirm the front app. It
  hung and I killed it. If that raised a macOS Automation consent prompt, the
  prompt is itself an os_security surface and would explain the
  `excluded_front:os_security` refusal; the owner should look for a pending
  "Terminal wants to control System Events" dialog. I did not run osascript
  again after that.
- No diamonds or money spent, no paid offer opened, no pin tapped, no rally,
  march or attack, no alliance diplomacy.
- Tracker: not touched (the unit was re-produced by the next sync).
- Follow-up: report the front app and the `excluded_front` mechanism to the
  coordinator; do not retry this unit until the front slot is verified clear
  immediately before the start.

## Correction, same pass

- The unit closed with `verified: yes`. That means the failure itself was
  confirmed on evidence (the run's `handoff` action record, the frontmost
  readings and the run screenshot), NOT that any collection or claim was
  observed. No reward, task or resource was verified as collected in this
  unit.
