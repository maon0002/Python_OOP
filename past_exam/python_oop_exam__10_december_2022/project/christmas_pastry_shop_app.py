from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    VALID_BOOTH_TYPES = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")
        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACY_TYPES.keys():
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(ChristmasPastryShopApp.VALID_DELICACY_TYPES[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in ChristmasPastryShopApp.VALID_BOOTH_TYPES.keys():
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(ChristmasPastryShopApp.VALID_BOOTH_TYPES[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        # first_not_reserved_booth = [b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people][0]
        try:
            first_not_reserved_booth = next(
                filter(lambda b: b.is_reserved == False and b.capacity >= number_of_people, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        first_not_reserved_booth.reserve(number_of_people)
        return f"Booth {first_not_reserved_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        if booth_number not in [b.booth_number for b in self.booths]:
            raise Exception(f"Could not find booth {booth_number}!")
        if delicacy_name not in [d.name for d in self.delicacies]:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        bill = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])
        self.income += bill
        for delicacy in booth.delicacy_orders:
            booth.delicacy_orders.remove(delicacy)
        booth.leave()
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

