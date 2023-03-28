from booths.booth import Booth


class PrivateBooth(Booth):
    RESERVATION_PRICE_PER_PERSON = 3.50

    def reserve(self, number_of_people: int):
        price_calculation = number_of_people * PrivateBooth.RESERVATION_PRICE_PER_PERSON
        self.price_for_reservation = price_calculation
        self.is_reserved = True
