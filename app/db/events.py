import asyncpg
from fastapi import FastAPI
from loguru import logger

from app.settings import Setting


async def connect_to_db(app: FastAPI, settings: Setting) -> None:
    logger.info("Connecting to PostgreSQL")

    app.state.pool = await asyncpg.create_pool(
        str(settings.database_url),
    )

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await app.state.pool.close()

    logger.info("Connection closed")
