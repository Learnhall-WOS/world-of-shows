## Prerequisites
- Docker: Make sure Docker is installed on your machine. You can download it from the official Docker website: https://www.docker.com/get-started
- Docker Compose: Make sure Docker Compose is installed on your machine. You can download it from the official Docker website: https://docs.docker.com/compose/install/

## Getting Started
1. Clone the repository to your local machine.
2. Navigate to the root directory of the project in a terminal or command prompt.
3. Build the Docker image by running the following command:
    ```
    docker build -t wos .
    ```
4. Start the Docker containers by running the following command:
    ```
    docker-compose up
    ```
5. Navigate to `http://localhost:8000` in a web browser to view the Django application.

## Additional Notes
- If you make changes to the code, you will need to rebuild the Docker image and restart the containers for the changes to take effect.
- To stop the Docker containers, press `Ctrl-C` in the terminal or command prompt where the containers are running. To remove the containers, use the `docker-compose down` command.

# Models (base\models.py)

This Django project has five models:

## Theater

The Theater model represents a theater in the database. A Theater object has the following fields:

* `name`: a `CharField` of maximum length 100, representing the name of the theater.
* `user`: a `OneToOneField` to the built-in `User` model, representing the user associated with the theater.

## Genre

The Genre model represents a genre in the database. A Genre object has the following field:

* `name`: a `CharField` of maximum length 50, representing the name of the genre.

## Talent

The Talent model represents a talent in the database. A Talent object has the following field:

* `name`: a `CharField` of maximum length 100, representing the name of the talent.

## Show

The Show model represents a show in the database. A Show object has the following fields:

* `name`: a `CharField` of maximum length 200, representing the name of the show.
* `host`: a `ForeignKey` to the Theater model, representing the theater that is hosting the show.
* `description`: a `TextField` that is nullable and blank, representing a description of the show.
* `genre`: a `ManyToManyField` to the Genre model, representing the genres associated with the show.
* `talent`: a `ManyToManyField` to the Talent model, representing the talents associated with the show.
* `updated`: a `DateTimeField` that auto-updates when the object is updated.
* `created`: a `DateTimeField` that auto-populates with the creation date and time of the object.

## Review

The Review model represents a review in the database. A Review object has the following fields:

* `author`: a `ForeignKey` to the built-in `User` model, representing the user who wrote the review.
* `show`: a `ForeignKey` to the Show model, representing the show being reviewed.
* `text`: a `TextField` representing the text of the review.
* `created`: a `DateTimeField` that auto-populates with the creation date and time of the object.
* `updated`: a `DateTimeField` that auto-updates when the object is updated.

## Relationship between models

* A Theater can have many Shows, but a Show can only have one Theater (one-to-many relationship).
* A Genre can be associated with many Shows, and a Show can be associated with many Genres (many-to-many relationship).
* A Talent can be associated with many Shows, and a Show can be associated with many Talents (many-to-many relationship).
* A User can write many Reviews, and a Review can be written by only one User (one-to-many relationship).
* A Show can have many Reviews, and a Review can be associated with only one Show (one-to-many relationship).
