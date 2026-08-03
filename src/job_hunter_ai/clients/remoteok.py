"""
RemoteOK API client.
"""

from __future__ import annotations

import requests

from job_hunter_ai.core.config import settings
from job_hunter_ai.core.constants import REMOTEOK_API
from job_hunter_ai.core.logger import get_logger

logger = get_logger(__name__)


class RemoteOKClient:
    """Client for fetching jobs from RemoteOK."""

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
        Fetch all jobs from RemoteOK.
        """

        logger.info("Fetching jobs from RemoteOK...")

        try:
            response = self.session.get(
                REMOTEOK_API,
                timeout=settings.request_timeout,
            )

            response.raise_for_status()

            data = response.json()

            # First element is metadata
            jobs = data[1:]

            logger.info("Fetched %s jobs from RemoteOK.", len(jobs))

            return jobs

        except requests.RequestException as exc:
            logger.error("RemoteOK request failed: %s", exc)
            return []