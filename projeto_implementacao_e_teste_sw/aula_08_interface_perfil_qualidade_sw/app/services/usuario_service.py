from app.repositories.usuario_repository import (
    listar_usuarios,
    buscar_usuario_por_id,
    criar_usuario,
    atualizar_usuario,
    excluir_usuario
)


def obter_usuarios():
    return listar_usuarios()


def obter_usuario(usuario_id):
    return buscar_usuario_por_id(usuario_id)


def cadastrar_usuario(usuario):
    return criar_usuario(usuario)


def alterar_usuario(usuario_id, usuario):
    return atualizar_usuario(usuario_id, usuario)


def remover_usuario(usuario_id):
    return excluir_usuario(usuario_id)