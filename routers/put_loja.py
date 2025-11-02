from fastapi import APIRouter
from sqlmodel import Session

from database import engine
from models.loja import Loja

router = APIRouter(tags=["Loja"])


@router.put("/loja/add/")
def add_loja(nome: str, banner: str, icone: str, cor_loja: str):
    with Session(engine) as session:
        loja = Loja(
            nome=nome,
            banner=banner,
            icone=icone,
            cor_loja=cor_loja,
        )
        session.add(loja)
        session.commit()
        session.refresh(loja)
        return loja.model_dump()
