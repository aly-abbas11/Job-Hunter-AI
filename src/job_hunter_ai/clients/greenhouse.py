"""
Greenhouse job board API client.
"""

from __future__ import annotations

import requests

from job_hunter_ai.core.config import settings
from job_hunter_ai.core.constants import GREENHOUSE_API, GREENHOUSE_BOARDS
from job_hunter_ai.core.logger import get_logger

logger = get_logger(__name__)


class GreenhouseClient:
    """Client for fetching jobs from company Greenhouse boards."""

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": settings.user_agent,
                "Accept": "application/json",
            }
        )

    def fetch_jobs(self) -> list[tuple[str, dict]]:
        """
        Fetch jobs from all configured Greenhouse boards.

        Returns a list of (board, job) tuples so the normalizer can
        attribute each job to its company board.
        """

        jobs: list[tuple[str, dict]] = []

        for company in GREENHOUSE_BOARDS:
            try:
                response = self.session.get(
                    GREENHOUSE_API.format(company=company),
                    params={
                        "content": "false",
                        "limit": "500",
                    },
                    timeout=settings.request_timeout,
                )

                response.raise_for_status()

                data = response.json()

                for job in data.get("jobs", []):
                    jobs.append((company, job))

            except requests.RequestException as exc:
                logger.error(
                    "Greenhouse board %s failed: %s",
                    company,
                    exc,
                )

        logger.info("Fetched %s jobs from Greenhouse.", len(jobs))

        return jobs
