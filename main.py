#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one original dad joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure Python stdlib.
"""

import os

JOKE = "I asked the librarian for the dad-joke books. She said, \"They're in the groan-up section.\""
# The punchline turns "grown-up" into "groan-up": the sound a dad joke earns.


def main() -> None:
    joke = JOKE
    # Gate checks: 1-200 chars, not only whitespace, single text.
    assert isinstance(joke, str)
    assert 1 <= len(joke) <= 200, f"joke is {len(joke)} chars, must be 1-200"
    assert joke.strip(), "joke must not be only whitespace"
    assert "\n" not in joke, "joke must be a single line of text"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(joke)
    print(f"Wrote {len(joke)} chars to {out_path}")


if __name__ == "__main__":
    main()
