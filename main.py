# app/main.py
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlmodel import Session

from database import engine 

API_TITLE = "MiniCurso Full Stack (FastAPI + Vite)"
API_VERSION = "0.1.0"

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Startup
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception as e:
        # Não derruba o app, mas registra (você pode trocar por log real)
        print(f"[startup] AVISO: falha ao conectar no banco: {e}")
    yield
   


app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)


# ──────────────────────────────────────────────────────────────
# CORS ──────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    
    allow_methods=["*"],    
    allow_headers=["*"],    
    allow_credentials=False, 
)


# ──────────────────────────────────────────────────────────────
# Dependência de sessão (Session por request)
# ──────────────────────────────────────────────────────────────
def get_session():
    with Session(engine) as session:
        yield session


# ──────────────────────────────────────────────────────────────
# Rotas básicas
# ──────────────────────────────────────────────────────────────
@app.get("/", tags=["meta"])
def read_root():
    return {
        "name": API_TITLE,
        "version": API_VERSION,
        "status": "ok",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health/db", tags=["health"])
def health_db(session: Session = Depends(get_session)):
    """
    Verifica conexão com o banco executando um SELECT 1.
    Retorna {"db": "ok"} se conectado.
    """
    try:
        session.exec(text("SELECT 1")).first()
        return {"db": "ok"}
    except Exception as e:
        return {"db": "error", "detail": str(e)}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
