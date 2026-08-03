from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Job:
    """
    Represents a normalized job posting from any supported provider.
    """

    id: str
    title: str
    company: str
    location: str
    job_type: str
    url: str
    source: str
    published_at: datetime
    remote: bool = True

    def to_dict(self) -> dict:
        """Convert the Job object into a JSON-serializable dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "job_type": self.job_type,
            "url": self.url,
            "source": self.source,
            "published_at": self.published_at.isoformat(),
            "remote": self.remote,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Job":
        """Create a Job object from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            company=data["company"],
            location=data["location"],
            job_type=data["job_type"],
            url=data["url"],
            source=data["source"],
            published_at=datetime.fromisoformat(data["published_at"]),
            remote=data.get("remote", True),
        )