from monty.core.path import path
from monty.books.views import BookView

route = [
    path("/book", BookView)
]