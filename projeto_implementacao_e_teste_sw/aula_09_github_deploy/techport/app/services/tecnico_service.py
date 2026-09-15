from app.repositories.tecnico_repository import (
    listar_tecnicos,
    buscar_tecnico_por_id,
    criar_tecnico,
    atualizar_tecnico,
    excluir_tecnico
)


# ==========================================================
# GET - LISTAR TÉCNICOS
# ==========================================================

def obter_tecnicos():
    """
    Retorna todos os técnicos cadastrados.
    """

    return listar_tecnicos()


# ==========================================================
# GET - BUSCAR TÉCNICO POR ID
# ==========================================================

def obter_tecnico_por_id(
    tecnico_id: int
):
    """
    Retorna um técnico específico pelo ID.
    """

    return buscar_tecnico_por_id(
        tecnico_id
    )


# ==========================================================
# POST - CADASTRAR TÉCNICO
# ==========================================================

def cadastrar_tecnico(
    tecnico
):
    """
    Cadastra um novo técnico.
    """

    return criar_tecnico(
        tecnico
    )


# ==========================================================
# PUT - ATUALIZAR TÉCNICO
# ==========================================================

def alterar_tecnico(
    tecnico_id: int,
    tecnico
):
    """
    Atualiza os dados de um técnico existente.
    """

    return atualizar_tecnico(
        tecnico_id,
        tecnico
    )


# ==========================================================
# DELETE - EXCLUIR TÉCNICO
# ==========================================================

def remover_tecnico(
    tecnico_id: int
):
    """
    Exclui um técnico pelo ID.
    """

    return excluir_tecnico(
        tecnico_id
    )