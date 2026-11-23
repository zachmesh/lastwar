---
title: The rule
created: 2026-11-23T08:37:00Z
modified: 2026-11-23T08:37:00Z
version: 0.1.0
sequence: 2
description: Main advances only by pull request merge.
---
## The rule

Main advances only by pull request merge. No job, agent or
script pushes directly to main, for any path. The tier-1
direct-push tier of version 1.0.0 is abolished: there is no
class of file that may be committed straight to main. Every
commit that lands on main is a pull request merge - a squash
merge for knowledge and code, a merge commit for records -
recognisable in the commit graph by its pull request
reference. The single exception is the break-glass clause
below.

