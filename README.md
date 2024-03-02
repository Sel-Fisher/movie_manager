# Movie Manager #

Welcome to the Movie Database project! This project aims to provide a comprehensive movie database where users can view, edit, and explore various movie details. The database is populated using the OMDB API, ensuring a vast collection of movie information.

## Features
1. **Retrieve Movies:** Users can fetch information about movies available in the database.
2. **Retrieve Directors and Actors:** Information about directors and actors involved in various movies can also be retrieved.
3. **Filtering Options:** The API offers filtering options based on movie year, director names, and actor names.
4. **Search Functionality:** Users can search for specific movies using keywords or filters.
5. **User Authentication:** Authentication is implemented using JWT tokens, providing a secure access mechanism.
6. **Admin Access:** Admin users have access to manage movies, including editing and deleting them.
7. **Regular User Access:** Regular users can only view movies, directors, and actors but cannot perform any editing actions.

## Technologies Used

* **Python:** The backend logic and scripting are implemented using Python.
* **Django:** Django framework is used for building the web application.
* **Django REST Framework:** Used for creating RESTful APIs to interact with the database.
* **OMDB API:** OMDB API is utilized for fetching movie information and populating the database.
* **PostgreSQL:** PostgreSQL database is used to store movie data.
* **Docker:** Docker containers are used for development and deployment environments.
* **JWT Authentication:** JSON Web Tokens (JWT) are used for user authentication.

## Getting Started
To get started with the Movie Manager, follow these steps:

1. **Clone the Repository:** Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/movie-database-api.git
   ```
2. **Navigate to Project Directory:** Change your current directory to the project directory.

   ```bash
   cd movie-database-api
   ```
3. Copy the .env.sample file and rename it to .env:
   ```bash
   cp .env.sample .env
   ```
   Open the .env file and fill in the configuration variables according to your local environment. Make sure to provide values for the following variables:
   ```bash
   POSTGRES_HOST=<PostgreSQL database host>
   POSTGRES_DB=<PostgreSQL database name>
   POSTGRES_USER=<PostgreSQL database user>
   POSTGRES_PASSWORD=<PostgreSQL database password>
   API_KEY=<Your OMDB API key>
   ```

4. **Build Docker Container:** Build the Docker container using Docker Compose.

   ```bash
   docker-compose build
   ```
5. **Start Docker Containers:** Start the Docker containers in detached mode.
   ```bash
   docker-compose up -d
   ```
6. **Run Database Migrations:** Run database migrations to create necessary tables.

   ```bash
   docker-compose exec app python manage.py migrate
   ```
7. **Fetch Movies:** Populate the database with movie information using the OMDB API.

   ```bash
   docker-compose exec app python manage.py fetch_movies
   ```
8. **Access API Endpoints:** The API is now accessible. You can use tools like Postman or curl to interact with the API endpoints.

## API Endpoints
The following endpoints are available:

* `GET /api/movies/`: Retrieve a list of all movies. You can filter the movies by year, director name, and actor name by providing the corresponding query parameters:
   * `year`: Filter movies by release year.
   * `director_name`: Filter movies by director name.
   * `actor_name`: Filter movies by actor name.

   Example usage: `/api/movies/?year=2005&director_name=Christopher Nolan&actor_name=Leonardo DiCaprio`
* `GET /api/movies/<id>/`: Retrieve details of a specific movie.
* `GET /api/directors/`: Retrieve a list of all directors.
* `GET /api/directors/<id>/`: Retrieve details of a specific director.
* `GET /api/actors/`: Retrieve a list of all actors.
* `GET /api/actors/<id>/`: Retrieve details of a specific actor.

## Authentication and Authorization

The API supports user registration and authentication using JWT tokens. Only administrators have permission to manage movies, while regular users can only view movie information.
## Contributing
Contributions to the Movie Database project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Be sure to follow the contribution guidelines outlined in the repository.


## Acknowledgments
We would like to express our gratitude to the creators of Django, OMDB API, and other open-source projects that made this project possible.

## Contact
For any inquiries or feedback, please contact us at deniskomandyr@gmail.com. I'd love to hear from you!

Enjoy exploring the Movie Manager! 🎬🍿

