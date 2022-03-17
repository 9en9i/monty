from monty.core.mixins import RetrieveView, CreateView, ListView, RetrieveAsyncView, CreateAsyncView, ListAsyncView

# region sync


class View:
    pass


class ViewSet(RetrieveView, CreateView, ListView, View):
    pass

# endregion


# regions async

class AsyncView:
    pass


class AsyncViewSet(RetrieveAsyncView, CreateAsyncView, ListAsyncView, AsyncView):
    pass

# endregion
