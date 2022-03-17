from monty.core.path import path
from server.books.views import BookView

route = [
    path("/book", BookView)
]