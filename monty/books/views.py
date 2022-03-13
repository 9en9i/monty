from monty.core.view import ViewSet
from webob import Response, Request


class BookView(ViewSet):
    def list(self, request: Request) -> Response:
        return Response("List book")

    def retrieve(self, request: Request, object_id: int, *args, **kwargs) -> Response:
        return Response(f"Retrieve book: {object_id}")
