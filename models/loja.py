from typing import List, Optional
from uuid import UUID

from sqlalchemy import text
from sqlmodel import Field, Relationship, SQLModel

class Loja(SQLModel, table=True):
    id: UUID | None = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()")},
    )
    nome: str = Field(index=True, nullable=False)
    banner: Optional[str] = None
    icone: Optional[str] = None
    cor_loja: Optional[str] = None

    produtos: List["Produto"] = Relationship(back_populates="loja")

from models.produto import Produto