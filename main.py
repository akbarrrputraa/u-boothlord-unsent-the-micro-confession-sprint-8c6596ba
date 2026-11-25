#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes the two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line
written exactly as it was typed, with no explanation after it.

Runs with no input and no network. Deterministic: the same file is
written on every run.
"""

import os
import sys

TO = "Dad"

MESSAGE = (
    "I got the scholarship letter in April and turned it down without "
    "telling you, because the university was four hours from home and I "
    "heard Mum crying in the kitchen the night she thought I was asleep."
)

MAX_MESSAGE_CHARS = 200
MAX_ENTRY_CHARS = 260


def build_entry(to: str, message: str) -> str:
    """Assemble the two-part confession and check the competition's caps."""
    message = message.strip()
    if not to.strip():
        raise ValueError("To: line must name who the message was meant for")
    if "\n" in message or "\r" in message:
        raise ValueError("the unsent message must be exactly one line")
    if len(message) > MAX_MESSAGE_CHARS:
        raise ValueError(
            f"message is {len(message)} chars, over the {MAX_MESSAGE_CHARS} cap"
        )
    entry = f"To: {to.strip()}\n{message}"
    if len(entry) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(entry)} chars, over the {MAX_ENTRY_CHARS} cap"
        )
    if not entry.strip():
        raise ValueError("entry must not be only white space")
    return entry


def main() -> int:
    entry = build_entry(TO, MESSAGE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
