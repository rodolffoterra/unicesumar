from app.repositories.chamado_repository import (
    listar_chamados,
    buscar_chamado_por_id,
    criar_chamado,
    atualizar_chamado,
    excluir_chamado
)


# ==========================================================
# GET - LISTAR CHAMADOS
# ==========================================================

def obter_chamados():
    """
    Retorna todos os chamados cadastrados.
    """

    return listar_chamados()


# ==========================================================
# GET - BUSCAR CHAMADO POR ID
# ==========================================================

def obter_chamado_por_id(
    chamado_id: int
):
    """
    Retorna um chamado específico pelo ID.
    """

    return buscar_chamado_por_id(
        chamado_id
    )


# ==========================================================
# POST - CADASTRAR CHAMADO
# ==========================================================

def cadastrar_chamado(
    chamado
):
    """
    Cadastra um novo chamado.
    """

    return criar_chamado(
        chamado
    )


# ==========================================================
# PUT - ATUALIZAR CHAMADO
# ==========================================================

def alterar_chamado(
    chamado_id: int,
    chamado
):
    """
    Atualiza os dados de um chamado.
    """

    return atualizar_chamado(
        chamado_id,
        chamado
    )


# ==========================================================
# DELETE - EXCLUIR CHAMADO
# ==========================================================

def remover_chamado(
    chamado_id: int
):
    """
    Exclui um chamado pelo ID.
    """

    return excluir_chamado(
        chamado_id
    )