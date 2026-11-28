#!/usr/bin/env python3
"""Checks for the SDLC folder (standard library only). Run from anywhere:  python3 tools/check.py

Fails (exit 1) when it finds:
  LINK     a relative link whose file does not exist, or whose #anchor does not exist
  OUTSIDE  a relative link that leaves this folder (the guide must be self-contained)
  RULES    a numbered rule list ("N. **must|should|may**") with a skipped or duplicate number
  UNLINKED a file in templates/ or images/ that no Markdown file mentions
  REF      words that point to course material (lecture, course note, module N, note NN, transcript)
  OVERDUE  a phase file or README whose "Next review due" date has passed
  RACI     a phase file's RACI table differs from its copy in README §3.1
CHANGELOG.md is exempt from REF (it is history).
"""
import datetime, glob, os, re, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
os.chdir(ROOT)
problems = []


def slug(h):
    h = re.sub(r"[*`_]", "", h).strip().lower()
    return re.sub(r"[^\w\- ]", "", h).replace(" ", "-")


def anchors(path):
    text = re.sub(r"```.*?```", "", open(path, encoding="utf-8").read(), flags=re.S)
    seen, out = {}, set()
    for h in re.findall(r"^#{1,6}\s+(.*)$", text, flags=re.M):
        a = slug(h)
        if a in seen:
            seen[a] += 1
            a = f"{a}-{seen[a]}"
        else:
            seen[a] = 0
        out.add(a)
    return out


mds = sorted(glob.glob("**/*.md", recursive=True))
texts = {f: open(f, encoding="utf-8").read() for f in mds}
cache = {}
for f, t in texts.items():
    body = re.sub(r"```.*?```", "", t, flags=re.S)
    for n, line in enumerate(body.splitlines(), 1):
        for m in re.finditer(r"\]\(([^)\s#]*)(#[^)\s]*)?\)", line):
            url, frag = m.group(1), (m.group(2) or "")[1:]
            if re.match(r"(https?:|mailto:)", url):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(f), url)) if url else f
            if target.startswith(".."):
                problems.append(f"OUTSIDE {f}: link leaves the SDLC folder: {url}")
                continue
            if not os.path.exists(target):
                problems.append(f"LINK    {f}: missing file {url}")
            elif frag and target.endswith(".md"):
                cache.setdefault(target, anchors(target))
                if slug(frag) not in cache[target] and frag not in cache[target]:
                    problems.append(f"LINK    {f}: missing anchor #{frag} in {target}")

for f, t in texts.items():
    prev = 0
    for n, line in enumerate(t.splitlines(), 1):
        m = re.match(r"^(\d+)\. \*\*(must|should|may)", line)
        if m:
            k = int(m.group(1))
            if k != prev + 1 and k != 1:
                problems.append(f"RULES   {f}:{n}: rule {k} follows rule {prev}")
            prev = k
        elif line.startswith(("#", "---")):
            prev = 0

alltext = "\n".join(texts.values())
for p in glob.glob("*/templates/*") + glob.glob("**/images/*", recursive=True):
    if os.path.isfile(p) and os.path.basename(p) not in alltext:
        problems.append(f"UNLINKED {p}: not mentioned in any Markdown file")

ref = re.compile(r"\b[Ll]ecture\b|\b[Cc]ourse notes?\b|\bmodule[- ]\d|\bnote[- ]\d\d|[Tt]ranscript")
for f, t in texts.items():
    if f == "CHANGELOG.md":
        continue
    for n, line in enumerate(re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), t, flags=re.S).splitlines(), 1):
        if ref.search(line):
            problems.append(f"REF     {f}:{n}: course reference: {line.strip()[:80]}")

# RACI: each phase file's Owners table must equal its README §3.1.N table
phase_files = {"Planning": "01-Planning/Planning.md", "Design": "02-Design/Design.md",
               "Development": "03-Development/Development.md", "Testing": "04-Testing/Testing.md",
               "Deployment": "05-Deployment/Deployment.md", "Maintenance": "06-Maintenance/Maintenance.md"}


def first_table(text):
    rows, started = [], False
    for line in text.splitlines():
        if line.startswith("|"):
            rows.append(line.strip())
            started = True
        elif started:
            break
    return rows


readme = texts.get("README.md", "")
for name, f in phase_files.items():
    m = re.search(r"^#### 3\.1\.\d Phase \d: " + name + r"\n(.*?)(?=^#{2,4} )", readme, flags=re.M | re.S)
    o = re.search(r"^### [68]\.1 Owners\n(.*?)(?=^### )", texts.get(f, ""), flags=re.M | re.S)
    if not m or not o:
        problems.append(f"RACI    {f}: RACI table or README §3.1 {name} table not found")
    elif first_table(m.group(1)) != first_table(o.group(1)):
        problems.append(f"RACI    {f}: Owners table differs from README §3.1 ({name})")

today = datetime.date.today()
for f, t in texts.items():
    m = re.search(r"Next (?:full-guide )?review due:\*\*\s*(\d{4}-\d{2}-\d{2})", t)
    if m and datetime.date.fromisoformat(m.group(1)) < today and "/templates/" not in f:
        problems.append(f"OVERDUE {f}: next review was due {m.group(1)}")

for p in problems:
    print(p)
print(f"Checked {len(mds)} Markdown files: {len(problems)} problem(s).")
sys.exit(1 if problems else 0)
