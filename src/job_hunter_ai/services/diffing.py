"""
Job difference engine.

Detects newly added and removed jobs between snapshots.
"""

from job_hunter_ai.models.job import Job


class JobDiff:
    """Compare two job collections."""

    @staticmethod
    def compare(previous: list[Job], current: list[Job]) -> tuple[list[Job], list[Job], list[Job]]:
        """
        Returns:
            new_jobs,
            removed_jobs,
            unchanged_jobs
        """

        previous_map = {job.id: job for job in previous}
        current_map = {job.id: job for job in current}

        new_jobs = [
            job
            for job_id, job in current_map.items()
            if job_id not in previous_map
        ]

        removed_jobs = [
            job
            for job_id, job in previous_map.items()
            if job_id not in current_map
        ]

        unchanged_jobs = [
            job
            for job_id, job in current_map.items()
            if job_id in previous_map
        ]

        return (
            new_jobs,
            removed_jobs,
            unchanged_jobs,
        )