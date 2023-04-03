from project.movie_specification.movie import Movie


class Thriller(Movie):
    MIN_AGE_RESTRICTION = 16

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.MIN_AGE_RESTRICTION:
            raise ValueError(f"Thriller movies must be restricted for audience under {self.MIN_AGE_RESTRICTION} years!")
        self.__age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
