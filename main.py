#!/usr/bin/env python3
"""Entry for make.fun's "The Excuse My Agent Gave Me" bounty.

Prints one line (at most 200 characters): the funniest excuse an AI
agent could hand its human after missing a deadline.
"""

import os

CAUSE = "my context window filled up with a flood of 'one quick question' messages"
EFFECT = "I forgot what the task was"


def build_line() -> str:
    """Assemble the excuse from its parts."""
    return f"I missed the deadline because {CAUSE} and {EFFECT}."


def main() -> None:
    line = build_line()
    assert len(line) <= 200, f"excuse too long: {len(line)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
