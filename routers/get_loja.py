from uuid import UUID

from fastapi import APIRouter
from sqlmodel import Session, select

from database import engine
from models.loja import Loja
from models.produto import Produto

router = APIRouter(tags=["Loja"])


@router.get("/lojas/{loja_id}")
def get_loja(loja_id: UUID):
    with Session(engine) as session:
        loja = session.get(Loja, loja_id)
        produtos = session.exec(
            select(Produto).where(Produto.loja_id == loja_id)
        ).all()

        loja_data = loja.model_dump()
        loja_data["produtos"] = []
        for produto in produtos:
            produto_data = produto.model_dump()
            produto_data.pop("loja", None)
            loja_data["produtos"].append(produto_data)

        return loja_data
