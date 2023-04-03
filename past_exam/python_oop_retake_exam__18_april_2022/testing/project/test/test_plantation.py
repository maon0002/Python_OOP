from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation1 = Plantation(1)
        self.plantation2 = Plantation(3)
        self.plantation2.workers = ["Maon"]
        self.plantation2.plants = {
            "Tomato": 1,
            "Potato": 5
        }

    def test_if_initialization_is_correct(self):
        self.assertEqual(1, self.plantation1.size)
        self.assertEqual({}, self.plantation1.plants)
        self.assertEqual([], self.plantation1.workers)

    def test_if_size_setter_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation1.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_if_size_setter_is_correct(self):
        self.plantation1.size = 1
        self.assertEqual(1, self.plantation1.size)

    def test_when_worker_is_already_hired_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation2.hire_worker("Maon")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_if_worker_is_hired_returns_correct_msg(self):
        result = self.plantation2.hire_worker("Maon2")
        self.assertEqual("Maon2 successfully hired.", result)

    def test_if__len__rewrite_return_correct_len(self):
        self.plantation1.hire_worker("Desi")
        self.plantation1.plants['Desi'] = ['Tomatoes']
        self.assertEqual(self.plantation1.__len__, 1)  # TODO hm...

    def test_when_worker_not_existed_for_planting_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation2.planting("Maon2", "Corn")
        self.assertEqual("Worker with name Maon2 is not hired!", str(ve.exception))

    # def test_if_planting_raises_ve_when_size_si_full(self):
    #     with self.assertRaises(ValueError) as ve:
    #
    #         self.plantation2.size = 1
    #         self.plantation2.planting("Maon", "Corn")
    #     self.assertEqual("The plantation is full!", str(ve.exception))


if __name__ == "__main__":
    main()
