---
title: Alliance donations queue run 0719
created: 2026-11-02T15:19:00Z
modified: 2026-11-02T15:19:00Z
version: 1.0.0
description: Ticker unit donations-2026-11-02-1055, Garrison Defense count read live at 5 of 30, coin Donate button unresponsive to three methods, no donations landed
status: partial
---

# Alliance donations queue run 0719

- Unit: donations-2026-11-02-1055, executor ticker-0704.
- Outcome: no donations landed, no coin or diamond spent.
  Status partial, tracker untouched. This unit does NOT
  close on arithmetic - the only count figure claimed is
  the live read below, per the hard closing rule and
  rule R1.
- Entry, re-grounded fresh from the base screenshot
  (never inherited): Alliance right-column button at
  norm 930,700 opened the alliance menu ([AP3x] The
  Apex, 94/100 members) at once; Alliance Techs tile
  at norm 748,665 opened ALLIANCE TECHS at once.
  War tab selected. Tree read live: Expert Nurse 1/10
  top, Garrison HP 7/10, Garrison Attack 7/10,
  Garrison Defense 7/10 carrying the red thumbs-up
  recommended marker, one lower node 7/10 partly
  visible. Tech Donation Today 3500, above the 1000
  reward line; no reward was claimed by hand, as the
  ranking reward settles at the 19:00 reset.
- Recommended node panel, read live: Garrison Defense
  7/10, Increased Hero Defense in Defense Support
  for Alliance members, Donation Reward plus 20
  percent, Tech EXP Required 163.8K/4.5M, Current
  plus 7 percent, Next Level plus 8 percent,
  Donation Reward 50 plus 50, Donation Count 5/30,
  Donate buttons diamond 2 (never tapped) and coin
  800.
- Donate failure, three methods, rule R2:
  - Single coordinate tap on the green coin Donate
    button centre at norm 735,647: no change, count
    still 5/30, Tech EXP still 163.8K/4.5M.
  - Pivot point within the same button at norm
    735,640: no change. The control channel then
    warned that background clicks do not reach some
    controls and advised click_element instead of
    clicking there again.
  - Pivot method click_element on the cost OCR
    control (element 29, 800): dispatched, no change,
    count still 5/30 on the following screenshot.
  - Method ends here inside this unit. No keyboard
    input was used (Return and Esc quit this app),
    and no hold-to-donate was used (untested as a
    closing method, and it would break the live
    count-step verification).
- Contrast that matters for the tooling owner:
  navigation taps in this same session all worked
  at once (Alliance menu, Alliance Techs tile,
  Garrison Defense node), while the green Donate
  action button did not respond to any of three
  input routes. This matches the pattern of GitHub
  Issue 171 (green action buttons unresponsive to
  background input while navigation taps worked),
  and this unit is commented there rather than
  filed as a duplicate. The diamond Donate button
  was never tapped, so whether it shares the
  failure is untested and must stay untested
  without owner approval.
- Tree change noted, not acted on: the War tab
  tree now reads Garrison HP, Attack and Defense
  at 7/10, where earlier units read Troop Movement
  and Rallied nodes. Whether the Rallied tier
  completed or the tree scrolled is unmeasured;
  the recommended marker governed this unit, and
  the tree change is named here for the next unit
  to confirm, not asserted as a completion.
- Game left safe: Garrison Defense panel open,
  coin button still green at 5/30, nothing spent,
  no other task type touched.
- Result stats: target 30, achieved 0 donations
  landed, donation count read live 5 of 30
  remaining, verified no, blocker_category c
  (action-button tap method). The next tick
  re-produces this regular because the tracker
  stays untouched for a partial unit; the inbox
  already holds later donations units, and no
  separate re-read unit is enqueued from here.
