"""
Normalization service.

Converts raw API responses from different job providers into
the unified Job model used throughout the application.
"""

from __future__ import annotations

from datetime import UTC, datetime

from dateutil import parser

from job_hunter_ai.core.constants import ASHBY_BOARD_NAMES
from job_hunter_ai.models.job import Job


def _make_aware(value: datetime) -> datetime:
    """Attach UTC timezone to naive datetimes."""

    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)

    return value


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
                        published_at=_make_aware(published),
                        remote=item.get("remote", False),
                    )
                )

            except Exception as exc:
                print(f"Arbeitnow normalization error: {exc}")

        return jobs

    @staticmethod
    def normalize_remotive(raw_jobs: list[dict]) -> list[Job]:
        """Normalize Remotive jobs."""

        jobs: list[Job] = []

        for item in raw_jobs:
            try:
                published = parser.parse(item.get("publication_date"))

                jobs.append(
                    Job(
                        id=f"remotive-{item.get('id')}",
                        title=item.get("title", "").strip(),
                        company=item.get("company_name", "").strip(),
                        location=item.get(
                            "candidate_required_location", ""
                        ).strip(),
                        job_type=", ".join(
                            filter(
                                None,
                                [
                                    item.get("category", ""),
                                    item.get("job_type", ""),
                                ],
                            )
                        ),
                        url=item.get("url", ""),
                        source="Remotive",
                        published_at=_make_aware(published),
                        remote=True,
                    )
                )

            except Exception as exc:
                print(f"Remotive normalization error: {exc}")

        return jobs

    @staticmethod
    def normalize_greenhouse(
        raw_jobs: list[tuple[str, dict]],
    ) -> list[Job]:
        """Normalize Greenhouse jobs."""

        jobs: list[Job] = []

        for board, item in raw_jobs:
            try:
                location = (item.get("location") or {}).get("name", "")

                first_published = item.get("first_published")

                if isinstance(first_published, (int, float)):
                    published = datetime.fromtimestamp(
                        first_published,
                        tz=UTC,
                    )
                else:
                    published = _make_aware(
                        parser.parse(str(first_published))
                    )

                jobs.append(
                    Job(
                        id=f"greenhouse-{item.get('internal_job_id')}",
                        title=item.get("title", "").strip(),
                        company=(
                            item.get("company_name")
                            or board.capitalize()
                        ),
                        location=location.strip(),
                        job_type="Full Time",
                        url=item.get("absolute_url", ""),
                        source="Greenhouse",
                        published_at=published,
                        remote="remote" in location.lower(),
                    )
                )

            except Exception as exc:
                print(f"Greenhouse normalization error: {exc}")

        return jobs

    @staticmethod
    def normalize_ashby(raw_jobs: list[tuple[str, dict]]) -> list[Job]:
        """Normalize Ashby jobs."""

        jobs: list[Job] = []

        for board, item in raw_jobs:
            try:
                published = parser.parse(item.get("publishedAt"))

                location = (
                    "Remote"
                    if item.get("isRemote")
                    else item.get("location", "")
                )

                jobs.append(
                    Job(
                        id=f"ashby-{item.get('id')}",
                        title=item.get("title", "").strip(),
                        company=(
                            item.get("company")
                            or ASHBY_BOARD_NAMES.get(
                                board,
                                board.capitalize(),
                            )
                        ),
                        location=str(location or "").strip(),
                        job_type=", ".join(
                            filter(
                                None,
                                [
                                    item.get("employmentType", ""),
                                    item.get("department", ""),
                                ],
                            )
                        ),
                        url=item.get("jobUrl", ""),
                        source="Ashby",
                        published_at=_make_aware(published),
                        remote=bool(item.get("isRemote")),
                    )
                )

            except Exception as exc:
                print(f"Ashby normalization error: {exc}")

        return jobs