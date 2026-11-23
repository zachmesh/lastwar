---
title: Black Market read BM1
created: 2026-11-23T09:33:00Z
modified: 2026-11-23T09:33:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-018 - read-only look at the Black Market and Black Market Challenge pages, nothing bought, refreshed or claimed; cash 10,350, bottom row three items at 500 cash each, Refresh free 62 of 62
status: done
grounded_in:
  - source: cu_bridge run 20261123T092921Z-181b74, events, final result and frames step-0002 and step-0003, 2026-11-23T09:29:21Z to 09:29:54Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-018 (Story 868, BM1) and coordinator assignment A-20261123-0928-operator
---

# Black Market read BM1

Rows in [0929-bm1-black-market.csv](../growth/0929-bm1-black-market.csv) (schema k_market).

- **Cash.** 10,350 (green banknote icon), up from 10,030 at 05:41Z. Event timer 20d 16:30:28
  at 09:29:30Z, so the market ends near 2026-12-14T02:00Z.
- **Top row.** Three tiles, all Sold Out, availability 0: a Free-ribbon gray stack x1, a
  Featured gray IV item x1, a Fantastic 5m speed-up x12. Their prices are not shown.
- **Bottom row.** Each tile availability 1, price **500 cash** (cash icon, no diamond, no
  real money): an orange IV item with a question mark x5, a purple chest x1, and a blue-silver
  chest with yellow chevrons x6 (the icon of the blue-frame SR Resource Choice Chest; the
  name was not read, no tile was tapped). No shard choice chest is on sale at this refresh.
- **Refresh.** A green button reading Refresh and Free, "Refreshes (today): 62/62". Quick Buy
  tick box empty. A Pack button with a small red mark sits top right; not opened.
- **Challenge.** Timer 6d 16:30:20. Earned today **550/600** (470/600 at 05:41Z). Sources:
  Radar Task (Double Rewards) counts toward the cap; Secret Mobile Squad (Special) does not
  count towards the BM Cash limit; Doom Elite earned today 5; Zombie earned today 0. No
  Bingo tab or section is visible, so the 1.5K Bingo final reward stays unverified.
- **Reading, unverified.** Cash rose 320 since 05:41Z while the capped counter rose 80, which
  fits the uncapped Secret Mobile Squad paying the rest.
- **Not done, by rule.** Nothing bought, refreshed, claimed or tapped on a tile; no Go To.
  Spending BM cash is not a diamond spend, but it is a purchase, so it needs the owner's word.
- **Run.** 5 steps, 8 actions done, 0 refused, no `local_input` pause, `claude-gateway/
  claude-sonnet-5-5`, 0.079503 USD against a stated cap of 0.60 (the harness stops near
  0.36 of it, 0.216). Token held from 09:28:53Z, released right after the run (about 09:31Z).
- Closing state: the base, no panel open.
