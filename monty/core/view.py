from monty.core.mixins import RetrieveView, CreateView, ListView


class View:
    pass


class ViewSet(RetrieveView, CreateView, ListView, View):
    pass
