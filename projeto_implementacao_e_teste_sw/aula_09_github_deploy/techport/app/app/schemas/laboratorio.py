from typing import Literal, Optional
from pydantic import BaseModel, Field


class AssumirChamado(BaseModel):
    tecnico_id: int


class AlterarStatusChamado(BaseModel):
    status: str = Field(min_length=2, max_length=30)
    tecnico_id: Optional[int] = None
    observacao: str = "Status atualizado pela interface do TechPort."


class ComentarioCriar(BaseModel):
    autor_tipo: Literal["usuario", "tecnico", "admin"]
    comentario: str = Field(min_length=1, max_length=2000)
    usuario_id: Optional[int] = None
    tecnico_id: Optional[int] = None
    visibilidade: str = "publico"
