from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlmodel import Session
from deps import get_session

router = APIRouter(tags=["health"])

@router.get("/health/db")
def health_db(session: Session = Depends(get_session)):
    try:
        session.exec(text("SELECT 1")).first()
        return {"db": "ok"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}
