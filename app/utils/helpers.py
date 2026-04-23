import random
import string


def generate_unique_job_code(length: int = 8) -> str:
    """Gera um código aleatório de letras para identificar a carga."""
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for _ in range(length))
