from django.urls import path

from movie_app.views import (
    MovieList,
    MovieDetail,
    DirectorList,
    DirectorDetail,
    ActorList,
    ActorDetail,
)

urlpatterns = [
    path("movies/", MovieList.as_view(), name="movie-list"),
    path(
        "movies/<int:pk>/",
        MovieDetail.as_view(),
        name="movie-detail",
    ),
    path("directors/", DirectorList.as_view(), name="director-list"),
    path(
        "directors/<int:pk>/",
        DirectorDetail.as_view(),
        name="director-detail",
    ),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path(
        "actors/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail",
    ),
]

app_name = "movie_app"
