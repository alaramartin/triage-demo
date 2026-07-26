"""Static app configuration. No external dependencies."""

APP_NAME = "shipyard"
DEBUG = False
MAX_UPLOAD_BYTES = 25 * 1024 * 1024
DEFAULT_CURRENCY = "USD"
LOG_LEVEL = "INFO"
FEATURE_FLAGS = {
    "dark_mode": False,
    "new_checkout": True,
}


def get_flag(name, default=False):
    return FEATURE_FLAGS.get(name, default)
