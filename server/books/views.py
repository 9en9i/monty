from monty.core.view import AsyncViewSet
from starlette.responses import Response
from monty.core.response import Response


class BookView(AsyncViewSet):
    async def list(self, request) -> Response:
        return Response("List book")

    async def retrieve(self, request, object_id: int, *args, **kwargs) -> Response:
        return Response(f"Retrieve book: {object_id}")
