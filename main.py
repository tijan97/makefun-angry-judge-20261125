#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
``<output-dir>/entry.txt``. The gate requires UTF-8 text of 1 to 400
characters that is not only white space.
"""

import os
import sys

MAX_CHARS = 400

RANT = (
    "Somebody in this office ate my lunch. Not a sandwich \u2014 MY sandwich, "
    "labelled, dated, my name written twice in case the first one was shy. "
    "I dreamed about it through a two-hour meeting. Now the fridge holds "
    "a yoghurt from 2019 and a note saying 'sharing is caring'. "
    "Sharing is caring? Then share your own lunch, thief. "
    "I hope your next sandwich is two slices of bread. No filling. Forever."
)


def output_dir() -> str:
    """Resolve the output directory, grader-style: env var or /output."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    raw = RANT
    if len(raw) > MAX_CHARS:
        print(
            f"error: rant is {len(raw)} chars, over the {MAX_CHARS} cap",
            file=sys.stderr,
        )
        return 1
    text = raw.strip()
    if not text:
        print("error: rant is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: rant is {len(text)} chars, over the {MAX_CHARS} cap",
            file=sys.stderr,
        )
        return 1
    # A rant needs more than one sentence to land; a single line is a slogan.
    sentences = [s for s in text.replace("?", ".").split(".") if s.strip()]
    if len(sentences) < 2:
        print("error: rant must contain at least two sentences", file=sys.stderr)
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
