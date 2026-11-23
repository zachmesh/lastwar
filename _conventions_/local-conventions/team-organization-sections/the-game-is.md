---
title: The game is not frontmost
created: 2026-11-23T09:04:37Z
modified: 2026-11-23T09:04:37Z
version: 0.1.0
sequence: 9
description: A notification or another app in front makes a click land on the wrong app.
---
### The game is not frontmost

A notification or another app in front makes a click land on the wrong
app. The computer-use policy refuses it (`excluded:terminal`) or the
run is handed over. Before a play run: activate Last War, dismiss
NotificationCenter, verify `lsappinfo front` names LastWar. If it does
not, do not claim or start; report `blocked: foreground`.

Measured 2026-11-22 20:03 PT: `com.apple.UserNotificationCenter`
(`/System/Library/CoreServices/UserNotificationCenter.app`) can hold
the global front slot for days and flip back within a minute, while the
screen shows no dialog. A click whose hit-test target is Last War is
still refused with `excluded_front:os_security`. The working fix is to
run `killall UserNotificationCenter NotificationCenter` in the same
shell immediately before the run start, then verify `lsappinfo front`
names LastWar. A read-only observation is the cheap probe: if its
`last_step` says `looked at app:lastwar.ios`, the front slot is clear.
The longer-term fix - judging `excluded_front` on the click's hit-test
target rather than the global front app - is a computer-use policy
change and needs the owner's call.

