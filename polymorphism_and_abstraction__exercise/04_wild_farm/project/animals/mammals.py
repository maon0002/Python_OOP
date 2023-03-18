from project.animals.animal import Animal
from project.food import Meat, Fruit, Vegetable, Seed


class Mouse(Animal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def gained_weight(self):
        return 0.10

    @property
    def food_that_eats(self):
        return [Fruit, Vegetable]


class Dog(Animal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def gained_weight(self):
        return 0.40

    @property
    def food_that_eats(self):
        return [Meat]


class Cat(Animal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def gained_weight(self):
        return 0.30

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]


class Tiger(Animal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def gained_weight(self):
        return 1.00

    @property
    def food_that_eats(self):
        return [Meat]
