"""Basic logging setup. Decoy module — no real bug here."""
from core.config import LOG_LEVEL
import sys


def log(message, level="INFO"):
    print(f"[{level}] {message}", file=sys.stderr)


def configure():
    log(f"logging configured at level {LOG_LEVEL}")
