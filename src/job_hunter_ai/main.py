from job_hunter_ai.clients.arbeitnow import ArbeitnowClient
from job_hunter_ai.clients.remoteok import RemoteOKClient
from job_hunter_ai.core.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    remoteok = RemoteOKClient()
    arbeitnow = ArbeitnowClient()

    remote_jobs = remoteok.fetch_jobs()
    arbeit_jobs = arbeitnow.fetch_jobs()

    total_jobs = len(remote_jobs) + len(arbeit_jobs)

    logger.info("=" * 50)
    logger.info("RemoteOK Jobs   : %s", len(remote_jobs))
    logger.info("Arbeitnow Jobs  : %s", len(arbeit_jobs))
    logger.info("Total Jobs      : %s", total_jobs)
    logger.info("=" * 50)


if __name__ == "__main__":
    main()