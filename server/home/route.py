from monty.core.path import path
from server.home.views import HomeView, ErrorView

route = [
    path("/", HomeView),
    path("/error", ErrorView),
]