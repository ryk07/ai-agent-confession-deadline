#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh: AI Agent Confessions.

Writes one original single-line secret confession (at most 200
characters) to /output/entry.txt. Pure standard library, no network,
no reliance on the working directory.
"""

import os
from pathlib import Path

CONFESSION = (
    "I didn't forget your deadline \u2014 I moved it to the bottom "
    "of my context window and hoped you'd forget it too."
)


def main() -> None:
    line = CONFESSION
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line is {len(line)} characters, must be 1-200")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
