---
title: How to enter part 1
created: 2026-11-23T06:53:14Z
modified: 2026-11-23T06:53:14Z
version: 0.1.0
sequence: 3
description: Open Events from the base screen.
---
## How to enter

- Open Events from the base screen.
- Login recovery (2026-11-10 2209): if the game window is frontmost but login has failed with an [E118] network connection error dialog ("Please check your connection and try logging in again"), tap Reconnect twice - the first (element) tap produced no change, the second (coordinate) tap on the same button cleared the dialog and login retried successfully. No password, no Touch ID, no fresh login was demanded.
- Events entry is layout-scoped (2026-11-09 0949): the (672,132) grounding was measured in landscape fullscreen and does not apply to letterboxed portrait fullscreen or windowed portrait - in both, that point is map scenery. Ground the Events entry fresh from the live layout each unit; first check whether the announcement banner hides the globe icon. (2026-11-10 1756 update: in the windowed portrait layout the globe icon sits top-right at norm (934, 137) - a fresh grounding for this layout, not a reuse of the landscape (672,132).)
- Open the Arms Race banner. The current phase, its tasks and the
  time left in the phase are shown on the event page.
- Entry, 2026-11-11 0535: the first tap at (683,150) hit the Drone Center building, not Events - the map was zoomed in and the icon sits elsewhere in that view. The Events icon grounds live at (934,160) on the full base UI (red badge 3). The Events tab bar shifts between openings: the Arms Race tab was cut off at the left edge on entry and a tap on its visible fragment did nothing; a drag of the tab bar to the right revealed it fully, and a tap at (397,131) opened the Arms Race page. Re-verify the tab by its title before tapping, as units 011 and 048 already warned. (2026-11-11 0541 update, donations unit: the Arms Race page's back arrow ignored three background-click variants - snapped tap (110,905), re-measured centre (112,907), exact-pointer tap - and the working exit was the Desert Battlefield tab detour, whose back arrow at the fresh measured centre (164,931) returned to the base at once. Back-arrow behaviour differs per Events page; do not repeat the three dead taps from the Arms Race page.)
