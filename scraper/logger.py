"""
scraper/logger.py
Centralised logging – writes to stdout AND a timestamped log file.
"""

import logging
import os
import sys
from datetime import datetime

from config.config import LOG_DIR

os.makedirs(LOG_DIR, exist_ok=True)

_LOG_FILE = os.path.join(
    LOG_DIR, f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)-30s  %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(_LOG_FILE, encoding="utf-8"),
    ],
)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)