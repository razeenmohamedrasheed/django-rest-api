from rest_framework import status
from watchlist_api.models import WatchList
from watchlist_api.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def list_movies(request):
    """
    Retrieve a list of all movies.
    """
    try:
        movies = WatchList.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    """
    Retrieve, update, or delete a specific movie by ID.
    """
    try:
        movie = WatchList.objects.get(pk=pk)
    except Exception as e:
        return Response({"error": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response({"message": "Movie deleted successfully."}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_movie(request):
    """
    Create a new movie.
    """
    try:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
