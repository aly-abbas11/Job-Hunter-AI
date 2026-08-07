"""
We Work Remotely RSS feed client.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET

import requests

from job_hunter_ai.core.config import settings
from job_hunter_ai.core.constants import WW_REMOTELY_RSS
from job_hunter_ai.core.logger import get_logger

logger = get_logger(__name__)


class WeWorkRemotelyClient:
    """Client for fetching jobs from the We Work Remotely RSS feed."""

    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": settings.user_agent,
                "Accept": "application/rss+xml",
            }
        )

    def fetch_jobs(self) -> list[dict]:
        """
        Fetch jobs from the We Work Remotely category feeds.
        """

        jobs: list[dict] = []

        for feed in WW_REMOTELY_RSS:
            logger.info("Fetching We Work Remotely feed %s...", feed)

            try:
                response = self.session.get(
                    feed,
                    timeout=settings.request_timeout,
                )

                response.raise_for_status()

                root = ET.fromstring(response.content)

                for item in root.findall(".//item"):
                    job = {}

                    for field in ("title", "link", "pubDate"):
                        node = item.find(field)

                        if node is not None and node.text:
                            job[field] = node.text.strip()

                    for field in ("region", "category"):
                        node = item.find(field)

                        if node is not None and node.text:
                            job[field] = node.text.strip()

                    if job.get("link"):
                        jobs.append(job)

            except (requests.RequestException, ET.ParseError) as exc:
                logger.error(
                    "We Work Remotely feed %s failed: %s",
                    feed,
                    exc,
                )

        logger.info("Fetched %s jobs from We Work Remotely.", len(jobs))

        return jobs
