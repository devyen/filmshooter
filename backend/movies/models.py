from django.db import models

# Create your models here.
class Genre(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length=1000)
    
    
class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name="movies")
    title = models.CharField(max_length=100)
    tmdb_id = models.IntegerField()
    release_date = models.DateField()
    overview = models.TextField(null=True, blank=True)
    original_language = models.TextField()
    poster_path = models.TextField(null=True, blank=True)
    backdrop_path = models.TextField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    tagline = models.TextField(null=True, blank=True)
    vote_average = models.FloatField()
    rate_average = models.FloatField(null=True)  # 우리 사이트 평점 평균

    def __str__(self):
        return self.title