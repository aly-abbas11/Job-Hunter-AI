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


def test_job_posted_within_24h_is_recent():
    recent = datetime.now(UTC) - timedelta(hours=12)

    job = make_job(published_at=recent)

    assert JobFilter.is_recent(job)


def test_job_older_than_24h_not_recent():
    old = datetime.now(UTC) - timedelta(hours=36)

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
        make_job(title="Python Developer", location="Remote"),
        make_job(title="Restaurant Chef", location="Remote"),
        make_job(title="Python Developer", location="Berlin", remote=False),
    ]

    filtered = JobFilter.filter_jobs(jobs)

    assert len(filtered) == 1
    assert filtered[0].title == "Python Developer"


def test_filter_pipeline_keeps_remote_internships():
    jobs = [
        make_job(
            title="Software Engineering Intern",
            location="Remote",
            remote=True,
        ),
    ]

    filtered = JobFilter.filter_jobs(jobs)

    assert len(filtered) == 1
    assert JobFilter.is_internship(filtered[0])
    assert JobFilter.is_remote(filtered[0])


def test_filter_pipeline_rejects_non_remote():
    jobs = [
        make_job(title="Python Developer", location="Berlin", remote=False),
        make_job(title="Python Developer", location="Lahore", remote=False),
    ]

    filtered = JobFilter.filter_jobs(jobs)

    assert filtered == []


def test_starter_job_detection():
    job = make_job(
        title="Virtual Assistant",
        location="Remote",
        remote=True,
    )

    assert JobFilter.is_starter_job(job)


def test_starter_job_detection_design():
    job = make_job(
        title="Graphic Designer",
        location="Remote",
        remote=True,
    )

    assert JobFilter.is_starter_job(job)


def test_tech_job_not_starter():
    job = make_job(
        title="Senior Backend Engineer",
        location="Remote",
        remote=True,
    )

    assert not JobFilter.is_starter_job(job)


def test_split_jobs_returns_starter_and_tech():
    jobs = [
        make_job(
            title="Python Developer",
            location="Remote",
            remote=True,
        ),
        make_job(
            title="Virtual Assistant",
            location="Remote",
            remote=True,
        ),
        make_job(
            title="Restaurant Chef",
            location="Remote",
            remote=True,
        ),
    ]

    tech, starter = JobFilter.split_jobs(jobs)

    assert len(tech) == 1
    assert tech[0].title == "Python Developer"
    assert len(starter) == 1
    assert starter[0].title == "Virtual Assistant"