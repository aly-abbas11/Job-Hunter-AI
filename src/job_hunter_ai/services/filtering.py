"""
Filtering and scoring service for Job Hunter AI.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Iterable

from job_hunter_ai.core.constants import (
    INTERNSHIP_KEYWORDS,
    MAX_JOB_AGE_HOURS,
    PAKISTAN_CITIES,
    REMOTE_KEYWORDS,
    STARTER_KEYWORDS,
    TECH_KEYWORDS,
)
from job_hunter_ai.models.job import Job
from job_hunter_ai.services.scoring import JobScorer


class JobFilter:
    """
    Handles filtering, validation and scoring of jobs.
    """

    @staticmethod
    def _normalize(text: str | None) -> str:
        """Normalize text for comparisons."""

        if not text:
            return ""

        return text.strip().lower()

    @classmethod
    def is_recent(cls, job: Job) -> bool:
        """Return True if the job is newer than MAX_JOB_AGE_HOURS."""

        age = datetime.now(UTC) - job.published_at
        return age.total_seconds() <= MAX_JOB_AGE_HOURS * 3600

    @classmethod
    def is_tech_job(cls, job: Job) -> bool:
        """
        Determine whether a job belongs to the tech industry.
        """

        searchable = (
            f"{job.title} "
            f"{job.job_type}"
        ).lower()

        words = set(
            searchable.replace("/", " ")
            .replace("-", " ")
            .split()
        )

        for keyword in TECH_KEYWORDS:

            keyword = keyword.lower()

            if " " in keyword:
                if keyword in searchable:
                    return True
            else:
                if keyword in words:
                    return True

        return False

    @classmethod
    def is_internship(cls, job: Job) -> bool:
        """
        Detect internship / graduate jobs.
        """

        title = cls._normalize(job.title)
        job_type = cls._normalize(job.job_type)

        return any(
            word in title or word in job_type
            for word in INTERNSHIP_KEYWORDS
        )

    @classmethod
    def is_remote(cls, job: Job) -> bool:
        """
        Detect remote jobs.
        """

        if job.remote:
            return True

        searchable = f"{job.location} {job.job_type}".lower()

        return any(word in searchable for word in REMOTE_KEYWORDS)

    @classmethod
    def is_starter_job(cls, job: Job) -> bool:
        """
        Detect career starter roles: admin, virtual assistant,
        graphics/design, writing, customer support.
        """

        searchable = (
            f"{job.title} {job.job_type}"
        ).lower()

        words = set(
            searchable.replace("/", " ")
            .replace("-", " ")
            .split()
        )

        for keyword in STARTER_KEYWORDS:

            keyword = keyword.lower()

            if " " in keyword:
                if keyword in searchable:
                    return True
            else:
                if keyword in words:
                    return True

        return False

    @classmethod
    def is_pakistan(cls, job: Job) -> bool:
        """
        Detect Pakistan-based jobs.
        """

        location = cls._normalize(job.location)

        return any(city in location for city in PAKISTAN_CITIES)

    @classmethod
    def is_valid(cls, job: Job) -> bool:
        """
        Reject obviously broken jobs.
        """

        if not job.title:
            return False

        if not job.company:
            return False

        if not job.url:
            return False

        if job.title.lower() == job.company.lower():
            return False

        if len(job.title) < 3:
            return False

        return True

    @classmethod
    def score(cls, job: Job) -> int:
        """
        Return the calculated job score.
        """

        return JobScorer.score(job)

    @classmethod
    def deduplicate(cls, jobs: Iterable[Job]) -> list[Job]:
        """
        Remove duplicate jobs.
        """

        unique: dict[str, Job] = {}

        for job in jobs:
            key = (
                f"{job.title.lower()}|"
                f"{job.company.lower()}|"
                f"{job.location.lower()}"
            )

            if key not in unique:
                unique[key] = job

        return list(unique.values())

    @classmethod
    def _filter_base(cls, jobs: list[Job]) -> list[Job]:
        """
        Shared pipeline: valid, recent and remote jobs, deduplicated.
        """

        filtered: list[Job] = []

        for job in jobs:

            if not cls.is_valid(job):
                continue

            if not cls.is_recent(job):
                continue

            if not cls.is_remote(job):
                continue

            filtered.append(job)

        return cls.deduplicate(filtered)

    @classmethod
    def split_jobs(cls, jobs: list[Job]) -> tuple[list[Job], list[Job]]:
        """
        Split filtered jobs into tech and career-starter lists.

        Career starter roles (admin, design, writing, support) take
        priority; tech jobs are what remains. Returns (tech, starter).
        """

        base = cls._filter_base(jobs)

        starter = [job for job in base if cls.is_starter_job(job)]
        starter_ids = {job.id for job in starter}

        tech = [
            job
            for job in base
            if job.id not in starter_ids and cls.is_tech_job(job)
        ]

        starter.sort(
            key=lambda job: (
                cls.score(job),
                job.published_at,
            ),
            reverse=True,
        )

        tech.sort(
            key=lambda job: (
                cls.score(job),
                job.published_at,
            ),
            reverse=True,
        )

        return tech, starter

    @classmethod
    def filter_jobs(cls, jobs: list[Job]) -> list[Job]:
        """
        Complete filtering pipeline for tech jobs.
        """

        tech, _ = cls.split_jobs(jobs)

        return tech