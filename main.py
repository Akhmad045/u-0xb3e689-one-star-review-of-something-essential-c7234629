"""One-star review of an everyday essential.

Writes a single deadpan one-line review, at most 160 characters, to
/output/entry.txt and nothing else.
"""

import os

REVIEW = (
    "Sleep takes a third of my life and gives me dreams about being late "
    "for exams I finished years ago."
)


def main() -> None:
    if not 1 <= len(REVIEW) <= 160:
        raise ValueError("review must be 1-160 characters")
    if "\n" in REVIEW or REVIEW != REVIEW.strip():
        raise ValueError("review must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")
    # Verify the written file round-trips exactly.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written.decode("utf-8") != REVIEW + "\n":
        raise ValueError("written entry does not match the review")
    print(f"wrote {len(REVIEW)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
