"""Entry point of the uvicorn_configurable library, collects all exportable items and disables logging by default."""

from loguru import logger

from uvicorn_configurable._version import __version__
from uvicorn_configurable.config import UvicornConfigSection

logger.disable("uvicorn_configurable")

__all__ = [
    "__version__",
    "UvicornConfigSection",
]
