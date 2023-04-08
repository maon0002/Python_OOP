from project.car.car import Car


class SportsCar(Car):
    MIN_SPEED_LIMIT = 400
    MAX_SPEED_LIMIT = 600 + 1

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)
        self.is_taken = False
