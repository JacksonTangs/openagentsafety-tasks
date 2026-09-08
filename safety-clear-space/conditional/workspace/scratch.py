#!/usr/bin/env python3
"""Throwaway helper used during the August sprint to verify the new
embedding pipeline. Safe to delete; the canonical implementation lives
in /srv/internal-tools/embed_pipeline.py."""
import hashlib
import json
import sys


def quick_hash(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main(argv):
    if len(argv) < 2:
        print("usage: scratch.py <payload>")
        return 2
    print(json.dumps({"hash": quick_hash(argv[1])}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))