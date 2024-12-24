from django.shortcuts import render
from watchlist_api.models import Movies
from django.http import JsonResponse


def list_all_movies(request):
    movies = Movies.objects.all().values()
    print(movies)
    return JsonResponse(list(movies), safe=False)