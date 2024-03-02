from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from movie_app.filters import MovieFilter
from movie_app.models import Movie, Director, Actor
from movie_app.serializers import (
    ActorSerializer,
    DirectorSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    DirectorListSerializer,
    ActorListSerializer,
)


class StandardListPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100


class MovieList(APIView):
    pagination_class = StandardListPagination
    filterset_class = MovieFilter

    def post(self, request) -> Response:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request) -> Response:
        movies = Movie.objects.all()
        movies = self.filterset_class(
            data=request.query_params, queryset=movies
        ).qs

        paginator = self.pagination_class()
        page = paginator.paginate_queryset(movies, request)

        if page is not None:
            serializer = MovieListSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MovieDetail(APIView):

    def get_object(self, pk: int) -> Movie:
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk: int) -> Response:
        movie = self.get_object(pk=pk)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk: int) -> Response:
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int) -> Response:
        self.get_object(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DirectorList(APIView):
    pagination_class = StandardListPagination

    def post(self, request) -> Response:
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request) -> Response:
        director = Director.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(director, request)

        if page is not None:
            serializer = DirectorListSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = DirectorListSerializer(director, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DirectorDetail(APIView):
    def get_object(self, pk: int) -> Director:
        return get_object_or_404(Director, pk=pk)

    def get(self, request, pk: int) -> Response:
        director = self.get_object(pk=pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, pk: int) -> Response:
        director = self.get_object(pk=pk)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int) -> Response:
        self.get_object(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(APIView):
    pagination_class = StandardListPagination

    def post(self, request) -> Response:
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request) -> Response:
        actor = Actor.objects.all()
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(actor, request)

        if page is not None:
            serializer = ActorListSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = ActorListSerializer(actor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActorDetail(APIView):
    def get_object(self, pk: int) -> Actor:
        return get_object_or_404(Actor, pk=pk)

    def get(self, request, pk: int) -> Response:
        actor = self.get_object(pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def put(self, request, pk: int) -> Response:
        actor = self.get_object(pk=pk)
        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int) -> Response:
        self.get_object(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
