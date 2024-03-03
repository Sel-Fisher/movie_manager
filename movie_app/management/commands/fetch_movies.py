import os

import requests
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.db import transaction


from movie_app.models import Movie, Director, Actor

load_dotenv()
API_KEY = os.environ["API_KEY"]


class Command(BaseCommand):
    help = "Fetch movies from OMDB API"
    MOST_POPULAR_WORD = "day"

    def handle(self, *args, **options) -> None:
        self.stdout.write("Waiting to fill database...")
        page = 1
        total_films = 0
        while total_films < 100:
            self.stdout.write(f"Getting info from page {page}")
            response = requests.get(
                f"https://www.omdbapi.com/",
                params={
                    "apikey": API_KEY,
                    "s": self.MOST_POPULAR_WORD,
                    "type": "movie",
                    "page": page,
                    "r": "json",
                },
            )
            data = response.json()
            if "Search" in data:
                for movie_data in data["Search"]:
                    detail_response = requests.get(
                        "https://www.omdbapi.com/",
                        params={
                            "apikey": API_KEY,
                            "i": movie_data["imdbID"],
                            "r": "json",
                        },
                    )
                    movie_details = detail_response.json()
                    if "Title" in movie_details:
                        with transaction.atomic():
                            director_name = (
                                movie_details["Director"]
                                .replace(",", "")
                                .split(" ")[:2]
                            )
                            director, _ = Director.objects.get_or_create(
                                first_name=director_name[0],
                                last_name=(
                                    director_name[1]
                                    if len(director_name) % 2 == 0
                                    else ""
                                ),
                            )

                            movie, created = Movie.objects.get_or_create(
                                title=movie_details["Title"],
                                year=movie_details["Year"],
                                director=director,
                            )
                            if created:
                                for actor_name in movie_details[
                                    "Actors"
                                ].split(", "):
                                    actor_name = actor_name.split(" ")
                                    actor, _ = Actor.objects.get_or_create(
                                        first_name=actor_name[0],
                                        last_name=(
                                            actor_name[1]
                                            if len(actor_name) % 2 == 0
                                            else ""
                                        ),
                                    )
                                    movie.actors.add(actor)

                                total_films += 1
            page += 1

        self.stdout.write(self.style.SUCCESS("Database is now filled!"))
