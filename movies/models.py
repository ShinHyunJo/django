from django.db import models

# Create your models here.
from accounts.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'movies_genre'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField(null=True)
    release_date = models.DateField()
    youtube_path = models.CharField(max_length=200, blank=True)
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'movies_movie'

class Movie_scrap_users(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'movies_movie_scrap_users'

class Movie_genres(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'movies_movie_genres'