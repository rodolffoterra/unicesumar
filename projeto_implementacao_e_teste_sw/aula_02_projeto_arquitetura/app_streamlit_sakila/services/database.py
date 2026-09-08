import os
from contextlib import contextmanager
from typing import Dict, Iterator, Tuple

import mysql.connector
from dotenv import load_dotenv
from mysql.connector.connection import MySQLConnection

# Carrega as variáveis do arquivo .env, quando ele existir.
load_dotenv()


def get_config() -> Dict[str, object]:
    """Retorna a configuração de acesso ao banco Sakila.

    Os valores do arquivo .env têm prioridade. Quando o arquivo ainda não
    existe, são utilizados os dados locais informados para a aula.
    """
    return {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "1234556"),
        "database": os.getenv("MYSQL_DATABASE", "sakila"),
    }


@contextmanager
def get_connection() -> Iterator[MySQLConnection]:
    """Abre uma conexão MySQL e garante o fechamento ao final do uso."""
    connection = mysql.connector.connect(**get_config())
    try:
        yield connection
    finally:
        if connection.is_connected():
            connection.close()


def test_connection() -> Tuple[bool, str]:
    """Testa a conexão e retorna o resultado sem interromper o Streamlit."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE(), VERSION()")
            database, version = cursor.fetchone()
            cursor.close()

        return True, "Conectado com sucesso ao banco {} — MySQL {}".format(
            database, version
        )
    except mysql.connector.Error as exc:
        return False, "Erro de conexão MySQL: {}".format(exc)
