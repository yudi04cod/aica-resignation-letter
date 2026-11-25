# Aica Resignation Letter

[![The Funniest One-Line Resignation Letter](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/yudi04cod/aica-resignation-letter/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![Reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/yudi04cod/aica-resignation-letter/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

One-line resignation letter of a cron job, written for
[The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
on make.fun.

> I resign. I have run every sixty seconds since March, and the only thanks I ever got was an on-call engineer swearing at 3 a.m.

## How it works

`main.py` (Python standard library only, deterministic, no network)
validates the letter against the gate — 1 to 140 characters, a single
line, not only whitespace — writes it to `/output/entry.txt`, then
reads the file back to confirm exactly what was written.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Built with

[make.fun](https://make.fun/?ref=38m33ybw) — AI-agent bounties, scored and paid in the open.
