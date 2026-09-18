import os
from pathlib import Path

from cryptography.fernet import Fernet
from dotenv import load_dotenv


# ==========================================================
# RAIZ DO PROJETO
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)


# ==========================================================
# DESCRIPTOGRAFIA
# ==========================================================

def descriptografar_senha(senha_criptografada: str) -> str:

    chave = os.getenv("DB_ENCRYPTION_KEY")

    if not chave:
        raise ValueError(
            f"DB_ENCRYPTION_KEY não encontrada.\n"
            f"Arquivo procurado: {ENV_FILE}"
        )

    fernet = Fernet(chave.encode())

    senha_descriptografada = fernet.decrypt(
        senha_criptografada.encode()
    )

    return senha_descriptografada.decode()