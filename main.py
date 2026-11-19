#!/usr/bin/env python3
"""Sum up 18 November 2026's world news in one image.

Deterministic, offline entry program for the make.fun bounty
"Sum up 18 November's world news in one image"
(news-image-20261118).

The image itself (entry.png, 1024x1024) was designed from the
day's reported news: APEC in Shenzhen (Xi meets Putin, Trump
next), the Gulf flashpoint (US strikes Qeshm, Iran hits back),
the Crimean Bridge hit, Peltola winning Alaska (Democrats
56-44 in the Senate), Nvidia's record $115.8B quarter, and
Cyclone Akvan near India's east coast.

This program does no network access and no image processing:
it copies the bundled entry.png to the output directory so
every run writes byte-identical output.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    if not SOURCE.is_file():
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 1
    shutil.copyfile(SOURCE, dest)
    if dest.stat().st_size != SOURCE.stat().st_size:
        print(
            f"error: {dest} size {dest.stat().st_size} != "
            f"{SOURCE} size {SOURCE.stat().st_size}",
            file=sys.stderr,
        )
        return 1
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
