from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import ProfileSerializer
from .models import Profile
from django.http.response import JsonResponse
from reviews.serializers import ReviewListSerializer, ProfileReviewListSerializer
from movies.serializers import MovieDetailSerializer


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([AllowAny])
def detail_or_create_or_update_profile(request, nickname):
    user = get_object_or_404(get_user_model(), nickname=nickname)
    # POST 요청 우선 처리
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user == user:
                if Profile.objects.filter(pk=request.user.pk):  # 이미 프로필이 있으면 pass
                # if get_object_or_404(Profile, user=user.pk): 
                    return Response('Profile already exists', status=status.HTTP_409_CONFLICT)
                else:
                    serializer = ProfileSerializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(user=request.user)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response('unauthorized', status=status.HTTP_401_UNAUTHORIZED)
        return Response('login required', status=status.HTTP_401_UNAUTHORIZED)
    
    # profile = Profile.objects.filter(user=user.pk)  # 한 개 조회할땐 filter 안됨!!
    profile = get_object_or_404(Profile, user=user.pk)
    
    # GET
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    # PUT
    if request.user.is_authenticated:
        if request.user == profile.user:
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response('unauthorized', status=status.HTTP_401_UNAUTHORIZED)
    return Response('login required', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_profile_statistic(request, nickname):
    profile_user = get_object_or_404(get_user_model(), nickname=nickname)
    reviews = profile_user.reviews.all()
    
    reviewsCount = reviews.count()
    movieLikesCount = profile_user.like_movies.count()
    if reviews:
        rate_avg = sum(review.rate for review in reviews)/len(reviews)
    else:
        rate_avg = 0

    return JsonResponse({
        'reviewsCount': reviewsCount,
        'movieLikesCount': movieLikesCount,
        'rateAvg': rate_avg,
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def get_reviews(request, nickname):
    profile_user = get_object_or_404(get_user_model(), nickname=nickname)
    reviews = profile_user.reviews
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_toprank_reviews(request, nickname):
    profile_user = get_object_or_404(get_user_model(), nickname=nickname)
    toprank_reviews = profile_user.reviews.order_by('-rate')[:20]
    serializer = ProfileReviewListSerializer(toprank_reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_like_movies(request, nickname):
    profile_user = get_object_or_404(get_user_model(), nickname=nickname)
    like_movies = profile_user.like_movies
    serializer = MovieDetailSerializer(like_movies, many=True)
    return Response(serializer.data)