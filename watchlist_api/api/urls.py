from django.urls import path
from watchlist_api.api.views import  movie_detail, create_movie ,list_movies

urlpatterns = [
    path("", list_movies, name="list_movies"),  # For GET (list all movies)
    path("create/", create_movie, name="create_movie"),  # For POST (create a new movie)
    path("<int:pk>/", movie_detail, name="movie_detail"),  # For GET (retrieve), PUT, and DELETE a specific movie
]