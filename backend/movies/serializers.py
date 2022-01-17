from movies.models import Movie, Review
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "release_year",
            "duration",
            "poster_uri",
        )


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            "id",
            "movie",
            "date",
            "rating",
        )