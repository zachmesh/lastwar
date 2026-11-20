---
title: Day record 2026-11-20
created: 2026-11-20T08:35:00Z
modified: 2026-11-20T08:35:00Z
version: 1.0.0
description: Day record for 2026-11-20 (America/Los_Angeles) - VPS SSH still down, Mac mini offline
status: unverified
---

# 2026-11-20

## 00:04 to about 00:40 - Ticker pass ticker-0004 (FAILED, Mac mini offline)

- 00:04 PT, ticker-0004 - FAILED, eighty-first consecutive failed
  ticker pass, THIRD device-offline occurrence. Mac mini OFFLINE
  per device.list, last_seen 2026-11-20T04:16:40Z (20:16:40 PST
  Nov 19, about 4 hours stale at probe); device.describe
  connection_state offline; connection.health x3 node_offline
  (08:32Z to 08:34Z, three attempts satisfy the retry-at-least-3
  rule); no computer session started, game window state
  unverifiable. Probe DEVICE_OFFLINE, high confidence, stop_pass
  yes (mac_capture_probe.py 1.2.0, exit 13). No game input sent.
  Token held 00:34-00:40 PT, released unused; no unit claimed,
  `next` never called.
- ORDERING DEVIATION, stated plainly: sync ran BEFORE the 2304
  record was re-read, the same deviation as 2304. The sync
  produced nothing and no unit was claimed, so it cost nothing,
  but it is NOT a honoring pass - the deviation-watch of
  fully-honoring passes stays at THREE (0434, 1347, 1404). The
  next pass must re-read the newest queue-ticker record FIRST,
  before sync and before any claim.
- Sync: due 22, produced 0, already_queued all 22, reaped 0,
  expired 1 (ghost-ops-2026-11-19-0000). Pool after sync: inbox
  73, claimed 0, done 2598. Branch reconcile warning: fetch of
  records/2026-11-20 failed (remote ref missing, issue #446).
  Zombie seeding skipped (event ended about the 19:00 reset
  Oct 30, chains closed, no live re-check possible).
- Own PRs first: VPS SSH Permission denied (publickey) at about
  08:31Z, about 179.8 hours into the outage; GitHub connector
  fallback read shows the same three open PRs as 2304 (#711,
  #708, #425), timestamps unchanged since 2026-11-12, none owned
  by this job, no PR for records/2026-11-19 or records/2026-11-20.
  No new issue filed (gh route down). Window-loss and
  device-offline failure-mode filings stay owed.
- Standing counts: no game unit since ticker-0214 gifts Nov 17
  02:14 PT (about 69.8 hours missed); seventh consecutive missed
  VIP day (same reset day 2304 counted, ends 18:00 PST Nov 20);
  Nov 19 pre-reset sweep pair expired unexecuted 18:19:25 PT,
  sixth missed sweep night per retro-2100; missed batches stay 42
  plus 2 due-but-unexecuted (15:00, 19:00), the 23:00 batch NOT
  counted (no integrator record visible, latest 2215); duel day 4
  Train Heroes ended 18:00 PT Nov 19, unreachable. VPS SSH still
  down, delivery blocked, commit left on local records/2026-11-20,
  no PR. This pass is partial. Record:
  queue-ticker/0004-queue-run.md.
