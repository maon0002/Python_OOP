from typing import List

from booths.booth import Booth
from delicacies.delicacy import Delicacy
from delicacies.gingerbread import Gingerbread
from delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    ALL_DELICACIES_NAMES = []
    VALID_DELICACY_TYPES = [d.__name__ for d in Delicacy.__subclasses__()]

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    # def __find_delicacy(self, delicacy_name: str):
    #     for delicacy in self.delicacies:
    #         if delicacy.name == delicacy_name:
    #             return delicacy

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if [d.name for d in self.delicacies if d.name == name]:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy_subclass = [d.__name__ for d in Delicacy.__subclasses__() if d.__name__ == type_delicacy][0]
        # delicacy_subclass = next(filter(lambda d: d.__name__ == type_delicacy, Delicacy.__subclasses__()))
        class_sel = next(filter(lambda d_class: d_class.__name__ == type_delicacy, Delicacy.__subclasses__()))
        # print(delicacy_subclass.__name__)
        subclass = class_sel.__name__
        new_delicacy = subclass(name, price,)

        self.delicacies.append(new_delicacy)


# print([d.__name__ for d in Delicacy.__subclasses__()])
shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
