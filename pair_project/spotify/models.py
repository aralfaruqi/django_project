from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=255, default='')
    image = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.genre

class Album(models.Model):
    album = models.CharField(max_length=255, default='')
    deskripsi = models.TextField(default='')
    image = models.CharField(max_length=255, default='')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    def __str__(self):
        return self.album

class Song(models.Model):
    title = models.CharField(max_length=255, default='')
    artist = models.CharField(max_length=255, default='')
    minutes = models.CharField(max_length=255, default='0:00')
    song = models.CharField(max_length=255, default='')
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.title