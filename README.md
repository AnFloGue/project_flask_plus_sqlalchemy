# MovieWeb App

## Overview

MovieWeb App is a web application that allows users to manage their favorite movies. Users can add, update, and delete movies from their list. The application uses Flask for the web framework and SQLAlchemy for database interactions with SQLite.

## Endpoints

### Home
- **URL**: `/`
- **Method**: GET
- **Description**: Renders the home page.

### List Users
- **URL**: `/users`
- **Method**: GET
- **Description**: Lists all users.

### User Movies
- **URL**: `/users/movies`
- **Method**: GET
- **Description**: Lists movies for a specific user if `user_id` is provided, otherwise lists all movies.

### Add User
- **URL**: `/add_user`
- **Methods**: GET, POST
- **Description**: Renders a form to add a new user and handles the form submission.

### Add Movie
- **URL**: `/add_movie`
- **Methods**: GET, POST
- **Description**: Renders a form to add a new movie and handles the form submission.

### Update Movie
- **URL**: `/users/<int:user_id>/update_movie/<int:movie_id>`
- **Methods**: GET, POST
- **Description**: Renders a form to update an existing movie and handles the form submission.

### Delete Movie
- **URL**: `/users/<int:user_id>/delete_movie/<int:movie_id>`
- **Method**: GET
- **Description**: Deletes a specific movie.

### Error Handling

#### 404 Error
- **URL**: Any non-existent route
- **Method**: GET
- **Description**: Displays a custom 404 error page.