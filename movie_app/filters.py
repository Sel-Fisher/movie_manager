import django_filters
from django.db.models import Q

from movie_app.models import Movie


class MovieFilter(django_filters.FilterSet):
    director_name = django_filters.CharFilter(method="filter_director_name")
    actor_name = django_filters.CharFilter(method="filter_actor_name")

    class Meta:
        model = Movie
        fields = ["year", "director_name", "actor_name"]

    def filter_director_name(self, queryset, name, value):
        return queryset.filter(
            Q(director__first_name__icontains=value)
            | Q(director__last_name__icontains=value)
        )

    def filter_actor_name(self, queryset, name, value):
        return queryset.filter(
            Q(actors__first_name__icontains=value)
            | Q(actors__last_name__icontains=value)
        )
