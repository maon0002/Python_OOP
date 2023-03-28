from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(1.1, 2.2)

    def test_default_fuel_consumption_correctness(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initialisation(self):
        self.assertEqual(1.1, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(2.2, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_car_wo_enough_fuel_raises_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_car_with_enough_fuel_with_fuel_decrease(self):
        self.vehicle.drive(0.5)
        self.assertEqual(0.4750000000000001, self.vehicle.fuel)

    def test_refuel_car_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_car_correctly_increase_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(1)
        self.assertEqual(1, self.vehicle.fuel)

    def test_correct__str__(self):
        self.assertEqual("The vehicle has 2.2 " +
                         "horse power with 1.1 fuel left and 1.25 fuel consumption", self.vehicle.__str__())
        # or str(self.vehicle)

if __name__ == '__main__':
    main()
