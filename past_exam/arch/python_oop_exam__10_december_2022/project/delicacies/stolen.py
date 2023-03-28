from delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    STOLEN_PORTION = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, Stolen.STOLEN_PORTION, price)

    def details(self):
        return f"Stolen {self.name}: {Stolen.STOLEN_PORTION}g - {self.price:.2f}lv."
