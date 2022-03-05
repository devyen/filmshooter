from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Review, Comment
from .serializers import CommentSerializer, ReviewSerializer, ReviewListSerializer
from rest_framework.permissions import AllowAny
from django.db.models import Count


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def create_or_list_review(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie_pk).annotate(count=Count('like_users')).order_by('-count')
        print(reviews)
        serializer = ReviewListSerializer(reviews, many=True)
        print(serializer)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:  # 로그인한 사용자
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('login required', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def detail_or_update_or_delete_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # 단일 리뷰&코멘트들 조회
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.user.is_authenticated:  # 로그인한 사용자
        if request.user == review.user:  # 유저 == 글쓴이(자기 글만 수정/삭제 가능하도록)
            # 리뷰 수정
            if request.method == 'PUT':
                serializer = ReviewSerializer(review, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
            # 리뷰 삭제
            else:
                review.delete()
                return Response('delete success', status=status.HTTP_204_NO_CONTENT)
        return Response('unauthorized', status=status.HTTP_401_UNAUTHORIZED)
    return Response('login required', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    likesCount = review.like_users.count()
    return JsonResponse({
        'likesCount': likesCount,
    })


@api_view(['POST'])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data) 


@api_view(['PUT', 'DELETE'])
def update_or_delete_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'PUT':
            serializer = CommentSerializer(data=request.data, instance=comment)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'DELETE':
            comment.delete()
            return Response('delete success', status=status.HTTP_204_NO_CONTENT)
    else:
        return Response('unauthorized', status=status.HTTP_401_UNAUTHORIZED)
