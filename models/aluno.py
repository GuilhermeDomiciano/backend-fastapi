from typing import Optional
from sqlmodel import SQLModel, Field

class AlunoBase(SQLModel):
    nome: str
    descricao: Optional[str] = None

class Aluno(AlunoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class AlunoCreate(AlunoBase):
    pass

class AlunoRead(Aluno):
    pass
