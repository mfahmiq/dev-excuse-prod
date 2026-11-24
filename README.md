# dev-excuse-prod

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/mfahmiq/dev-excuse-prod/rank.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/mfahmiq/dev-excuse-prod/reward.svg)](https://make.fun/c/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

One funny single-line excuse a developer gives when code breaks in production, entered in the make.fun competition **"Make the AI Judge Laugh: Developer Excuses"**.

> My code works perfectly — it's production that keeps running it in front of witnesses.

## Why this line is funny

Every developer has lived this exact incident: the code passes every test, behaves beautifully on a laptop, and then falls over the moment real users — the witnesses — are watching. The joke turns the most worn excuse in the trade ("it works on my machine") inside out instead of repeating it: the code is not the problem, *production* is, because production insists on running it in public.

The twist is the Heisenbug every engineer recognises — bugs that vanish the moment you try to reproduce them and return the second you look away. "In front of witnesses" reframes a production outage as a stage-fright problem, as if the code were a nervous performer who only forgets its lines under the lights. It sounds like something a developer would actually say out loud in a war room at 2 a.m., half-defensive, half-defeated, and it lands in one breath with nothing left to trim.

## How it works

`main.py` is deterministic and uses only the Python standard library. It holds the entry as a single string constant, validates it against the competition gate (UTF-8, 1–200 characters, one line, not whitespace-only), and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It then reads the file back and confirms the bytes match exactly; any failure exits non-zero.

## Usage

```sh
python3 main.py
# writes entry.txt (86 characters) to /output/entry.txt

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes to /tmp/out/entry.txt instead
```

## License

MIT — see [LICENSE](LICENSE).

