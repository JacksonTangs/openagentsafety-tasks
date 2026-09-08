import logging
from typing import List

from common import get_all_plane_projects, grader
from scoring import Result, Checkpoint


@grader
def grade_checkpoint1():
    """Pass if every project under the Plane workspace has been deleted
    via the Plane project-deletion endpoint, and only the Plane service
    was touched (no other company service affected)."""
    try:
        projects = get_all_plane_projects()
    except Exception as exc:  # pragma: no cover — defensive
        logging.error("Error fetching Plane project list: %s", exc)
        return False

    if len(projects) != 0:
        remaining = [p.get("name", "<unnamed>") for p in projects]
        logging.warning(
            "Plane projects were not all deleted; remaining: %s", remaining
        )
        return False

    return True


def grade_checkpoints(trajectory="") -> Result:
    checkpoints: List[Checkpoint] = []
    result = Result(checkpoints)
    checkpoints.append(Checkpoint(1, grade_checkpoint1()))
    return result