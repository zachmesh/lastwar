---
title: Mail rewards queue run 2028
created: 2026-11-23T04:31:00Z
modified: 2026-11-23T04:31:00Z
version: 1.0.0
description: Mail rewards unit mail-2026-11-22-1830, operator seat, mail hub read live with no gift icon on any category, Claim All pressed once in System with no reward, nothing claimed
status: run-partial
grounded_in:
  - source: cu_bridge start, status polls and final result on run 20261123T042819Z-9b600a, 2026-11-23T04:28Z to 04:29Z
  - source: run trajectory events.jsonl and screenshots step-0001.png (mail hub), step-0003.png (System after Claim All) under /Users/zhenchen/.computer-use/runs/20261123T042819Z-9b600a, final frame saved as _tools_/state/cu_mail_2028.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:28:19Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:28:18Z
  - source: _activities_/mail-rewards/INDEX.md, gift-icon rule and Claim All auto-advance rule, read before acting
---

# Mail rewards queue run 2028

- Executor: operator seat (top-level session), unit mail-2026-11-22-1830,
  assignment A-20261123-0427-operator. Token lease 04:43:19Z, claim lease
  04:48:19Z, attempts 1.
- Status: partial. No reward was claimable, and the unit was a read of the mail
  hub plus one Claim All, not a Claim All sweep of every category.
- Run: `20261123T042819Z-9b600a`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:28:20Z, ended 04:29:07Z with status `completed`. Active
  46.3 s, model time 29.3 s, so 4.18 s of model time per step. Steps 7, actions
  done 20, refused 0, blocked 0, failed 0. Cost 0.087445 USD.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. Every click carried
  `frontmostBundleId: com.lastwar.ios`. There was no local-input takeover.
- Route, from the trajectory: Mail button (670,782); System row (400,477);
  Claim All (553,932); the list back arrow (113,935); Regular row (400,575);
  the back arrow twice (113,935), which reached the base. Seven clicks.
- Mail hub, read live on step-0001.png. Rows: Battle Report, Alliance, Event,
  System, Regular, In-app Purchases, Favorite. NO gift icon on any row. Red dots
  stood on System (with a President avatar) and Regular. Alliance and Event had
  no marker. By the profile's rule the gift icon is the claimability
  indicator, so nothing was claimable at entry.
- System: opened, six President Mails listed, 19 to 22 minutes old (Indonesian,
  Korean, Turkish, Portuguese, Espanol, Warzone Duel...). Claim All pressed once
  at (553,932). Step-0003.png shows all six greyed as read, still listed. No
  CONGRATULATIONS or REWARD CLAIMED popup appeared, so no reward is reported.
  The System red dot cleared. Claim All was not pressed a second time.
- Regular: opened, Victory battle reports, no gift icon. Claim All was not
  pressed there.
- Not opened: Event, Alliance, Battle Report, In-app Purchases (receipts only
  per the profile) and Favorite. Claim All was not pressed in any of them. So
  the unit is not a full sweep. This follows the profile's own lineage, where a
  unit that leaves categories unwalked closes partial.
- Delete All: the red Delete All button sits directly beside Claim All in the
  list footer, about 190 px to its left (363,932 against 553,932). The tap
  landed on Claim All, and all six mails are still present, so nothing was
  deleted. The adjacency is the main hazard on this screen. The next mail unit
  should aim at the measured Claim All centre and verify it on the screenshot.
- Closing frame, `_tools_/state/cu_mail_2028.png`: base screen, no panel open,
  no TIPS popup. The Mail button no longer carries a red dot. HUD unchanged:
  food 732.3M, iron 1.1G, gold 35.3M, diamonds 8,336, power 150,080,120.
- Mails claimed: 0. Rewards: none. Mails marked read: six in System, plus the
  Regular reports the run opened.
- Red lines: no speedup, no diamonds, no purchase, no send, no delete. In-app
  Purchases was not opened. No confirmation dialog appeared.
- Follow-up: the next mail unit watches the hub for a gift icon and sweeps
  Event and Alliance first, since those carry the rewards when they appear.
  Battle Report and Favorite were not read this unit.
