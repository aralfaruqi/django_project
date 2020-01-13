from django.contrib import admin
from .models import Genre, Album, Song

# Register your models here.

admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Song)