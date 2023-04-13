from rest_framework import serializers
from .models import Rating, Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    synopsis = serializers.CharField(default=None)
    added_by = serializers.CharField(source='user.email', read_only=True)
    rating = serializers.ChoiceField(choices=Rating.choices, default=Rating.G)  # errors menssage?


    def create(self, validated_data: dict) -> Movie:
        # if validated_data['rating'] not in Rating.values:
        #     print(f"""\"{validated_data['rating']}\" is not a valid choice.""")
        return Movie.objects.create(**validated_data)

