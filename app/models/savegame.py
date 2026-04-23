from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class SaveGame:
    id: str        # nome da pasta (ex: "1", "autosave")
    name: str      # nome amigável do save
    path: str      # caminho completo
    updated_at: datetime

    @property
    def display_name(self) -> str:
        return f"{self.name} - {self.updated_at.strftime('%d/%m/%Y, %H:%M')}"


@dataclass
class Profile:
    id: str        # nome da pasta em Hex
    name: str      # nome decodificado
    path: str
    last_updated: datetime
