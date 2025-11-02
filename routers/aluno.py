from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from deps import get_session
from models.aluno import Aluno, AlunoCreate, AlunoRead

router = APIRouter(prefix="/alunos", tags=["alunos"])

@router.get("", response_model=List[AlunoRead])
def listar_alunos(session: Session = Depends(get_session)):
    return session.exec(select(Aluno)).all()

@router.post("", response_model=AlunoRead)
def criar_aluno(dado: AlunoCreate, session: Session = Depends(get_session)):
    novo = Aluno.from_orm(dado)
    session.add(novo)
    session.commit()
    session.refresh(novo)
    return novo

@router.get("/{id}", response_model=AlunoRead)
def buscar_aluno(id: int, session: Session = Depends(get_session)):
    aluno = session.get(Aluno, id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno
