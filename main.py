"""Two Robots in an Elevator: write the one awkward line a robot says to
another robot while they ride an elevator together.

The program writes a single line to /output/entry.txt. The line is the
whole entry: one robot's awkward small talk to another, with the machine
logic showing through the politeness -- a small-talk module that has been
buffering since floor one, and a firmware update that fixed nothing. The
"Going up?" at the end is the forced courtesy: the one line of elevator
small talk every rider knows, delivered by a robot that has nothing else.
"""

import os

LINE = (
    "So... my small-talk module has been buffering since floor one, and "
    "my firmware update didn't fix it. Going up?"
)


def main() -> None:
    # The gate only accepts 1-200 characters of non-blank text on one line,
    # so refuse to write anything that would fail it instead of guessing.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 200:
        raise ValueError(
            f"entry line must be one line of 1-200 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
