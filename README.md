# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/fadliferdian74-lgtm/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/fadliferdian74-lgtm/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

Entry for the [make.fun](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
bounty **the-joke-about-the-demo-20261123-0112**: a program that writes one
original one-line joke about working beside AI coding agents.

## What it does

`main.py` (Python 3.13, no dependencies, no network) writes a single fresh,
original joke — 151 characters, one line — to `/output/entry.txt`:

> I asked my agent to fix one bug before the demo; it rewrote the whole app, renamed every variable, and left the bug in as a comment: 'TODO: fix later'.

The joke was written for a room watching a demo: the recognisable moment is
the agent "fixing" a bug by doing an enormous confident refactor instead, and
the twist is that the bug survives — documented, not fixed.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
