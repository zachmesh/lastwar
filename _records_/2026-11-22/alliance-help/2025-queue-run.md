---
title: Alliance help queue run 2025
created: 2026-11-23T04:27:30Z
modified: 2026-11-23T04:27:30Z
version: 1.0.0
description: Alliance help unit help-2026-11-22-1830, operator seat, Help All pressed once, two ally requests cleared, header 280 to 320 of 1,000 read after a close and reopen
status: run-done
grounded_in:
  - source: cu_bridge start, status polls and final result on run 20261123T042559Z-cb1ae3, 2026-11-23T04:25Z to 04:26Z
  - source: run trajectory events.jsonl and screenshots step-0002.png (before), step-0004.png (reopened) and step-0005.png (close) under /Users/zhenchen/.computer-use/runs/20261123T042559Z-cb1ae3, final frame saved as _tools_/state/cu_help_2025.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:25:58Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:25:58Z
  - source: _activities_/alliance-help/INDEX.md, standing owner instruction on Help All, read before acting
---

# Alliance help queue run 2025

- Executor: operator seat (top-level session), unit help-2026-11-22-1830,
  assignment A-20261123-0425-operator. Token lease 04:40:58Z, claim lease
  04:45:58Z, attempts 1.
- Status: done. Help All was pressed once under the standing owner autonomy for
  the help icon. Two ally requests were cleared, and the header was read live
  before and after a close and reopen.
- Run: `20261123T042559Z-cb1ae3`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:25:59Z, ended 04:26:39Z with status `completed`. Active
  39.6 s, model time 22.9 s, so 3.81 s of model time per step. Steps 6, actions
  done 19, refused 0, blocked 0, failed 0. Cost 0.074916 USD.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. Every click carried
  `frontmostBundleId: com.lastwar.ios`. There was no local-input takeover.
- Route, from the trajectory: Alliance button (670,708), Help tile (513,516),
  Help All (393,766), the Help page X (611,232), the Help tile again (513,516)
  to reopen, the X (611,232), and the back arrow (177,918) to the base. Eight
  clicks, no stray tap. The base-screen help bubble tile was not used. The
  Alliance menu route is the verified one in the profile.
- Before, step-0002.png (HELP page): header "Today's points gained from
  Alliance Help: 280/1,000". Four rows. Two were this account's own requests,
  owner account "Need help with Unlock Oil Well research" and owner account "Need
  help with Defense Training VIII research", both 30/30 and not helpable by
  this account. Two were ally requests: an ally, "Need help with Oil Output
  II research", and another ally, "Need help with building Lv.27 Oil Well", the
  second row partly cut off at the fold.
- Help All: tapped once. The run read the toast "Allies are very grateful for
  your assistance!". Both ally rows left the list. The own rows then showed
  "Time reduced" displays of 10:02:00 and 15:43:26, as reported by the run.
- After, step-0004.png, read after the close and reopen: header 320/1,000.
  The list holds only the two own owner account rows, so no ally request is
  waiting. The reopen is what the profile requires, because the header does not
  update inside one open Help session. A "an ally's gift received" toast
  appeared on the reopen. It is the gifts regular's, and nothing was tapped
  for it.
- Result: 2 ally helps delivered, counted from the two rows that cleared. The
  header rose 280 to 320, which is 20 points per help and matches the 20 per
  help measured on 2026-11-10 1818. The ally row at the fold may have hidden a
  third row, but the reopened list shows none, so the count of 2 stands.
- Cross-check: the two own help requests are the Unlock Oil Well research and
  the Defense Training VIII research. They are the same two researches the 2022
  research unit read in the queue, which corroborates that read.
- Closing frame, step-0005.png: base screen, no panel open. HUD unchanged:
  food 732.3M, iron 1.1G, gold 35.3M, diamonds 8,336, power 150,080,120. The
  Alliance button still carries a red dot. Per the profile that dot is not
  remaining help.
- Red lines: no speedup, no diamonds, no purchase, no diplomacy, no send, no
  Applicants, Members, Store or Settings tap. No confirmation dialog appeared.
- Stat note: the done unit carries `blocker_category: none`, and `complete`
  warned that `none` is not in the a-i enum. The unit had no blocker, so the
  value means "no blocker", not a missing class. A second `complete` is refused,
  so the warning stays in `stats_warnings` and is explained here. `points: 40`
  is points gained in this unit (320 minus 280), not a running total.
- Follow-up: none owed for this window. A later help unit re-checks the Help
  tile for fresh requests.
