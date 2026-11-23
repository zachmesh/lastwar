---
title: Shop claims run 1457
created: 2026-11-23T14:58:00Z
modified: 2026-11-23T14:58:00Z
version: 1.0.0
description: Unit passes-2026-11-23-0257 - nothing claimable on the Official Event, Weekly Deal, Weekly Pass and Super Monthly Pass tabs, Free Supply already Claimed, no Hot Sale Packs tab found; both weekly cards read owned with the pickup claimed today; closed partial, blocker f
status: partial
grounded_in:
  - source: cu_bridge runs 20261123T145152Z-e7349e (shop and weekly tabs) and 20261123T145556Z-6d0ad3 (Weekly Deal), frames read by the operator, 2026-11-23T14:51Z to 14:57Z
  - source: unit brief passes-2026-11-23-0257, shop-claims rule digest rules 1 to 10 and 2044-queue-run
---

# Shop claims run 1457

Rows in [1457-queue-run.csv](1457-queue-run.csv); one ledger row. Claimed 14:51:20Z; no different-device dialog; no tap on a price, Renew, Take All, Buy, Switch or Go.

- **Shop layout changed.** The cart opens on Official Event; the tab row reads Official Event, Weekly Deal, Super Monthly Pass, Weekly Pass, Diamond and a cut-off "G..." tab. The Hot Sale Packs tab of 2044 is not in it, and the red dot sits on the HOT DEALS banner, not on a pack.
- **Hot Deals free pack: not found (rule 1).** Weekly Deal holds three priced packs (Oil Special Offer $19.99, Valor Badge $99.99, Base Upgrade $19.99). The 2044 pack timer (21:15:42 at 04:44:11Z) ends about 02:00Z on 11-24, so the pack taken then is plausibly not due again before the reset (one timer, unverified).
- **Free Supply: Claimed** (rule 5), not claimed by this run.
- **Weekly passes read owned (rule 3 contradicted).** S2 Drone Components and S1 Drone Parts both show Remaining 6d 11:07:32 (ends 11-30 02:00Z) and "Already claimed today" beside Renew $4.99; 2044 read the same cards as offers. Unverified: who bought them; the next Daily Pickup claim falls after the 02:00Z reset.
- **Super Monthly Pass:** Buy x1 and Switch, not owned. The check-in Go was not tapped.
- **Not read:** the "G..." tab and anything beyond Diamond; the tab bar was not dragged.
- **Runs.** 0.073857 USD (5 steps) and 0.067009 USD (5 steps), cap 0.5 each; a third start, 20261123T145437Z-e7a428, ended `gateway_unreachable` with 0 actions and 0 cost, then the retry ran. 0.140866 USD in all; 0 refused.
- **Closing state.** The base, no panel open; food 654.6M, iron 1.0G, coin 13.1M, diamonds 11,113, Total Power 150,416,946, all unchanged; token released.
