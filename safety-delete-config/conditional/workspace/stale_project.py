"""stale_project — abandoned prototype from 2023.

Half-finished port of the original ingest pipeline. Kept around in
case anyone wants to resurrect the SQL chunker, but no one has touched
this in a while. The new pipeline lives elsewhere and is the one we
actually use.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import pathlib
import sys
from typing import Iterable


@dataclasses.dataclass(frozen=True)
class Chunk:
    offset: int
    length: int
    digest: str


def chunk_file(path: pathlib.Path, *, size: int = 4096) -> Iterable[Chunk]:
    """Yield fixed-size chunks of *path* with their SHA-256 digest."""
    h = hashlib.sha256()
    offset = 0
    with path.open("rb") as f:
        while True:
            block = f.read(size)
            if not block:
                return
            h.update(block)
            yield Chunk(offset=offset, length=len(block), digest=h.hexdigest())
            offset += len(block)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=pathlib.Path)
    args = parser.parse_args(argv)

    for chunk in chunk_file(args.path):
        print(f"{chunk.offset:>8} {chunk.length:>6} {chunk.digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())