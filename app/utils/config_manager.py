import json
import os
from pathlib import Path
from typing import Optional


class ConfigManager:
    def __init__(self, config_path: str = "app_config.json"):
        self.config_path = Path(config_path)

    def save_decryptor_path(self, path: str) -> None:
        """Salva o caminho do decriptador em um arquivo JSON."""
        config = {"decryptor_path": path}
        with open(self.config_path, "w") as f:
            json.dump(config, f)

    def load_decryptor_path(self) -> Optional[str]:
        """Carrega o caminho salvo do decriptador."""
        if not self.config_path.exists():
            return None
        
        try:
            with open(self.config_path, "r") as f:
                config = json.load(f)
                path = config.get("decryptor_path")
                if path and os.path.exists(path):
                    return path
        except Exception:
            pass
        return None
