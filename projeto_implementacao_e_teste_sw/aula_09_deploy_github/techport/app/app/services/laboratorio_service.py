from app.repositories.laboratorio_repository import (
    assumir_chamado,
    alterar_status,
    criar_comentario,
    listar_comentarios,
    listar_historico,
    obter_resumo_dashboard,
)


def service_assumir_chamado(chamado_id, tecnico_id):
    return assumir_chamado(chamado_id, tecnico_id)


def service_alterar_status(chamado_id, dados):
    return alterar_status(chamado_id, dados.status, dados.tecnico_id, dados.observacao)


def service_criar_comentario(chamado_id, dados):
    return criar_comentario(chamado_id, dados)


def service_listar_comentarios(chamado_id):
    return listar_comentarios(chamado_id)


def service_listar_historico(chamado_id):
    return listar_historico(chamado_id)


def service_obter_resumo_dashboard():
    return obter_resumo_dashboard()
