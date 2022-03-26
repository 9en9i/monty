from starlette.responses import Response

from core.errors import Errors


class ExceptionValueError(Errors):
    type_error = ValueError

    def handler(self, *args, **kwargs):
        return Response(args[0].args[0])