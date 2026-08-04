"""
Global constants for Job Hunter AI.
"""

from __future__ import annotations

# ==========================================================
# API Endpoints
# ==========================================================

REMOTEOK_API = "https://remoteok.com/api"

ARBEITNOW_API = "https://www.arbeitnow.com/api/job-board-api"

# ==========================================================
# Filtering Configuration
# ==========================================================

MAX_JOB_AGE_DAYS = 14

SUPPORTED_SOURCES = (
    "RemoteOK",
    "Arbeitnow",
)

# ==========================================================
# Tech Keywords
# ==========================================================

TECH_KEYWORDS = {
    "software",
    "developer",
    "engineer",
    "backend",
    "frontend",
    "front-end",
    "fullstack",
    "full-stack",
    "python",
    "java",
    "javascript",
    "typescript",
    "react",
    "next",
    "nextjs",
    "next.js",
    "vue",
    "angular",
    "node",
    "nodejs",
    "node.js",
    "django",
    "flask",
    "fastapi",
    "laravel",
    "php",
    ".net",
    "dotnet",
    "c",
    "c++",
    "c#",
    "go",
    "golang",
    "rust",
    "swift",
    "kotlin",
    "android",
    "ios",
    "mobile",
    "web",
    "devops",
    "docker",
    "kubernetes",
    "terraform",
    "linux",
    "cloud",
    "aws",
    "azure",
    "gcp",
    "database",
    "sql",
    "postgres",
    "postgresql",
    "mysql",
    "mongodb",
    "redis",
    "qa",
    "testing",
    "automation",
    "sdet",
    "security",
    "cybersecurity",
    "network",
    "ai",
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "ml",
    "nlp",
    "computer vision",
    "data",
    "data engineer",
    "data analyst",
    "data scientist",
    "blockchain",
    "web3",
    "it",
    "it support",
}

# ==========================================================
# Internship Keywords
# ==========================================================

INTERNSHIP_KEYWORDS = {
    "intern",
    "internship",
    "graduate",
    "graduate program",
    "entry level",
    "entry-level",
    "junior",
    "trainee",
    "associate",
}

# ==========================================================
# Remote Keywords
# ==========================================================

REMOTE_KEYWORDS = {
    "remote",
    "worldwide",
    "distributed",
    "work from home",
    "wfh",
}

# ==========================================================
# Pakistan Locations
# ==========================================================

PAKISTAN_CITIES = {
    "pakistan",
    "lahore",
    "karachi",
    "islamabad",
    "rawalpindi",
    "multan",
    "faisalabad",
    "peshawar",
    "quetta",
    "sialkot",
    "gujranwala",
}

# ==========================================================
# Job Score Weights
# ==========================================================

SCORE_WEIGHTS = {
    "internship": 40,
    "graduate": 35,
    "junior": 25,
    "remote": 15,
    "python": 15,
    "ai": 20,
    "backend": 10,
    "frontend": 10,
    "fullstack": 15,
    "qa": 10,
    "cloud": 10,
}

# ==========================================================
# README Configuration
# ==========================================================

MAX_README_JOBS = 30

README_DATE_FORMAT = "%d %B %Y %H:%M UTC"