from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    HORSE_MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.is_taken = False

    def train(self):
        self.speed = min(self.speed + 3, self.HORSE_MAX_SPEED)  # TODO check if it works properly
