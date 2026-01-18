from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)

class Game(models.Model):
    name = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()
    rating = models.IntegerField()
    