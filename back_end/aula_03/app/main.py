from typing import List

from fastapi import FastAPI, HTTPException, status
from mysql.connector import Error

from app.database import obter_conexao
from app.schemas import AtorEntrada, AtorResposta


app = FastAPI(
    title="API Sakila - Atores",
    description="CRUD da tabela actor do banco Sakila.",
    version="1.0.0",
)


# =========================================================
# INÍCIO
# =========================================================

@app.get("/")
def inicio():
    return {
        "mensagem": "API Sakila em funcionamento",
        "swagger": "/docs",
    }


# =========================================================
# TESTAR CONEXÃO
# =========================================================

@app.get("/health")
def verificar_conexao():
    try:
        with obter_conexao() as conexao:
            cursor = conexao.cursor()

            cursor.execute("SELECT DATABASE()")
            banco = cursor.fetchone()[0]

            cursor.close()

        return {
            "status": "ok",
            "banco": banco,
        }

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro de conexão com o MySQL: {erro}",
        )


# =========================================================
# GET - LISTAR TODOS OS ATORES
# =========================================================

@app.get(
    "/atores",
    response_model=List[AtorResposta],
)
def listar_atores():
    try:
        with obter_conexao() as conexao:
            cursor = conexao.cursor(dictionary=True)

            cursor.execute(
                """
                SELECT
                    actor_id,
                    first_name,
                    last_name,
                    last_update
                FROM actor
                ORDER BY actor_id
                """
            )

            atores = cursor.fetchall()
            cursor.close()

            return atores

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar atores: {erro}",
        )


# =========================================================
# GET - CONSULTAR ATOR POR ID
# =========================================================

@app.get(
    "/atores/{actor_id}",
    response_model=AtorResposta,
)
def buscar_ator(actor_id: int):
    try:
        with obter_conexao() as conexao:
            cursor = conexao.cursor(dictionary=True)

            cursor.execute(
                """
                SELECT
                    actor_id,
                    first_name,
                    last_name,
                    last_update
                FROM actor
                WHERE actor_id = %s
                """,
                (actor_id,),
            )

            ator = cursor.fetchone()
            cursor.close()

            if ator is None:
                raise HTTPException(
                    status_code=404,
                    detail="Ator não encontrado.",
                )

            return ator

    except HTTPException:
        raise

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao buscar ator: {erro}",
        )


# =========================================================
# POST - CADASTRAR ATOR
# =========================================================

@app.post(
    "/atores",
    response_model=AtorResposta,
    status_code=status.HTTP_201_CREATED,
)
def cadastrar_ator(ator: AtorEntrada):
    try:
        with obter_conexao() as conexao:
            cursor = conexao.cursor(dictionary=True)

            primeiro_nome = ator.first_name.strip().upper()
            sobrenome = ator.last_name.strip().upper()

            cursor.execute(
                """
                INSERT INTO actor (
                    first_name,
                    last_name
                )
                VALUES (%s, %s)
                """,
                (
                    primeiro_nome,
                    sobrenome,
                ),
            )

            actor_id = cursor.lastrowid

            conexao.commit()

            cursor.execute(
                """
                SELECT
                    actor_id,
                    first_name,
                    last_name,
                    last_update
                FROM actor
                WHERE actor_id = %s
                """,
                (actor_id,),
            )

            novo_ator = cursor.fetchone()
            cursor.close()

            return novo_ator

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao cadastrar ator: {erro}",
        )


# =========================================================
# PUT - ATUALIZAR ATOR
# =========================================================

@app.put(
    "/atores/{actor_id}",
    response_model=AtorResposta,
)
def atualizar_ator(
    actor_id: int,
    ator: AtorEntrada,
):
    try:
        with obter_conexao() as conexao:
            cursor = conexao.cursor(dictionary=True)

            cursor.execute(
                """
                SELECT actor_id
                FROM actor
                WHERE actor_id = %s
                """,
                (actor_id,),
            )

            ator_existente = cursor.fetchone()

            if ator_existente is None:
                cursor.close()

                raise HTTPException(
                    status_code=404,
                    detail="Ator não encontrado.",
                )

            primeiro_nome = ator.first_name.strip().upper()
            sobrenome = ator.last_name.strip().upper()

            cursor.execute(
                """
                UPDATE actor
                SET
                    first_name = %s,
                    last_name = %s
                WHERE actor_id = %s
                """,
                (
                    primeiro_nome,
                    sobrenome,
                    actor_id,
                ),
            )

            conexao.commit()

            cursor.execute(
                """
                SELECT
                    actor_id,
                    first_name,
                    last_name,
                    last_update
                FROM actor
                WHERE actor_id = %s
                """,
                (actor_id,),
            )

            ator_atualizado = cursor.fetchone()
            cursor.close()

            return ator_atualizado

    except HTTPException:
        raise

    except Exception as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao atualizar ator: {erro}",
        )


# =========================================================
# DELETE - EXCLUIR ATOR
# =========================================================

@app.delete("/atores/{actor_id}")
def excluir_ator(actor_id: int):
    try:
        with obter_conexao() as conexao:
            cursor = conexao.cursor(dictionary=True)

            # Verifica se o ator existe
            cursor.execute(
                """
                SELECT
                    actor_id,
                    first_name,
                    last_name
                FROM actor
                WHERE actor_id = %s
                """,
                (actor_id,),
            )

            ator = cursor.fetchone()

            if ator is None:
                cursor.close()

                raise HTTPException(
                    status_code=404,
                    detail="Ator não encontrado.",
                )

            # Exclui diretamente da tabela actor
            cursor.execute(
                """
                DELETE FROM actor
                WHERE actor_id = %s
                """,
                (actor_id,),
            )

            conexao.commit()
            cursor.close()

            return {
                "mensagem": "Ator excluído com sucesso.",
                "actor_id": actor_id,
                "nome": (
                    f'{ator["first_name"]} '
                    f'{ator["last_name"]}'
                ),
            }

    except HTTPException:
        raise

    except Error as erro:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao excluir ator: {erro}",
        )