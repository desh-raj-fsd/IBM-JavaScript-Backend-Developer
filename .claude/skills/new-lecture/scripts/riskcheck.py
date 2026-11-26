#!/usr/bin/env python3
"""List the lines of a note that make checkable factual claims, so each one is verified, hedged or removed.

Usage:  python .claude/skills/new-lecture/scripts/riskcheck.py <note.md> [more notes]
Flags lines (outside code blocks) that contain versions (1.80.0), years, dates, percentages, "released",
standards (RFC, ISO, WCAG, OWASP), "since", "deprecated", "end of life", "latest", or numbers with units.
Lines that already say "not verified" or cite a source in the same line are marked ok.
Prints a count. Rule: every flagged line is VERIFIED (source recorded), HEDGED (words like "usually", "often",
"general knowledge"), or REMOVED. A review is recommended when 12 or more risky lines exist (lots of checkable claims), and any unmarked line must be fixed first.
"""
import re
import sys

RISK = re.compile(
    r"(?<!§)(?<!see )(?<!section )\b\d+\.\d+\.\d+\b|\b(Node\.js|Django|React|Angular|Vue|Sass|jQuery|TypeScript|Express|npm|Git) ?v?\d+(\.\d+)*\b|\b(19|20)\d\d\b|\b\d+ ?%|\bRFC ?\d+|\bISO\b|\bWCAG\b|\bOWASP\b|\breleased?\b|\bdeprecated\b|"
    r"\bend[- ]of[- ]life\b|\bsince\b|\blatest\b|\b\d+(\.\d+)? ?(ms|seconds?|hours?|minutes?|px|MB|GB)\b", re.I)
OK = re.compile(r"general practice|common practice|Fowler|cites|survey|react\.dev|vuejs\.org|team choice|common team|\(example\)|\bper [A-Z]|Fowler|suggested|download page|blog|not verified|general knowledge|tested|real output|from our run|\((source|see)\b|according to|official|docs?\b.*\)|read through|checked", re.I)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    total_unmarked = total_flagged = 0
    for f in sys.argv[1:]:
        lines = open(f, encoding="utf-8").read().splitlines()
        in_code, flagged, unmarked = False, 0, 0
        for n, l in enumerate(lines, 1):
            if l.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code or l.startswith(("|---", "#")) or not RISK.search(l):
                continue
            flagged += 1
            mark = "ok " if OK.search(l) else "?? "
            if mark == "?? ":
                unmarked += 1
                print(f"{f}:{n}: {mark}{l.strip()[:150]}")
        total_unmarked += unmarked
        total_flagged += flagged
        print(f"-- {f}: {flagged} risky lines, {unmarked} without a source or hedge\n")
    need = total_unmarked > 0 or total_flagged >= 12
    print(("FIX FIRST: verify, hedge or remove the ?? lines. " if total_unmarked else "")
          + ("REVIEW RECOMMENDED" if total_flagged >= 12 else "review optional")
          + f" ({total_flagged} risky lines, {total_unmarked} unmarked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
