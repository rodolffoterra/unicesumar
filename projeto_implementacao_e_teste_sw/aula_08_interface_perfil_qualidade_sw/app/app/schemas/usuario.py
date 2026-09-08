from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# ==========================================================
# DADOS PARA CADASTRAR USUÁRIO
# ==========================================================

class UsuarioCriar(BaseModel):
    nome: str
    email: str
    senha_hash: str
    perfil: str = "cliente"
    ativo: bool = True


# ==========================================================
# DADOS PARA ATUALIZAR USUÁRIO
# ==========================================================

class UsuarioAtualizar(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    senha_hash: Optional[str] = None
    perfil: Optional[str] = None
    ativo: Optional[bool] = None


# ==========================================================
# DADOS RETORNADOS PELA API
# ==========================================================

class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str
    perfil: str
    ativo: bool
    data_cadastro: Optional[datetime] = None