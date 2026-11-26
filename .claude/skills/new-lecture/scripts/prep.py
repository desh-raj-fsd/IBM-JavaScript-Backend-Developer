#!/usr/bin/env python3
"""Phase 0 in one call: git pull, find the target module, next note number, create folders.

Usage (from the repo root):  python .claude/skills/new-lecture/scripts/prep.py <topic-slug>
Prints NOTE / IMAGES / TRANSCRIPT paths and the number NN. Never writes the transcript itself:
save only the transcript's KEY POINTS (about 300 words) to the TRANSCRIPT path.
"""
import glob
import os
import re
import subprocess
import sys


def natural(p):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", p)]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    slug = re.sub(r"[^a-z0-9]+", "-", sys.argv[1].lower()).strip("-")
    pull = subprocess.run(["git", "pull", "--ff-only"], capture_output=True, text=True)
    print("git pull:", (pull.stdout.strip() or pull.stderr.strip()).splitlines()[-1] if (pull.stdout or pull.stderr) else "ok")
    dirty = subprocess.run(["git", "status", "--short", "--untracked-files=no"], capture_output=True, text=True).stdout.strip()
    if dirty:
        print("WARNING tracked files are modified:\n" + dirty)
    modules = sorted(glob.glob("course-*/module-*/"), key=natural)
    if not modules:
        print("No course/module folder found: ask the user for the names.")
        return 1
    module = modules[-1].rstrip("/")
    nums = [int(m.group(1)) for f in glob.glob(f"{module}/notes/*.md") if (m := re.match(r"(\d+)-", os.path.basename(f)))]
    nn = f"{(max(nums) + 1) if nums else 1:02d}"
    for sub in ("notes", "images"):
        os.makedirs(f"{module}/{sub}", exist_ok=True)
    tdir = f".transcripts/{module}"
    os.makedirs(tdir, exist_ok=True)
    print(f"MODULE     {module}  (newest; ask the user only if the title clearly starts a new module)")
    print(f"NN         {nn}")
    print(f"NOTE       {module}/notes/{nn}-{slug}.md")
    print(f"IMAGES     {module}/images/{nn}-{slug}-<short-name>.svg")
    print(f"TRANSCRIPT {tdir}/{nn}-{slug}.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
