from monty.core.view import AsyncViewSet, ViewSet
from starlette.responses import Response
from monty.core.response import Response


class BookView(AsyncViewSet):
    async def list(self, request) -> Response:
        return Response("List book")

    async def retrieve(self, request, object_id: int, *args, **kwargs) -> Response:
        return Response(f"Retrieve book: {object_id}")


class AuthorsView(ViewSet):
    def list(self, request) -> Response:
        return Response("List authors")

    def retrieve(self, request, object_id: int, *args, **kwargs) -> Response:
        return Response(f"Retrieve author: {object_id}")


class CompaniesView(ViewSet):
    def list(self, request) -> Response:
        return Response("List companies")

    async def retrieve(self, request, object_id: int, *args, **kwargs) -> Response:
        return Response(f"Retrieve company: {object_id}")
