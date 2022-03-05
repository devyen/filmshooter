from django.db.models.query import Prefetch
import requests
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from rest_framework import serializers
from .serializers import GenreSerializer, MovieSerializer, MovieListSerializer, MovieDetailSerializer
from .models import Genre, Movie
from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

API_KEY = '9c6ea1359122cbfc10ce7bb9e6a0400e'
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_genres(request):
    url = BASE_URL + f'/genre/movie/list?api_key={API_KEY}&language=ko-kr'
    data = requests.get(url).json()['genres']
    serializer = GenreSerializer(data=data, many=True)
    
    if serializer.is_valid():
        serializer.save()


def fetch_movies(request):
    pop_url = BASE_URL + f'/movie/popular?api_key={API_KEY}&language=ko-kr'
    ids = []
    for page in range(1, 26):
        ids += [movie['id'] for movie in requests.get(pop_url+f'&page={page}').json()['results']]

    for id in ids:
        detail_url = BASE_URL + f'/movie/{id}?api_key={API_KEY}&language=ko-KR'
        data = requests.get(detail_url).json()
        genre_ids = [genre['id'] for genre in data['genres']]
        data['genre_ids'] = genre_ids
        del data['genres']
        
        serializer = MovieSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


@api_view(['GET'])
@permission_classes([AllowAny])
def get_movie_list(request):
    movies = Movie.objects.all()[:100]
    serializer = MovieDetailSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    likesCount = movie.like_users.count()
    return JsonResponse({
        'likesCount': likesCount,
    })
    

@api_view(['GET'])
def recommend(request):
    genre_scores = [0] * 19
    like_movies = request.user.like_movies.all()
    reviews = request.user.reviews.all()

    seen_movies = set()
    for review in reviews:
        rate = review.rate
        seen_movies.add(review.movie.id)
        genres = Movie.objects.get(pk=review.movie.id).genres.only('pk')
        for genre in genres:
            genre_scores[genre.pk - 1] += rate

    for movie in like_movies:
        genres = Movie.objects.get(pk=movie.id).genres.only('pk')
        seen_movies.add(movie.id)
        for genre in genres:
            genre_scores[genre.pk - 1] += 4    

    movie_scores = []
    for movie in Movie.objects.all():
        if movie.id in seen_movies:
            continue
        temp = 0
        for obj in movie.genres.values('pk'):
            temp += genre_scores[obj['pk'] - 1]
        movie_scores.append((movie, temp))

    movie_scores.sort(key=lambda arr: -arr[1])

    serializer = MovieDetailSerializer([movie[0] for movie in movie_scores[:24]], many=True)
    return Response(serializer.data)
