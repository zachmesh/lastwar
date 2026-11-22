---
title: Harvest queue run 0312
created: 2026-11-21T11:15:00Z
executor: ticker-0310
unit: harvest-2026-11-21-0203
status: failed
---

# Harvest - 0312 queue run (failed)

Session 03:12-03:15 PT (11:12-11:15Z), executor ticker-0310, unit
harvest-2026-11-21-0203 (planned for 2026-11-21 10:03Z, expires
2026-11-21 14:03Z). Second consecutive game unit blocked by the
fullscreen precondition (radar 0201 at 02:01 PT, harvest 0312 at
03:12 PT).

## What happened

- Mac mini online (device list 03:10 PT, last seen 11:04:57Z);
  computer session cc-3 started 03:12 PT. Last War IS running
  (window 96101, pid 95844) at the base view. No login was
  demanded, no "active on a different device" dialog appeared.
- Blocker - the LastWar window is in native fullscreen 1920x1080
  on its own Space (on_current_space false). The control channel
  refuses every pointer-input route, verified live in this
  session:
  - coordinate click at a fresh-grounded bubble centre (469,319,
    from the 03:14 PT screen capture) refused: "Pointer input
    requires the window on the Space the user is looking at"
    (action_failed, nothing sent);
  - menu View -> Exit Full Screen refused: arrangement change
    while fullscreen on its own Space, user cannot see it
    (action_failed, nothing sent);
  - activate raise=true refused at first ("not_tried_in_place" -
    no in-place action refused yet in this session); after the
    menu refusal the tool's own guidance permits a raise, but
    the raise guidance states a raise switches back when its
    request ends, so a follow-up click can never land - the same
    conclusion ticker-0159 reached at 02:01 PT;
  - full Accessibility observe: the window exposes NO controls
    (title bar only); the 6 numbered items are OCR text only
    (HUD fragments). Bubbles are canvas points, so click_element
    cannot reach them either. key/type go to the app's keyboard
    window and cannot tap bubbles.
- Live read from the 03:14 PT screen capture (1280x720
  downsample): food 665.3M, iron 1.0G, coin 50.2M, diamonds
  17.72K, 4,706; "Alliance Gift (R) received!" toast; Component
  Factory Lv.20; many green/white resource bubbles visible over
  the farmland and the gold buildings, uncollected.
- Result: NO game action taken. No bubble collected, no truck
  check, no stamina spent, no items used. The harvest target was
  not met on any line. Tracker untouched (failed).

## Remaining work

- Many resource bubbles remain visible and uncollected; the Armed
  Truck loot state is still unchecked. The next tick re-produces
  this regular as a fresh unit (failed: tracker untouched).
- The owner action that unblocks this in seconds: on the Mac mini,
  switch to the Last War window or exit fullscreen (menu View ->
  Exit Full Screen). An Issue for this failure mode (fullscreen
  off-Space window blocks the ticker) is owed once the gh route
  via the VPS returns; it cannot be filed now (VPS SSH still
  Permission denied, gh unauthenticated locally) - same standing
  note as 0159. The fullscreen blocker has now stopped two
  consecutive game units (radar 0201, harvest 0312); it appeared
  between 00:49 PT (ticker-0048 tapped fine) and 02:01 PT and has
  persisted since.

## Delivery

- VPS SSH still Permission denied (publickey) - probed 03:10 PT,
  the outage since 2026-11-12 continues (about 207 hours). Push
  and PR delivery are impossible this pass; the commit sits on
  the local records/2026-11-21 branch (from main 22601972), push
  pending VPS recovery.
- Own PRs first: open PRs via the GitHub connector
  (list_pull_requests, zachmesh/lastwar) are exactly 3, all
  unchanged since 2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator), #425 tools log gate (owner-gated). No
  PR for records/2026-11-21 and none names this job
  (lastwar-queue-ticker); no conflict, no unanswered question
  addressed to this job.
- Zombie Invasion: NOT seeded - the event ended (last live check
  2026-11-15, chain zombie-2026-11-10 closed with no successor;
  activity metadata forbids seeding until a Zombie Invasion tab
  is seen live again).
- Action-log note: this pass's entry is appended to the worktree
  (main-lineage) copy of action-log.jsonl only (1967 lines); the
  live tree's copy is diverged and must NOT be copied over it
  (see the 0049 record).
- Device token released at pass end; computer session cc-3 ended
  with the game left on the base view (untouched).

## Stats

- coin_before 50.2M, coin_after 50.2M, food_before 665.3M,
  food_after 665.3M, iron_before 1.0G, iron_after 1.0G
- verified yes (blocker observed live in this session; HUD
  figures are live reads from the 03:14 PT capture),
  blocker_category f (missing precondition - game window not
  reachable for pointer input)
- bubbles_remaining many, truck_checked no
