from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def refuel(self, fuel: float):
        ...


class Car(Vehicle):
    CONDITIONER_FUEL = 0.9

    def drive(self, distance: float) -> None:
        current_consumption = distance * (self.fuel_consumption + Car.CONDITIONER_FUEL)
        if current_consumption <= self.fuel_quantity:
            self.fuel_quantity -= current_consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_FUEL = 1.6
    TRUCK_TANK_CAPACITY = 0.95

    def drive(self, distance: float) -> None:
        current_consumption = distance * (self.fuel_consumption + Truck.CONDITIONER_FUEL)
        if current_consumption <= self.fuel_quantity:
            self.fuel_quantity -= current_consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * Truck.TRUCK_TANK_CAPACITY


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
