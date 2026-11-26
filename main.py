"""The Internet in One Word (make.fun bounty).

The entry is one word, written to <output>/entry.txt. The judge weighs,
most important first: a single word for the whole internet; funny by
itself; true about the internet as a whole; surprising; lands in one beat.

Candidate words, scored against that brief:
  feral       - wild, untamed, occasionally bites: funny, true of the whole
                internet, surprising, 5 letters, one beat. THE PICK.
  unhinged    - strong and funny, but 8 letters and a beat slower.
  tabs        - relatable (47 open tabs) but a browser habit, not the net.
  void        - good ("screaming into the void") but less funny alone.
  screaming   - vivid and true, but 9 letters.
  loud        - true and short, but only mildly funny.
  abyss       - dramatic like void, less funny than feral.
  rabbithole  - a common metaphor, 10 letters.
  doomscroll  - one behaviour, not the whole internet.
  sidequest   - funny to gamers, too niche for the whole internet.

"feral" makes a reader laugh and then nod: the internet is feral.
Pure stdlib, deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

WORD = "feral"


def _check(word: str) -> None:
    """Gate mirror: 1-30 UTF-8 chars, one word, not only whitespace."""
    if not 1 <= len(word.encode("utf-8")) <= 30:
        raise ValueError("word must be 1-30 characters")
    if not word.strip() or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main() -> None:
    _check(WORD)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
