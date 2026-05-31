"""
config/config.py
All tunable settings, timeouts, routing vectors, and anti-fingerprinting 
primitives for the Talent Intelligence pipeline.
"""

import os
import random

# ── Paths & Workspace Auto-Provisioning ───────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR  = os.path.join(BASE_DIR, "output")
LOG_DIR     = os.path.join(BASE_DIR, "logs")

EXCEL_FILE  = os.path.join(OUTPUT_DIR, "companies.xlsx")
JSON_FILE   = os.path.join(OUTPUT_DIR, "companies.json")

# Ensure required workspaces exist dynamically on package invocation
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# ── Browser Core Engine Performance Controls ──────────────────────────────────
HEADLESS        = True      # Set False to watch the browser execution live
PAGE_TIMEOUT    = 30_000    # ms – per-page Playwright timeout limit boundary
NAV_TIMEOUT     = 60_000    # ms – total navigation hook connection limit allowance
RETRY_DELAY_SEC = 4         # Seconds delay between individual recovery pass cycles
MAX_RETRIES     = 3

# ── Scraping Capacity Volumes ──────────────────────────────────────────────────
MAX_COMPANIES   = 100       # Cap boundary limit for ingestion processing passes
MIN_FUNDING_USD = 4_000_000 # Minimum funding filtering floor scale ($4M USD)

# ── Target Discovery Sources ──────────────────────────────────────────────────
YC_URL = (
    "https://www.ycombinator.com/companies"
    "?isHiring=true&sortBy=top&batch=&top_company=false"
)
WELLFOUND_URL = (
    "https://wellfound.com/companies"
    "?funding_min=4000000&hiring=true&sort=recently_funded"
)
CRUNCHBASE_URL = (
    "https://www.crunchbase.com/discover/organization.companies"
    "/64dc7b40ea72e2a01e8b73f4893c4e93"
)
DEALROOM_URL = (
    "https://app.dealroom.co/companies/filter/fundingRaised_min/4000000"
    "/hqLocations//tags//growthStage//teamSize//revenue//fundingYear/"
)

# ── Social Media Pattern Signature Rules ──────────────────────────────────────
SOCIAL_PATTERNS = {
    "linkedin_url":  ["linkedin.com/company/"],
    "twitter_url":   ["twitter.com/", "x.com/"],
    "facebook_url":  ["facebook.com/"],
    "instagram_url": ["instagram.com/"],
    "youtube_url":   ["youtube.com/"],
}

# ── Careers Page Routing Anchor Matches ───────────────────────────────────────
CAREERS_KEYWORDS = [
    "careers", "jobs", "hiring", "work-with-us", "work_with_us",
    "join-us", "join_us", "openings", "opportunities", "positions",
]

# ── Job Role Filtering Indices ────────────────────────────────────────────────
JOB_ROLE_KEYWORDS = [
    "software engineer", "data scientist", "product manager",
    "ml engineer", "machine learning", "frontend", "backend",
    "full stack", "fullstack", "devops", "designer", "analyst",
    "marketing", "sales", "recruiter", "qa engineer", "research scientist",
]

# ── Positive & Negative Semantic Signals ──────────────────────────────────────
HIRING_SIGNALS = [
    "open positions", "open roles", "join our team", "we're hiring",
    "we are hiring", "current openings", "apply now", "view openings",
    "explore careers", "job openings", "no positions",
]

# ── Anti-Fingerprint User-Agent Library ───────────────────────────────────────
USER_AGENTS = [
    (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
]

def get_random_user_agent() -> str:
    """Returns a completely random user-agent fingerprint string selection wrapper."""
    return random.choice(USER_AGENTS)