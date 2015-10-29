import time

class Actor:

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

class Movie:

    def __init__(self, id, title, release_date, rating):
        self._id = id
        self._title = title
        self._release_date = release_date
        self._rating = rating

    def get_title(self):
        return self._title

    def get_release_date(self):
        return self._release_date

    def get_rating(self):
        return self._rating

class MoviePart:

    def __init__(self, movie, character_name):
        self._movie = movie
        self._character_name = character_name

    def get_movie_title(self):
        return self._movie.get_title()

    def get_movie_year(self):
        release_date = self._movie.get_release_date()
        return release_date.split('-')[0]

    def get_movie_rating(self):
        return self._movie.get_rating()

    def get_character_name(self):
        return self._character_name

    def is_future_part(self):
        release_date = self._movie.get_release_date()
        return release_date > time.strftime('%Y-%m-%d')