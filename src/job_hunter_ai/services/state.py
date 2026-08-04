"""
State management service.

Stores and loads previous job snapshots.
"""

from __future__ import annotations

import json
from pathlib import Path

from job_hunter_ai.models.job import Job


STATE_FILE = Path("data/state/previous_jobs.json")


class JobState:
    """Manage persisted job snapshots."""

    @staticmethod
    def load() -> list[Job]:
        """Load previous jobs."""

        if not STATE_FILE.exists():
            return []

        with open(STATE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Job.from_dict(item) for item in data]

    @staticmethod
    def save(jobs: list[Job]) -> None:
        """Save current jobs."""

        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(STATE_FILE, "w", encoding="utf-8") as file:
            json.dump(
                [job.to_dict() for job in jobs],
                file,
                indent=4,
                ensure_ascii=False,
            )