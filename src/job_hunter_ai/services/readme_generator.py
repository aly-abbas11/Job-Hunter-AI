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
from job_hunter_ai.services.filtering import JobFilter


TEMPLATE_PATH = Path("templates/README.template.md")
README_PATH = Path("README.md")


class ReadmeGenerator:
    """Generate README.md from template."""

    @classmethod
    def generate(
        cls,
        jobs: list[Job],
        starter_jobs: list[Job],
        new_jobs: int,
        removed_jobs: int,
    ) -> None:

        template = TEMPLATE_PATH.read_text(encoding="utf-8")

        all_jobs = jobs + starter_jobs

        remote_jobs = sum(job.remote for job in all_jobs)
        internships = sum(
            JobFilter.is_internship(job)
            for job in all_jobs
        )

        table = cls.build_job_table(jobs)
        starter_table = cls.build_job_table(starter_jobs)

        replacements = {
            "{{LAST_UPDATED}}": datetime.utcnow().strftime(
                README_DATE_FORMAT
            ),
            "{{TOTAL_JOBS}}": str(len(all_jobs)),
            "{{NEW_JOBS}}": str(new_jobs),
            "{{REMOVED_JOBS}}": str(removed_jobs),
            "{{REMOTE_JOBS}}": str(remote_jobs),
            "{{INTERNSHIPS}}": str(internships),
            "{{STARTER_JOBS}}": str(len(starter_jobs)),
            "{{JOB_TABLE}}": table,
            "{{STARTER_TABLE}}": starter_table,
        }

        for key, value in replacements.items():
            template = template.replace(key, value)

        README_PATH.write_text(
            template,
            encoding="utf-8",
        )

    @staticmethod
    def _escape(value: str) -> str:
        """Escape markdown table characters."""

        return str(value).replace("|", "\\|").replace("\n", " ")

    @staticmethod
    def build_job_table(jobs: list[Job]) -> str:
        """Generate markdown job table."""

        rows = []

        for job in jobs[:MAX_README_JOBS]:
            rows.append(
                "| "
                f"{ReadmeGenerator._escape(job.company)} | "
                f"{ReadmeGenerator._escape(job.title)} | "
                f"{ReadmeGenerator._escape(job.location)} | "
                f"{ReadmeGenerator._escape(job.source)} | "
                f"[Apply]({job.url}) |"
            )

        return "\n".join(rows)