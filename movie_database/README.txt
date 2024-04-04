Django Movies Database Application
==================================

Description:
------------
This Django application is designed to manage a database of movies. It provides features to add, view, update, and delete movies, along with details such as title, description, director, genre, release date, and user ratings. Additionally, the application allows users to upload cover images for each movie.

Requirements:
-------------
- Pillow (for image processing, install via pip)

Installation:
-------------
1. Clone the repository:
git clone https://github.com/vasilGerchev/Movie_Database_Application_Functionality_Django.git

2. Navigate to the project directory:

3. Apply database migrations:
python manage.py migrate

4. Run the development server:
python manage.py runserver


The application will be accessible at http://localhost:8000/ by default.

Usage:
------
1. Access the admin interface:
- Navigate to http://localhost:8000/admin/
- Login with superuser credentials created during the setup.
- Add, view, update, or delete movies using the provided interface.

2. View movies list:
- Navigate to http://localhost:8000/movies/
- Browse through the list of movies with titles and brief descriptions.

3. Movie details page:
- Click on a movie title to view detailed information about that movie, including description, director, genre, release date, user ratings, and cover image.

Contributing:
--------------
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

