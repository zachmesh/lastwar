#!/usr/bin/env python3
"""home_glob_check: finds code that globs, lists or walks from the home folder (read-only; Steer A and the Coach, 2026-11-26).

On 2026-11-26 a tool's `glob(~/*/*/TEAM.yaml)` walked Desktop, Documents, Music and Library and made macOS ask for them (the same breach as `ls ~`:
~/.dsh/AGENTS.md forbids it). This reads source and flags, never runs it:
  - a path pattern whose FIRST component under the home folder is a wildcard (`Path.home() / "*"`, "~/*/x", "$HOME/*");
  - a listing (listdir, scandir, iterdir, glob, rglob, os.walk) whose base is the home folder itself or Desktop, Documents, Downloads, Music,
    Movies, Pictures or Public (or Library itself) under it;
  - the same in shell (`ls ~`, `find ~`, `for f in ~/*`, `ls ~/Desktop`) and in Node (`readdir(os.homedir())`).
A named root passes (`~/.dsh/sessions/*/x`, `~/.computer-use`, `~/dtadpole/reflection/x`). `home-glob: ok <reason>` on the line or the line above
allows one. Python is read with `ast` (docstrings and comments never count); a name set from the home folder is followed within the file.

  home_glob_check.py [--root DIR] [--staged] [PATH...]   exit 0 clean, 1 findings, 2 cannot read
"""
from __future__ import annotations

import argparse
import ast
import os
import re
import subprocess
import sys
from pathlib import Path

PROTECTED = {"desktop", "documents", "downloads", "music", "movies", "pictures", "public"}
LIBRARY_PROTECTED = {"mail", "messages", "safari", "calendars", "cookies", "application support", "containers", "group containers", "photos", "homekit",
                     "suggestions", "accounts", "findmy", "metadata", "preferences", "keychains", "autosave information"}      # Library itself is flagged; LaunchAgents is not
LISTERS = {"listdir", "scandir", "walk", "iterdir", "glob", "iglob", "rglob"}
EXTENSIONS = {".py": "python", ".sh": "shell", ".bash": "shell", ".mjs": "node", ".js": "node", ".cjs": "node"}
ALLOW = re.compile(r"home-glob:\s*ok")
WILD = re.compile(r"[*?\[]")
UNKNOWN = "<unknown>"                                         # a component we cannot read: never a wildcard, never a protected name


def split_components(text: str) -> list[str]:
    return [c for c in text.split("/") if c]


def home_prefix(text: str):
    """The components after a home prefix in a string (`~`, `$HOME`, `/Users/<name>`), or None when the string is not home-rooted."""
    for prefix in ("~", "$HOME", "${HOME}"):
        if text == prefix or text.startswith(prefix + "/"):
            return split_components(text[len(prefix):])
    m = re.match(r"^/Users/[^/]+(/.*)?$", text)
    if m:
        return split_components(m.group(1) or "")
    return None


class PythonScan(ast.NodeVisitor):
    def __init__(self, source: str):
        self.findings: list[tuple[int, str]] = []
        self.tainted: dict[str, list] = {}
        self.docstrings: set[int] = set()
        tree = ast.parse(source)
        for node in ast.walk(tree):                                   # string statements (docstrings) are text, not paths
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                self.docstrings.add(id(node.value))
        self.taint_body(tree.body)                                    # module level first; every function gets its own scope below
        self.visit(tree)

    def taint_body(self, body):
        """Names assigned a home expression in these statements (nested function bodies are their own scope)."""
        for stmt in body:
            for node in ast.walk(stmt) if not isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) else []:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                    comps = self.comps(node.value)
                    if comps is not None:
                        self.tainted[node.targets[0].id] = comps

    def visit_FunctionDef(self, node):
        saved = dict(self.tainted)
        params = node.args.posonlyargs + node.args.args + node.args.kwonlyargs + ([node.args.vararg] if node.args.vararg else []) + \
            ([node.args.kwarg] if node.args.kwarg else [])
        for param in params:                                          # a parameter shadows a module-level name: it is whatever the caller passes
            self.tainted.pop(param.arg, None)
        defaults = list(zip(reversed(node.args.args), reversed(node.args.defaults))) + [
            (a, d) for a, d in zip(node.args.kwonlyargs, node.args.kw_defaults) if d is not None]
        for param, default in defaults:                               # unless its default IS the home folder
            comps = self.comps(default)
            if comps is not None:
                self.tainted[param.arg] = comps
        self.taint_body(node.body)
        self.generic_visit(node)
        self.tainted = saved

    visit_AsyncFunctionDef = visit_FunctionDef

    def comps(self, node):
        """Components under the home folder when `node` is a home-rooted path expression (None when it is not or cannot be told)."""
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return None if id(node) in self.docstrings else home_prefix(node.value)
        if isinstance(node, ast.Name):
            return self.tainted.get(node.id)
        if isinstance(node, ast.JoinedStr):
            head = node.values[0] if node.values else None
            if isinstance(head, ast.Constant) and isinstance(head.value, str):
                got = home_prefix(head.value.rstrip("/") + ("/" if len(node.values) > 1 and head.value.endswith("/") else ""))
                if got is not None and len(node.values) > 1:
                    return got + [UNKNOWN] if head.value.endswith("/") else got
                return got
            return None
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Div, ast.Add)):
            left = self.comps(node.left)
            if left is None:
                return None
            if isinstance(node.right, ast.Constant) and isinstance(node.right.value, str):
                return left + split_components(node.right.value)
            return left + [UNKNOWN]
        if isinstance(node, ast.BoolOp):                              # home or Path.home(): rooted when an operand is
            for value in node.values:
                got = self.comps(value)
                if got is not None:
                    return got
            return None
        if isinstance(node, ast.IfExp):
            return self.comps(node.body) if self.comps(node.body) is not None else self.comps(node.orelse)
        if isinstance(node, ast.Subscript):                           # os.environ["HOME"]
            if isinstance(node.value, ast.Attribute) and node.value.attr == "environ" and isinstance(node.slice, ast.Constant) \
                    and node.slice.value == "HOME":
                return []
            return None
        if isinstance(node, ast.Call):
            name = call_name(node)
            args = node.args
            if name == "home" and not args and isinstance(node.func, ast.Attribute) and (
                    (isinstance(node.func.value, ast.Name) and node.func.value.id in ("Path", "PurePath"))
                    or (isinstance(node.func.value, ast.Attribute) and node.func.value.attr in ("Path", "PurePath"))):     # Path.home(), not a local home()
                return []
            if name == "expanduser" and isinstance(node.func, ast.Attribute) and not args:     # Path("~/x").expanduser()
                return self.comps(node.func.value)
            if name in ("expanduser", "str", "Path", "PurePath", "resolve", "realpath", "abspath", "normpath", "fspath") and args:
                return self.comps(args[0])
            if name in ("resolve", "absolute") and isinstance(node.func, ast.Attribute):
                return self.comps(node.func.value)
            if name == "get" and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Attribute) \
                    and node.func.value.attr == "environ" and args and isinstance(args[0], ast.Constant) and args[0].value == "HOME":
                return []
            if name == "join" and args:
                base = self.comps(args[0])
                if base is None:
                    return None
                out = list(base)
                for a in args[1:]:
                    out += split_components(a.value) if isinstance(a, ast.Constant) and isinstance(a.value, str) else [UNKNOWN]
                return out
            if name == "joinpath" and isinstance(node.func, ast.Attribute):
                base = self.comps(node.func.value)
                if base is None:
                    return None
                out = list(base)
                for a in args:
                    out += split_components(a.value) if isinstance(a, ast.Constant) and isinstance(a.value, str) else [UNKNOWN]
                return out
        return None

    def bad(self, comps) -> str:
        if comps is None:
            return ""
        if not comps:
            return "the home folder itself"
        first = comps[0]
        if WILD.search(first):
            return "a wildcard directly under the home folder"
        if first.lower() in PROTECTED:
            return f"a protected folder ({first}) under the home folder"
        if first.lower() == "library" and (len(comps) == 1 or WILD.search(comps[1]) or comps[1].lower() in LIBRARY_PROTECTED):
            return "Library or a protected folder in it"
        return ""

    def visit_Call(self, node: ast.Call):
        name = call_name(node)
        if name in LISTERS:
            target = None
            if isinstance(node.func, ast.Attribute) and name in ("iterdir", "glob", "rglob") and not (
                    isinstance(node.func.value, ast.Name) and node.func.value.id in ("glob", "os")):
                base = self.comps(node.func.value)
                if base is not None:
                    extra = split_components(node.args[0].value) if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str) else (
                        [UNKNOWN] if node.args else [])
                    target = base if name in ("iterdir", "rglob") else base + extra          # rglob recurses: its base alone decides
            elif node.args:
                target = self.comps(node.args[0])
            why = self.bad(target)
            if why:
                self.findings.append((node.lineno, f"{name}() over {why}"))
        self.generic_visit(node)

    def visit_BinOp(self, node: ast.BinOp):
        self.check_expression(node)
        self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant):
        if isinstance(node.value, str):
            self.check_expression(node)

    def check_expression(self, node):
        comps = self.comps(node)
        if comps and WILD.search(comps[0]):
            self.findings.append((node.lineno, "a path pattern with a wildcard directly under the home folder"))


def call_name(node: ast.Call) -> str:
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    if isinstance(node.func, ast.Name):
        return node.func.id
    return ""


SHELL_COMMANDS = r"(?:ls|find|du|tree|cat|grep|rg|fd|rsync|cp|mv|rm|open|stat|wc|head|tail|xargs|mdfind|for\s+\w+\s+in)"
HOME_ARG = re.compile(r"(?<![\w/.\-])(?:~|\$HOME|\$\{HOME\})(?:/(?:\*|" + "|".join(sorted(p.capitalize() for p in PROTECTED)) +
                      r")(?![\w.\-])\S*|/?(?=[\s\"';|&)]|$))")


def scan_shell(text: str):
    out = []
    for number, line in enumerate(text.splitlines(), 1):
        code = line.split("#", 1)[0] if not re.search(r"""["'][^"']*#""", line) else line
        if not re.search(r"(^|[\s;&|(`$])" + SHELL_COMMANDS + r"\b", code):
            continue
        for m in HOME_ARG.finditer(code):
            arg = m.group(0)
            if arg.startswith(("~", "$HOME", "${HOME}")) and arg.rstrip("/") in ("~", "$HOME", "${HOME}") or re.search(r"/(\*|[A-Z])", arg):
                out.append((number, "a shell command over the home folder, a wildcard under it or a protected folder"))
                break
    return out


NODE_CALL = re.compile(r"(?:readdir|readdirSync|opendir|opendirSync|glob|globSync|scandir)\s*\(")
NODE_HOME_EXPR = r"(?:os\.homedir\(\)|process\.env\.HOME|homedir\(\))"


def balanced(text: str, start: int) -> str:
    """The text between the parenthesis that opens at `start - 1` and its match (or to the end of the line)."""
    depth = 1
    for i in range(start, len(text)):
        depth += {"(": 1, ")": -1}.get(text[i], 0)
        if depth == 0:
            return text[start:i]
    return text[start:]


def first_argument(args: str) -> str:
    depth = 0
    for i, ch in enumerate(args):
        depth += {"(": 1, "[": 1, "{": 1, ")": -1, "]": -1, "}": -1}.get(ch, 0)
        if ch == "," and depth == 0:
            return args[:i].strip()
    return args.strip()


def node_argument_bad(arg: str) -> bool:
    arg = arg.strip()
    if re.fullmatch(NODE_HOME_EXPR, arg):                                                   # the home folder itself
        return True
    m = re.fullmatch(r"(?:path\.)?join\(\s*" + NODE_HOME_EXPR + r"\s*(?:,(.*))?\)", arg)
    if m:
        parts = re.findall(r"""['"`]([^'"`]*)['"`]""", m.group(1) or "")
        first = split_components(parts[0])[0] if parts and split_components(parts[0]) else ""
        return not first or bool(WILD.search(first)) or first.lower() in PROTECTED
    m = re.fullmatch(NODE_HOME_EXPR + r"\s*\+\s*['\"`]/?([^'\"`/]*)[^'\"`]*['\"`]", arg)
    if m:
        return not m.group(1) or bool(WILD.search(m.group(1))) or m.group(1).lower() in PROTECTED
    m = re.fullmatch(r"`\$\{" + NODE_HOME_EXPR + r"\}/?([^`/]*)[^`]*`", arg)
    if m:
        return not m.group(1) or bool(WILD.search(m.group(1))) or m.group(1).lower() in PROTECTED
    m = re.fullmatch(r"['\"`](~[^'\"`]*)['\"`]", arg)
    if m:
        comps = home_prefix(m.group(1))
        return comps is not None and (not comps or bool(WILD.search(comps[0])) or comps[0].lower() in PROTECTED)
    return False


def scan_node(text: str):
    out = []
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("//"):
            continue
        for m in NODE_CALL.finditer(line):
            if node_argument_bad(first_argument(balanced(line, m.end()))):
                out.append((number, "a Node listing over the home folder, a wildcard under it or a protected folder"))
                break
    return out


def allowed(lines: list[str], number: int) -> bool:
    here = lines[number - 1] if 0 < number <= len(lines) else ""
    before = lines[number - 2] if number >= 2 else ""
    return bool(ALLOW.search(here) or ALLOW.search(before))


def scan_text(path: str, text: str, kind: str):
    try:
        found = PythonScan(text).findings if kind == "python" else scan_shell(text) if kind == "shell" else scan_node(text)
    except SyntaxError:
        return [(1, "unreadable Python (syntax error): not checked")] if kind == "python" else []
    lines = text.splitlines()
    return sorted({(n, why) for n, why in found if not allowed(lines, n)})


def files_under(paths: list[Path]):
    for base in paths:
        if base.is_file():
            if base.suffix in EXTENSIONS:
                yield base
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames if d not in (".git", "node_modules", "__pycache__"))
            for name in sorted(filenames):
                if Path(name).suffix in EXTENSIONS:
                    yield Path(dirpath) / name


def staged_files(root: Path):
    out = subprocess.run(["git", "-C", str(root), "diff", "--cached", "--name-only", "--diff-filter=ACMR"], capture_output=True, text=True)
    if out.returncode != 0:
        raise OSError("git diff --cached failed")
    for rel in out.stdout.splitlines():
        if Path(rel).suffix in EXTENSIONS:
            blob = subprocess.run(["git", "-C", str(root), "show", f":{rel}"], capture_output=True)
            if blob.returncode == 0:
                yield rel, blob.stdout.decode("utf-8", errors="replace")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="home_glob_check.py", description=__doc__.split("\n\n")[0])
    p.add_argument("paths", nargs="*")
    p.add_argument("--root", default=str(Path(__file__).resolve().parent.parent.parent))
    p.add_argument("--staged", action="store_true", help="the staged blobs of .py, .sh and Node files in the repository at --root")
    a = p.parse_args(argv)
    root = Path(a.root)
    findings, checked = [], 0
    try:
        if a.staged:
            sources = list(staged_files(root))
        else:
            targets = [Path(x) for x in a.paths] or [root / "_tools_"]
            sources = []
            for f in files_under(targets):
                sources.append((str(f.relative_to(root)) if f.is_relative_to(root) else str(f), f.read_text(encoding="utf-8", errors="replace")))
    except OSError as exc:
        print(f"home_glob_check: cannot read: {exc.__class__.__name__}", file=sys.stderr)
        return 2
    for rel, text in sources:
        checked += 1
        for number, why in scan_text(rel, text, EXTENSIONS.get(Path(rel).suffix, "python")):
            findings.append((rel, number, why))
    for rel, number, why in findings:
        print(f"{rel}:{number}: {why}")
    print(f"home_glob_check: {len(findings)} finding(s) in {checked} file(s)"
          + ("; a named root passes, or put 'home-glob: ok <reason>' on the line (roots are named paths: ~/.dsh/AGENTS.md)" if findings else ""))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
