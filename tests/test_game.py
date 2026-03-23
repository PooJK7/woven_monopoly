import unittest
from game.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("board.json")

    def test_four_players(self):
        self.assertEqual(len(self.game.players), 4)

    def test_player_names(self):
        names = [p.name for p in self.game.players]
        self.assertEqual(names, ["Peter", "Billy", "Charlotte", "Sweedal"])

    def test_players_start_with_16(self):
        for player in self.game.players:
            self.assertEqual(player.balance, 16)

    def test_players_start_on_go(self):
        for player in self.game.players:
            self.assertEqual(player.position, 0)

    def test_normal_rent(self):
        prop = self.game.board.get_space(1)
        prop.owner = self.game.players[0]
        rent = self.game.get_rent(prop)
        self.assertEqual(rent, prop.price)

    def test_doubled_rent_when_full_colour_owned(self):
        brown = self.game.board.get_properties_by_colour("Brown")
        for prop in brown:
            prop.owner = self.game.players[0]
        rent = self.game.get_rent(brown[0])
        self.assertEqual(rent, brown[0].price * 2)

    def test_game_1_winner(self):
        self.game.play("rolls_1.json")
        winner = max(self.game.players, key=lambda p: p.balance)
        self.assertEqual(winner.name, "Peter")

    def test_game_2_winner(self):
        self.game = Game("board.json")
        self.game.play("rolls_2.json")
        winner = max(self.game.players, key=lambda p: p.balance)
        self.assertEqual(winner.name, "Charlotte")


if __name__ == "__main__":
    unittest.main()
