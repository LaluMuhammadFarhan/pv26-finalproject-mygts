"""
Utils: Photo Upload
Upload foto ke Supabase Storage.
"""
import os
from api.supabase_client import get_client

BUCKET = "rental-photos"


def upload_photo(file_path: str, destination_name: str) -> str:
    """Upload file lokal ke Supabase Storage. Return public URL."""
    client = get_client()
    with open(file_path, "rb") as f:
        client.storage.from_(BUCKET).upload(destination_name, f, {"content-type": "image/jpeg"})
    public_url = client.storage.from_(BUCKET).get_public_url(destination_name)
    return public_url
