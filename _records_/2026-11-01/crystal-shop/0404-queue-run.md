---
title: Ticker 0404 crystal-shop access-failed
created: 2026-11-01T12:10:00Z
modified: 2026-11-01T12:10:00Z
---

# Ticker 0404 - crystal-shop-2026-11-01-0500, failed (device offline)

Session window: 2026-11-01 about 04:04 to 04:10 local.
Executor: ticker-0404. Unit status: failed. Tracker untouched,
as a failed unit requires, so the next tick re-produces this
regular.

## What was done

- Pass opening: sync reaped 0, expired 4 (the 2026-10-31
  2230/2257 help, mail, secrets and treasures units), produced
  nothing new; the 20 due regulars were already queued by the
  planner. No zombie chain seeded: the Zombie Invasion event
  ended at about the 19:00 reset on 2026-10-30 and its chain
  closed at unit 066, per the activity metadata, which states
  explicitly not to seed a new chain until a Zombie Invasion
  tab is seen live in the Events hub again.
- Own PRs first: one open pull request exists for
  zachmesh/lastwar - PR 49 (records/2026-11-01, Owner:
  lastwar-pr-integrator), held by the integrator at 0345 and
  again at 0400 for the branch truncation introduced by
  commit 1ba06f3f5 (day INDEX 627 lines on main down to
  93, later 138; action log 373 down to 7). This pass
  repaired the branch before any game work: both files
  restored from main and only the branch-only content
  re-appended (INDEX sections from the 0330 run through
  the 0400 integration run; the 0330, knowledge-organization
  0332, ticker-0334 and planner-0344 action-log lines),
  verified additions-only against main (INDEX +114 lines,
  627 to 741; action log +4 lines plus a trailing-newline
  fix on main's last line), commit 5963cfa81 pushed to
  records/2026-11-01 and ls-remote verified, and a repair
  comment posted on PR 49 for integrator re-review. The
  already-merged 03:15/03:20 sections were not duplicated.
  This repair work was done in a temporary worktree on the
  VPS so the local working tree's other-job state was
  never disturbed.
- Token acquired by ticker-0404; no other pass held it.
- Next unit by earliest expiry: crystal-shop-2026-11-01-0500
  (priority 1, owner-named 2026-10-25, escalation rule R5),
  claimed by ticker-0404 until 2026-11-01T12:27:22Z.
  The crystal-shop activity metadata was read before
  claiming: the job is to enter the Store Building section
  (not the Hot Deals storefront) and open the Crystal Shop
  tab, which no unit has ever entered.

## What was not done, and why failed

- Device channel offline: three computer.session starts on
  the Mac mini (device 1c817413-83e2-0545-cb90-36d5e096a6bd)
  each returned node_offline with no wake-up path
  advertised; a connection.health probe and a
  connection.repair (web) attempt on the same device
  returned the same error. The device last seen time was
  2026-11-01T09:47:27Z (01:47 local) and did not move
  across the pass. Three session attempts meet the
  at-least-3-attempts rule in the recording rules before
  this unit is written down as access-failed.
- No game input was dispatched in this unit: no screen was
  read, the Store was never opened, the Building section
  and the Crystal Shop tab were never entered or verified,
  nothing was claimed, nothing was spent, and no
  different-device dialog was seen. The Crystal Shop
  location therefore remains unlocated, and its age under
  rule R5 now runs from 2026-10-25 to today.
- No other unit was executed in this pass: with the device
  channel down, the remaining inbox units could not be
  attempted either, and the pass ends here rather than
  burning the pass budget on further offline retries or
  burning other units' attempt counts.
- Tracker untouched (failed unit). Nothing claimed.

## Queue hygiene note - sync expire overwrite caught and reverted

- This pass's sync expired 4 inbox units (help-2026-10-31-2230,
  mail-2026-10-31-2230, secrets-2026-10-31-2257,
  treasures-2026-10-31-2257) by moving them into done, but
  done already held real executed results for the same unit
  ids (ticker-0134/0136 executions with their records and
  claims), and the move overwrote those results with
  "expired" placeholders. The inbox copies were stale
  duplicates of already-executed units, not unexecuted work.
- This pass reverted the 4 done files to their branch state
  before committing, keeping the real results intact, and
  kept only the removal of the stale inbox duplicates.
  The sync expire path needs a tool-side guard (never
  overwrite an existing done result for the same unit id);
  that fix is tier 2 and is left for the tool developer,
  not swept into this records commit.

## Follow-up

- Next tick retries the crystal-shop regular as a fresh
  unit and re-checks the device channel; if the channel
  is still offline then, that pass records it the same way.
- This is the fourth consecutive access-failed ticker pass
  (02:34 arms-race, 03:04 donations, 03:34 radar, now 04:04
  crystal-shop, all on the same offline channel, last seen
  01:47 local and unmoved since), so this pass is material
  under the ticker reporting rule: the main agent decides
  whether the owner needs to bring the Mac gateway back
  (the channel recovered only on a local Mac message in
  the 2026-10-29 recurrence).
- PR 49, repaired by this pass, awaits integrator
  re-review; it is not merged by this pass.
