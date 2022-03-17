# region sync
class RetrieveView:
    def retrieve(self, request, object_id, *args, **kwargs):
        pass


class CreateView:
    def create(self, request):
        pass


class ListView:
    def list(self, request):
        pass

# endregion


# region async

class RetrieveAsyncView:
    async def retrieve(self, request, object_id, *args, **kwargs):
        pass


class CreateAsyncView:
    async def create(self, request):
        pass


class ListAsyncView:
    async def list(self, request):
        pass

# endregion
