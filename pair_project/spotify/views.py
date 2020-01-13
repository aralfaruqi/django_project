from django.shortcuts import render
from .models import Genre, Album, Song

# Create your views here.

def home(request):
    genres = Genre.objects.all()
    albums = Album.objects.all()
    return render(request, 'spotify/home.html', {'genres' : genres, 'albums' :  albums})

def genre(request):
    genres = Genre.objects.all()
    return render(request, 'spotify/search.html', {'genres' : genres})

def album(request, album_id):
    album = Album.objects.get(pk=album_id)
    songs = Song.objects.filter(album_id=album_id)
    return render(request, 'spotify/album.html', {'album' : album, 'songs' : songs})

def song(request, album_id, song_id):
    album = Album.objects.get(pk=album_id)
    songs = Song.objects.filter(album_id=album_id)
    song = Song.objects.get(pk=song_id)
    return render(request, 'spotify/song.html', {'album' : album, 'songs' : songs, 'song' : song})