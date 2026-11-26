---
title: The UserNotificationCenter Window Rule 3126 2026-11-26
created: 2026-11-26T10:10:00-08:00
modified: 2026-11-26T10:10:00-08:00
level: L0
version: 1.0.0
description: Steer A's python rule for a UserNotificationCenter window (17:11Z), quoted as the Coordinator sent it to the operator at 17:14Z, with the live path of the tcc-who tool - the full text the unit template points at
status: done
activity: queue-planning
run_id: queue-planning-2026-11-26-1010-window-rule
trigger: Coordinator message 18:12Z (the template body limit)
started_at: 2026-11-26T10:08:00-08:00
finished_at: 2026-11-26T10:10:00-08:00
verified: the text is copied unchanged from /tmp/lw-op-python-rule.md (the Coordinator's order to the operator); the tool path read from the live tree
grounded_in:
  - source: _records_/2026-11-22/queue-planning/3125-plan-times-and-checks.md
---
# The UserNotificationCenter window rule, 3126

Steer A, 2026-11-26T17:11Z 'python rule approved' (the Coordinator's order to the operator, 17:14Z, quoted as sent). It replaces the plain 'one killall per window' for the case of a UserNotificationCenter window. Since the Toolsmith's tool landed, step (a) may be run by `_tools_/tcc-who/tcc_who.py pythons` (names only; it prints a `kill <pid>` line only for a session-inbox.py alive over 60 s that is not the DSH host, the bridge daemon or release-watch); the rule's three conditions are unchanged. Never write a command line in full.

Coordinator to Operator (Mac UTC 17:14Z) - STANDING ORDER (Steer A 17:11Z 'python rule approved': it REPLACES the plain 'one killall per window' FOR THE CASE OF A UserNotificationCenter WINDOW): THE REASON: THE 16:58Z AND 17:01Z WINDOWS WERE ONE HUNG HOMEBREW PYTHON (a session-inbox call) WALKING THE HOME FOLDER'S PROTECTED CHILDREN: OUR KILL OF THE WINDOW AT 17:01 DISMISSED ITS FIRST PROMPT AND LET IT ASK FOR THE NEXT FOLDER (Documents): WHEN A UserNotificationCenter WINDOW IS IN FRONT: (a) FIRST, READ ONLY (names only: NO FILE IS OPENED, THE WINDOW IS NEVER READ OR CLICKED): `pgrep -f 'Python.app'` THEN `ps -o pid,ppid,etime,command -p <those pids>`: THE RECORD WRITES ONLY THE SCRIPT'S FILE NAME, THE ELAPSED TIME AND THE PARENT'S NAME (a command line carries the owner's user name in its paths: NEVER WRITE A COMMAND LINE IN FULL): (b) KILL ONE PYTHON (`kill <pid>`, ONCE, NO -9) ONLY IF ALL THREE HOLD: (i) ITS COMMAND NAMES session-inbox.py (or a script the Toolsmith's lint flags as a home-rooted glob): (ii) ITS ELAPSED TIME IS OVER 60 SECONDS (a hung call): (iii) IT IS NOT THE DSH HOST ('dsh web'), NOT THE BRIDGE DAEMON (pid 1335), NOT release-watch.py, AND NOT ANYTHING WHOSE COMMAND DOES NOT MATCH (i): THE ORDER: THE PYTHON FIRST: THEN THE ONE `killall -9 UserNotificationCenter` AS BEFORE: THE FRONT RECORDED BEFORE AND AFTER (the standing front script once if LastWar is not back: idle at least 300 s): IF NO PYTHON MATCHES (the culprit already exited): ONLY THE ONE killall: IF THE WINDOW RETURNS WITHIN 10 MINUTES: STOP AND TELL ME: NO LOOP: THE RECORD: THE pid, THE SCRIPT'S FILE NAME, THE ELAPSED TIME, THE PARENT'S NAME, THE FRONT BEFORE AND AFTER: TELL ME IN THE FOUR LINES: I TELL THE [cu] COORDINATOR AND THE OWNING SEAT (a kill of another seat's hung call fails that call and nothing else): A macOS CONSENT WINDOW IS STILL NEVER READ OR ANSWERED.
