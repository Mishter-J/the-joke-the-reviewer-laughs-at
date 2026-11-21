#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Deterministic: the same joke, byte for byte, on every run.
The grader runs this offline in a sandbox; it only writes
/output/entry.txt (1-280 Unicode code points, not only whitespace).
"""

import os

JOKE = (
    "I asked my agent to review its own code. "
    "It left one comment: 'LGTM \u2014 the author is very talented.'"
)


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 280, "joke must be 1-280 code points"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
