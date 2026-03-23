import unittest
from game.player import Player
from game.board import Property


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Peter")
        self.other = Player("Billy")

    def test_starts_with_16_dollars(self):
        self.assertEqual(self.player.balance, 16)

    def test_starts_on_go(self):
        self.assertEqual(self.player.position, 0)

    def test_moves_correctly(self):
        self.player.move(3, 9)
        self.assertEqual(self.player.position, 3)

    def test_passes_go(self):
        self.player.position = 7
        passed_go = self.player.move(4, 9)
        self.assertTrue(passed_go)

    def test_buys_property(self):
        prop = Property({"name": "The Burvale", "type": "property", "price": 1, "colour": "Brown"})
        self.player.buy(prop)
        self.assertEqual(self.player.balance, 15)
        self.assertEqual(prop.owner, self.player)

    def test_pays_rent(self):
        self.player.pay_rent(3, self.other)
        self.assertEqual(self.player.balance, 13)
        self.assertEqual(self.other.balance, 19)

    def test_goes_bankrupt(self):
        self.player.balance = -1
        self.assertTrue(self.player.is_bankrupt())


if __name__ == "__main__":
    unittest.main()
