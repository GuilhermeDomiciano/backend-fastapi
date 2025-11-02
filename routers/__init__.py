from fastapi import APIRouter
from .demo import router as demo_router
from .health import router as health_router
from .aluno import router as aluno_router
api_router = APIRouter()
api_router.include_router(demo_router)
api_router.include_router(health_router)
api_router.include_router(aluno_router)
