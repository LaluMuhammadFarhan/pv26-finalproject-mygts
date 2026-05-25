"""
Utils: Validators
Validasi input form yang dipakai di seluruh controller.
"""
import re
from datetime import datetime


def is_empty(value: str) -> bool:
    return not value or not value.strip()


def is_valid_email(email: str) -> bool:
    return bool(re.match(r"^[\w.-]+@[\w.-]+\.\w{2,}$", email))


def is_valid_date(date_str: str, fmt: str = "%Y-%m-%d") -> bool:
    try:
        datetime.strptime(date_str, fmt)
        return True
    except ValueError:
        return False


def is_positive_int(value: str) -> bool:
    try:
        return int(value) > 0
    except ValueError:
        return False


def validate_rental_dates(start: str, end: str) -> tuple[bool, str]:
    if not is_valid_date(start) or not is_valid_date(end):
        return False, "Format tanggal tidak valid (YYYY-MM-DD)."
    if datetime.strptime(start, "%Y-%m-%d") >= datetime.strptime(end, "%Y-%m-%d"):
        return False, "Tanggal mulai harus sebelum tanggal selesai."
    return True, ""
