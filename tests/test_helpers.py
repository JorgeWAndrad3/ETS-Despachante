import pytest
from app.utils.helpers import generate_unique_job_code


def test_generate_unique_job_code_length():
    code = generate_unique_job_code(8)
    assert len(code) == 8


def test_generate_unique_job_code_only_letters():
    code = generate_unique_job_code(100)
    assert code.isalpha()
    assert code.isupper()


def test_generate_unique_job_code_randomness():
    code1 = generate_unique_job_code(8)
    code2 = generate_unique_job_code(8)
    assert code1 != code2
