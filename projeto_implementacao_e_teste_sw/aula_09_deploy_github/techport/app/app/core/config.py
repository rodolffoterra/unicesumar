import os
from pathlib import Path

from dotenv import load_dotenv


# ==========================================================
# LOCALIZAR A RAIZ DO PROJETO
# ==========================================================

BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
)


# ==========================================================
# LOCALIZAR O .env
# ==========================================================

ENV_FILE = BASE_DIR / ".env"


# ==========================================================
# CARREGAR .env
# ==========================================================

load_dotenv(
    dotenv_path=ENV_FILE
)


# ==========================================================
# CONFIGURAÇÕES MYSQL
# ==========================================================

DB_HOST = os.getenv(
    "DB_HOST"
)

DB_PORT = int(
    os.getenv(
        "DB_PORT",
        "3306"
    )
)

DB_DATABASE = os.getenv(
    "DB_DATABASE"
)

DB_USER = os.getenv(
    "DB_USER"
)

DB_PASSWORD = os.getenv(
    "DB_PASSWORD"
)

DB_ENCRYPTION_KEY = os.getenv(
    "DB_ENCRYPTION_KEY"
)