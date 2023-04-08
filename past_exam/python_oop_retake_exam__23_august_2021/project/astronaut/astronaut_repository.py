from typing import List
from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astronaut = [a for a in self.astronauts if a.name == name]
        if astronaut:
            return astronaut[0]
