---
title: Survivor intake queue run 2003
created: 2026-11-23T04:06:30Z
modified: 2026-11-23T04:06:30Z
version: 1.0.0
description: Survivor unit survivors-2026-11-22-1803, operator seat, first landed computer-use play unit after the front-slot fix
status: run-done
grounded_in:
  - source: cu_bridge start, status polls and final result on run 20261123T040352Z-ef05dc, 2026-11-23T04:03Z to 04:05Z
  - source: run trajectory events.jsonl and final screenshot step-0005.png under /Users/zhenchen/.computer-use/runs/20261123T040352Z-ef05dc
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:03:52Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:03Z
---

# Survivor intake queue run 2003

- Executor: operator seat, unit survivors-2026-11-22-1803, est 3 minutes,
  token lease 04:18:52Z, claim lease 04:23:52Z.
- Status: done. This is the first operator unit whose clicks actually landed -
  the front-slot blocker measured in the 1955 and 2000 units is cleared.
- Run: `20261123T040352Z-ef05dc`, desktop, apps `com.lastwar.ios`,
  max-steps 20, max-minutes 15, max-cost 1.0 USD. Started 04:03:52Z, ended
  04:04:44Z (51.7 s active). Steps 6, actions done 17, refused 0, blocked 0,
  skipped 0, handed_off 0. Cost 0.133481 USD.
- Front precondition, the check that made the difference: `killall -9
  UserNotificationCenter NotificationCenter` in the same shell immediately
  before the start, then `lsappinfo front` named `"LastWar" ... (in front)`.
  Every landed action's effect carried `frontmostBundleId: com.lastwar.ios`;
  no `excluded_front:os_security` and no `excluded:terminal` refusal occurred.
- Gate (Zombies-signed entrance, left edge of the base): one white "?" bubble
  was present. A single tap at about (146,649) was dispatched and landed.
  Observed after the tap: the "?" became a short speech bubble reading
  "welcome", and the figure under it was no longer visible in the next
  screenshot. NO recruit card appeared, so per rule R1 this is an intake
  PROCESSED but UNVERIFIED in detail - there is no name and no role, and it is
  not counted as a recruit.
- Incidental side effect, disclosed: the first tap meant for the iron mine
  body landed on a standing iron bubble and collected it - the run reports
  pop-ups of about +44K to +54K per mine. That is harvest output, not part of
  this activity; the harvest regular still owns the rest of the bubbles.
- Building panel: second tap on the iron-mine body opened the radial menu, the
  blue paw icon opened Building Details. Read live on the final screenshot:
  IRON MINE Lv.27, Output/hr +110681, Max Production Time 11hr 36min,
  Survivors Charles, Jolene, Alyssa, Harry - all Miner, 4 posts.
  Roster drift against the 0932 unit's read (Christopher, Elina, Alyssa,
  Jolene): Charles and Harry are new here, Christopher and Elina are gone. The
  roster is not static across units; the next unit re-reads it rather than
  assuming either list.
- Quick Dispatch: tapped ONCE. Verified effect - a toast appeared at the top of
  the panel, "There are no survivors available for dispatch right now.", and
  the four Miner posts were unchanged on the re-read. This is the first
  verified Quick Dispatch effect recorded in the recent lineage: the 0932
  unit's tap was unverified, this one is not.
- Verification: the Quick Dispatch result is verified by the toast and the
  unchanged post list on the final screenshot. The gate-clear state is NOT
  verified - the unit closed with the Iron Mine panel open and the gate area
  only partly in frame, so "gate clear" is an inference, not a read.
- Red lines: no diamonds, no money, no purchase, no attack, rally or march, no
  alliance diplomacy, no speedup, no map pin tapped. HUD at close unchanged
  against the entry read - food 732.3M, iron 1.1G, gold 35.3M, diamonds 8,336.
- Record of the process: the front-slot fix is what unblocked play. Two
  previous units (harvest 1955, radar 2000) burned leases with zero clicks
  for want of it.
- Tracker: done unit, regular satisfied for this window.
