from booths.booth import Booth


class OpenBooth(Booth):
    RESERVATION_PRICE_PER_PERSON = 2.50

    def reserve(self, number_of_people: int):
        price_calculation = number_of_people * OpenBooth.RESERVATION_PRICE_PER_PERSON
        self.price_for_reservation = price_calculation
        self.is_reserved = True
