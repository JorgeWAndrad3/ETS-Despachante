import pytest
from unittest.mock import patch, MagicMock
from app.services.save_manager import SaveManagerService


def test_decode_profile_name():
    service = SaveManagerService(base_path="/tmp")
    # "4a6f726765" é "Jorge" em Hex
    decoded = service.decode_profile_name("4a6f726765")
    assert decoded == "Jorge"


def test_decode_invalid_hex():
    service = SaveManagerService(base_path="/tmp")
    # Caso de erro: deve retornar o próprio ID se falhar
    decoded = service.decode_profile_name("invalid_hex")
    assert decoded == "invalid_hex"


@patch("os.scandir")
@patch("pathlib.Path.exists")
def test_list_profiles(mock_exists, mock_scandir):
    mock_exists.return_value = True
    
    # Mock de uma entrada de diretório
    mock_entry = MagicMock()
    mock_entry.is_dir.return_value = True
    mock_entry.name = "4a6f726765"
    mock_entry.path = "/fake/path/4a6f726765"
    mock_entry.stat.return_value.st_mtime = 1712595240 # 08/04/2024
    
    mock_scandir.return_value = [mock_entry]
    
    service = SaveManagerService(base_path="/fake")
    profiles = service.list_profiles()
    
    assert len(profiles) == 1
    assert "Jorge" in profiles[0].name
    assert profiles[0].id == "4a6f726765"


def test_get_save_friendly_name():
    service = SaveManagerService(base_path="/tmp")
    assert service._get_save_friendly_name("autosave") == "Auto Save"
    assert service._get_save_friendly_name("1") == "Save 1"
