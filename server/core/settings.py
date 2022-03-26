from pathlib import Path

HOME_DIR = Path(__file__).resolve().parent.parent


INSTALLED_APPS = (
    "server.books",
    "server.home",
)

TEMPLATES = "templates"

EXCEPTIONS = (
    "core.exceptions.ExceptionValueError",
)
