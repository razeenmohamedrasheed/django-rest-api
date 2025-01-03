from rest_framework import serializers
from watchlist_api.models import WatchList , StreamingPlatform


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"

    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Desc should not be same")
        else:
            return data

    def validate_name(self,value):
        if len(value)>2:
            raise serializers.ValidationError("Length too short")
        else:
            return value

class StreamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = '__all__'

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movies.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data('name',validated_data.name)
#         instance.description = validated_data('description', validated_data.description)
#         instance.active = validated_data('active', validated_data.active)
#         instance.save()
