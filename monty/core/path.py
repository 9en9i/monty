from typing import Type

from monty.core.mixins import RetrieveView, CreateView, ListView, RetrieveAsyncView, CreateAsyncView, ListAsyncView


def path(url: str, view: Type) -> (str, [(str,)]):
    view_obj = view()
    route = []
    if issubclass(view, RetrieveView) or issubclass(view, RetrieveAsyncView):
        route.append(("GET", f"{url}/""{object_id:d}", view_obj.retrieve))
    if issubclass(view, CreateView) or issubclass(view, CreateAsyncView):
        route.append(("POST", f"{url}", view_obj.create))
    if issubclass(view, ListView) or issubclass(view, ListAsyncView):
        route.append(("GET", f"{url}", view_obj.list))
    return url, route
