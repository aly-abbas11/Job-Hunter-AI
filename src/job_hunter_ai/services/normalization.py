"""
Normalization service.

Converts raw API responses from different job providers into
the unified Job model used throughout the application.
"""

from __future__ import annotations

from datetime import UTC, datetime

from dateutil import parser

from job_hunter_ai.models.job import Job


class JobNormalizer:
    """Normalize job listings from different providers."""

    @staticmethod
    def normalize_remoteok(raw_jobs: list[dict]) -> list[Job]:
        """Normalize RemoteOK jobs."""

        jobs: list[Job] = []

        for item in raw_jobs:
            try:
                jobs.append(
                    Job(
                        id=f"remoteok-{item.get('id')}",
                        title=item.get("position", "").strip(),
                        company=item.get("company", "").strip(),
                        location=item.get("location", "").strip(),
                        job_type="Remote",
                        url=item.get("apply_url") or item.get("url", ""),
                        source="RemoteOK",
                        published_at=parser.parse(item["date"]),
                        remote=True,
                    )
                )

            except Exception as exc:
                print(f"RemoteOK normalization error: {exc}")

        return jobs

    @staticmethod
    def normalize_arbeitnow(raw_jobs: list[dict]) -> list[Job]:
        """Normalize Arbeitnow jobs."""

        jobs: list[Job] = []

        for item in raw_jobs:
            try:
                timestamp = item.get("created_at")

                if isinstance(timestamp, (int, float)):
                    published = datetime.fromtimestamp(timestamp, tz=UTC)
                else:
                    published = parser.parse(str(timestamp))

                jobs.append(
                    Job(
                        id=f"arbeitnow-{item.get('slug')}",
                        title=item.get("title", "").strip(),
                        company=item.get("company_name", "").strip(),
                        location=item.get("location", "").strip(),
                        job_type=", ".join(item.get("job_types", [])),
                        url=item.get("url", ""),
                        source="Arbeitnow",
                        published_at=published,
                        remote=item.get("remote", False),
                    )
                )

            except Exception as exc:
                print(f"Arbeitnow normalization error: {exc}")

        return jobs