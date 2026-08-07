"""
Application configuration.
"""

from dataclasses import dataclass

from job_hunter_ai.core.constants import MAX_JOB_AGE_HOURS


@dataclass(slots=True)
class Settings:
    """
    Global application settings.
    """

    max_job_age_hours: int = MAX_JOB_AGE_HOURS

    request_timeout: int = 15

    user_agent: str = (
        "Job-Hunter-AI "
        "(https://github.com/aly-abbas11/Job-Hunter-AI)"
    )


settings = Settings()