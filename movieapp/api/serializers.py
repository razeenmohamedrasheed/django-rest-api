from movieapp.models import Movie
from rest_framework import serializers


class Movieserializer(serializers.Serializer):
     id = serializers.IntegerField(read_only =True)
     title = serializers.CharField(max_length=100)  # A string field
     description = serializers.CharField(max_length=100)  # A text field for longer content
     is_active = serializers.BooleanField()

