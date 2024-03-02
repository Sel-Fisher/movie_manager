from rest_framework import serializers

from movie_app.models import Actor, Movie, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class DirectorListSerializer(serializers.ModelSerializer):
    full_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Director
        fields = ("id", "full_name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class ActorListSerializer(serializers.ModelSerializer):
    full_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "full_name")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "year", "director", "actors")


class MovieListSerializer(MovieSerializer):
    director = DirectorListSerializer()
    actors = ActorListSerializer(many=True)


class MovieDetailSerializer(MovieSerializer):
    director = DirectorSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
