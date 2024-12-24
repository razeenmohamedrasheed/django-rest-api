from django.urls import path
from watchlist_api.views import list_all_movies

urlpatterns = [
    path("",list_all_movies, name="list_movies")
]
