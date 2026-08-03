from datetime import datetime

from job_hunter_ai.models.job import Job


def main() -> None:
    job = Job(
        id="1",
        title="Python Developer",
        company="OpenAI",
        location="Remote",
        job_type="Full-time",
        url="https://example.com",
        source="Demo",
        published_at=datetime.now(),
    )

    print(job)
    print(job.to_dict())


if __name__ == "__main__":
    main()