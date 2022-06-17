from fastapi import APIRouter

from app.api.routes import ping

router = APIRouter()
router.include_router(ping.router, tags=["about"], prefix="/about")
