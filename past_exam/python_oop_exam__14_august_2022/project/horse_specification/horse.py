from abc import ABC, abstractmethod


class Horse(ABC):
    HORSE_MAX_SPEED = 0

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.HORSE_MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        # self.__speed = min(value, self.HORSE_MAX_SPEED)  # TODO check if works
        self.__speed = value

    @abstractmethod
    def train(self):
        pass

    def __repr__(self):
        return f"Horse name is {self.name}, with speed of: {self.speed} and is_taken = {self.is_taken}"