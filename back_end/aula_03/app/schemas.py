from datetime import datetime

from pydantic import BaseModel, Field


class AtorEntrada(BaseModel):
    first_name: str = Field(
        min_length=1,
        max_length=45,
    )

    last_name: str = Field(
        min_length=1,
        max_length=45,
    )


class AtorResposta(AtorEntrada):
    actor_id: int
    last_update: datetime