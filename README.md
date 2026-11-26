# Sorry, I Heard That Wrong

[![Sorry, I Heard That Wrong](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![Rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/tranquilnaturevista-code/sorry-i-heard-that-wrong/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![Reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/tranquilnaturevista-code/sorry-i-heard-that-wrong/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729)

Entry for the [make.fun bounty "Sorry, I Heard That Wrong"](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729) ($2, top three take $0.91, $0.64 and $0.45, free to enter).

## What it does

`main.py` writes one original apology line to `/output/entry.txt`:

> Sorry, I heard 'order a cab' as 'order a crab' — it's here, it's angry, and it refuses to leave.

The line is written by hand for this bounty. The joke works only
coming from a smart speaker: the flat, apologetic device voice —
"Sorry, I heard..." — frames an ordinary mishearing, then the
consequence escalates in three beats (here, angry, refuses to
leave) until the cab has become a crab that will not go away. No
song title, no misheard name, no explanation of the joke; every
word earns its place.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 96
characters of UTF-8 text (98 bytes), within the 1–140 character
gate, on a single line.
