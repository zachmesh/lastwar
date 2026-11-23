---
title: Building queues queue run 2024
created: 2026-11-23T04:26:00Z
modified: 2026-11-23T04:26:00Z
version: 1.0.0
description: Building queues unit building-queues-2026-11-22-1803, operator seat, all four builders read live and idle, no build started because starting one is owner-only
status: run-partial
grounded_in:
  - source: cu_bridge start, status polls and final result on run 20261123T042406Z-ff5098, 2026-11-23T04:24Z
  - source: run trajectory events.jsonl and screenshots step-0002.png and step-0003.png under /Users/zhenchen/.computer-use/runs/20261123T042406Z-ff5098, final frame saved as _tools_/state/cu_buildq_2024.png
  - source: lsappinfo front reading and killall of UserNotificationCenter and NotificationCenter before the start, 2026-11-23T04:24:06Z
  - source: queue.py token-acquire and claim on the live pool, 2026-11-23T04:24:06Z
  - source: _activities_/building-queues/INDEX.md 1.6.0 and owner decision OD-20261109-02 (Issue #517), read before acting
---

# Building queues queue run 2024

- Executor: operator seat (top-level session), unit building-queues-2026-11-22-1803,
  assignment A-20261123-0423-operator. Token lease 04:39:06Z, claim lease
  04:44:06Z, attempts 1.
- Status: partial. The read half is done and verified. The start half was NOT
  done, on purpose: starting a build is owner-only under the standing profile.
- Run: `20261123T042406Z-ff5098`, desktop, apps `com.lastwar.ios`, model
  `claude-gateway/claude-sonnet-5-5`, max-steps 8, max-minutes 15, max-cost
  1.0 USD. Started 04:24:07Z, ended 04:24:26Z with status `completed`. Active
  19.2 s, model time 13.5 s, so 3.37 s of model time per step. Steps 4, actions
  done 9, refused 0, blocked 0, failed 0. Cost 0.050798 USD.
- Front precondition: `killall -9 UserNotificationCenter NotificationCenter`
  ran in the same shell immediately before the start, and `lsappinfo front`
  named `"LastWar" ... (in front)`. Every click carried
  `frontmostBundleId: com.lastwar.ios`. There was no local-input takeover.
- What the run did, from its trajectory: step 1 click (608,360), the X of the
  Research Queue panel left open by the previous run, which closed it. Step 2
  click (110,200) on the hammer icon labelled 0/4, which opened the BUILDING
  QUEUE panel on the first try. Step 3 click (612,237), the panel's own X.
  Step 4 only reported. Three clicks, all passive.
- Live read, step-0002.png (BUILDING QUEUE panel): slots 1, 2, 3 and 4 all read
  "Idle", each with a blue Construct button carrying a red dot. None of the
  Construct buttons was tapped. This is consistent with the 0/4 hammer label.
- Closing frame, step-0003.png: base screen, both panels closed. HUD unchanged
  against the research unit's close: food 732.3M, iron 1.1G, gold 35.3M,
  diamonds 8,336, power 150,080,120. Hammer 0/4, flask 2/2. The banner quest
  still reads "Build: Oil Well (0/1)". Nothing was started.
- Why no build was started. `_activities_/building-queues/INDEX.md` says
  starting an upgrade "spends resources and locks a queue for a long time, so
  it needs the owner choice unless it was already queued", and the open
  questions still ask what the idle slots should build. The only filed choice,
  OD-20261109-02 (Issue #517, Builders Hut Lv.25 to Lv.26, 15d 08:05:18
  original time), has no owner answer. The profile names no "next build" and
  no standing owner choice exists. The assignment asked to start the profile's
  next build but cited no owner approval, so the unit stopped at the owner
  surface per the seat protocol and records `needs-owner` for that half. No
  resources were spent.
- Inference, unverified: the open banner quest is "Build: Oil Well", and the
  research queue read 20 minutes earlier shows "Lv.0 Unlock Oil Well" still
  running with 07:20:35 left, which completes about 11:43Z. The Oil Well build
  is therefore probably not available until that research finishes. The
  Construct panel was not opened here, so this is a guess from two reads, not a
  finding.
- Drill Ground: the Lv.25 Drill Ground upgrade read at 1012 would have finished
  about 17:30 PT, and all four slots are now idle, which agrees with it. The
  troop-training unit at 2017 still raised the Drill Ground Full toast after
  that time, so the upgrade did not clear the requeue block. This is recorded
  as an observation. The Drill Ground level was not read here.
- Red lines: no speedup, no diamonds, no purchase, no Construct, no Upgrade, no
  Finish Now, no green up-arrow, no building tapped. No confirmation dialog
  appeared.
- Game left on the base screen with no panel open.
- Follow-up: the owner chooses what the four idle builders build, either by
  answering OD-20261109-02 or by naming a build. Until then every
  building-queues unit is a read. Four idle builders is a standing cost, and
  the Arms Race Base Building phase (18,900 of 30,000) needs a finished
  building upgrade to score.
