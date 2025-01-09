"""Module that defines a ConfigSection for uvicorn"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from application_settings import ConfigSectionBase, attributes_doc, dataclass


@attributes_doc
@dataclass(frozen=True)
class UvicornConfigSection(ConfigSectionBase):
    """ConfigSection for uvicorn."""

    host: str = "127.0.0.1"
    """IP where the server will be hosted on."""

    port: int = 6543
    """Port wehre the server will be hosted on."""

    log_level: str = "debug"
    """Level of logging for uvicorn."""

    reload: bool = False
    """If the server should automaticly reload. Should be FALSE for production."""

    set_default_log_config: bool = True
    """If True, the default LOG_CONFIG of uvicorn is set; if False, then no log config is set; defaults to True"""

    def as_uvicorn_config_dict(self) -> dict[str, Any]:
        """Converts UvicornConfigSection to a dictionary suitable for Uvicorn configuration."""

        uvicorn_config_dict = asdict(self)
        if not uvicorn_config_dict.pop("set_default_log_config"):
            uvicorn_config_dict["log_config"] = None

        return uvicorn_config_dict
