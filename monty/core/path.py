from typing import Type

from monty.core.mixins import RetrieveView, CreateView, ListView


def path(url: str, view: Type) -> (str, [(str,)]):
    view_obj = view()
    route = []
    if issubclass(view, RetrieveView):
        route.append(("GET", f"{url}/""{object_id:d}", view_obj.retrieve))
    if issubclass(view, CreateView):
        route.append(("POST", f"{url}", view_obj.create))
    if issubclass(view, ListView):
        route.append(("GET", f"{url}", view_obj.list))
    return url, route
