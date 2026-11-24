---
title: Troop training finished batch lesson
created: 2026-11-24T04:15:43Z
modified: 2026-11-24T04:15:43Z
version: 0.1.0
description: The dated lesson of 2026-11-24 - a Drill Ground Full toast does not mean idle, because a finished batch can wait behind it; one pistol press per barracks per read when room could exist
---

# Troop training finished batch lesson

Dated 2026-11-24, from the Coach's idle-blocked audit (`_records_/2026-11-22/coach/idle-blocked-audit.csv`) and Steer A's ruling of 04:13Z. Back to the [rule digest](rule-digest.md).

## The rule

Press the pistol once per barracks per read whenever room could exist. The toast "Drill Ground Full" is identical for an empty queue and for a finished batch waiting behind room 0, so a read classifies each barracks as EMPTY QUEUE, FINISHED BATCH WAITING (with its size) or BLOCKED BY THE TOAST in this read, and records the ready bubble per tent. A toast alone is never "idle".

## The two precedents

The knowledge was already there. On 2026-11-10 (12:29 PT, `_records_/2026-11-10/troop-training/1229-queue-run.md`) the pistol collected the finished Lv.24 batch on the tap; on 2026-11-22 (10:05 PT, `_records_/2026-11-22/arms-race/1005-queue-run.md`) a finished Lv.24 batch of 143 Lv.8 was collected. The 11-23 read schema still wrote "idle, blocked": the failure was knowledge that did not carry.

## The case of 2026-11-23

A Lv.24 barracks held a finished batch of 274 (collected 03:51Z, +291,262) under four "idle, blocked" reads, and a Lv.27 one held 726 (collected 03:30:53Z). Room was 0 until the siege freed it (01:15Z to 01:51Z), so no earlier read could have collected them: the cost is the delay after room opened, 120 and 99 minutes, nothing permanent.

## Open

- Who queued the 274 after 11-22 10:09 PT (666 queued on 11-10, 143 on 11-22)? An unexplained batch may be the owner's own queue (the phone), which units must not disturb.
- The next presses: the Lv.20 barracks (empty by the bubble census [G]) and the Lv.30 batch at 11:18Z, a free test of whether a collect with room below the batch size succeeds.
