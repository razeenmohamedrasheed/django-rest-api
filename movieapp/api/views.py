from movieapp.models import Movie
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movieapp.api.serializers import Movieserializer


@api_view(['GET','POST'])
def movie(request):
    """
      Handles retrieving all movies (GET) and adding a new movie (POST).
    """
    if request.method == 'GET':
        try:
            movie = Movie.objects.all()
            response_data = Movieserializer(movie,many=True)
            return Response(response_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {   "error": "Failed to fetch movies. Please try again later."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
