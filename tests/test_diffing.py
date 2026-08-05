from datetime import datetime, UTC

from job_hunter_ai.models.job import Job
from job_hunter_ai.services.diffing import JobDiff


def make_job(job_id: str) -> Job:
    return Job(
        id=job_id,
        title="Python Developer",
        company="OpenAI",
        location="Remote",
        job_type="Full Time",
        url=f"https://example.com/{job_id}",
        source="RemoteOK",
        published_at=datetime.now(UTC),
        remote=True,
    )


def test_compare_jobs():
    previous = [
        make_job("1"),
        make_job("2"),
        make_job("3"),
    ]

    current = [
        make_job("2"),
        make_job("3"),
        make_job("4"),
    ]

    new_jobs, removed_jobs, unchanged_jobs = JobDiff.compare(
        previous,
        current,
    )

    assert len(new_jobs) == 1
    assert new_jobs[0].id == "4"

    assert len(removed_jobs) == 1
    assert removed_jobs[0].id == "1"

    assert len(unchanged_jobs) == 2