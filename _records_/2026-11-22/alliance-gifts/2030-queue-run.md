---
title: Alliance gifts queue run 2030
created: 2026-11-23T04:33:00Z
modified: 2026-11-23T04:33:00Z
version: 1.0.0
description: Alliance gifts unit gifts-2026-11-22-1830, operator seat, 1,028 Regular and 106 Premium gifts claimed with Claim All on both tabs, dialog-confirmed, both tabs clear on re-check
status: run-done
grounded_in:
  - source: cu_bridge start, status polls and final result on run 20261123T043042Z-53161f, 2026-11-23T04:30Z to 04:31Z
  - source: run trajectory events.jsonl and screenshots step-0002.png (Regular before), step-0003.png (Regular dialog), step-0005.png (Premium dialog), step-0006.png (Regular re-check) and step-0007.png (base) under /Users/zhenchen/.computer-use/runs/20261123T043042Z-53161f, final frame saved as _tools_/state/cu_gifts_2030.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:30:41Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:30:41Z
  - source: _activities_/alliance-gifts/INDEX.md, Claim All on both tabs, Premium Claim All sits right, read before acting
---

# Alliance gifts queue run 2030

- Executor: operator seat (top-level session), unit gifts-2026-11-22-1830,
  assignment A-20261123-0430-operator. Token lease 04:45:41Z, claim lease
  04:50:41Z, attempts 1.
- Status: done. Claim All was pressed once on each tab. The dialogs confirm
  1,028 Regular and 106 Premium gifts, 1,134 in total. A Regular re-check after
  the Premium sweep found nothing new.
- Run: `20261123T043042Z-53161f`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:30:43Z, ended 04:31:43Z with status `completed`. Active
  60.6 s, model time 37.0 s, so 4.62 s of model time per step. Steps 8, actions
  done 27, refused 0, blocked 0, failed 0. Cost 0.090002 USD.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. Every click carried
  `frontmostBundleId: com.lastwar.ios`. There was no local-input takeover.
- Route, from the trajectory: Alliance (670,708), Alliance Gifts tile
  (273,595), Regular Claim All (393,918), dialog dismiss (400,820), Premium tab
  (517,287), Premium Claim All (549,918), dialog dismiss (400,830), Regular tab
  (273,287), the Gifts back arrow (113,930) and the Alliance back arrow
  (177,919). Ten clicks, all on the intended controls. Premium Claim All was
  grounded on its own screenshot and landed first try, to the right of the
  footer, so the Regular point was not reused.
- Regular, before (step-0002.png): Gift Level 29, progress 31,789,710 of
  257,900,000, Claim All badge 1,028, red dots on both tabs. Claim All pressed
  once. Dialog (step-0003.png): "A total of 1028 Regular Alliance Gifts were
  claimed this time". Rewards as displayed: a golden chest x98, 600 coin x4.2K,
  gem 5 x118, 5m speedup x88, bread 1.0K x4.3K, iron 1.0K x4.5K, coin 6.0K x174,
  bread 10.0K x116, iron 10.0K x174. Progress after: 31,799,990.
- Premium, before: badge 106, as read by the run. Claim All pressed once.
  Dialog (step-0005.png): "A total of 106 Premium Alliance Gifts were claimed
  this time". Tiles as displayed: bread chest x73, coin chest x54, purple chest
  x37, iron chest x55, medal 50 x5, gem 20 x4, 5m speedup x12 and x23, gem 10
  x2, 5m hammer speedup x1, iron plate x120. A top row of tiles was cut off by
  the dialog banner and is not recorded. A "Recruit Heroes! 115/10" banner
  slid across the dialog. It is a game notification, and nothing was tapped for
  it. Progress after: 31,823,740.
- Re-check (step-0006.png): Regular tab selected after the Premium sweep. Every
  visible row reads Claimed, there is no Claim All button, and neither tab
  carries a red dot. No new gift had arrived, so no second Claim All was
  pressed. The Premium tab was not re-opened after its claim. Its cleared red
  dot is read from this frame.
- Progress deltas, as measured and not attributed. Regular: +10,280 for 1,028
  gifts, which is exactly 10 points per gift. Premium: +23,750 for 106 gifts,
  with the tier mix not itemised, so no decomposition is claimed. The bar is
  alliance-wide (Issue #183), so the dialog counts are the verification, not
  the bar. Total +34,030.
- Resources, stated plainly. The dialogs list coins, bread and iron in the
  millions, but the HUD totals did not move across the unit: food 732.3M,
  iron 1.1G, coin 35.3M before and after, diamonds 8,336, power 150,080,120. The
  tiles look like inventory items (resource packs, chests, speedups) and not
  direct credits. The Inventory button gained a red dot on the closing frame,
  which fits items arriving there. That is an inference, and the Inventory
  was not opened. No reward value is claimed beyond the displayed tiles.
- Untouched: the "Hide your name on Gifts" checkbox (not clicked, state not
  read), the Regular tab's "Defeat the Doom Elite ... Go" row, the Alliance
  Store and every Buy button. No confirmation dialog appeared.
- Closing frame, `_tools_/state/cu_gifts_2030.png`: base screen, no panel open.
- Red lines: no speedup used (speedups were received as gifts, not applied), no
  diamonds, no purchase, no send.
- Follow-up: none owed for this window. New gifts arrive as allies play, so the
  next gifts unit sweeps both tabs again.
