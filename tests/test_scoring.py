from datetime import UTC, datetime

from job_hunter_ai.models.job import Job
from job_hunter_ai.services.scoring import JobScorer


def make_job(
    title: str,
    company: str = "OpenAI",
    location: str = "Remote",
    job_type: str = "Full Time",
    remote: bool = True,
) -> Job:
    return Job(
        id="1",
        title=title,
        company=company,
        location=location,
        job_type=job_type,
        url="https://example.com",
        source="RemoteOK",
        published_at=datetime.now(UTC),
        remote=remote,
    )


def test_python_job_scores():
    job = make_job("Python Backend Developer")
    assert JobScorer.score(job) > 0


def test_internship_scores_higher():
    normal = make_job("Python Developer")
    intern = make_job("Python Internship")

    assert JobScorer.score(intern) > JobScorer.score(normal)


def test_remote_job_scores():
    remote_job = make_job("Software Engineer", remote=True)
    onsite_job = make_job(
        "Software Engineer",
        location="Berlin",
        remote=False,
    )

    assert JobScorer.score(remote_job) > JobScorer.score(onsite_job)


def test_ai_job_scores():
    job = make_job("AI Machine Learning Engineer")
    assert JobScorer.score(job) > 0


def test_junior_job_scores():
    junior = make_job("Junior Python Developer")
    senior = make_job("Senior Python Developer")

    assert JobScorer.score(junior) > JobScorer.score(senior)