from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    # OXYGEN_UNITS_WHEN_BREATHING = 5

    def get_initial_units_of_oxygen(self):
        return 50


# maon = Geodesist("Maon", 10)
# print(maon.name)
# print(maon.oxygen)
# maon.breathe()
# print(maon.oxygen)
# maon.increase_oxygen(10)
# print(maon.oxygen)