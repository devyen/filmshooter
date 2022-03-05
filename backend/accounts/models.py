from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movies = models.ManyToManyField(Movie, related_name='like_users')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_message = models.CharField(max_length=100, blank=True, null=True)
    favorite_genre_1 = models.CharField(max_length=20)
    favorite_genre_2 = models.CharField(max_length=20)
    favorite_genre_3 = models.CharField(max_length=20)
