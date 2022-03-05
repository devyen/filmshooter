from django.conf import settings
from django.db.models import fields
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from movies.models import Movie
from .models import Review, Comment
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'nickname', )


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'review', 'content', 'created_at', 'updated_at', )


# 전체리뷰 READ - comments 안보냄
class ReviewListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)
    
    # READ only
    user = UserSerializer(read_only=True)
    movie = MovieSerializer()
    comments_count = serializers.ReadOnlyField(source='comments.count')
    like_users_count = serializers.ReadOnlyField(source='like_users.count')

    class Meta:
        model = Review
        fields = ('comments_count', 'user', 'like_users', 'like_users_count', 'id', 'movie', 'rate', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('like_users',)


# 프로필페이지 READ용
class ProfileReviewListSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'release_date')

    # READ only
    user = UserSerializer(read_only=True)
    comments_count = serializers.ReadOnlyField(source='comments.count')
    like_users_count = serializers.ReadOnlyField(source='like_users.count')
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = ('comments_count', 'user', 'like_users', 'like_users_count', 'id', 'movie', 'rate', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('like_users',)


# 단일리뷰 READ, CREATE, UPDATE
class ReviewSerializer(serializers.ModelSerializer):
    
    # READ only
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.ReadOnlyField(source='comments.count')
    like_users_count = serializers.ReadOnlyField(source='like_users.count')

    class Meta:
        model = Review
        fields = ('comments', 'comments_count', 'user', 'like_users', 'like_users_count', 'id', 'movie', 'rate', 'content', 'created_at', 'updated_at',)
        read_only_fields = ('like_users',)
