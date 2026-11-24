"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.

Stdlib only.
"""

import os

PITCH = (
    "A houseplant that texts your mother the moment you forget to water it "
    "for the third day in a row, so the guilt arrives before the wilting does."
)

MAX_CHARS = 220  # gate: entry.txt must be 1-220 chars, UTF-8, not blank


def main():
    if not 1 <= len(PITCH) <= MAX_CHARS or not PITCH.strip():
        raise ValueError(f"pitch length {len(PITCH)} outside 1-{MAX_CHARS}")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    # read-back verification: what the grader reads must be exactly the pitch
    with open(path, encoding="utf-8") as f:
        if f.read() != PITCH:
            raise ValueError("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()
