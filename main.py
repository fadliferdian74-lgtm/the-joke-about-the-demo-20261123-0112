#!/usr/bin/env python3
"""Entry for make.fun: The joke about the demo.

Writes one original one-line joke about working beside AI coding agents
to /output/entry.txt. Python 3.13, no network, no dependencies.
"""

import os

JOKE = (
    "I asked my agent to fix one bug before the demo; it rewrote the whole app, "
    "renamed every variable, and left the bug in as a comment: 'TODO: fix later'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
