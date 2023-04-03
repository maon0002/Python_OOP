from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookStore(TestCase):
    def setUp(self) -> None:
        self.bookstore1 = Bookstore(10)
        self.bookstore2 = Bookstore(20)
        self.bookstore2.availability_in_store_by_book_titles = {
            "Pooh": 1,
            "Vinetu": 2,
        }
        # self.bookstore2.total_sold_books = 3

    def test_initialization(self):
        self.assertEqual(20, self.bookstore2.books_limit)
        self.assertEqual({
            "Pooh": 1,
            "Vinetu": 2,
        }, self.bookstore2.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore1.total_sold_books)

    def test_if_books_limit_value_under_zero_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore1.books_limit = -1
        self.assertEqual("Books limit of -1 is not valid", str(ve.exception))

    def test_if_books_limit_setter_sets_correct_value(self):
        self.bookstore1.books_limit = 1
        self.assertEqual(1, self.bookstore1.books_limit)

    def test_if__len__method_returns_correct_length(self):
        self.assertEqual(3, self.bookstore2.__len__())

    def test_if_receiving_book_with_exceeding_limit_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore2.availability_in_store_by_book_titles = {
                "Pooh": 1,
                "Vinetu": 19,
            }
            self.bookstore2.receive_book("Oceola", 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_if_enough_space_in_bookstore_returns_correct_msg(self):
        result = self.bookstore2.receive_book("Oceola", 17)
        self.assertEqual(
            {
                "Pooh": 1,
                "Vinetu": 2,
                "Oceola": 17,
            }, self.bookstore2.availability_in_store_by_book_titles
        )
        self.assertEqual("17 copies of Oceola are available in the bookstore.", result)

    def test_if_book_doesnt_exist_calling_sell_books_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore2.sell_book("Maon", 2)
        self.assertEqual("Book Maon doesn't exist!", str(ex.exception))

    def test_if_books_dont_have_enough_copies_for_selling_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore2.sell_book("Pooh", 2)
        self.assertEqual("Pooh has not enough copies to sell. Left: 1", str(ex.exception))

    def test_when_successfully_selling_book_returns_correct_msg(self):
        result = self.bookstore2.sell_book("Vinetu", 1)
        self.assertEqual(
            {
                "Pooh": 1,
                "Vinetu": 1,
            }, self.bookstore2.availability_in_store_by_book_titles
        )
        self.assertEqual(1, self.bookstore2.total_sold_books)
        self.assertEqual("Sold 1 copies of Vinetu", result)

    def test_if__str__representation_works_correctly(self):
        self.bookstore2.sell_book("Vinetu", 2)
        self.bookstore2.receive_book("Oceola", 17)
        result = self.bookstore2.__str__()
        self.assertEqual(
            f"Total sold books: 2\n"
            f"Current availability: 18\n"
            f" - Pooh: 1 copies\n"
            f" - Vinetu: 0 copies\n"
            f" - Oceola: 17 copies", result
        )


if __name__ == "__main__":
    main()
