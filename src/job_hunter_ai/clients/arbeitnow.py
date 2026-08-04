"""
Arbeitnow API client.
"""

from __future__ import annotations

import requests

from job_hunter_ai.core.config import settings
from job_hunter_ai.core.constants import ARBEITNOW_API
from job_hunter_ai.core.logger import get_logger

logger = get_logger(__name__)


class ArbeitnowClient:
    """Client for fetching jobs from Arbeitnow."""

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": settings.user_agent,
                "Accept": "application/json",
            }
        )

    def fetch_jobs(self) -> list[dict]:
        """Fetch jobs from Arbeitnow."""

        logger.info("Fetching jobs from Arbeitnow...")

        try:
            response = self.session.get(
                ARBEITNOW_API,
                timeout=settings.request_timeout,
            )

            response.raise_for_status()

            data = response.json()

            jobs = data.get("data", [])

            logger.info("Fetched %s jobs from Arbeitnow.", len(jobs))

            return jobs

        except requests.RequestException as exc:
            logger.error("Arbeitnow request failed: %s", exc)
            return []