"""Tests for answering a model question through the bridge (`respond`) and for reporting a run that waits on, or ended on, a question
(`status`). A fake MCP server that speaks computer_use_start, status and respond stands in for the real one; nothing real is touched.
Like the other bridge tests these are SKIPPED while `_queue_/claimed/` holds a file.

Run: python3 -m unittest discover -s _tools_/cu-bridge-tests
"""
from __future__ import annotations

import json

from test_cu_bridge import BridgeCase, FAKE_SERVER

QUESTION = "Which hero should lead the squad?"
# Question flow on top of the lifecycle fake: FAKE_QUESTION keeps a pending question q-1 in status until computer_use_respond answers it;
# FAKE_ENDED makes status report a finished run whose result is needs_input with the question as its final message.
QUESTION_SERVER = FAKE_SERVER.replace(
    '        elif name == "computer_use_status":',
    '''        elif name == "computer_use_respond":
            rid = args.get("run_id")
            if rid not in runs:
                say(mid, {"content": [{"type": "text", "text": "error: no run in this server"}], "isError": True})
            elif args.get("question_id") != "q-1" or os.path.exists(os.environ["FAKE_ANSWER"]):
                say(mid, {"content": [{"type": "text", "text": "question '%s' is not pending in run %s" % (args.get("question_id"), rid)}], "isError": True})
            else:
                open(os.environ["FAKE_ANSWER"], "w").write(args.get("answer", ""))
                text(mid, {"run_id": rid, "state": "running"})
        elif name == "computer_use_status" and args.get("run_id") in runs and os.environ.get("FAKE_ENDED"):
            text(mid, {"run_id": args["run_id"], "state": "finished", "question": None,
                       "result": {"status": "needs_input", "finalMessage": os.environ["FAKE_QUESTION_TEXT"]}})
        elif name == "computer_use_status" and args.get("run_id") in runs and os.environ.get("FAKE_QUESTION") and not os.path.exists(os.environ["FAKE_ANSWER"]):
            text(mid, {"run_id": args["run_id"], "state": "running", "question": {"question_id": "q-1", "text": os.environ["FAKE_QUESTION_TEXT"]}})
        elif name == "computer_use_status":''', 1)


class QuestionCase(BridgeCase):
    def setUp(self):
        super().setUp()
        (self.root / "fake" / "_tools_" / "computer-use-mcp" / "server.mjs").write_text(QUESTION_SERVER)
        self.answer = self.root / "answer"
        self.env.update(FAKE_ANSWER=str(self.answer), FAKE_QUESTION_TEXT=QUESTION)

    def status(self, run_id):
        r = self.run_bridge("status", "--run-id", run_id)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return r, json.JSONDecoder().raw_decode(r.stdout)[0]

    def record(self, run_id):
        return next(r for r in json.loads((self.root / "_tools_/state/cu_runs.json").read_text())["runs"] if r["run_id"] == run_id)


class Pending(QuestionCase):
    def test_a_pending_question_is_reported_with_the_exact_answer_command(self):
        self.env["FAKE_QUESTION"] = "1"
        run_id = self.start_run()
        r, body = self.status(run_id)
        self.assertEqual(body["question"], {"question_id": "q-1", "text": QUESTION})
        self.assertIn("QUESTION PENDING in run", body["bridge_note"])
        self.assertIn(f"respond --run-id {run_id} --question-id q-1 --answer", body["bridge_note"])
        self.assertIn("QUESTION PENDING", r.stderr)
        rec = self.record(run_id)
        self.assertEqual((rec["question_id"], rec["question"], rec["ended_on_question"]), ("q-1", QUESTION, False))

    def test_respond_delivers_the_answer_intact_and_clears_the_question(self):
        self.env["FAKE_QUESTION"] = "1"
        run_id = self.start_run()
        answer = 'Use "Murphy" - then the second tab,\nand stop there'
        r = self.run_bridge("respond", "--run-id", run_id, "--question-id", "q-1", "--answer", answer)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.answer.read_text(), answer)
        self.assertEqual(json.loads(r.stdout)["state"], "running")
        _r, body = self.status(run_id)
        self.assertNotIn("bridge_note", body)
        rec = self.record(run_id)
        self.assertEqual((rec["question_id"], rec["question"]), ("", ""))
        self.assertIn("answered_at", rec)

    def test_a_wrong_question_id_is_refused_and_the_question_stays_pending(self):
        self.env["FAKE_QUESTION"] = "1"
        run_id = self.start_run()
        r = self.run_bridge("respond", "--run-id", run_id, "--question-id", "q-9", "--answer", "x")
        self.assertEqual(r.returncode, 1)
        self.assertIn("respond refused: question 'q-9' is not pending", r.stderr)
        self.assertFalse(self.answer.exists())
        self.assertIn("QUESTION PENDING", self.status(run_id)[1]["bridge_note"])

    def test_a_blank_answer_is_exit_two_and_sends_nothing(self):
        self.env["FAKE_QUESTION"] = "1"
        run_id = self.start_run()
        for blank in ("", "   "):
            r = self.run_bridge("respond", "--run-id", run_id, "--question-id", "q-1", "--answer", blank)
            self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertFalse(self.answer.exists())

    def test_a_run_the_server_does_not_know_is_refused_cleanly(self):
        self.start_run()
        r = self.run_bridge("respond", "--run-id", "run-nope", "--question-id", "q-1", "--answer", "x")
        self.assertEqual(r.returncode, 1)
        self.assertIn("respond refused: error: no run in this server", r.stderr)


class Ended(QuestionCase):
    def test_a_run_that_ended_on_a_question_is_reported_as_one_and_not_as_a_timeout(self):
        self.env["FAKE_ENDED"] = "1"
        run_id = self.start_run()
        r, body = self.status(run_id)
        self.assertEqual(body["result"]["status"], "needs_input")
        self.assertIn(f"RUN {run_id} ENDED ON A QUESTION (needs_input), not a timeout", body["bridge_note"])
        self.assertIn(QUESTION, body["bridge_note"])
        self.assertIn("never ask", body["bridge_note"])
        self.assertIn("ENDED ON A QUESTION", r.stderr)
        rec = self.record(run_id)
        self.assertEqual((rec["ended_on_question"], rec["question"]), (True, QUESTION))

    def test_a_run_that_simply_runs_gets_no_note_and_an_unchanged_body(self):
        run_id = self.start_run()
        r, body = self.status(run_id)
        self.assertEqual({k: v for k, v in body.items() if not k.startswith("bridge_")}, {"state": "awaiting_consent"})    # only the owner-idle and project values are added
        self.assertNotIn("bridge_note", r.stdout)
        self.assertEqual(r.stderr.strip().splitlines(), [f"cu_bridge: {body['bridge_owner_idle']}", f"cu_bridge: {body['bridge_project']}"])   # and its two lines, nothing else
        self.assertFalse(self.record(run_id)["ended_on_question"])


if __name__ == "__main__":
    import unittest
    unittest.main()
