from monty.core.path import path
from server.books.views import BookView, AuthorsView, CompaniesView

route = [
    path("/book", BookView),
    path("/author", AuthorsView),
    path("/company", CompaniesView)
]