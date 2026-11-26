#!/usr/bin/env python3
"""Repo audit for the IBM notes + LumenVenture SDLC guide.

Checks, for every Markdown/SVG file under the given paths (default: whole repo):
  1. Relative links point to files that exist, and #anchors exist (GitHub slug rules).
  2. Mermaid: no `flowchart LR`; edge labels |...| contain no ( ) < > " characters.
  3. SVG files are well-formed XML.
  4. File and folder names are Windows-safe (same rules as .githooks/pre-commit).
  5. Course notes: every "⚠️ **Correction" badge has a "Lecture wording (for the quiz)" line.
Optional:
  --leak "phrase"   report lines containing a wrong (corrected) phrase outside quiz lines,
                    badges and comparison tables' "Lecture" column (repeatable).
  --keys FILE       one phrase per line; report phrases missing from the --note file
                    (cheap coverage check: list 30-60 key phrases of the transcript).
  --note FILE       the note used by --keys.
  --acronyms        course notes only: report acronyms that are never expanded in the note
                    (look for "ABC (Full Form)" or "Full Form (ABC)").
  --leak-file FILE  like --leak, one wrong phrase per line.

Exit code 1 if any problem is found. Run from the repo root:
  python .claude/skills/new-lecture/scripts/audit.py
  python .claude/skills/new-lecture/scripts/audit.py SDLC
  python .claude/skills/new-lecture/scripts/audit.py course-1-*/module-1-*/notes/08-software-testing.md --leak "ensure error-free"
"""
import argparse
import glob
import os
import re
import sys
import xml.dom.minidom

SKIP_DIRS = {".git", "node_modules", ".claude", ".transcripts"}
SKIP_FILES = {"master-prompt.md"}  # contains example paths and rule text, not real links or diagrams
BAD_NAME = re.compile(r'[:*?"<>|\\]')
ACRO_IGNORE = {"OK", "PR", "TODO", "GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "NOT", "MUST", "ONLY",
               "NEVER", "AND", "OR", "WHAT", "HOW", "WHY", "SHOULD", "MAY", "ALWAYS", "NO", "YES", "UTF", "LF", "PX", "MS", "KB",
               "MB", "GB", "ID", "TV", "AA", "AAA", "LEGO", "IBM", "AWS", "PHP", "NGINX", "WHATWG", "IDEA", "FAQ", "AI", "ES", "DB", "JS"}
ROMAN = re.compile(r"^[IVXL]+$")
RESERVED = re.compile(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(\.|$)", re.I)


def slug(heading: str) -> str:
    h = re.sub(r"[*`_]", "", heading).strip().lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


_anchor_cache: dict[str, set[str]] = {}


def anchors(path: str) -> set[str]:
    if path not in _anchor_cache:
        text = open(path, encoding="utf-8").read()
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        seen: dict[str, int] = {}
        out: set[str] = set()
        for m in re.findall(r"^#{1,6}\s+(.*)$", text, flags=re.M):
            a = slug(m)
            if a in seen:
                seen[a] += 1
                a = f"{a}-{seen[a]}"
            else:
                seen[a] = 0
            out.add(a)
        _anchor_cache[path] = out
    return _anchor_cache[path]


def collect(paths: list[str]) -> list[str]:
    files: list[str] = []
    for p in paths or ["."]:
        for g in glob.glob(p) or [p]:
            if os.path.isfile(g):
                files.append(g)
                continue
            for root, dirs, names in os.walk(g):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                files += [os.path.join(root, n) for n in names]
    return sorted(set(os.path.normpath(f) for f in files if os.path.basename(f) not in SKIP_FILES))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--leak", action="append", default=[])
    ap.add_argument("--keys")
    ap.add_argument("--note")
    ap.add_argument("--acronyms", action="store_true")
    ap.add_argument("--leak-file")
    args = ap.parse_args()

    problems: list[str] = []
    files = collect(args.paths)
    if args.leak_file:
        args.leak += [l.strip() for l in open(args.leak_file, encoding="utf-8") if l.strip()]

    for f in files:
        for part in f.replace("\\", "/").split("/"):
            if part in (".", ".."):
                continue
            if BAD_NAME.search(part) or part.endswith((" ", ".")) or part.startswith(" ") or RESERVED.match(part):
                problems.append(f"NAME   {f}: '{part}' is not Windows-safe")

        if f.endswith(".svg"):
            try:
                xml.dom.minidom.parse(f)
            except Exception as e:  # noqa: BLE001
                problems.append(f"SVG    {f}: {e}")
            continue
        if not f.endswith(".md"):
            continue

        text = open(f, encoding="utf-8").read()
        no_code = re.sub(r"```.*?```", "", text, flags=re.S)
        for link in re.findall(r"\]\(([^)\s]+)\)", no_code):
            if re.match(r"^[a-z]+:", link):
                continue
            target, _, anchor = link.partition("#")
            full = os.path.normpath(os.path.join(os.path.dirname(f), target)) if target else f
            if not os.path.exists(full):
                problems.append(f"LINK   {f}: missing {link}")
            elif anchor and full.endswith(".md") and anchor not in anchors(full):
                problems.append(f"ANCHOR {f}: no heading for #{anchor}")

        for block in re.findall(r"```mermaid(.*?)```", text, flags=re.S):
            if re.search(r"flowchart\s+LR|graph\s+LR", block):
                problems.append(f"MERMAID {f}: horizontal layout (use flowchart TD)")
            for label in re.findall(r"\|([^|\n]*)\|", block):
                if re.search(r'[()<>"]', label):
                    problems.append(f"MERMAID {f}: edge label has ( ) < > or quotes: |{label}|")

        if "/notes/" in f.replace("\\", "/"):
            badges = text.count("⚠️ **Correction")
            quiz = text.count("Lecture wording (for the quiz)")
            if badges != quiz:
                problems.append(f"BADGE  {f}: {badges} correction badges but {quiz} quiz-wording lines")
            for phrase in args.leak:
                for n, line in enumerate(text.splitlines(), 1):
                    if phrase.lower() in line.lower() and "Lecture wording" not in line and not line.startswith("> ⚠️"):
                        problems.append(f"LEAK   {f}:{n}: '{phrase}' outside a quiz line (OK only in a 'Lecture' table column): {line[:100]}")

    if args.acronyms:
        for f in files:
            if not f.endswith(".md") or "/notes/" not in f.replace("\\", "/"):
                continue
            t = open(f, encoding="utf-8").read()
            t = re.sub(r"```.*?```", "", t, flags=re.S)
            t = re.sub(r"`[^`\n]*`", "", t)
            t = re.sub(r"\]\([^)]*\)", "]", t)
            t = re.sub(r"https?://\S+", "", t)
            seen: set[str] = set()
            for m in re.finditer(r"(?<![A-Za-z0-9_/.\-])([A-Z][A-Z0-9]{1,6})(?![A-Za-z0-9_/\-])", t):
                a = m.group(1)
                if a in seen or a in ACRO_IGNORE or ROMAN.match(a) or re.search(r"\d", a):
                    continue
                seen.add(a)
                # expanded somewhere in the file: "ABC (Full Form)", "(ABC)", "(ABC," or "(the ABC, or ...)"
                if re.search(r"\b" + a + r"\b[*_]*\s*\(|\([^)\n]{0,40}\b" + a + r"\b", t):
                    continue
                n = t.count("\n", 0, m.start()) + 1
                problems.append(f"ACRONYM {f}: '{a}' (first used about line {n}) is never expanded")

    if args.keys:
        note = open(args.note, encoding="utf-8").read().lower() if args.note else ""
        for key in open(args.keys, encoding="utf-8").read().splitlines():
            if key.strip() and key.strip().lower() not in note:
                problems.append(f"KEY    missing from note: {key.strip()}")

    md = sum(f.endswith(".md") for f in files)
    svg = sum(f.endswith(".svg") for f in files)
    for p in problems:
        print(p)
    print(f"\nChecked {md} Markdown and {svg} SVG files: {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
