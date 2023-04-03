from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver("Name", 10)

    def test_initialization(self):
        self.assertEqual("Name", self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_when_earned_money_is_negative_number_raises_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual("Name went bankrupt.", str(ve.exception))

    def test_when_earned_money_is_positive_number_setter_works_properly(self):
        self.driver.earned_money = 1
        self.assertEqual(1, self.driver.earned_money)

    def test_if_cargo_location_is_already_added_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.driver.available_cargos = {"Location": 20}
            self.driver.add_cargo_offer("Location", 999)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_when_cargo_location_not_existed_is_returned_correct_string(self):
        result = self.driver.add_cargo_offer("Location", 999)
        self.assertEqual({"Location": 999}, self.driver.available_cargos)
        self.assertEqual("Cargo for 999 to Location was added as an offer.", result)

    def test_if_drive_best_cargo_raises_exception_if_no_cargo_in_list(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual("There are no offers available.", result)

    def test_when_drive_best_cargo_offer_is_chosen_returns_correct_message(self):
        self.driver.available_cargos = {"Location1": 20, "Location2": 21}
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("Name is driving 21 to Location2.", result)
        self.assertEqual(210, self.driver.earned_money)
        self.assertEqual(21, self.driver.miles)

    def test_if_all_activities_subtract_proper_amount_of_money(self):

        self.driver.earned_money = 1000000
        self.driver.check_for_activities(150000)
        self.assertEqual(818750, self.driver.earned_money)

    def test_if_eat_subtract_correct_money(self):
        self.driver.earned_money = 21
        self.driver.eat(250)
        self.assertEqual(1, self.driver.earned_money)

    def test_if_sleep_subtract_correct_money(self):
        self.driver.earned_money = 46
        self.driver.sleep(1000)
        self.assertEqual(1, self.driver.earned_money)

    def test_if_pump_gas_subtract_correct_money(self):
        self.driver.earned_money = 501
        self.driver.pump_gas(1500)
        self.assertEqual(1, self.driver.earned_money)

    def test_if_repair_truck_subtract_correct_money(self):
        self.driver.earned_money = 7501
        self.driver.repair_truck(10000)
        self.assertEqual(1, self.driver.earned_money)

    def test_if__repr__returns_correct_message(self):

        self.assertEqual("Name has 0 miles behind his back.", str(self.driver))


if __name__ == "__main__":
    main()
