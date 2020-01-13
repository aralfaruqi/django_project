from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('genre', views.genre, name="genre"),
    path('album/<int:album_id>', views.album, name='album'),
    path('album/<int:album_id>/<int:song_id>', views.song, name="song")
]