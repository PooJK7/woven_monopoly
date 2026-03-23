import unittest
from game.player import Player
from game.board import Property


class TestPlayer(unittest.TestCase):

    def setUp(self):
        # Create fresh players before each test
        self.player = Player("Peter")
        self.other = Player("Billy")

    def test_starts_with_16_dollars(self):
        self.assertEqual(self.player.balance, 16)

    def test_starts_on_go(self):
        self.assertEqual(self.player.position, 0)

    def test_moves_correctly(self):
        # Player should move to the new position after a roll
        self.player.move(3, 9)
        self.assertEqual(self.player.position, 3)

    def test_passes_go(self):
        self.player.position = 7
        passed_go = self.player.move(4, 9)
        self.assertTrue(passed_go)

    def test_buys_property(self):
        # Buying a property deducts money and set ownership
        prop = Property({"name": "The Burvale", "type": "property", "price": 1, "colour": "Brown"})
        self.player.buy(prop)
        self.assertEqual(self.player.balance, 15)
        self.assertEqual(prop.owner, self.player)

    def test_pays_rent(self):
        # Paying rent should transfer money from payer to the owner
        self.player.pay_rent(3, self.other)
        self.assertEqual(self.player.balance, 13)
        self.assertEqual(self.other.balance, 19)

    def test_goes_bankrupt(self):
        # Negative balance means the player is bankrupt
        self.player.balance = -1
        self.assertTrue(self.player.is_bankrupt())


if __name__ == "__main__":
    unittest.main()
