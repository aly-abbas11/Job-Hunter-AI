"""
Remotive API client.
"""

from __future__ import annotations

import requests

from job_hunter_ai.core.config import settings
from job_hunter_ai.core.constants import REMOTIVE_API
from job_hunter_ai.core.logger import get_logger

logger = get_logger(__name__)


class RemotiveClient:
    """Client for fetching jobs from Remotive."""

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": settings.user_agent,
                "Accept": "application/json",
            }
        )

    def fetch_jobs(self) -> list[dict]:
        """
        Fetch all jobs from Remotive.
        """

        logger.info("Fetching jobs from Remotive...")

        try:
            response = self.session.get(
                REMOTIVE_API,
                timeout=settings.request_timeout,
            )

            response.raise_for_status()

            data = response.json()

            jobs = data.get("jobs", [])

            logger.info("Fetched %s jobs from Remotive.", len(jobs))

            return jobs

        except requests.RequestException as exc:
            logger.error("Remotive request failed: %s", exc)
            return []
