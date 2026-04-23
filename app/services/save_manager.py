import os
from datetime import datetime
from typing import List, Optional
from pathlib import Path
from app.models.savegame import Profile, SaveGame


class SaveManagerService:
    def __init__(self, base_path: Optional[str] = None):
        # Se não fornecido, tenta o caminho padrão do ETS2 no Windows
        if base_path:
            self.base_path = Path(base_path)
        else:
            self.base_path = Path(os.path.expanduser("~")) / "Documents" / "Euro Truck Simulator 2"

    def decode_profile_name(self, hex_name: str) -> str:
        """Decodifica o nome da pasta do perfil (Hex) para string."""
        try:
            return bytes.fromhex(hex_name).decode('utf-8', errors='ignore')
        except Exception:
            return hex_name

    def list_profiles(self) -> List[Profile]:
        """Lista todos os perfis encontrados na pasta profiles."""
        profiles_path = self.base_path / "profiles"
        if not profiles_path.exists():
            return []

        profiles = []
        for entry in os.scandir(profiles_path):
            if entry.is_dir():
                profile_name = self.decode_profile_name(entry.name)
                # No ETS2 real, o nome costuma vir acompanhado do ID Hex
                display_name = f"{profile_name} - {entry.name[:8]}..."
                
                stats = entry.stat()
                profiles.append(Profile(
                    id=entry.name,
                    name=display_name,
                    path=entry.path,
                    last_updated=datetime.fromtimestamp(stats.st_mtime)
                ))
        
        # Ordenar pelos mais recentes
        return sorted(profiles, key=lambda x: x.last_updated, reverse=True)

    def list_saves(self, profile_id: str) -> List[SaveGame]:
        """Lista os saves dentro de um perfil específico."""
        save_path = self.base_path / "profiles" / profile_id / "save"
        if not save_path.exists():
            return []

        saves = []
        for entry in os.scandir(save_path):
            if entry.is_dir():
                # Em um app real, leríamos info.sii aqui. 
                # Por simplicidade e robustez, usaremos o nome da pasta e data do arquivo.
                stats = entry.stat()
                save_name = self._get_save_friendly_name(entry.name)
                
                saves.append(SaveGame(
                    id=entry.name,
                    name=save_name,
                    path=entry.path,
                    updated_at=datetime.fromtimestamp(stats.st_mtime)
                ))
        
        return sorted(saves, key=lambda x: x.updated_at, reverse=True)

    def _get_save_friendly_name(self, folder_name: str) -> str:
        """Converte o nome da pasta em algo legível (Ex: autosave -> Auto Save)."""
        mapping = {
            "autosave": "Auto Save",
            "autosave_drive": "Auto Save (Drive)",
            "quicksave": "Quick Save"
        }
        return mapping.get(folder_name, f"Save {folder_name}")
