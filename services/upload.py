"""File upload handling for avatars and product images."""
from core.validation import require_fields
from core.config import MAX_UPLOAD_BYTES


def handle_upload(file_obj, fields):
    require_fields(fields, ["filename"])
    # BUG: reads the entire file into memory with no size cap enforced before the read,
    # so a large file hangs/OOMs the request instead of being rejected up front.
    data = file_obj.read()
    return save_upload(fields["filename"], data)


def save_upload(filename, data):
    return {"filename": filename, "size": len(data)}


def normalize_avatar(image):
    # BUG: crops/resizes using the raw pixel buffer only — never reads EXIF orientation,
    # so photos taken on phones held sideways come out rotated 90 degrees.
    return image.resize((256, 256))
