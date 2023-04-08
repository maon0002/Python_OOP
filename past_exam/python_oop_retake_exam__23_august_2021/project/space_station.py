from typing import List

from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }
    number_of_successful_missions = 0
    number_of_not_successful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."
        if astronaut_type not in SpaceStation.VALID_ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")
        # astronaut_obj =
        self.astronaut_repository.add(SpaceStation.VALID_ASTRONAUT_TYPES[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."
        planet_obj = Planet(name)
        self.planet_repository.add(planet_obj)
        planet_obj.items.extend(items.split(", "))  # [str(i) for i in items.split(", ")])
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        astronaut_picks = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        # print(astronaut_picks)
        if not astronaut_picks:
            raise Exception("You need at least one astronaut to explore the planet!")
        sorted_astronauts_by_oxygen_lvl = sorted(astronaut_picks, key=lambda a: -a.oxygen)
        # print(sorted_astronauts_by_oxygen_lvl)
        final_astronaut_selection = []
        if len(sorted_astronauts_by_oxygen_lvl) > 5:
            final_astronaut_selection = sorted_astronauts_by_oxygen_lvl[0:5]
        else:
            final_astronaut_selection = sorted_astronauts_by_oxygen_lvl
        # print(*final_astronaut_selection, sep="\n")
        # print(planet.items)
        astronauts_participated_in_collection = 0
        for a in final_astronaut_selection:
            astronauts_participated_in_collection += 1
            for i in range(len(planet.items)):
                if a.oxygen < 1:
                    break
                item = planet.items.pop()
                # print(item)
                a.backpack.append(item)
                # a.backpack.append(planet.items.pop())
                a.breathe()
                # print(a.backpack)
                # print(a.oxygen)
        # print(planet.items)

        if planet.items:
            SpaceStation.number_of_not_successful_missions += 1
            return "Mission is not completed."

        SpaceStation.number_of_successful_missions += 1
        return f"Planet: {planet_name} was explored. {len(final_astronaut_selection)} astronauts participated in collecting items."
        # return f"Planet: {planet_name} was explored. {astronauts_participated_in_collection} astronauts participated in collecting items."

    def report(self, ):
        result = [f"{SpaceStation.number_of_successful_missions} successful missions!\n"
                  f"{SpaceStation.number_of_not_successful_missions} missions were not completed!\n"
                  f"Astronauts' info:"]

        for a in self.astronaut_repository.astronauts:
            info_to_append = [f"Name: {a.name}\n"
                              f"Oxygen: {a.oxygen}\n"
                              f"Backpack items: {', '.join(a.backpack) if a.backpack else 'none'}"]

            result.extend(info_to_append)
        return "\n".join(str(r) for r in result)

#
# babylon5 = SpaceStation()
# print(babylon5.add_astronaut("Biologist", "Plant"))
# print(babylon5.add_astronaut("Geodesist", "Geo"))
# print(babylon5.add_astronaut("Meteorologist", "Meteo"))
# for a in [a for a in babylon5.astronaut_repository.astronauts]:
#     print(a.name)
#     print(a.oxygen)
#     a.breathe()
#     print(a.oxygen)
#     a.increase_oxygen(7)
#     print(a.oxygen)
#     print(str(a.get_initial_units_of_oxygen))
# print(babylon5.add_planet("Mars", "1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23"))
#
# for p in [p for p in babylon5.planet_repository.planets]:
#     print(p.name)
#     print(p.items)
#
# print(babylon5.add_planet("Mars", "Hammer, Xbox, Socks"))
# print(babylon5.retire_astronaut("Meteo"))
# # print(babylon5.retire_astronaut("Maon4o"))
# babylon5.recharge_oxygen()
# # print(babylon5.add_astronaut("Meteorologist", "Meteo Jr."))
# for a in [a for a in babylon5.astronaut_repository.astronauts]:
#     print(a.name)
#     print(a.oxygen)
#     print(str(a.get_initial_units_of_oxygen))
#
# # print(babylon5.add_astronaut("Biologist", "Plant2"))
# # print(babylon5.add_astronaut("Biologist", "Plant3"))
# # print(babylon5.add_astronaut("Geodesist", "Geo2"))
# # print(babylon5.add_astronaut("Geodesist", "Geo3"))
# # print(babylon5.add_astronaut("Meteorologist", "Meteo Sr"))
# # print(babylon5.add_astronaut("Meteorologist", "Meteo Sr2"))
# print(babylon5.send_on_mission("Mars"))
# print(babylon5.report())
