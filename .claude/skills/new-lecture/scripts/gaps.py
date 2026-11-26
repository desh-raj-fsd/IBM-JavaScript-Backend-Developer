#!/usr/bin/env python3
"""SDLC gap table in one call: for each regex, where does SDLC/ already mention it?

Usage (from the repo root):
  python .claude/skills/new-lecture/scripts/gaps.py "squad|tribe" "working agreement" "bus factor"
Prints, per pattern: total hits, the top files with counts, and the first hit line. 0 hits = a real gap.
CHANGELOG.md is skipped (it records changes, not rules).
"""
import glob
import re
import sys
from collections import Counter


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    files = [f for f in glob.glob("SDLC/**/*.md", recursive=True) if not f.endswith("CHANGELOG.md")]
    texts = {f: open(f, encoding="utf-8").read() for f in files}
    for pat in sys.argv[1:]:
        rx = re.compile(pat, re.I)
        counts, first = Counter(), None
        for f, t in texts.items():
            for n, line in enumerate(t.splitlines(), 1):
                if rx.search(line):
                    counts[f] += 1
                    first = first or f"{f}:{n}: {line.strip()[:110]}"
        total = sum(counts.values())
        top = ", ".join(f"{f.replace('SDLC/', '')}({c})" for f, c in counts.most_common(3))
        print(f"{pat!r}: {total} hit(s)" + (f" -> {top}\n    {first}" if total else "  <- GAP"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
