from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# ==========================================================
# SCHEMA PARA CRIAÇÃO DE TÉCNICO
# ==========================================================

class TecnicoCriar(BaseModel):
    """
    Dados necessários para cadastrar
    um novo técnico no sistema TechPort.
    """

    nome: str
    email: str
    especialidade: str
    nivel: str

    disponivel: bool = True
    ativo: bool = True


# ==========================================================
# SCHEMA PARA ATUALIZAÇÃO DE TÉCNICO
# ==========================================================

class TecnicoAtualizar(BaseModel):
    """
    Dados que poderão ser alterados
    em um técnico já cadastrado.

    Todos os campos são opcionais.
    """

    nome: Optional[str] = None
    email: Optional[str] = None
    especialidade: Optional[str] = None
    nivel: Optional[str] = None

    disponivel: Optional[bool] = None
    ativo: Optional[bool] = None


# ==========================================================
# SCHEMA DE RESPOSTA DA API
# ==========================================================

class TecnicoResposta(BaseModel):
    """
    Estrutura retornada pela API
    ao consultar um técnico.
    """

    id: int
    nome: str
    email: str
    especialidade: str
    nivel: str

    disponivel: bool
    ativo: bool

    data_cadastro: datetime