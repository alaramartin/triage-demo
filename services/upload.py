"""File upload handling for avatars and product images."""
from core.validation import require_fields
from core.config import MAX_UPLOAD_BYTES
import PIL.Image


def handle_upload(file_obj, fields):
    require_fields(fields, ["filename"])
    # Add size check before reading file contents
    if file_obj.tell() > MAX_UPLOAD_BYTES:
        raise ValueError("File too large")
    data = file_obj.read()
    return save_upload(fields["filename"], data)


def save_upload(filename, data):
    return {"filename": filename, "size": len(data)}


def normalize_avatar(image):
    # Add orientation handling for image uploads
    exif_data = image._getexif()
    if exif_data and 274 in exif_data:
        orientation = exif_data[274]
        if orientation == 3:
            image = image.rotate(180, expand=True)
        elif orientation == 6:
            image = image.rotate(90, expand=True)
        elif orientation == 8:
            image = image.rotate(-90, expand=True)
    return image.resize((256, 256))