from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_UNITS_WHEN_BREATHING = 15

    def get_initial_units_of_oxygen(self):
        return 90


# maon = Meteorologist("Maon", 10)
# print(maon.name)
# print(maon.oxygen)
# maon.breathe()
# print(maon.oxygen)
# maon.increase_oxygen(10)
# print(maon.oxygen)