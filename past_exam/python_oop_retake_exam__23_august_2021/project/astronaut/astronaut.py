from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_UNITS_WHEN_BREATHING = 10

    def __init__(self, name: str, oxygen: int = 0):
        self.name = name
        self.oxygen = oxygen + self.get_initial_units_of_oxygen()
        self.backpack = []

    @property
    @abstractmethod
    def get_initial_units_of_oxygen(self):
        pass

    # @property
    # def get_oxygen_units_when_breathing(self):
    #     return 10

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.OXYGEN_UNITS_WHEN_BREATHING
        # self.oxygen -= self.get_oxygen_units_when_breathing

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def __repr__(self):
        return f"Astr name is: {self.name}, Astr oxygen is: {self.oxygen} and the astr backpack contains: {self.backpack}"
