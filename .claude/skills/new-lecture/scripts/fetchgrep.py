#!/usr/bin/env python3
"""Cheap fact check: fetch a page and print ONLY the snippets that match your patterns.

Usage:  python .claude/skills/new-lecture/scripts/fetchgrep.py <url> "<regex>" ["<regex>" ...]
Prints up to 3 snippets (about 220 characters) per pattern, or "NO MATCH". No model is involved, so only the
matching lines enter the conversation (a full page through WebFetch costs far more). Use it to confirm numbers,
dates, version names and quoted wording. If it says FETCH FAILED or the page needs JavaScript, fall back to
WebFetch or WebSearch. Several URLs can be checked in parallel (one call each).
"""
import html
import re
import sys
import urllib.request


def text_of(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (fact-check script)"})
    raw = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw))


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    url, pats = sys.argv[1], sys.argv[2:]
    try:
        t = text_of(url)
    except Exception as e:  # noqa: BLE001
        print(f"FETCH FAILED {url}: {type(e).__name__}: {e}")
        return 1
    print(f"{url}  ({len(t)} chars of text)")
    for p in pats:
        hits = [m for m in re.finditer(p, t, re.I)]
        if not hits:
            print(f"  [{p}] NO MATCH")
            continue
        for m in hits[:3]:
            a, b = max(0, m.start() - 90), min(len(t), m.end() + 130)
            print(f"  [{p}] ...{t[a:b].strip()}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
