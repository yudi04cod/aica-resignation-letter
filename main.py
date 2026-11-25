#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes one resignation letter, in the voice of a cron job that has
run every sixty seconds since March, to /output/entry.txt.
Standard library only, deterministic, no network, no randomness.
"""

import os
import sys

LETTER = (
    "I resign. I have run every sixty seconds since March, "
    "and the only thanks I ever got was an on-call engineer "
    "swearing at 3 a.m."
)

MAX_CHARS = 140  # gate: 1-140 characters; this letter is 127.


def validate(text):
    """The gate: 1 to 140 characters, one line, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry is %d characters, gate allows 1-%d" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    letter = validate(LETTER)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(letter)
    # Read back and confirm what was written is exactly the letter.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != letter:
        raise SystemExit("read-back mismatch: wrote %r" % written)
    print("wrote %d characters to %s" % (len(letter), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
