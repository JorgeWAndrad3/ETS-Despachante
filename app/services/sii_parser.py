import subprocess
import os
import shutil
from pathlib import Path
from typing import List, Set


import shutil

class SiiParserService:
    def __init__(self, decryptor_path: str = "sii_decrypt.exe"):
        self._decryptor_path = Path(decryptor_path).absolute()
        self.auto_find_decryptor()

    @property
    def decryptor_path(self) -> Path:
        return self._decryptor_path

    @decryptor_path.setter
    def decryptor_path(self, value: Path):
        self._decryptor_path = value

    def is_decryptor_available(self) -> bool:
        """Verifica se o executável do decriptador existe."""
        return self._decryptor_path.exists()

    def auto_find_decryptor(self) -> None:
        """Busca profunda por um decriptador funcional."""
        # 1. Caminhos óbvios
        paths_to_check = [
            Path.cwd() / "sii_decrypt.exe",
            Path(os.path.expanduser("~")) / "Downloads" / "sii_decrypt.exe",
            Path(os.path.expanduser("~")) / "Documents" / "sii_decrypt.exe",
        ]
        
        for p in paths_to_check:
            if p.exists():
                self._decryptor_path = p.absolute()
                print(f"DEBUG: Encontrado decriptador em: {p}")
                return

        # 2. Busca no PATH
        path_in_env = shutil.which("sii_decrypt.exe")
        if path_in_env:
            self._decryptor_path = Path(path_in_env)
            return

        # 3. Busca recursiva no diretório do projeto
        for p in Path.cwd().rglob("sii_decrypt.exe"):
            self._decryptor_path = p.absolute()
            return

    def decrypt_file(self, input_path: Path) -> Path:
        """Cria uma cópia descriptografada do arquivo SII usando sandbox local."""
        if not self.is_decryptor_available():
            raise FileNotFoundError(f"Decriptador não encontrado em: {self.decryptor_path}")

        # Pasta do decriptador
        exe_dir = self._decryptor_path.parent
        # Algumas versões LEGACY só funcionam se o nome for game.sii ou info.sii
        local_temp_file = exe_dir / input_path.name 
        
        try:
            print(f"DEBUG: Copiando para a pasta do EXE com nome original: {local_temp_file.name}")
            if local_temp_file.exists():
                os.remove(local_temp_file)
            shutil.copy2(input_path, local_temp_file)
            os.chmod(local_temp_file, 0o777)
            
            exe_path = str(self._decryptor_path.absolute())
            exe_name = self._decryptor_path.name
            target_path = str(local_temp_file.absolute())

            print(f"DEBUG: Chamada direta: {exe_path} {target_path}")
            
            # Tenta chamada direta sem Shell (mais estável para alguns EXEs 32-bit)
            result = subprocess.run(
                [exe_path, target_path],
                capture_output=True,
                text=True,
                timeout=20,
                cwd=str(exe_dir),
                shell=False,
                stdin=subprocess.DEVNULL
            )
            
            print(f"DEBUG: Retorno: {result.returncode}")
            
            # Se falhar sem shell, tenta com shell em string única (último recurso)
            if "SiiNunit" not in open(local_temp_file, "r", encoding="utf-8", errors="ignore").read(8):
                print("DEBUG: Falhou sem shell, tentando com shell...")
                subprocess.run(f'"{exe_name}" "{local_temp_file.name}"', shell=True, cwd=str(exe_dir), timeout=10)

            # Verifica o Header final
            with open(local_temp_file, "r", encoding="utf-8", errors="ignore") as f:
                header = f.read(8)
                print(f"DEBUG: Header final: {header}")
                if "SiiNunit" not in header:
                    raise Exception(f"Decriptador incompatível com este save. Header: {header}")

            return local_temp_file
            
        except Exception as e:
            print(f"DEBUG ERROR: {str(e)}")
            if local_temp_file.exists():
                os.remove(local_temp_file)
            raise Exception(f"Falha na Sandbox de decriptação: {str(e)}")

    def extract_discovered_cities(self, decrypted_file: Path) -> Set[str]:
        """Extrai a lista de cidades descobertas do arquivo game.sii."""
        cities = set()
        if not decrypted_file.exists():
            return cities

        try:
            with open(decrypted_file, "r", encoding="utf-8", errors="ignore") as f:
                # Debug: Mostra as primeiras 5 linhas no terminal para confirmar decriptação
                print("DEBUG: Primeiras 5 linhas do arquivo descriptografado:")
                for i in range(5):
                    line = f.readline()
                    if not line: break
                    print(f"  > {line.strip()}")
                
                f.seek(0) # Volta pro início para ler tudo
                for line in f:
                    if "visited_cities[" in line:
                        parts = line.split(":")
                        if len(parts) > 1:
                            # Remove "city.", aspas e espaços
                            raw_name = parts[1].strip().strip('"')
                            clean_name = raw_name.replace("city.", "")
                            if clean_name:
                                cities.add(clean_name)
        except Exception as e:
            print(f"DEBUG ERROR na leitura: {str(e)}")
        
        return cities

    def cleanup(self, file_path: Path):
        """Remove o arquivo temporário."""
        if file_path.exists() and file_path.suffix == ".txt":
            os.remove(file_path)
