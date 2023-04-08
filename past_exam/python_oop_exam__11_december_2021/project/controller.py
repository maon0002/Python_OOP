from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar,
                       "SportsCar": SportsCar, }

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in Controller.VALID_CAR_TYPES:
            if [c for c in self.cars if c.model == model]:
                raise Exception(f"Car {model} is already created!")
            # curr_car_type = next(filter(lambda c: c.type == car_type, self.cars))
            self.cars.append(Controller.VALID_CAR_TYPES[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if [d for d in self.drivers if d.name == driver_name]:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if [r for r in self.races if r.name == race_name]:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = [d for d in self.drivers if d.name == driver_name][0]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken][-1]
        if not car:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car:
            driver_taken_car = driver.car
            driver_taken_car.is_taken = False
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {driver_taken_car.model} to {car.model}."
        else:
            if not car.is_taken:
                driver.car = car
                car.is_taken = True
                return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = [r for r in self.races if r.name == race_name][0]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        driver = [d for d in self.drivers if d.name == driver_name][0]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = driver.car
        if not car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if [r for r in self.races if driver in r.drivers]:
            return f"Driver {driver_name} is already added in {race_name} race."
        if race and driver and car:
            race.drivers.append(driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name][0]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # participated_drivers = [d for d in race.drivers]
        # participated_cars = [d for d in race.drivers]
        participated_drivers_and_cars_dict = dict()
        for driver in race.drivers:
            participated_drivers_and_cars_dict[driver] = driver.car.speed_limit

        sorted_drivers_and_cars_dict = sorted(participated_drivers_and_cars_dict.items(), key=lambda x: -x[1])[0:3]
        # print(sorted_drivers_and_cars_dict)

        race_result = []
        for pair in sorted_drivers_and_cars_dict:
            driver_name = pair[0].name
            car_speed = pair[1]
            pair[0].number_of_wins += 1
            race_result.append(f"Driver {driver_name} wins the {race_name} race with a speed of {car_speed}.")
        return "\n".join([line for line in race_result])



controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]