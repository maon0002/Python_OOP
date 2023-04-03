from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    HORSE_MAX_SPEED = 120

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)
        self.is_taken = False

    def train(self):
        self.speed = min(self.speed + 2, self.HORSE_MAX_SPEED)
