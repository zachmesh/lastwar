---
title: Alliance train queue run 2034
created: 2026-11-23T04:36:00Z
modified: 2026-11-23T04:36:00Z
version: 1.0.0
description: Alliance train unit train-2026-11-22-1830, operator seat, both preparation signals absent on the base screen, no train preparing, nothing tapped, checked only
status: run-partial
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T043412Z-f41a23, 2026-11-23T04:34Z
  - source: run screenshot step-0000.png under /Users/zhenchen/.computer-use/runs/20261123T043412Z-f41a23, the only observation of the run, final frame saved as _tools_/state/cu_train_2034.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:34:12Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:34:12Z
  - source: _activities_/alliance-train/INDEX.md, preparation signals and the Limits section, read before acting
---

# Alliance train queue run 2034

- Executor: operator seat (top-level session), unit train-2026-11-22-1830,
  assignment A-20261123-0433-operator. Token lease 04:49:12Z, claim lease
  04:54:12Z, attempts 1.
- Status: partial, checked only. No train was preparing, so there was nothing to
  read on the station platform and nothing to board. This is the same close as
  the profile's earlier no-train units.
- Run: `20261123T043412Z-f41a23`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:34:13Z, ended 04:34:19Z with status `completed`. Active
  5.7 s, model time 5.2 s. Steps 1, so 5.18 s of model time per step. Actions
  done 0, refused 0, blocked 0, failed 0. Cost 0.016142 USD.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. There was no local-input takeover.
- Preparation signals, read on step-0000.png, the base screen at entry:
  - No "Boarding closes in HH:MM:SS" banner under the resource bar. The strip
    there is the scrolling news line ("... dug up 2 Golden Mobile Squad with the
    treasure map - congrats!"), which the profile names as not the banner.
  - No locomotive icon in the left column. The column holds hammer 0/4, flask
    2/2, the blue Trucks circle with badge 3, a vehicle icon with badge 9,
    radar with badge 4 and a wrench with badge 1. The Trucks circle is not the
    train per the profile, and nothing in the column was tapped.
- Per the profile's preparation-only rule, the unit stopped at the signals: no
  pan, no drag, no ground tap, no station platform visit. The run made no input
  at all.
- Caveat, the same one the earlier units carry: this is a banner and column
  check, not a station-panel verification. A preparing train is neither
  confirmed nor ruled out beyond the absent signals. The base-edge pan that
  would show the station was not used, because the profile retires it.
- Boarding rule not exercised. The standing owner instruction (carriage 2, 3
  Trade Contracts, a gift to the conductor) was not tested here. For this
  assignment the unit was limited to free steps with no send, so the run was
  told to read the platform and stop without tapping any plus if a train had
  been boarding. That limit was never reached. If a boarding train shows up, the
  coordinator should say whether the 3-contract ticket applies, because the
  gift dialog does not reopen once closed.
- Closing frame: the base screen, unchanged. HUD: food 732.3M, iron 1.1G, coin
  35.3M, diamonds 8,336, power 150,080,120.
- Red lines: no speedup, no diamonds, no purchase, no send, no diplomacy, no
  Trade Contracts spent, no train summoned, no conductor role taken.
- Follow-up: the next train unit is train-2026-11-23-0230, not before
  2026-11-23T10:30:00Z. Boarding windows are short, so a train can appear and
  close between units. The banner is the signal to act on.

## Addendum 2026-11-23T04:36Z - coordinator ruling on the boarding question

The coordinator answered the question in the NEXT line, citing the profile's
lines 120 to 124. The standing owner instruction of 2026-10-25 applies whenever a
train is boarding: always carriage 2, always 3 Trade Contracts for the ticket in
the THANK THE CONDUCTOR dialog, autonomously. "Free steps only" in that
assignment meant no diamonds, premium currency or purchases, and Trade Contracts
are not those. The rules that stay: skip the cinematic with a single tap and a
fresh observation, never a blind double-tap; verify carriage 2 before tapping its
plus; set the slider to 3, read it back, then tap Gift Contract; the dialog does
not reopen once closed. No train preparing means no action. This changes no
result of the 2034 run, which found no train. A later train unit under this
operator follows the ruling.
