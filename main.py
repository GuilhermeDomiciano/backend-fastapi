from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from database import engine
from routers import api_router

API_TITLE = "MiniCurso Full Stack (FastAPI + Vite)"
API_VERSION = "0.1.0"

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Valida banco no startup (não derruba a app se falhar)
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception as e:
        print(f"[startup] AVISO: falha ao conectar no banco: {e}")
    yield

app = FastAPI(title=API_TITLE, version=API_VERSION, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False,
)

# monta as rotas
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
