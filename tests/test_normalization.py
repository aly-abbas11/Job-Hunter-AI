from datetime import UTC, datetime

from job_hunter_ai.services.normalization import JobNormalizer


def test_normalize_greenhouse():
    jobs = JobNormalizer.normalize_greenhouse(
        [
            (
                "gitlab",
                {
                    "internal_job_id": "12345",
                    "title": "Backend Engineer",
                    "company_name": "GitLab",
                    "location": {"name": "Remote, Europe"},
                    "absolute_url": "https://boards.greenhouse.io/jobs/12345",
                    "first_published": 1710000000,
                },
            ),
        ]
    )

    assert len(jobs) == 1
    job = jobs[0]

    assert job.id == "greenhouse-12345"
    assert job.title == "Backend Engineer"
    assert job.company == "GitLab"
    assert job.location == "Remote, Europe"
    assert job.source == "Greenhouse"
    assert job.remote is True
    assert job.published_at == datetime.fromtimestamp(
        1710000000, tz=UTC
    )


def test_normalize_ashby():
    jobs = JobNormalizer.normalize_ashby(
        [
            (
                "openai",
                {
                    "id": "abc-123",
                    "title": "ML Engineer",
                    "isRemote": True,
                    "location": "San Francisco",
                    "publishedAt": "2026-08-07T10:00:00Z",
                    "jobUrl": "https://jobs.ashbyhq.com/openai/abc-123",
                    "employmentType": "FullTime",
                    "department": "Research",
                },
            ),
        ]
    )

    assert len(jobs) == 1
    job = jobs[0]

    assert job.id == "ashby-abc-123"
    assert job.title == "ML Engineer"
    assert job.company == "OpenAI"
    assert job.location == "Remote"
    assert job.remote is True
    assert job.source == "Ashby"
    assert "Research" in job.job_type


def test_normalize_ashby_onsite_not_remote():
    jobs = JobNormalizer.normalize_ashby(
        [
            (
                "linear",
                {
                    "id": "xyz-9",
                    "title": "Accountant",
                    "isRemote": False,
                    "location": "New York",
                    "publishedAt": "2026-08-07T10:00:00Z",
                    "jobUrl": "https://jobs.ashbyhq.com/linear/xyz-9",
                },
            ),
        ]
    )

    assert len(jobs) == 1
    job = jobs[0]

    assert job.remote is False
    assert job.location == "New York"
