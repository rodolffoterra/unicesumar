from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()


ARQUIVO = "usuarios.json"


# ==========================
# MODELO
# ==========================

class Usuario(BaseModel):
    id: int
    nome: str
    idade: int
    endereco: str
    profissao: str
    salario: float


# ==========================
# FUNÇÕES AUXILIARES
# ==========================

def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_usuarios(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)


# ==========================
# GET
# ==========================

@app.get("/usuarios")
def listar_usuarios():
    return carregar_usuarios()


# ==========================
# GET POR ID
# ==========================

@app.get("/usuarios/{id}")
def buscar_usuario(id: int):

    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )


# ==========================
# POST
# ==========================

@app.post("/usuarios")
def cadastrar_usuario(usuario: Usuario):

    usuarios = carregar_usuarios()

    usuarios.append(usuario.dict())

    salvar_usuarios(usuarios)

    return {
        "mensagem": "Usuário cadastrado com sucesso!"
    }


# ==========================
# PUT
# ==========================

@app.put("/usuarios/{id}")
def atualizar_usuario(id: int, usuario: Usuario):

    usuarios = carregar_usuarios()

    for indice, item in enumerate(usuarios):

        if item["id"] == id:

            usuarios[indice] = usuario.dict()

            salvar_usuarios(usuarios)

            return {
                "mensagem": "Usuário atualizado com sucesso!"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )


# ==========================
# DELETE
# ==========================

@app.delete("/usuarios/{id}")
def excluir_usuario(id: int):

    usuarios = carregar_usuarios()

    for usuario in usuarios:

        if usuario["id"] == id:

            usuarios.remove(usuario)

            salvar_usuarios(usuarios)

            return {
                "mensagem": "Usuário removido com sucesso!"
            }

    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )