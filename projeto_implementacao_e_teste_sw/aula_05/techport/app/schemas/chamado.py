from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# ==========================================================
# SCHEMA PARA CRIAÇÃO DE CHAMADO
# ==========================================================

class ChamadoCriar(BaseModel):
    """
    Dados necessários para cadastrar
    um novo chamado no sistema TechPort.
    """

    usuario_id: int

    tecnico_id: Optional[int] = None

    titulo: str

    descricao: str

    categoria: str

    prioridade: str

    status: str = "aberto"

    canal_abertura: str


# ==========================================================
# SCHEMA PARA ATUALIZAÇÃO DE CHAMADO
# ==========================================================

class ChamadoAtualizar(BaseModel):
    """
    Dados que poderão ser alterados
    em um chamado já cadastrado.

    Todos os campos são opcionais.
    """

    usuario_id: Optional[int] = None

    tecnico_id: Optional[int] = None

    titulo: Optional[str] = None

    descricao: Optional[str] = None

    categoria: Optional[str] = None

    prioridade: Optional[str] = None

    status: Optional[str] = None

    canal_abertura: Optional[str] = None

    data_fechamento: Optional[datetime] = None


# ==========================================================
# SCHEMA DE RESPOSTA DA API
# ==========================================================

class ChamadoResposta(BaseModel):
    """
    Estrutura retornada pela API
    ao consultar um chamado.
    """

    id: int

    usuario_id: int

    tecnico_id: Optional[int] = None

    titulo: str

    descricao: str

    categoria: str

    prioridade: str

    status: str

    canal_abertura: str

    data_abertura: datetime

    data_atualizacao: datetime

    data_fechamento: Optional[datetime] = None