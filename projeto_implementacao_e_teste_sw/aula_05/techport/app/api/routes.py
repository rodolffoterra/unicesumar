from typing import List

from fastapi import APIRouter, HTTPException


# ==========================================================
# SCHEMAS - USUÁRIOS
# ==========================================================

from app.schemas.usuario import (
    UsuarioCriar,
    UsuarioAtualizar,
    UsuarioResposta
)


# ==========================================================
# SCHEMAS - TÉCNICOS
# ==========================================================

from app.schemas.tecnico import (
    TecnicoCriar,
    TecnicoAtualizar,
    TecnicoResposta
)


# ==========================================================
# SCHEMAS - CHAMADOS
# ==========================================================

from app.schemas.chamado import (
    ChamadoCriar,
    ChamadoAtualizar,
    ChamadoResposta
)


# ==========================================================
# SERVICES - USUÁRIOS
# ==========================================================

from app.services.usuario_service import (
    obter_usuarios,
    obter_usuario,
    cadastrar_usuario,
    alterar_usuario,
    remover_usuario
)


# ==========================================================
# SERVICES - TÉCNICOS
# ==========================================================

from app.services.tecnico_service import (
    obter_tecnicos,
    obter_tecnico_por_id,
    cadastrar_tecnico,
    alterar_tecnico,
    remover_tecnico
)


# ==========================================================
# SERVICES - CHAMADOS
# ==========================================================

from app.services.chamado_service import (
    obter_chamados,
    obter_chamado_por_id,
    cadastrar_chamado,
    alterar_chamado,
    remover_chamado
)


# ==========================================================
# CRIAÇÃO DO ROUTER
# ==========================================================

router = APIRouter()


# ==========================================================
# USUÁRIOS
# ==========================================================


# ----------------------------------------------------------
# GET - LISTAR TODOS OS USUÁRIOS
# ----------------------------------------------------------

@router.get(
    "/usuarios",
    response_model=List[UsuarioResposta],
    tags=["Usuários"]
)
def get_usuarios():

    return obter_usuarios()


# ----------------------------------------------------------
# GET - BUSCAR USUÁRIO POR ID
# ----------------------------------------------------------

@router.get(
    "/usuarios/{usuario_id}",
    response_model=UsuarioResposta,
    tags=["Usuários"]
)
def get_usuario(
    usuario_id: int
):

    usuario = obter_usuario(
        usuario_id
    )

    if usuario is None:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    return usuario


# ----------------------------------------------------------
# POST - CADASTRAR USUÁRIO
# ----------------------------------------------------------

@router.post(
    "/usuarios",
    status_code=201,
    tags=["Usuários"]
)
def post_usuario(
    usuario: UsuarioCriar
):

    usuario_id = cadastrar_usuario(
        usuario
    )

    return {
        "mensagem": "Usuário cadastrado com sucesso.",
        "id": usuario_id
    }


# ----------------------------------------------------------
# PUT - ATUALIZAR USUÁRIO
# ----------------------------------------------------------

@router.put(
    "/usuarios/{usuario_id}",
    tags=["Usuários"]
)
def put_usuario(
    usuario_id: int,
    usuario: UsuarioAtualizar
):

    resultado = alterar_usuario(
        usuario_id,
        usuario
    )

    if resultado == 0:

        # Antes de dizer que não existe,
        # pode ser interessante verificar
        # se nenhum campo foi efetivamente alterado.
        #
        # Para nossa aula, manteremos a resposta simples.

        raise HTTPException(
            status_code=404,
            detail=(
                "Usuário não encontrado "
                "ou nenhum dado foi alterado."
            )
        )

    return {
        "mensagem": "Usuário atualizado com sucesso."
    }


# ----------------------------------------------------------
# DELETE - EXCLUIR USUÁRIO
# ----------------------------------------------------------

@router.delete(
    "/usuarios/{usuario_id}",
    tags=["Usuários"]
)
def delete_usuario(
    usuario_id: int
):

    try:

        resultado = remover_usuario(
            usuario_id
        )

    except Exception:

        raise HTTPException(
            status_code=409,
            detail=(
                "Não foi possível excluir o usuário. "
                "Ele pode possuir registros relacionados."
            )
        )

    if resultado == 0:

        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )

    return {
        "mensagem": "Usuário excluído com sucesso."
    }


# ==========================================================
# TÉCNICOS
# ==========================================================


# ----------------------------------------------------------
# GET - LISTAR TODOS OS TÉCNICOS
# ----------------------------------------------------------

@router.get(
    "/tecnicos",
    response_model=List[TecnicoResposta],
    tags=["Técnicos"]
)
def get_tecnicos():

    return obter_tecnicos()


# ----------------------------------------------------------
# GET - BUSCAR TÉCNICO POR ID
# ----------------------------------------------------------

@router.get(
    "/tecnicos/{tecnico_id}",
    response_model=TecnicoResposta,
    tags=["Técnicos"]
)
def get_tecnico(
    tecnico_id: int
):

    tecnico = obter_tecnico_por_id(
        tecnico_id
    )

    if tecnico is None:

        raise HTTPException(
            status_code=404,
            detail="Técnico não encontrado."
        )

    return tecnico


# ----------------------------------------------------------
# POST - CADASTRAR TÉCNICO
# ----------------------------------------------------------

@router.post(
    "/tecnicos",
    status_code=201,
    tags=["Técnicos"]
)
def post_tecnico(
    tecnico: TecnicoCriar
):

    tecnico_id = cadastrar_tecnico(
        tecnico
    )

    return {
        "mensagem": "Técnico cadastrado com sucesso.",
        "id": tecnico_id
    }


# ----------------------------------------------------------
# PUT - ATUALIZAR TÉCNICO
# ----------------------------------------------------------

@router.put(
    "/tecnicos/{tecnico_id}",
    tags=["Técnicos"]
)
def put_tecnico(
    tecnico_id: int,
    tecnico: TecnicoAtualizar
):

    resultado = alterar_tecnico(
        tecnico_id,
        tecnico
    )

    if resultado == 0:

        raise HTTPException(
            status_code=404,
            detail=(
                "Técnico não encontrado "
                "ou nenhum dado foi alterado."
            )
        )

    return {
        "mensagem": "Técnico atualizado com sucesso."
    }


# ----------------------------------------------------------
# DELETE - EXCLUIR TÉCNICO
# ----------------------------------------------------------

@router.delete(
    "/tecnicos/{tecnico_id}",
    tags=["Técnicos"]
)
def delete_tecnico(
    tecnico_id: int
):

    try:

        resultado = remover_tecnico(
            tecnico_id
        )

    except Exception:

        raise HTTPException(
            status_code=409,
            detail=(
                "Não foi possível excluir o técnico. "
                "Ele pode possuir chamados atribuídos."
            )
        )

    if resultado == 0:

        raise HTTPException(
            status_code=404,
            detail="Técnico não encontrado."
        )

    return {
        "mensagem": "Técnico excluído com sucesso."
    }


# ==========================================================
# CHAMADOS
# ==========================================================


# ----------------------------------------------------------
# GET - LISTAR TODOS OS CHAMADOS
# ----------------------------------------------------------

@router.get(
    "/chamados",
    response_model=List[ChamadoResposta],
    tags=["Chamados"]
)
def get_chamados():

    return obter_chamados()


# ----------------------------------------------------------
# GET - BUSCAR CHAMADO POR ID
# ----------------------------------------------------------

@router.get(
    "/chamados/{chamado_id}",
    response_model=ChamadoResposta,
    tags=["Chamados"]
)
def get_chamado(
    chamado_id: int
):

    chamado = obter_chamado_por_id(
        chamado_id
    )

    if chamado is None:

        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado."
        )

    return chamado


# ----------------------------------------------------------
# POST - CADASTRAR CHAMADO
# ----------------------------------------------------------

@router.post(
    "/chamados",
    status_code=201,
    tags=["Chamados"]
)
def post_chamado(
    chamado: ChamadoCriar
):

    chamado_id = cadastrar_chamado(
        chamado
    )

    return {
        "mensagem": "Chamado cadastrado com sucesso.",
        "id": chamado_id
    }


# ----------------------------------------------------------
# PUT - ATUALIZAR CHAMADO
# ----------------------------------------------------------

@router.put(
    "/chamados/{chamado_id}",
    tags=["Chamados"]
)
def put_chamado(
    chamado_id: int,
    chamado: ChamadoAtualizar
):

    resultado = alterar_chamado(
        chamado_id,
        chamado
    )

    if resultado == 0:

        raise HTTPException(
            status_code=404,
            detail=(
                "Chamado não encontrado "
                "ou nenhum dado foi alterado."
            )
        )

    return {
        "mensagem": "Chamado atualizado com sucesso."
    }


# ----------------------------------------------------------
# DELETE - EXCLUIR CHAMADO
# ----------------------------------------------------------

@router.delete(
    "/chamados/{chamado_id}",
    tags=["Chamados"]
)
def delete_chamado(
    chamado_id: int
):

    try:

        resultado = remover_chamado(
            chamado_id
        )

    except Exception:

        raise HTTPException(
            status_code=409,
            detail=(
                "Não foi possível excluir o chamado. "
                "Existem comentários, histórico "
                "ou anexos vinculados."
            )
        )

    if resultado == 0:

        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado."
        )

    return {
        "mensagem": "Chamado excluído com sucesso."
    }