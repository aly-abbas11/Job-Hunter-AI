"""
Global constants for Job Hunter AI.
"""

from __future__ import annotations

# ==========================================================
# API Endpoints
# ==========================================================

REMOTEOK_API = "https://remoteok.com/api"

ARBEITNOW_API = "https://www.arbeitnow.com/api/job-board-api"

REMOTIVE_API = "https://remotive.com/api/remote-jobs"

GREENHOUSE_API = "https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

ASHBY_API = "https://api.ashbyhq.com/posting-api/job-board/{company}"

WW_REMOTELY_RSS = (
    "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-design-jobs.rss",
    "https://weworkremotely.com/categories/remote-customer-support-jobs.rss",
    "https://weworkremotely.com/categories/remote-copywriting-jobs.rss",
)

# ==========================================================
# Filtering Configuration
# ==========================================================

MAX_JOB_AGE_HOURS = 24

SUPPORTED_SOURCES = (
    "RemoteOK",
    "Arbeitnow",
    "Remotive",
    "Greenhouse",
    "Ashby",
    "WeWorkRemotely",
)

GREENHOUSE_BOARDS = (
    "airbnb",
    "stripe",
    "gitlab",
    "reddit",
    "pinterest",
    "cloudflare",
    "coinbase",
    "roblox",
    "dropbox",
    "instacart",
    "datadog",
)

ASHBY_BOARDS = (
    "openai",
    "ramp",
    "linear",
    "supabase",
    "resend",
    "warp",
)

ASHBY_BOARD_NAMES = {
    "openai": "OpenAI",
    "ramp": "Ramp",
    "linear": "Linear",
    "supabase": "Supabase",
    "resend": "Resend",
    "warp": "Warp",
}

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
    "entry",
    "junior",
    "trainee",
    "associate",
    "apprentice",
    "apprenticeship",
    "student",
    "working student",
    "werkstudent",
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
# API Endpoints
# ==========================================================

REMOTEOK_API = "https://remoteok.com/api"

ARBEITNOW_API = "https://www.arbeitnow.com/api/job-board-api"

REMOTIVE_API = "https://remotive.com/api/remote-jobs"

GREENHOUSE_API = "https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

ASHBY_API = "https://api.ashbyhq.com/posting-api/job-board/{company}"


# ==========================================================
# Filtering Configuration
# ==========================================================

MAX_JOB_AGE_HOURS = 24

SUPPORTED_SOURCES = (
    "RemoteOK",
    "Arbeitnow",
    "Remotive",
    "Greenhouse",
    "Ashby",
    "WeWorkRemotely",
)

GREENHOUSE_BOARDS = (
    "airbnb",
    "stripe",
    "gitlab",
    "reddit",
    "pinterest",
    "cloudflare",
    "coinbase",
    "roblox",
    "dropbox",
    "instacart",
    "datadog",
)

ASHBY_BOARDS = (
    "openai",
    "ramp",
    "linear",
    "supabase",
    "resend",
    "warp",
)

ASHBY_BOARD_NAMES = {
    "openai": "OpenAI",
    "ramp": "Ramp",
    "linear": "Linear",
    "supabase": "Supabase",
    "resend": "Resend",
    "warp": "Warp",
}

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
    "entry",
    "junior",
    "trainee",
    "associate",
    "apprentice",
    "apprenticeship",
    "student",
    "working student",
    "werkstudent",
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
# Career Starter Keywords
# ==========================================================
# Entry-level friendly roles: admin, virtual assistance,
# graphics/design, writing, customer support. Data entry and
# transcription are intentionally excluded (scam magnets).

STARTER_KEYWORDS = {
    "admin",
    "administrative",
    "assistant",
    "virtual assistant",
    "support",
    "customer service",
    "customer support",
    "helpdesk",
    "receptionist",
    "scheduler",
    "office manager",
    "executive assistant",
    "designer",
    "graphic design",
    "graphic designer",
    "product designer",
    "ui designer",
    "ux designer",
    "web designer",
    "visual designer",
    "brand designer",
    "creative designer",
    "ui",
    "ux",
    "illustrator",
    "photoshop",
    "figma",
    "copywriter",
    "copywriting",
    "content writer",
    "content creator",
    "social media",
    "writer",
    "writing",
    "editor",
    "proofreader",
    "blogger",
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