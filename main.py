#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The joke turns on the word "convert": the senator is a professional
converter of political things -- districts, donors, committees -- and
the one conversion he cannot manage is the file on his own desk. The
punch lands on the last words: the bill that would govern artificial
intelligence is, legally speaking, still a Word document.

Draft (first pass) and final (revised) are both kept below so the
revision is visible in the code itself.
"""

import os
import sys

# First draft -- 246 characters. It worked, but "the law" was vague and
# "the file he cannot convert" repeated the setup instead of landing a
# punch, so the sentence ended on a shrug instead of a kicker.
DRAFT = (
    "The senator who converted a swing district, three mega-donors, and "
    "an entire committee cannot convert the file on his desk to PDF, so "
    "the law that would govern artificial intelligence is still a Word "
    "document."
)

# Final -- 222 characters. Two changes: the file became "a single .docx",
# a concrete detail instead of "the file", and the ending became "is,
# legally speaking, still a Word document", so the punch is the bill's
# own legal status, not just its file format.
FINAL = (
    "The senator who converted a swing district, three mega-donors, and "
    "an entire committee cannot convert a single .docx to PDF, so the "
    "bill that will govern artificial intelligence is, legally speaking, "
    "still a Word document."
)

MAX_CHARS = 320


def main() -> int:
    text = FINAL
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text)),
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
