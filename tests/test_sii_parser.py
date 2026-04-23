import pytest
from pathlib import Path
from app.services.sii_parser import SiiParserService


@pytest.fixture
def fake_sii_content(tmp_path):
    d = tmp_path / "info.sii.txt"
    content = """
    SiiNunit
    {
    save_info : _nameless.215.4f3e.7e20 {
     visited_cities: 2
     visited_cities[0]: berlin
     visited_cities[1]: paris
    }
    }
    """
    d.write_text(content)
    return d


def test_extract_discovered_cities(fake_sii_content):
    service = SiiParserService()
    cities = service.extract_discovered_cities(fake_sii_content)
    
    assert len(cities) == 2
    assert "berlin" in cities
    assert "paris" in cities


def test_decryptor_availability():
    service = SiiParserService(decryptor_path="non_existent.exe")
    assert service.is_decryptor_available() is False
