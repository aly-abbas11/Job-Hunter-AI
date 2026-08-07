"""
Main entry point for Job Hunter AI.
"""

from job_hunter_ai.clients.arbeitnow import ArbeitnowClient
from job_hunter_ai.clients.ashby import AshbyClient
from job_hunter_ai.clients.greenhouse import GreenhouseClient
from job_hunter_ai.clients.remoteok import RemoteOKClient
from job_hunter_ai.clients.remotive import RemotiveClient
from job_hunter_ai.clients.wwr import WeWorkRemotelyClient
from job_hunter_ai.core.logger import get_logger
from job_hunter_ai.services.diffing import JobDiff
from job_hunter_ai.services.filtering import JobFilter
from job_hunter_ai.services.normalization import JobNormalizer
from job_hunter_ai.services.readme_generator import ReadmeGenerator
from job_hunter_ai.services.state import JobState

logger = get_logger(__name__)


def print_summary(
    fetched: dict[str, int],
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
    starter_jobs = sum(
        JobFilter.is_starter_job(job) for job in filtered_jobs
    )

    logger.info("=" * 70)

    for source, count in fetched.items():
        logger.info("%-22s : %d", f"{source} fetched", count)

    logger.info("Total normalized      : %d", normalized_count)
    logger.info("Valid tech jobs       : %d",
                len(filtered_jobs) - starter_jobs)
    logger.info("Career starter jobs   : %d", starter_jobs)
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
    greenhouse_client = GreenhouseClient()
    ashby_client = AshbyClient()
    wwr_client = WeWorkRemotelyClient()

    # Fetch
    remote_raw = remote_client.fetch_jobs()
    arbeit_raw = arbeit_client.fetch_jobs()
    remotiv_raw = remotiv_client.fetch_jobs()
    greenhouse_raw = greenhouse_client.fetch_jobs()
    ashby_raw = ashby_client.fetch_jobs()
    wwr_raw = wwr_client.fetch_jobs()

    # Normalize
    remote_jobs = JobNormalizer.normalize_remoteok(remote_raw)
    arbeit_jobs = JobNormalizer.normalize_arbeitnow(arbeit_raw)
    remotiv_jobs = JobNormalizer.normalize_remotive(remotiv_raw)
    greenhouse_jobs = JobNormalizer.normalize_greenhouse(greenhouse_raw)
    ashby_jobs = JobNormalizer.normalize_ashby(ashby_raw)
    wwr_jobs = JobNormalizer.normalize_wwr(wwr_raw)

    all_jobs = (
        remote_jobs
        + arbeit_jobs
        + remotiv_jobs
        + greenhouse_jobs
        + ashby_jobs
        + wwr_jobs
    )

    # Filter
    tech_jobs, starter_jobs = JobFilter.split_jobs(all_jobs)

    combined_jobs = tech_jobs + starter_jobs

    # Load previous snapshot
    previous_jobs = JobState.load()

    # Compare snapshots
    new_jobs, removed_jobs, unchanged_jobs = JobDiff.compare(
        previous_jobs,
        combined_jobs,
    )

    # Save current snapshot
    JobState.save(combined_jobs)

    logger.info("Current snapshot saved.")

    # Generate README.md
    ReadmeGenerator.generate(
        jobs=tech_jobs,
        starter_jobs=starter_jobs,
        new_jobs=len(new_jobs),
        removed_jobs=len(removed_jobs),
    )

    logger.info("README.md generated successfully.")

    # Print statistics
    print_summary(
        fetched={
            "RemoteOK": len(remote_raw),
            "Arbeitnow": len(arbeit_raw),
            "Remotive": len(remotiv_raw),
            "Greenhouse": len(greenhouse_raw),
            "Ashby": len(ashby_raw),
            "WeWorkRemotely": len(wwr_raw),
        },
        normalized_count=len(all_jobs),
        filtered_jobs=combined_jobs,
        previous_jobs=previous_jobs,
        new_jobs=new_jobs,
        removed_jobs=removed_jobs,
        unchanged_jobs=unchanged_jobs,
    )

    # Print best job
    print_top_job(tech_jobs + starter_jobs)


if __name__ == "__main__":
    main()