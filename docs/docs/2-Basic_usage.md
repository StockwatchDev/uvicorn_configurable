# Basic usage #

The `uvicorn_configurable` package is designed to simplify the configuration of the `uvicorn` ASGI web server
implementation for Python. This guide explains how to use `uvicorn_configurable` in your Python application.

## Setting Up Configuration

### Configuration Module

Define a module to load and manage the configuration of your application. For example, `config.py`:

```python
from application_settings import ConfigBase, config_filepath_from_cli, dataclass
from uvicorn_configurable import UvicornConfigSection

@dataclass(frozen=True)
class ExampleConfig(ConfigBase):
    """Config for the application."""

    uvicorn: UvicornConfigSection = UvicornConfigSection()

# Load config.
config_filepath_from_cli(ExampleConfig, load=True)
```

This module uses `application_settings` to load the configuration from file.

### Configuration File

Create a `config.toml` file to configure your `uvicorn` setup. That file should at the very least specify an item `app`
in a section `[uvicorn.application]`. Here is an example:

```toml
[uvicorn.application]
app = "main:app"

[uvicorn.production]
workers = 4

[uvicorn.http]
set_default_forwarded_allow_ips = "false"
forwarded_allow_ips = [ '*' ]

[uvicorn.socket_binding]
host = "localhost"
port = 6543
```

This file defines:

- The ASGI app that will be served;
- The number of workers that will be started
- The list of IP Addresses to trust with proxy headers (here: all);
- The host and port to use for serving.

## Using a configured uvicorn

Here's a main script (`__main__.py`) and a supporting module (`main.py`) to demonstrate the server behavior. The
supporting module shows in the `main` function how the method `as_uvicorn_config_dict()` is used to convert the
dataclass instance into a dictionary that can be used to configure `uvicorn`.

### `__main__.py`

```python
"""Call the main function, which runs a configured uvicorn process.
"""

import config  # pylint: disable=unused-import  # isort: skip

import sys

from main import main

sys.exit(main())
```

### `main.py`

```python
"""Main function"""

import uvicorn

from config import ExampleConfig


async def app(scope, receive, send):  # type: ignore  # pylint: disable=unused-argument
    """Dummy app"""

    assert scope["type"] == "http"

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"Hello, world!",
        }
    )


def main() -> int:
    """Run a simple uvicorn process that is configured with uvicorn_configurable"""
    cfg = ExampleConfig.get().uvicorn.as_uvicorn_config_dict()
    uvicorn.run(**cfg)
    return 0


if __name__ == "__main__":
    main()
```

### Output Example

Depending on your `config.toml` settings, you will see:

- Logs in the console stating that one or more workers have been started.
- A message `Hello world!` in the web browser when opening the configured host and port.
- Logs in the console what requests have been made and what the response has been.
