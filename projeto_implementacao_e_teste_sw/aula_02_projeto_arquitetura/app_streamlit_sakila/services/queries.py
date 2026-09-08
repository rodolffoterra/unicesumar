from typing import Dict, Optional, Tuple, Union

import pandas as pd
from mysql.connector import Error

from services.database import get_connection

SQLParams = Optional[Union[Tuple[object, ...], Dict[str, object]]]


def read_sql(query: str, params: SQLParams = None) -> pd.DataFrame:
    """Executa uma consulta SELECT e devolve o resultado em DataFrame."""
    with get_connection() as connection:
        return pd.read_sql(query, connection, params=params)


def execute_sql(query: str, params: SQLParams = None) -> int:
    """Executa INSERT, UPDATE ou DELETE e retorna as linhas afetadas."""
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            affected_rows = cursor.rowcount
            cursor.close()
            return affected_rows
    except Error:
        raise
