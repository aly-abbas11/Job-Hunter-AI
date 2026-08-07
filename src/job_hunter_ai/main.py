"""
Main entry point for Job Hunter AI.
"""

from job_hunter_ai.clients.arbeitnow import ArbeitnowClient
from job_hunter_ai.clients.remoteok import RemoteOKClient
from job_hunter_ai.clients.remotive import RemotiveClient
from job_hunter_ai.core.logger import get_logger
from job_hunter_ai.services.diffing import JobDiff
from job_hunter_ai.services.filtering import JobFilter
from job_hunter_ai.services.normalization import JobNormalizer
from job_hunter_ai.services.readme_generator import ReadmeGenerator
from job_hunter_ai.services.state import JobState

logger = get_logger(__name__)


def print_summary(
    remote_count: int,
    arbeit_count: int,
    remotiv_count: int,
    normalized_count: int,
    filtered_jobs: list,
    previous_jobs: list,
    new_jobs: list,
    removed_jobs: list,
    unchanged_jobs: list,
) -> None:
    """Print application statistics."""

    internships = sum(JobFilter.is_internship(job) for job in filtered_jobs)
    remote_jobs = sum(JobFilter.is_remote(job) for job in filtered_jobs)
    pakistan_jobs = sum(JobFilter.is_pakistan(job) for job in filtered_jobs)

    logger.info("=" * 70)
    logger.info("RemoteOK fetched      : %d", remote_count)
    logger.info("Arbeitnow fetched     : %d", arbeit_count)
    logger.info("Remotive fetched      : %d", remotiv_count)
    logger.info("Total normalized      : %d", normalized_count)
    logger.info("Valid tech jobs       : %d", len(filtered_jobs))
    logger.info("")
    logger.info("Previous snapshot     : %d", len(previous_jobs))
    logger.info("Current snapshot      : %d", len(filtered_jobs))
    logger.info("")
    logger.info("New jobs              : %d", len(new_jobs))
    logger.info("Removed jobs          : %d", len(removed_jobs))
    logger.info("Unchanged jobs        : %d", len(unchanged_jobs))
    logger.info("")
    logger.info("Internships           : %d", internships)
    logger.info("Remote jobs           : %d", remote_jobs)
    logger.info("Pakistan jobs         : %d", pakistan_jobs)
    logger.info("=" * 70)


def print_top_job(filtered_jobs: list) -> None:
    """Print the highest ranked job."""

    if not filtered_jobs:
        logger.warning("No jobs available.")
        return

    top = max(filtered_jobs, key=JobFilter.score)

    logger.info("")
    logger.info("Top Ranked Job")
    logger.info("-" * 70)
    logger.info("Title      : %s", top.title)
    logger.info("Company    : %s", top.company)
    logger.info("Location   : %s", top.location)
    logger.info("Type       : %s", top.job_type)
    logger.info("Remote     : %s", top.remote)
    logger.info("Published  : %s", top.published_at.strftime("%Y-%m-%d"))
    logger.info("Source     : %s", top.source)
    logger.info("Score      : %d", JobFilter.score(top))
    logger.info("URL        : %s", top.url)
    logger.info("-" * 70)


def main() -> None:
    """Execute the complete Job Hunter AI pipeline."""

    logger.info("Starting Job Hunter AI...")

    remote_client = RemoteOKClient()
    arbeit_client = ArbeitnowClient()
    remotiv_client = RemotiveClient()

    # Fetch
    remote_raw = remote_client.fetch_jobs()
    arbeit_raw = arbeit_client.fetch_jobs()
    remotiv_raw = remotiv_client.fetch_jobs()

    # Normalize
    remote_jobs = JobNormalizer.normalize_remoteok(remote_raw)
    arbeit_jobs = JobNormalizer.normalize_arbeitnow(arbeit_raw)
    remotiv_jobs = JobNormalizer.normalize_remotive(remotiv_raw)

    all_jobs = remote_jobs + arbeit_jobs + remotiv_jobs

    # Filter
    filtered_jobs = JobFilter.filter_jobs(all_jobs)

    # Load previous snapshot
    previous_jobs = JobState.load()

    # Compare snapshots
    new_jobs, removed_jobs, unchanged_jobs = JobDiff.compare(
        previous_jobs,
        filtered_jobs,
    )

    # Save current snapshot
    JobState.save(filtered_jobs)

    logger.info("Current snapshot saved.")

    # Generate README.md
    ReadmeGenerator.generate(
        jobs=filtered_jobs,
        new_jobs=len(new_jobs),
        removed_jobs=len(removed_jobs),
    )

    logger.info("README.md generated successfully.")

    # Print statistics
    print_summary(
        len(remote_raw),
        len(arbeit_raw),
        len(remotiv_raw),
        len(all_jobs),
        filtered_jobs,
        previous_jobs,
        new_jobs,
        removed_jobs,
        unchanged_jobs,
    )

    # Print best job
    print_top_job(filtered_jobs)


if __name__ == "__main__":
    main()