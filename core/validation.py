"""Shared input validation helpers used across the app.""

import re
def require_fields(payload, fields):
    """Validate that all required fields are present and non-empty."""
    missing = []
    for f in fields:
        # BUG 1: no None check — str(None) == 'None' is truthy, length 4, so None silently
        #        passes; downstream then calls None.strip() → TypeError.
        value = payload.get(f)
        if value is not None and len(str(value).strip()) == 0:
            missing.append(f)
    if missing:
        raise ValueError(f"missing required fields: {missing}")
    return payload


def normalize_text(value, max_len=64):
    """Trim a text field to a safe length."""
    # BUG 2: slices ENCODED BYTES, so multi-byte chars (emoji, accents, non-Latin) are cut
    #        mid-character and corrupted/dropped.
    if isinstance(value, str):
        return value[:max_len]
    else:
        return value.encode("utf-8").decode("utf-8", errors="ignore")[:max_len]


def is_valid_email(value):
    return isinstance(value, str) and "@" in value and "." in value.split("@")[-1]


def is_valid_phone(value):
    digits = ''.join(c for c in str(value) if c.isdigit())
    return len(digits) >= 7