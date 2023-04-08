from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.player = TennisPlayer("Maon", 18, 111.11)
        self.player2 = TennisPlayer("Maon2", 20, 222.22)

    def test_init(self):
        self.assertEqual("Maon", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(111.11, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_if_name_setter_raises_error_when_wrong_len(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "MA"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_if_age_setter_raises_error_after_underage(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_when_add_new_win_not_existed_tournament(self):
        self.player.wins = ["Sofia Open"]
        self.player.add_new_win("Varna Open")
        self.assertEqual(["Sofia Open", "Varna Open"], self.player.wins)

    def test_when_add_new_win_existed_tournament_returns(self):
        self.player.wins = ["Sofia Open"]
        result = self.player.add_new_win("Sofia Open")
        self.assertEqual("Sofia Open has been already added to the list of wins!", result)

    def test_if__lt__overloading_returns_correct_msg_when_true(self):
        self.assertEqual('Maon2 is a top seeded player and he/she is better than Maon',
                         self.player.__lt__(self.player2))

    def test_if__lt__overloading_returns_correct_msg_when_false(self):
        self.assertEqual('Maon2 is a better player than Maon', self.player2.__lt__(self.player))

    def test_if__str__overloading_returns_correct_string(self):
        self.player.wins = ["Sofia Open", "Varna Open"]
        self.assertEqual(
            f"Tennis Player: Maon\n"
            f"Age: 18\n"
            f"Points: 111.1\n"
            f"Tournaments won: Sofia Open, Varna Open",
            self.player.__str__()
        )


if __name__ == "__main__":
    main()
