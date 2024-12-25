from watchlist_api.models import Movies
from watchlist_api.api.serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def list_all_movies(request):
    try:
        movies = Movies.objects.all()
        MovieSerializer(movies)
        return Response(MovieSerializer.data)
    except Exception as e:
        print(f"Error occurred: {e}")
