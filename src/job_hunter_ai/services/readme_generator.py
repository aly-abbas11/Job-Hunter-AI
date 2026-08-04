"""
README generator.
"""

from datetime import datetime
from pathlib import Path

from job_hunter_ai.models.job import Job


README_PATH = Path("README.md")


class ReadmeGenerator:
    """Generate README.md."""

    @staticmethod
    def generate(
        jobs: list[Job],
        new_jobs: int,
        removed_jobs: int,
    ) -> None:

        lines = [
            "# 🚀 Job Hunter AI",
            "",
            "Automatically updated job listings.",
            "",
            f"**Last Updated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
            "",
            "## Statistics",
            "",
            f"- Total Jobs: {len(jobs)}",
            f"- New Jobs: {new_jobs}",
            f"- Removed Jobs: {removed_jobs}",
            "",
            "---",
            "",
            "## Latest Jobs",
            "",
            "| Company | Position | Location | Source |",
            "|---------|----------|----------|--------|",
        ]

        for job in jobs[:100]:
            lines.append(
                f"| {job.company} | {job.title} | {job.location} | {job.source} |"
            )

        README_PATH.write_text(
            "\n".join(lines),
            encoding="utf-8",
        )