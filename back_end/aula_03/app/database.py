import os
from contextlib import contextmanager
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv


# Pasta raiz do projeto:
# aula_03/
# ├── .env
# └── app/
#     └── database.py
PASTA_RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_ENV = PASTA_RAIZ / ".env"

load_dotenv(
    dotenv_path=ARQUIVO_ENV,
    override=True,
)


def criar_conexao():
    """Cria uma conexão com o banco MySQL definido no .env."""

    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "sakila"),
    )


@contextmanager
def obter_conexao():
    """Abre, disponibiliza e fecha a conexão automaticamente."""

    conexao = None

    try:
        conexao = criar_conexao()

        if not conexao.is_connected():
            raise ConnectionError(
                "Não foi possível estabelecer conexão com o MySQL."
            )

        yield conexao

    except Exception:
        if conexao and conexao.is_connected():
            conexao.rollback()

        raise

    finally:
        if conexao and conexao.is_connected():
            conexao.close()