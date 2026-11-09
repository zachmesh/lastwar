#!/bin/bash
set -euo pipefail
cd /tmp/pi-0100-1109
echo "worktree HEAD: $(git rev-parse --short HEAD)"
echo "status before:"
git status --short

# 1. Append the day INDEX entry (same style as the 0045 entry).
cat >> _records_/2026-11-09/INDEX.md <<'EOF'

- Integrator pr-integration-2026-11-09-0100 (NON-batch).
  Checker due no (next batch 03:00 PT); no merges; records PRs
  493 and 491 clean against main e786ef8918, awaiting the
  03:00 batch; records PRs 478, 351, 301 still conflicted on
  the single action-log file, re-probed, scope unchanged;
  re-verification notes posted on 425, 301, 351, 478 against
  new main e786ef8918; tools PR 425 owner-gated, clean,
  unchanged (OD-20261108-01 open). No Slack sync by this
  run (no merges, no new escalation; silent in chat).
  Full detail in pr-integration/0100-run.md.
EOF

# 2. Append this run's own action-log line with the branch copy of log_append.py.
python3 -c 'import json,datetime; print(json.dumps({"action": "pr-integration run pr-integration-2026-11-09-0100: NON-batch pass (checker _tools_/records_batch.py due no, next batch 03:00 PT); no merges; no PRs opened; re-verification notes posted on tools PR 425 (owner-gated, clean against main e786ef8918, OD-20261108-01 open, no covering issue) and records PRs 301, 351, 478 (still conflicted on the single file _logs_/repo-actions/action-log.jsonl, re-probed, scope unchanged); records PRs 493 and 491 clean against main e786ef8918, awaiting the 03:00 batch; end-of-pass sweep: 6 open PRs, all decided, no unprocessed PRs", "actor": "lastwar-pr-integrator", "files": ["_records_/2026-11-09/pr-integration/0100-run.md", "_records_/2026-11-09/INDEX.md", "_logs_/repo-actions/action-log.jsonl"], "reason": "owner-directed PR-only policy 2.0.0/2.3.0 and full-sweep rule; this run own action-log line, committed to the records branch so it rides records PR 493", "ts": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}))' | python3 _tools_/log_append.py append --file _logs_/repo-actions/action-log.jsonl --stdin

# 3. Re-validate the action log with the branch copy.
python3 _tools_/log_append.py check --file _logs_/repo-actions/action-log.jsonl

echo "status after:"
git status --short
git diff --stat

# 4. Commit and push to records/2026-11-09.
git add _records_/2026-11-09/pr-integration/0100-run.md _records_/2026-11-09/INDEX.md _logs_/repo-actions/action-log.jsonl
git commit -m "records: pr-integration 2026-11-09 0100 run (non-batch, no merges, 4 re-verification notes)"
NEW_HEAD=$(git rev-parse HEAD)
echo "committed: $NEW_HEAD"
git push github HEAD:records/2026-11-09
echo "ls-remote after push:"
git ls-remote github 'records/2026-11-09'
echo "pushed commit files:"
git show --stat --format='%h %s' HEAD | head -10
