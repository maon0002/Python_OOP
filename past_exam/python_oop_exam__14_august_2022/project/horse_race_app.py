from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def _find_horse(self, horse_name):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

    def _find_jockey(self, jockey_name):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        self._find_horse(horse_name)
        if horse_type in HorseRaceApp.VALID_HORSE_TYPES.keys():
            self.horses.append(HorseRaceApp.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed))
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        self._find_jockey(jockey_name)
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey_obj = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse_obj = next(filter(lambda h: h.is_taken == False and h.__class__.__name__ == horse_type, self.horses))
        except StopIteration:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey_obj.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey_obj.horse = horse_obj
        horse_obj.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse_obj.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        if race_type not in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} could not be found!")
        try:
            jockey_obj = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey_obj.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        # if jockey_obj in [h.jockeys for h in self.horse_races if h.race_type == race_type]:
        if jockey_obj in [j for j in race.jockeys]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey_obj)  # TODO check if works properly

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if race_type not in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} could not be found!")
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races))
        if len([j for j in race.jockeys]) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = None
        winners_speed = 0
        winner_horse_name = None
        for jockey in race.jockeys:
            # print(jockey.horse.speed)
            # print(jockey.name)
            # print(jockey.horse.name)
            if jockey.horse.speed > winners_speed:
                winner = jockey.name
                winners_speed = jockey.horse.speed
                winner_horse_name = jockey.horse.name

        return f"The winner of the {race_type} race, with a speed of {winners_speed}km/h is {winner}! Winner's horse: {winner_horse_name}."


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))

# print

print(horseRaceApp.start_horse_race("Summer"))
