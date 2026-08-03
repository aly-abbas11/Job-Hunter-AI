from job_hunter_ai.core.config import settings
from job_hunter_ai.core.logger import get_logger

logger = get_logger(__name__)


def main() -> None:
    logger.info("Job Hunter AI started.")
    logger.info("Maximum job age: %s days", settings.max_job_age_days)


if __name__ == "__main__":
    main()