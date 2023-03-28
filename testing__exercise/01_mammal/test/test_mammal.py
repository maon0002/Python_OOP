from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("name", "type", "sound")

    def test_if_initialisation_is_correct(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)

    def test_if_make_sound_return_correct_message(self):
        self.assertEqual("name makes sound", self.mammal.make_sound())

    def test_if_kingdom_returns_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if_info_returns_correct_message(self):
        self.assertEqual("name is of type type", self.mammal.info())




if __name__ == '__main__':
    main()



