import importlib
from abc import ABC, abstractmethod
from typing import Iterable, Callable, Optional

import parse
from webob import Request, Response
from starlette.responses import PlainTextResponse, Response as UResponse
from asgiref.typing import HTTPScope
from monty.core.exceptions import DuplicatedUrl


class Monty(ABC):
    def __init__(self, name: str):
        self.route = {}
        for i in importlib.import_module(name + ".core.settings").__getattribute__("INSTALLED_APPS"):
            self.include(i)

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


class AsgiMixin:

    async def __call__(self, scope: HTTPScope, receive, send):

        response = await self.handle_request(scope)
        await response(scope, receive, send)

    async def handle_request(self: "Monty", request: dict) -> PlainTextResponse:
        for path, handlers in self.route.items():
            if request["path"].startswith(path):
                method, kwargs = self.find_method(handlers, request["path"], request["method"])
                if method:
                    response = await method(request, **kwargs)
                    return response

        response = self.default_response()
        return response

    def default_response(self) -> UResponse | PlainTextResponse:
        response = UResponse("Not found.")
        response.status_code = 404
        return response


class WsgiMixin:
    def __call__(self, environ, start_response) -> Response:
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self: Monty, request: Request) -> Response:
        for path, handlers in self.route.items():
            if request.path.startswith(path):
                method, kwargs = self.find_method(handlers, request.path, request.method)
                if method:
                    response = method(request, **kwargs)
                    return response

        response = self.default_response()
        return response

    def default_response(self) -> Response:
        response = Response("Not found.")
        response.status_code = 404
        return response


class SyncMonty(WsgiMixin, Monty):
    pass


class AsyncMonty(AsgiMixin, Monty):
    pass

