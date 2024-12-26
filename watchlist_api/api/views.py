from watchlist_api.models import  Movies
from watchlist_api.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_all_movies(request):
    try:
        movie = Movies.objects.all()
        serialzed = MovieSerializer(movie,many=True)
        return Response(serialzed.data)
    except Exception as e:
        print(f"Error at {e}")

