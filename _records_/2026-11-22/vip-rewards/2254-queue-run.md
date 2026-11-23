---
title: VIP rewards queue run 2254
created: 2026-11-23T06:57:00Z
modified: 2026-11-23T06:57:00Z
version: 1.0.0
description: VIP unit vip-2026-11-22-1800 attempt 2, operator seat, VIP screen read live, Daily Freebie and login chest already taken this reset day, nothing to claim
status: run-done
grounded_in:
  - source: cu_bridge start, status poll and final result on run 20261123T065437Z-d05263, 2026-11-23T06:54Z
  - source: run screenshots step-0002.png and the closing frame under /Users/zhenchen/.computer-use/runs/20261123T065437Z-d05263, final frame saved as _tools_/state/cu_vip_2255.png
  - source: lsappinfo front reading before the start, 2026-11-23T06:54:37Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T06:54:37Z
---

# VIP rewards queue run 2254

- Unit vip-2026-11-22-1800, operator seat, assignment A-20261123-0654-operator,
  attempt 2 of 3. Attempt 1 was the blocked run in
  [2234-queue-run.md](2234-queue-run.md). Measured rows are in the sidecar
  [2254-queue-run-detail.md](2254-queue-run-detail.md).
- Status: done, checked only. The VIP screen was opened and read live, and nothing
  was claimable.
- Run `20261123T065437Z-d05263`, model `claude-gateway/claude-sonnet-5-5`,
  max-steps 8, ended `completed` after 5 steps. Actions done 8, refused 0, failed 0,
  one tap per turn. Model time 4.81 s per step. Cost 0.070903 USD. No local-input
  takeover.
- Front precondition held: `killall -9 UserNotificationCenter NotificationCenter`
  in the same shell, then `lsappinfo front` named the game. The first frame was the base,
  with no account-elsewhere dialog, no boarding banner and no loading screen.
- Route: the avatar opened MY PROFILE, the gold VIP badge opened the VIP screen, and
  the back arrow and the profile's X returned to the base.
- Daily Freebie: the button shows a greyed countdown, not Claim. The countdown ends at
  the 02:00Z reset, so the freebie was already taken this reset day, not by this seat.
- Login chest: the chest icon at the top right carries no red dot, so the day's login
  points are already taken.
- VIP level 13, with the points bar and the login streak in the sidecar. The streak
  line reads five days, which is far below the streak the profile recorded earlier.
  That is a measured reading and it is not explained here.
- The only red dot on the screen sits on the shop cart. It is a purchase surface and was
  not touched. The paid VIP exclusive offer was not touched either.
- Closing state: the base screen.
- Confirm: not needed. The account-elsewhere dialog did not appear.
- Red lines held: no purchase, no diamonds, no speedup, no diplomacy, the mid-base
  trophy bubble not tapped.
- Follow-up: none owed. The next freebie unlocks at the 02:00Z reset.
