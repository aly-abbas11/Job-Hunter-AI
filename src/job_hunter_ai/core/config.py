"""
Application configuration.
"""

from dataclasses import dataclass

from job_hunter_ai.core.constants import MAX_JOB_AGE_DAYS


@dataclass(slots=True)
class Settings:
    """
    Global application settings.
    """

    max_job_age_days: int = MAX_JOB_AGE_DAYS

    request_timeout: int = 15

    user_agent: str = (
        "Job-Hunter-AI "
        "(https://github.com/aly-abbas11/Job-Hunter-AI)"
    )


settings = Settings()