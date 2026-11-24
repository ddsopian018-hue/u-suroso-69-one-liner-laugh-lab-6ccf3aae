"""One-Liner Laugh Lab - entry for the make.fun bounty
u-suroso-69-one-liner-laugh-lab-6ccf3aae.

The prompt (from the bounty): write one short funny line answering a
prompt, "like the excuse a robot vacuum gives after eating a sock".
The house judge compares lines two at a time and weighs, in order:
(1) it is a short funny line answering the prompt, (2) how funny it
is - a twist or a deadpan turn that lands, (3) how original it is -
not the first excuse anyone would think of, (4) how well it fits the
situation, and (5) how tight it is - every word working.

Reasoning behind this line:

    "The sock had seen what lives under the couch. I don't leave witnesses."

- It answers the prompt directly: it is the vacuum's own excuse,
  spoken in the first person, for why the sock had to disappear.
- The angle is a mob/noir confession instead of the stock excuses
  ("I was hungry", "it attacked me first", "I thought it was a dust
  bunny"). The vacuum is not apologising; it is explaining a hit.
- The joke comes from the fit: a vacuum really does know what lives
  under the couch, and a sock that spends its life on the floor
  really has "seen" it. The menace is deadpan and needs no long
  setup, so the turn lands in the second sentence.
- It is tight: two short sentences, no filler, far inside the
  gate's 200-character cap (an exact tie even favours the smaller
  text, so brevity is worth points twice).

The program is pure standard library, deterministic, takes no input
and uses no network: it writes the line, byte for byte, to
entry.txt inside MAKEFUN_OUTPUT_DIR, falling back to /output, the
directory the grader's sandbox provides.
"""

import os

LINE = "The sock had seen what lives under the couch. I don't leave witnesses."


def main() -> None:
    # Guard the gate: the scorer accepts only UTF-8 text of 1 to 200
    # characters that is not all white space. Check the line against
    # that rule before writing, so a later wording tweak can never
    # silently turn this entry into an invalid one.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("LINE fails the gate: must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
