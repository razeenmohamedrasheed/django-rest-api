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
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    elif request.method == 'POST':
         try:
            serializer = Movieserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
         except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
@api_view(['GET','PUT','DELETE'])
def individual_movie(request,pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
            response_data = Movieserializer(movie,many=True)
            return Response(response_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    elif request.method == 'PUT':
        try:
          serializer = Movieserializer(data=request.data)
          if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )
          return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    elif request.method == 'DELETE':
        serializer = Movieserializer(data=request.data)
        serializer.delete()
        return Response(status=204)
