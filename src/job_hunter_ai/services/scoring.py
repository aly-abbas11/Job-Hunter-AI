"""
Job scoring service.
"""

from __future__ import annotations

from job_hunter_ai.core.constants import SCORE_WEIGHTS
from job_hunter_ai.models.job import Job


class JobScorer:
    """Scores jobs based on relevance."""

    @staticmethod
    def score(job: Job) -> int:
        score = 0

        text = (
            f"{job.title} "
            f"{job.company} "
            f"{job.location} "
            f"{job.job_type}"
        ).lower()

        # Internship / Graduate
        if "intern" in text:
            score += SCORE_WEIGHTS["internship"]

        if "graduate" in text:
            score += SCORE_WEIGHTS["graduate"]

        if "junior" in text:
            score += SCORE_WEIGHTS["junior"]

        # Remote
        if job.remote or "remote" in text:
            score += SCORE_WEIGHTS["remote"]

        # Technical keywords
        for keyword, weight in SCORE_WEIGHTS.items():
            if keyword in text:
                score += weight

        return score