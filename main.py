"""Write one funny line to /output/entry.txt.

One sentence, 73 characters: an everyday purchase meant to fix a habit,
defeated by the buyer in the last few words. The setup promises health;
the punchline is a taller chair. Plain, concrete words; nothing in it
explains the joke.
"""

import os

TEXT = "I bought a standing desk to be healthier, so now I sit on a taller chair."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
