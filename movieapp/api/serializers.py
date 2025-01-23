from movieapp.models import Movie
from rest_framework import serializers


class Movieserializer(serializers.Serializer):
     id = serializers.IntegerField(read_only =True)
     title = serializers.CharField(max_length=100)  # A string field
     description = serializers.CharField(max_length=100)  # A text field for longer content
     is_active = serializers.BooleanField()

     def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

     def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance

