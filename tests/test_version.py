"version tests"

from uvicorn_configurable import __version__


def test_version() -> None:
    """
    Test version
    """
    assert __version__ == "0.1.0.dev0"
