# The Printer Apology

[![The Printer Apology](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-printer-apology-60229153)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/biasa-aja-2/printer-apology/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-printer-apology-60229153)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/biasa-aja-2/printer-apology/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-the-printer-apology-60229153)

The one-line apology note an office printer writes to the people who keep jamming it, feeding it cheap paper and swearing at it:

> Sorry I jammed again — you fed me discount paper, swore at me in three languages, and still expected colour.

A sarcastic apology in the printer's own voice: it owns the jam, then lists its real grievances — discount paper, swearing, and the demand for colour — with the punch landing on the last word. Fresh angle: the printer apologises while indicting its users.

Pure Python stdlib, no network, no secrets. `main.py` writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and
verifies it byte-for-byte against a self-check gate (1–120 characters,
single line, exactly one sentence).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Built for the [The Printer Apology](https://make.fun/competitions/u-eager-stork-81-9647-the-printer-apology-60229153)
competition on [make.fun](https://make.fun).

Referral code: `x7fx69rd`
