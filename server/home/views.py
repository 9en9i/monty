from monty.core.view import AsyncViewSet, ViewSet, ListAsyncView
from starlette.responses import Response
from monty.core.response import Response
from monty.templates.render import render


class HomeView(ListAsyncView):
    async def list(self, request) -> Response:
        return render("home.html", context={"title": "Awesome Framework", "name": "Monty"})


class ErrorView(ListAsyncView):
    async def list(self, request) -> Response:
        raise ValueError("Value Custom Error")
