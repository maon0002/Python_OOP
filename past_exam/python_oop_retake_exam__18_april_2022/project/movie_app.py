from typing import List

from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        if username not in [u.username for u in self.users_collection]:
            self.users_collection.append(User(username, age))
            return f"{username} registered successfully."
        else:
            raise Exception(f"User already exists!")

    def upload_movie(self, username: str, movie: Movie):
        try:
            user = next(filter(lambda u: u.username == username, self.users_collection))
        except StopIteration:
            raise Exception(f"This user does not exist!")

        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in [m for m in self.movies_collection]:  # and movie in [m for m in user.movies_owned]:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for pair in kwargs.items():
            attribute = pair[0]
            new_value = pair[1]
            movie.__setattr__(attribute, new_value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie in [m for m in user.movies_owned]:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in [m for m in user.movies_liked]:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie not in [m for m in user.movies_liked]:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        sorted_movies = sorted([m for m in self.movies_collection], key=lambda x: (-x.year, x.title))
        return "\n".join([m.details() for m in sorted_movies] if sorted_movies else 'No movies found.')

    def __str__(self):
        first_line = f"All users: {', '.join([u.username for u in self.users_collection] if self.users_collection else 'All users: No users.')}"
        second_line = f"All movies: {', '.join([m.title for m in self.movies_collection] if self.movies_collection else 'All movies: No movies.')}"
        return f"{first_line}\n{second_line}"


movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))

user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))

print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))

user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)

print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.dislike_movie('Martin', movie2))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())
print(movie_app)
