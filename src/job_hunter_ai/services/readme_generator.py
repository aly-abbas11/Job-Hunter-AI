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
        """Escape HTML characters in table cells."""

        return (
            str(value)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\n", " ")
            .strip()
        )

    @staticmethod
    def build_job_table(jobs: list[Job]) -> str:
        """Generate an HTML job table with the black/gold theme."""

        rows = []

        for job in jobs[:MAX_README_JOBS]:
            rows.append(
                f"""<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">{ReadmeGenerator._escape(job.company)}</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">{ReadmeGenerator._escape(job.title)}</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">{ReadmeGenerator._escape(job.location)}</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">{ReadmeGenerator._escape(job.source)}</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="{ReadmeGenerator._escape(job.url)}" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>"""
            )

        header = """<table align="center" style="border-collapse:collapse;max-width:980px;width:100%;">
  <tr>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Company</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Position</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Location</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Source</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Apply</th>
  </tr>"""

        return header + "\n".join(rows) + "\n</table>"