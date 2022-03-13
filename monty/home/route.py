from monty.core.path import path
from monty.home.views import BookView

route = [
    path("/book", BookView)
]