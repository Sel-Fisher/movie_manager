# Movie Manager #

Welcome to the Movie Database project! This project aims to provide a comprehensive movie database where users can view, edit, and explore various movie details. The database is populated using the OMDB API, ensuring a vast collection of movie information.

## The content

- [Check it out!](#check-it-out)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Getting started](#getting-started)
- [Endpoints](#api-endpoints)
- [Contact](#contact)

## Check it out!
You can access the deployed version of the [Movie Manager on render.com](https://movie-manager-j72f.onrender.com). Try it out and explore the features by registering a new user or using the provided admin user credentials:

**Admin User Credentials:**

* Email: admin@admin.com
* Password: admin123

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
* **JWT Authentication:** JSON Web Tokens (JWT) are used for user authentication.

## Getting Started
To get started with the Movie Manager, follow these steps:

1. **lone the Repository:** Clone this repository to your local machine.
    
    ```bash 
    git clone https://github.com/Sel-Fisher/movie_manager.git
    ```
2. **Navigate to Project Directory:** Change your current directory to the project directory.

    ```bash 
    cd movie_manager
    ```
3. Copy the .env.sample file and rename it to .env:
    ```bash 
    cp .env.sample .env
    ```
    Open the .env file and fill in the configuration variables according to your local environment. Make sure to provide values for the following variables:

    ```bash 
    API_KEY=API_KEY
    DJANGO_SECRET_KEY=DJANGO_SECRET_KEY
    DJANGO_DEBUG=DJANGO_DEBUG
    DATABASE_URL=DATABASE_URL
    ```
4. **Install Dependencies:** Install project dependencies using pip.

    ```bash 
    pip install -r requirements.txt
    ```

5. **Run Migrations:** Apply database migrations to create necessary tables.

    ```bash 
    python manage.py migrate
    ```
6. **Fetch Movies (Optional):** Populate the database with movie information using the OMDB API.

    ```bash 
    python manage.py fetch_movies
    ```
7. **Run the Server:** Start the Django development server.

    ```bash
    python manage.py runserver
    ```

8. **Access API Endpoints:** The API is now accessible. You can use tools like Postman or curl to interact with the API endpoints.

## API Endpoints

### Authentication
* `POST /api/auth/register/`: Register a new user. Requires providing email, and password in the request body.
* `POST /api/auth/token/`: Obtain a JWT token by providing email and password in the request body.
* `POST /api/auth/token/refresh/`: Refresh an existing JWT token by providing a valid refresh token in the request body.

### Movies
* `GET /api/movies/`: Retrieve a list of all movies. You can filter the movies by year, director name, and actor name by providing the corresponding query parameters:
   * `year`: Filter movies by release year.
   * `director_name`: Filter movies by director name.
   * `actor_name`: Filter movies by actor name.

   Example usage: `/api/movies/?year=2005&director_name=Christopher Nolan&actor_name=Leonardo DiCaprio`
* `GET /api/movies/<id>/`: Retrieve details of a specific movie.

### Directors
* `GET /api/directors/`: Retrieve a list of all directors.
* `GET /api/directors/<id>/`: Retrieve details of a specific director.

### Actors
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

