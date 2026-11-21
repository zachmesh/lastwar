---
title: Radar stack unit 0201 queue run
created: 2026-11-21T10:05:00Z
modified: 2026-11-21T10:05:00Z
version: 1.0.0
description: Radar stack unit radar-2026-11-20-2203 by ticker-0159 - FAILED, game window fullscreen on its own Space, pointer input refused by the control channel
status: unverified
---

# 2026-11-21 02:01-02:06 PT - radar stack unit (FAILED)

- Unit: radar-2026-11-20-2203 (duel day 6, stack posture), claimed 02:01:49 PT by ticker-0159, lease to 02:21:49 PT.
- Device: Zhen's Mac mini online (device list, 01:59 PT); computer session cc-2 started 02:02 PT. The game IS running: LastWar window 96101 open at the base screen (Component Factory Lv.20; HUD 665.3M / 1.0G / 50.2M coin / 17.72K / 4,706 read live from the screenshot). No "active on a different device" dialog.
- Blocker: the LastWar window is in native fullscreen (1920x1080) on its own Space. The control channel refuses every pointer-input route to it:
  - coordinate click at the radar dish estimate refused: "Pointer input requires the window on the Space the user is looking at" (action_failed, nothing sent);
  - menu View -> Exit Full Screen refused: arrangement change while fullscreen on its own Space, user cannot see it (action_failed, nothing sent);
  - activate raise=true DID bring the window forward once (brought_to_front true, Space borrowed about 9.7 s) but it switched back before the receipt, so a click sent after the raise is refused again;
  - batching activate+click and activate+menu inside one actions call is rejected by the tool schema (activate cannot go inside actions; raise applies only to a standalone activate).
  - The tool's own guidance, repeated in every refusal, is the sanctioned path: the user switches to the game themselves or exits fullscreen. That step needs the user; this detached run cannot ask. No Touch ID, no password, no Esc / Ctrl-Cmd-F used (both crash this app per the standing lesson).
- Result: NO game action taken. No radar entry, no Quick Execute, no claims, no stamina spent, no items used. The stack-day completion standard was not met on any line.
- Stats: target run Quick Execute batches until no offer remains (stack day); achieved 0, no radar read; resources_gained none; costs about 5 minutes of device session time, no stamina or items; verified yes (the blocker was observed live, three distinct input routes refused); blocker_category f (missing precondition - game window not reachable for pointer input).
- Follow-up: the next ticker pass should retry only if the window state changed (windowed 642x951 on the main Space, as on 2026-11-15 when pointer input worked). Owner action that unblocks it in seconds: on the Mac mini, switch to the Last War window or exit fullscreen (menu View -> Exit Full Screen). An Issue for this failure mode (fullscreen off-Space window blocks the ticker) is owed once the gh route via the VPS returns; it cannot be filed now (VPS SSH still Permission denied, gh unauthenticated locally).
- Pass context: VPS SSH still Permission denied (publickey), probed 02:00 PT (about 205 hours into the outage since 2026-11-12); push and PR creation both blocked, so this pass is partial: the record is committed to the local records/2026-11-21 branch only. Own PRs first: open PRs via the GitHub REST API are exactly 3, all unchanged since 2026-11-12 - #711 knowledge fold, #708 records 2026-11-12 (open, mergeable, clean, 0 comments, awaits the integrator batch), #425 tools log gate. No records PR exists for 2026-11-21 and none names this job. Zombie Invasion: NOT seeded - the event ended (last live check 2026-11-15, chain zombie-2026-11-10 closed with no successor; activity metadata forbids seeding until a Zombie Invasion tab is seen live again).
