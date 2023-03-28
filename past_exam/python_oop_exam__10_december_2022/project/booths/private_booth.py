from project.booths.booth import Booth


class PrivateBooth(Booth):
    RESERVATION_PRICE_PER_PERSON = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        calculated_price = self.RESERVATION_PRICE_PER_PERSON * number_of_people
        self.price_for_reservation = calculated_price
        self.is_reserved = True

    def leave(self):
        self.price_for_reservation = 0
        self.is_reserved = False
