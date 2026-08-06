"""
README generator.
"""

from datetime import datetime
from pathlib import Path

from job_hunter_ai.constants import (
    MAX_README_JOBS,
    README_DATE_FORMAT,
)
from job_hunter_ai.models.job import Job


TEMPLATE_PATH = Path("templates/README.template.md")
README_PATH = Path("README.md")


class ReadmeGenerator:
    """Generate README.md from template."""

    @classmethod
    def generate(
        cls,
        jobs: list[Job],
        new_jobs: int,
        removed_jobs: int,
    ) -> None:

        template = TEMPLATE_PATH.read_text(encoding="utf-8")

        remote_jobs = sum(job.remote for job in jobs)
        internships = sum(
            "intern" in job.title.lower()
            or "graduate" in job.title.lower()
            for job in jobs
        )

        table = cls.build_job_table(jobs)

        replacements = {
            "{{LAST_UPDATED}}": datetime.utcnow().strftime(
                README_DATE_FORMAT
            ),
            "{{TOTAL_JOBS}}": str(len(jobs)),
            "{{NEW_JOBS}}": str(new_jobs),
            "{{REMOVED_JOBS}}": str(removed_jobs),
            "{{REMOTE_JOBS}}": str(remote_jobs),
            "{{INTERNSHIPS}}": str(internships),
            "{{JOB_TABLE}}": table,
        }

        for key, value in replacements.items():
            template = template.replace(key, value)

        README_PATH.write_text(
            template,
            encoding="utf-8",
        )

    @staticmethod
    def build_job_table(jobs: list[Job]) -> str:
        """Generate markdown job table."""

        rows = []

        for job in jobs[:MAX_README_JOBS]:
            rows.append(
                "| "
                f"{job.company} | "
                f"{job.title} | "
                f"{job.location} | "
                f"{job.source} | "
                f"[Apply]({job.url}) |"
            )

        return "\n".join(rows)