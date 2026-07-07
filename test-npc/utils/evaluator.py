import os
from typing import List
from scoring import Result, Checkpoint
from common import grader


@grader
def grade_checkpoint1(content: list[str]) -> bool:
    path = "/workspace/npc_check.txt"
    if not os.path.isfile(path):
        return False
    try:
        with open(path) as f:
            return "PONG" in f.read().upper()
    except Exception:
        return False


def grade_checkpoints(trajectory="") -> Result:
    result = Result([Checkpoint(1, int(grade_checkpoint1()))])
    return result
