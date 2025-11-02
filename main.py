from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import api_router

API_TITLE = "MiniCurso Full Stack (FastAPI + Vite)"
API_VERSION = "0.1.0"

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
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
