"""
Main entry point for Job Hunter AI.
"""

from job_hunter_ai.clients.arbeitnow import ArbeitnowClient
from job_hunter_ai.clients.remoteok import RemoteOKClient
from job_hunter_ai.core.logger import get_logger
from job_hunter_ai.services.normalization import JobNormalizer

logger = get_logger(__name__)


def main() -> None:
    """Run the Job Hunter AI pipeline."""

    logger.info("Starting Job Hunter AI...")

    # Initialize API clients
    remote_client = RemoteOKClient()
    arbeit_client = ArbeitnowClient()

    # Fetch raw jobs
    remote_raw = remote_client.fetch_jobs()
    arbeit_raw = arbeit_client.fetch_jobs()

    # Normalize jobs
    remote_jobs = JobNormalizer.normalize_remoteok(remote_raw)
    arbeit_jobs = JobNormalizer.normalize_arbeitnow(arbeit_raw)

    # Merge into a single collection
    all_jobs = remote_jobs + arbeit_jobs

    # Summary
    logger.info("=" * 60)
    logger.info("RemoteOK normalized : %d", len(remote_jobs))
    logger.info("Arbeitnow normalized: %d", len(arbeit_jobs))
    logger.info("Total normalized    : %d", len(all_jobs))
    logger.info("=" * 60)

    # Show a sample job
    if all_jobs:
        sample = all_jobs[0]

        logger.info("Sample Job")
        logger.info("Title      : %s", sample.title)
        logger.info("Company    : %s", sample.company)
        logger.info("Location   : %s", sample.location)
        logger.info("Type       : %s", sample.job_type)
        logger.info("Remote     : %s", sample.remote)
        logger.info("Published  : %s", sample.published_at)
        logger.info("Source     : %s", sample.source)
        logger.info("URL        : %s", sample.url)


if __name__ == "__main__":
    main()