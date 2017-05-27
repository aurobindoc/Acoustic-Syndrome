from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=1000)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo = models.CharField(max_length=1000)
    album = models.CharField(max_length=100)
