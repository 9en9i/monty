from templates.loader import global_templates
from starlette.responses import Response


def render(path, context):
    if context is None:
        context = {}

    return Response(global_templates.get_template(path).render(**context))

