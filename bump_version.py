import subprocess
import os

def bump():
    # 1. Lê a versão atual
    with open("version.txt", "r") as f:
        v = f.read().strip().split('.')
    
    # 2. Incrementa o último dígito (0.0.1 -> 0.0.2)
    new_v = f"{v[0]}.{v[1]}.{int(v[2]) + 1}"
    
    # 3. Salva a nova versão
    with open("version.txt", "w") as f:
        f.write(new_v)
    
    # 4. Git Comands
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"release: version {new_v}"], check=True)
        subprocess.run(["git", "push", "origin", "master"], check=True)
        
        # 5. GitHub Release (Tag)
        subprocess.run(["gh", "release", "create", f"v{new_v}", "--title", f"Release v{new_v}", "--notes", "Nova versão automática do ETS Despachante."], check=True)
        
        print(f"✅ Versão {new_v} lançada com sucesso no GitHub!")
    except Exception as e:
        print(f"❌ Erro ao lançar versão: {e}")

if __name__ == "__main__":
    bump()
