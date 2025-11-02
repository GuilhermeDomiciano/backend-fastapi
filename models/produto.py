from typing import Optional
from uuid import UUID

from sqlalchemy import text
from sqlmodel import Field, Relationship, SQLModel

class Produto(SQLModel, table=True):
    id: UUID | None = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={"server_default": text("gen_random_uuid()")},
    )
    nome: str = Field(nullable=False)
    icone: Optional[str] = None
    loja_id: UUID = Field(foreign_key="loja.id", index=True, nullable=False)

    loja: Optional["Loja"] = Relationship(back_populates="produtos")

from models.loja import Loja