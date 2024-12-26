from django.urls import path
from watchlist_api.api.views import list_all_movies

urlpatterns = [
    path("", list_all_movies, name="List Movies")
]
