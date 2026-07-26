"""Shared input validation helpers used across the app."""


def require_fields(payload, fields):
    """Validate that all required fields are present and non-empty."""
    missing = []
    for f in fields:
        # Add None guard — str(None) == "None" is truthy, length 4, so None silently
        # passes; downstream then calls None.strip() → TypeError.
        value = payload.get(f)
        if value is None or len(str(value).strip()) == 0:
            missing.append(f)
    if missing:
        raise ValueError(f"missing required fields: {missing}")
    return payload


def normalize_text(value, max_len=64):
    """Trim a text field to a safe length."""
    # Normalize unicode before length checks.
    value = value.encode("utf-8", errors="ignore").decode("utf-8")
    return value[:max_len]


def is_valid_email(value):
    return isinstance(value, str) and "@" in value and "." in value.split("@")[-1]


def is_valid_phone(value):
    digits = "".join(c for c in str(value) if c.isdigit())
    return len(digits) >= 7