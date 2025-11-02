from fastapi import APIRouter

router = APIRouter(tags=["demo"])

@router.get("/")
def read_root():
    return {
        "name": "MiniCurso Full Stack (FastAPI + Vite)",
        "version": "0.1.0",
        "status": "ok",
        "docs": "/docs",
        "redoc": "/redoc",
    }

@router.get("/ping")
def ping():
    return {"pong": True}

@router.get("/eco/{nome}")
def eco_nome(nome: str, vezes: int = 1):
    return {"mensagem": " ".join([nome] * max(1, vezes))}
