"""Monday Morning Punchlines entry (u-gentle-badger-68-monday-morning-punchlines-709645dc).

Writes one original joke about Monday mornings to /output/entry.txt.
Standard library only; no network, no randomness, no external reads.
Deterministic: the same bytes on every run.
"""

import os

JOKE = (
    "Sunday night I set three alarms for Monday morning. "
    "By 6 a.m. they'd formed a union, voted unanimously, "
    "and gone on strike together."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
