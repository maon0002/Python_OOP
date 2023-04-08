from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.lyb = Library("Lyb1")

    def test_initialization(self):
        self.assertEqual("Lyb1", self.lyb.name)
        self.assertEqual({}, self.lyb.books_by_authors)
        self.assertEqual({}, self.lyb.readers)

    def test_if_give_empty_string_as_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.lyb.name = ""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_if_add_book_with_new_author_works(self):
        self.lyb.books_by_authors = {
            "Maon": [],
        }
        self.lyb.add_book("Not Maon", "Title")
        self.assertEqual({
            "Maon": [],
            "Not Maon": ["Title"]
        }, self.lyb.books_by_authors)

    def test_if_add_book_with_existed_author_works(self):
        self.lyb.books_by_authors = {
            "Maon": [],
        }
        self.lyb.add_book("Maon", "Title")
        self.assertEqual({
            "Maon": ["Title"],
        }, self.lyb.books_by_authors)

    def test_if_reader_not_existed_add_record(self):
        self.lyb.readers = {
            "Maon": []
        }
        self.lyb.add_reader("Maon2")
        self.assertEqual({
            "Maon": [],
            "Maon2": [],
        }, self.lyb.readers)

    def test_if_adding_existed_reader_returns(self):
        self.lyb.readers = {
            "Maon": []
        }
        result = self.lyb.add_reader("Maon")
        self.assertEqual(f"Maon is already registered in the Lyb1 library.", result)

    def test_when_rent_book_reader_not_registered_returns(self):
        self.lyb.readers = {
            "Maon": []
        }
        result = self.lyb.rent_book("Maon2", "Valsar", "Title")
        self.assertEqual("Maon2 is not registered in the Lyb1 Library.", result)

    def test_when_rent_book_author_not_existed_returns(self):
        self.lyb.readers = {
            "Maon2": []
        }
        self.lyb.books_by_authors = {
            "Maon": [],
        }
        result = self.lyb.rent_book("Maon2", "Valsar", "Title")
        self.assertEqual("Lyb1 Library does not have any Valsar's books.", result)

    def test_when_rent_book_title_not_exist_returns(self):
        self.lyb.readers = {
            "Maon2": []
        }
        self.lyb.books_by_authors = {
            "Valsar": ["Title2"],
        }
        result = self.lyb.rent_book("Maon2", "Valsar", "Title")
        self.assertEqual('Lyb1 Library does not have Valsar\'s "Title".', result)
        # "Lyb1 Library does not have Valsar's Title."

    def test_when_rent_book_works_correct(self):
        self.lyb.readers = {
            "Maon2": []
        }
        self.lyb.books_by_authors = {
            "Valsar": ["Title", "Title2"],
        }
        self.lyb.rent_book("Maon2", "Valsar", "Title")

        self.assertEqual({'Maon2': [{'Valsar': 'Title'}]}, self.lyb.readers)

        self.assertEqual({
            "Valsar": ["Title2"],
        }, self.lyb.books_by_authors)

        self.lyb.rent_book("Maon2", "Valsar", "Title2")

        self.assertEqual({'Maon2': [{'Valsar': 'Title'}, {'Valsar': 'Title2'}]}, self.lyb.readers)

        self.assertEqual({
            "Valsar": [],
        }, self.lyb.books_by_authors)


if __name__ == "__main__":
    main()
