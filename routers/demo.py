from fastapi import APIRouter

router = APIRouter(tags=["meta"])

@router.get("/")
def read_root():
    return {
        "name": "MiniCurso Full Stack (FastAPI + Vite)",
        "version": "0.1.0",
        "status": "ok",
        "docs": "/docs",
        "redoc": "/redoc",
    }
