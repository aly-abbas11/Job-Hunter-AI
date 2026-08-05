from datetime import UTC, datetime, timedelta

from job_hunter_ai.models.job import Job
from job_hunter_ai.services.filtering import JobFilter


def make_job(
    title="Python Developer",
    company="ABC Company",
    location="Berlin",
    remote=False,
    published_at=None,
):
    if published_at is None:
        published_at = datetime.now(UTC)

    return Job(
        id=f"{title}-{company}",
        title=title,
        company=company,
        location=location,
        job_type="Full Time",
        url="https://example.com",
        source="RemoteOK",
        published_at=published_at,
        remote=remote,
    )


def test_is_recent():
    job = make_job()

    assert JobFilter.is_recent(job)


def test_old_job_not_recent():
    old = datetime.now(UTC) - timedelta(days=30)

    job = make_job(published_at=old)

    assert not JobFilter.is_recent(job)


def test_is_tech_job():
    job = make_job(title="Python Backend Developer")

    assert JobFilter.is_tech_job(job)


def test_non_tech_job():
    job = make_job(title="Restaurant Manager")

    assert not JobFilter.is_tech_job(job)


def test_remote_detection():
    job = make_job(
        title="Python Developer",
        location="Remote",
        remote=True,
    )

    assert JobFilter.is_remote(job)


def test_pakistan_detection():
    job = make_job(location="Lahore")

    assert JobFilter.is_pakistan(job)


def test_internship_detection():
    job = make_job(title="Software Engineering Intern")

    assert JobFilter.is_internship(job)


def test_valid_job():
    job = make_job()

    assert JobFilter.is_valid(job)


def test_invalid_job():
    job = make_job(
        title="",
        company="",
    )

    assert not JobFilter.is_valid(job)


def test_deduplicate():
    jobs = [
        make_job(),
        make_job(),
    ]

    unique = JobFilter.deduplicate(jobs)

    assert len(unique) == 1


def test_filter_pipeline():
    jobs = [
        make_job(title="Python Developer"),
        make_job(title="Restaurant Chef"),
    ]

    filtered = JobFilter.filter_jobs(jobs)

    assert len(filtered) == 1
    assert filtered[0].title == "Python Developer"