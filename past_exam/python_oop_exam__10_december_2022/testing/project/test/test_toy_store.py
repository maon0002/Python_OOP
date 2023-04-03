from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self):
        self.toystore = ToyStore()
        self.toystore_one = ToyStore()
        self.toystore_one.toy_shelf = {
            "A": "Toy1",
            "B": "Toy2",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

    def test_if_toy_shelf_is_correct(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toystore.toy_shelf)

    def test_if_shelf_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("Z", "Toy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_if_toy_is_already_in_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toystore_one.add_toy("A", "Toy1")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_if_shelf_is_already_taken_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toystore_one.add_toy("B", "Toy99")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_if_adding_toy_goes_smooth_returns_proper_message(self):
        result = self.toystore_one.add_toy("C", "Toy3")
        self.assertEqual({"A": "Toy1",
                          "B": "Toy2",
                          "C": "Toy3",
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None, },

                         self.toystore_one.toy_shelf)
        self.assertEqual("Toy:Toy3 placed successfully!", result)

    def test_if_removing_from_not_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("Z", "Toy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_if_removing_non_existing_toy_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toystore_one.remove_toy("A", "Toy2")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_when_removing_of_toy_is_successfull_returns_correct_message(self):
        result = self.toystore_one.remove_toy("B", "Toy2")
        self.assertEqual({"A": "Toy1",
                          "B": None,
                          "C": None,
                          "D": None,
                          "E": None,
                          "F": None,
                          "G": None, },

                         self.toystore_one.toy_shelf)
        self.assertEqual("Remove toy:Toy2 successfully!", result)


if __name__ == "__main__":
    main()
