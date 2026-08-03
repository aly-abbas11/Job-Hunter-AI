from job_hunter_ai.clients.remoteok import RemoteOKClient
from job_hunter_ai.core.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    client = RemoteOKClient()

    jobs = client.fetch_jobs()

    logger.info("Received %s jobs.", len(jobs))

    if jobs:
        logger.info("First job: %s", jobs[0].get("position"))


if __name__ == "__main__":
    main()