from django.contrib import admin

from movie_app.models import Movie, Actor, Director

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Director)
