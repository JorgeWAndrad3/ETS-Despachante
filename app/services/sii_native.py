import zlib
import os
import ctypes
from typing import List

class SiiNativeService:
    # Chaves conhecidas para formatos ScsC (SCS Software)
    SCS_KEY_256 = bytes([
        0x2A, 0x5F, 0xCB, 0x17, 0x91, 0xD2, 0x2F, 0xB6, 
        0x02, 0x45, 0xB3, 0xD8, 0x36, 0x9E, 0xD0, 0xB2, 
        0xC2, 0x73, 0x71, 0x56, 0x3F, 0xBF, 0x1F, 0x3C, 
        0x9E, 0xDF, 0x6B, 0x11, 0x82, 0x5A, 0x5D, 0x0A
    ])

    def decrypt_save(self, file_path: str) -> str:
        """Lê e descriptografa o arquivo game.sii."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        with open(file_path, "rb") as f:
            data = f.read()

        if not data:
            raise ValueError("Arquivo vazio.")

        # Verifica Assinatura
        signature = data[:4]
        
        if signature == b"SiiN":
            return data
        
        if signature == b"ScsC":
            return self._decrypt_scsc(data)
            
        raise ValueError(f"Formato de save desconhecido: {signature}")

    def _decrypt_scsc(self, data: bytes) -> str:
        """Descriptografa o formato ScsC v3 usando AES-256-CBC."""
        try:
            from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
            from cryptography.hazmat.backends import default_backend
            
            # DIAGNÓSTICO: Mostra o cabeçalho no terminal
            print(f"DEBUG HEX HEADER: {data[:64].hex(' ')}")

            # 1. Extração de Componentes
            iv = data[36:52]
            payload = data[56:]
            print(f"DEBUG: IV extraído ({len(iv)} bytes)")
            
            # Alinhamento
            valid_len = (len(payload) // 16) * 16
            payload_aligned = payload[:valid_len]
            print(f"DEBUG: Payload alinhado ({valid_len} bytes)")
            
            # 2. Decriptação AES-256-CBC
            print("DEBUG: Iniciando decriptação AES...")
            cipher = Cipher(algorithms.AES(self.SCS_KEY_256), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted = decryptor.update(payload_aligned) + decryptor.finalize()
            print(f"DEBUG: Decriptação concluída ({len(decrypted)} bytes)")
            
            # 3. Localização Zlib
            print("DEBUG: Procurando assinatura Zlib...")
            for header in [b"\x78\x9c", b"\x78\x01", b"\x78\xda"]:
                idx = decrypted.find(header, 0, 1024)
                if idx != -1:
                    print(f"DEBUG: Assinatura {header.hex().upper()} encontrada no offset {idx}")
                    try:
                        result = zlib.decompress(decrypted[idx:])
                        print("DEBUG: Descompactação Zlib OK!")
                        return result # Retorna bytes
                    except Exception as ze:
                        print(f"DEBUG: Falha Zlib: {str(ze)}")
                        continue
            
            # 4. Fallback
            print("DEBUG: Tentando fallback Raw Deflate...")
            try:
                result = zlib.decompress(decrypted, -zlib.MAX_WBITS)
                print("DEBUG: Fallback Raw OK!")
                return result # Retorna bytes
            except Exception as re:
                print(f"DEBUG: Fallback Raw Falhou: {str(re)}")

            raise Exception("Chave padrão falhou. Possível Steam Cloud.")

        except ImportError:
            raise Exception("Instale: pip install cryptography")
        except Exception as e:
            raise Exception(f"Erro ScsC: {str(e)}")

    def extract_cities(self, content_bytes: bytes, known_city_ids: list = None) -> set:
        """Extrai as cidades usando um scanner de strings universal nos bytes."""
        import re
        cities = set()
        
        print(f"DEBUG: Iniciando varredura universal de strings no binário...")
        
        # 1. Scanner de Strings: Pega qualquer sequência de letras minúsculas e underscores (3 a 30 caracteres)
        # Isso é o formato padrão dos IDs internos da SCS.
        string_pattern = re.compile(b'[a-z_0-9]{3,30}')
        found_strings = string_pattern.findall(content_bytes)
        
        # Convertemos para set de strings para busca rápida
        all_strings_in_save = {s.decode("utf-8", errors="ignore") for s in found_strings}
        
        if known_city_ids:
            print(f"DEBUG: Cruzando dados com {len(known_city_ids)} cidades do banco de dados...")
            for city_id in known_city_ids:
                # Remove o prefixo 'city.' se existir para a busca
                clean_id = city_id.replace("city.", "")
                if clean_id in all_strings_in_save:
                    cities.add(city_id)
        
        if cities:
            print(f"DEBUG: Cidades encontradas: {list(cities)}")
            
        print(f"DEBUG: {len(cities)} cidades validadas e encontradas.")
        return cities
