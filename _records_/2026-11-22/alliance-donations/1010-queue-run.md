---
title: Donations run 1010
created: 2026-11-23T10:11:00Z
modified: 2026-11-23T10:11:00Z
version: 1.0.0
description: Second donations pass of unit donations-2026-11-23-0711 (assignment A-20261123-1008-operator) - five coin donations to Quick Construction, count 6/30 to 1/30, floor read at 10:07:00Z with no timer, no tap at 1/30
status: done
grounded_in:
  - source: cu_bridge runs 20261123T100556Z-ca3303 and 20261123T100752Z-01a51d (close-out), events, final results and frames step-0009 and step-0010, 2026-11-23T10:05Z to 10:08Z
  - source: coordinator assignment A-20261123-1008-operator and the alliance-donations rule digest rules 1 to 5
---

# Donations run 1010

Rows in [1010-queue-run.csv](1010-queue-run.csv); one ledger row in
[ledger.csv](../growth/ledger.csv). Part two of [1002-queue-run.md](1002-queue-run.md).

- **Donations (rule 1).** Quick Construction 9/10 stayed the recommended node. Five coin donations
  at **1,000 coins** each, 10:06:21.835Z, 10:06:28.053Z, 10:06:34.983Z, 10:06:41.336Z and
  10:06:58.225Z, count **6/30 to 5, 4, 3, 2 and 1/30** (rule 4: read after each tap; one frame
  was hidden by the reward animation, so the count was read again after a wait, no tap).
- **Floor read for the researcher's test T1.** The count first read **1/30 at 10:07:00Z** (frame
  10:07:00.439Z, two seconds after the fifth tap). The only text near it is "Donation Count:
  1/30"; **no timer, no cooldown, no other label**, and the green coin Donate (1,000) still shows
  active. No tap was made at 1/30 (rule 5); the diamond Donate (2 gems) was never pressed.
- **Reward.** Each donation pays 50 Tech EXP and 50 alliance coin; Crit x5 and x2 animations
  showed on some taps. Alliance coin chip 82.3K at 10:03Z to 82.8K at 10:07Z (rounded).
- **Unit total.** Eight donations in the unit (3 at 10:03Z, 5 now), 8,000 coins, count 9/30 to
  1/30 as the profile floor asks; the count refills about every 20 minutes, so the floor read is
  only valid within minutes.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 11 steps, 21 actions, 0.142328 USD against a stated
  cap of 0.5 so that the close-out was not cut off (the 0.4 named would stop near 0.144); it
  ran out of turns on the Alliance menu, so a 4-step close-out (`20261123T100752Z-01a51d`,
  0.052162 USD) returned to the base. 0.194490 USD in all, 0 refused, no `local_input` pause.
- Closing state: the base, no panel open, token released.
