import importlib
import os

from jinja2 import Environment, FileSystemLoader


settings = importlib.import_module("server.core.settings")
global_templates = Environment(
            loader=FileSystemLoader(os.path.join(settings.HOME_DIR, settings.TEMPLATES))
        )