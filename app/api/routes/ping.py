from typing import Any, Dict

from fastapi import APIRouter, Depends

from app.settings import Setting, get_setting

router = APIRouter()


@router.get("/ping")
async def pong(settings: Setting = Depends(get_setting)) -> Dict[str, Any]:
    """Get information about the working environment."""
    return {
        "ping": "pong",
        "debug": settings.debug,
        "title": settings.title,
        "version": settings.version,
    }
