---
title: Test T3 focus incident 1528
created: 2026-11-23T15:33:00Z
modified: 2026-11-23T15:33:00Z
version: 1.0.0
description: Addendum to the T3 record 1511 - the one click on the check-in Go took the front from LastWar for 8 minutes 11 seconds (Chrome, then a notification dialog, then Chrome again); timeline to the millisecond where the sources allow, the front log, the consent request text and the recovery; finding Go does not pay in game, digest rule 9 supported
status: done
grounded_in:
  - source: cu_bridge run 20261123T151100Z-91131b events (clicks, consent request and answer) and frame step-0002
  - source: a front-app log (1 s resolution, 360 samples 15:11:00Z to 15:14:17Z) and hand polling to 15:19:29Z
  - source: coordinator rulings of 15:13Z and 15:19Z and the standing rule of 15:28Z
---

# Test T3 focus incident

Timeline rows in [1528-t3-focus-incident.csv](1528-t3-focus-incident.csv). This is a new entry beside [1511-queue-run.md](1511-queue-run.md), which stays as written; the unit was closed there as `skipped-needs-owner` because focus had not returned.

- **Finding (closes T3).** Go does **not** pay in game. One click at **15:11:14.951Z** (attempted 15:11:14.843Z) moved the banner to its second slide ("Claim points and redeem great rewards", POINTS 1000) and brought **Google Chrome** to the front: digest rule 9 is **supported** by one click. No reward popup, Claimed state or counter change. **The Go button must never be clicked again.**
- **Focus theft.** The front log reads LastWar to 15:11:14 and Chrome from 15:11:15: a switch within 1.05 s of the click (the log has one-second resolution, so no finer bound). LastWar was not frontmost for 8 min 11 s, until 15:19:26Z: Chrome 15:11:15 to at least 15:17:12, a notification dialog from 15:17:22 to at least 15:19:02, Chrome again at 15:19:24. The Chrome page was never looked at or touched.
- **Consent request.** At **15:11:20.718Z**, raised by the run's own `wait` action: class `new_app`, rule `app:not_approved`, "use com.google.Chrome, an app this run has no approval for (frontmost)". The seat did **not** answer it; the stop of the run at **15:11:50.714Z** recorded `approved: false, answeredBy: stop`. Consent stays human-only.
- **Side effect.** From 15:17:22Z `UserNotificationCenter` held the front until at least 15:19:02Z (sampled every 10 s; its content was not looked at and no input was sent).
- **Recovery.** On the coordinator's word: the standard `killall` of the notification apps and `_tools_/mac_lastwar_front.sh` at about 15:19:24Z (exit 0; it activates the game window, no tap anywhere); LastWar frontmost by 15:19:26Z and it held through the next unit. Chrome and its page were left open for the owner.
- **Cost.** The test run cost 0.034873 USD; nothing was spent or bought. T3 ran as assigned with its brief's stop rules followed; the standing rule of 15:28Z (approval and an exit plan before any test that may open another app) postdates it.
