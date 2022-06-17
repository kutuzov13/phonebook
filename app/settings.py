import logging
import sys

from loguru import logger
from pydantic import BaseSettings, PostgresDsn

from app.logging import InterceptHandler


class Setting(BaseSettings):
    """Check defines the environment."""

    database_url: PostgresDsn

    debug: bool = False
    docs_url: str = "/docs"
    title: str = "phonebook"
    version: str = "0.1.0"

    logging_level: int = logging.INFO
    loggers: str = "uvicorn"

    class Config:
        env_file = ".env"
        validate_assignment = True

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])


def get_setting() -> Setting:
    return Setting()
