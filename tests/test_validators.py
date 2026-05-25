"""
Test: Validators
Jalankan: python -m pytest tests/
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from utils.validators import (
    is_empty, is_valid_email, is_valid_date,
    is_positive_int, validate_rental_dates
)


def test_is_empty():
    assert is_empty("") is True
    assert is_empty("  ") is True
    assert is_empty("hello") is False


def test_is_valid_email():
    assert is_valid_email("user@example.com") is True
    assert is_valid_email("invalid-email") is False


def test_is_valid_date():
    assert is_valid_date("2025-01-15") is True
    assert is_valid_date("2025-13-01") is False


def test_is_positive_int():
    assert is_positive_int("5") is True
    assert is_positive_int("0") is False
    assert is_positive_int("abc") is False


def test_validate_rental_dates():
    ok, msg = validate_rental_dates("2025-06-01", "2025-06-05")
    assert ok is True

    ok, msg = validate_rental_dates("2025-06-05", "2025-06-01")
    assert ok is False
    assert msg != ""
