from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router
from app.events import create_start_app_handler, create_stop_app_handler
from app.settings import get_setting


def get_application() -> FastAPI:
    settings = get_setting()

    settings.configure_logging()

    application = FastAPI(
        debug=settings.debug,
        title=settings.title,
        version=settings.version,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )

    application.include_router(api_router)

    return application


app = get_application()
