---
title: Truck run 0953
created: 2026-11-23T09:58:00Z
modified: 2026-11-23T09:58:00Z
version: 1.0.0
description: Unit trucks-2026-11-23-0711 - own trade trucks, two returned SR trucks settled for 5.0M iron, 5.0M bread, 3.2M gold and about 100 blue chests, no dispatch because the offered truck stayed below SR after the one free refresh
status: partial
grounded_in:
  - source: cu_bridge runs 20261123T095300Z-ed648f and 20261123T095440Z-dad0cc, events, final results and frames, 2026-11-23T09:53Z to 09:55Z
  - source: unit brief trucks-2026-11-23-0711 (planner A-20261123-0706), truck-plunder rule digest rules 2, 4 and 5, coordinator assignment A-20261123-0952-operator
---

# Truck run 0953

Rows in [0953-queue-run.csv](0953-queue-run.csv); both state changes are in the
[ledger](../growth/ledger.csv) with `serves: upkeep`.

- **Entry.** The blue-circle vehicle icon with a red dot, top of the base's left column at about
  (107,580), opened Intercity Trade on the Your Truck tab on the first tap (tabs Others' Trucks
  with red dot 4 and Your Truck with red dot 3). The white pickup below it stays the Secret
  Command Post. The trade screen entry is therefore known again for this window.
- **Settled.** Slots 1 and 2 held returned trucks. Tapping slot 1 opened Truck Details (SR
  Hero Escorts, "Intercity Trade Reward!") and both trucks cleared: **iron 5.0M, bread 5.0M,
  gold 3.2M** in all (2.5M, 2.5M, 1.6M each), two 500 badges, blue chests x40 and x60, two
  green items and one red-gem-looking "50" item. HUD: food 643.4M to 648.5M, coin 11.1M to
  14.4M, **diamonds 11,136 unchanged** (so the "50" item is not diamonds), Total Power
  150,211,809 unchanged.
- **Dispatch.** Today's Trade Count 2/5 before and after. Slot 1 first offered an N truck
  (04:47:49); one Refresh labelled Free gave an R truck (04:41:52). Both are below SR, so
  nothing was dispatched (rule 2). The next Refresh shows a contract cost 267/1 and was not
  tapped: the unit allows free refreshes only. Slots 1 to 3 are idle, slot 4 locked.
- **Not done, by rule.** No Plunder, no Mega Mode, no Recover, no Others' Trucks beyond the tab.
- **Open for the coordinator.** Three idle slots until the contract refresh is allowed; the
  profile rule 2 names Trade Contract refreshes, owner-authorized 2026-10-26, never diamonds.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 9 steps, 15 actions, 0.136143 USD against a
  stated cap of 0.4 (harness stops near 0.144); a 4-step close-out and HUD run
  (`20261123T095440Z-dad0cc`, 0.051219 USD) closed the screen. 0.187362 USD in all, 0 refused,
  no `local_input` pause.
- Closing state: the base, no panel open, token released.
