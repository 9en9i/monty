import importlib
from typing import Iterable, Callable, Optional

import parse
from webob import Request, Response

from monty.core.exceptions import DuplicatedUrl


class Monty:

    def __init__(self, name: str):
        self.route = {}
        for i in importlib.import_module(name + ".settings").__getattribute__("INSTALLED_APPS"):
            self.include(i)

    def __call__(self, environ: dict, start_response: Callable) -> Response:
        request = Request(environ)
        response = self.handle_request(request)

        return response(environ, start_response)

    def default_response(self) -> Response:
        response = Response()
        response.status_code = 404
        response.text = "Not found."
        return response

    def handle_request(self, request: Request) -> Response:
        for path, handlers in self.route.items():
            if request.path.startswith(path):
                method, kwargs = self.find_method(handlers, request.path, request.method)
                if method:
                    response = method(request, **kwargs)
                    return response

        response = self.default_response()
        return response

    def find_method(self, handlers: Iterable[tuple], path: str, method: str) -> (Optional[Callable], Optional[dict]):
        for handler in handlers:
            if (result := parse.parse(handler[1], path)) and method == handler[0]:
                return handler[2], result.named
        return None, None

    def include(self, name_app: str) -> None:
        for url, router in importlib.import_module(name_app + ".route").__getattribute__("route"):
            if url in self.route:
                raise DuplicatedUrl
            self.route[url] = router

