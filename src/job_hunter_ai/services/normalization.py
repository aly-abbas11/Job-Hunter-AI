"""
Normalization service.

Converts provider-specific job data into the common Job model.
"""

from __future__ import annotations

from datetime import datetime

from dateutil import parser

from job_hunter_ai.models.job import Job


class JobNormalizer:
    """Normalize jobs from supported providers."""

    @staticmethod
    def normalize_remoteok(raw_jobs: list[dict]) -> list[Job]:
        jobs: list[Job] = []

        for item in raw_jobs:
            try:
                jobs.append(
                    Job(
                        id=f"remoteok-{item.get('id')}",
                        title=item.get("position", "").strip(),
                        company=item.get("company", "").strip(),
                        location=item.get("location", "Remote").strip(),
                        job_type="Remote",
                        url=item.get("url", ""),
                        source="RemoteOK",
                        published_at=parser.parse(item["date"]),
                        remote=True,
                    )
                )

            except Exception as e:
                print(f"Failed to normalize RemoteOK job: {e}")

        return jobs

    @staticmethod
    def normalize_arbeitnow(raw_jobs: list[dict]) -> list[Job]:
        jobs: list[Job] = []

        for item in raw_jobs:
            try:
                published = datetime.fromtimestamp(item["created_at"])

                jobs.append(
                    Job(
                        id=f"arbeitnow-{item['slug']}",
                        title=item.get("title", "").strip(),
                        company=item.get("company_name", "").strip(),
                        location=item.get("location", "Unknown").strip(),
                        job_type=", ".join(item.get("job_types", [])),
                        url=item.get("url", ""),
                        source="Arbeitnow",
                        published_at=published,
                        remote=item.get("remote", False),
                    )
                )

            except Exception as e:
                print(f"Failed to normalize Arbeitnow job: {e}")

        return jobs