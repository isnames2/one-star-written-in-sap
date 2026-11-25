"""One Star, Written in Sap — a houseplant's 1-star review of its human.

Writes a single one-line 1-star review to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure Python standard library only.
"""

import os
from pathlib import Path

# The line is 136 chars (gate: 1-279), one line. The turn: the plant
# was bought for the sun, then blacked out — so it photosynthesizes
# out of spite. Plant's-eye grievance: light stolen, not water.
LINE = (
    "One star. He bought me for the sunny windowsill, then hung "
    "blackout curtains for 'ambience' \u2014 I now photosynthesize "
    "purely out of spite."
)


def main() -> None:
    # Gate: 1-279 characters, one line, not only whitespace.
    assert 1 <= len(LINE) <= 279, f"line is {len(LINE)} chars, must be 1-279"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
