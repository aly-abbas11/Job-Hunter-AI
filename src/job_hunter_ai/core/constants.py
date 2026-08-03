"""
Application constants.

This module contains values that rarely change and are shared across
multiple parts of the application.
"""

from pathlib import Path

# ---------------------------------------------------------------------
# Project Paths
# ---------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_DIR = PROJECT_ROOT / "data"

STATE_DIR = DATA_DIR / "state"
CACHE_DIR = DATA_DIR / "cache"
HISTORY_DIR = DATA_DIR / "history"

README_FILE = PROJECT_ROOT / "README.md"

PREVIOUS_JOBS_FILE = STATE_DIR / "previous_jobs.json"
METADATA_FILE = STATE_DIR / "metadata.json"
JOB_HISTORY_FILE = HISTORY_DIR / "job_history.json"

# ---------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------

REMOTEOK_API = "https://remoteok.com/api"

ARBEITNOW_API = "https://www.arbeitnow.com/api/job-board-api"

# ---------------------------------------------------------------------
# README markers
# ---------------------------------------------------------------------

README_START = "<!-- JOBS:START -->"

README_END = "<!-- JOBS:END -->"

# ---------------------------------------------------------------------
# Automation
# ---------------------------------------------------------------------

UPDATE_INTERVAL_HOURS = 3

MAX_JOB_AGE_DAYS = 14