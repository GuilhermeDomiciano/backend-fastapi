from uuid import UUID

from fastapi import APIRouter
from sqlmodel import Session

from database import engine
from models.produto import Produto

router = APIRouter(tags=["Loja"])


@router.put("/loja/{loja_id}/produto/add/")
def add_produto(loja_id: str, nome: str, icone: str):
    with Session(engine) as session:
        produto = Produto(
            nome=nome,
            icone=icone,
            loja_id=UUID(loja_id),
        )
        session.add(produto)
        session.commit()
        session.refresh(produto)
        data = produto.model_dump()
        data.pop("loja", None)
        return data
