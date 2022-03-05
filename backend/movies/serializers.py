from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Genre, Movie

API_KEY = '9c6ea1359122cbfc10ce7bb9e6a0400e'
BASE_URL = 'https://api.themoviedb.org/3'

class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='tmdb_id')
    class Meta:
        model = Genre
        fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name')

    genres = GenreSerializer(many=True, read_only=True)
    genre_ids = serializers.ListField(write_only=True)
    id = serializers.IntegerField(source='tmdb_id')

    class Meta:
        model = Movie
        fields = ('title', 'genres', 'genre_ids', 'id', 'release_date', 'overview', 'original_language', 'poster_path', 'backdrop_path', 'runtime', 'tagline', 'vote_average','rate_average')

    def create(self, validated_data):
        genre_ids = validated_data.pop('genre_ids')
        movie = Movie.objects.create(**validated_data)
        for genre_id in genre_ids:
            genre = Genre.objects.get(tmdb_id=genre_id)
            movie.genres.add(genre.pk)
        return movie


class MovieDetailSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name', )
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('id', 'genres', 'title', 'tmdb_id', 'release_date', 'overview', 'original_language', 'poster_path', 'backdrop_path', 'rate_average', 'like_users', 'runtime', 'tagline', 'vote_average', )
        read_only_fields = ('like_users',)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path', 'rate_average', 'like_users', )