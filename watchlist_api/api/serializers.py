from rest_framework import serializers
from watchlist_api.models import Movies


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data('name',validated_data.name)
        instance.description = validated_data('description', validated_data.description)
        instance.active = validated_data('active', validated_data.active)
        instance.save()
