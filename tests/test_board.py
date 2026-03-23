import unittest
from game.board import Board, Space, Property


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board("board.json")

    def test_board_has_9_spaces(self):
        self.assertEqual(self.board.size(), 9)

    def test_first_space_is_go(self):
        self.assertEqual(self.board.get_space(0).name, "GO")

    def test_properties_load_correctly(self):
        for space in self.board.spaces[1:]:
            self.assertIsInstance(space, Property)

    def test_wraps_around(self):
        self.assertEqual(self.board.get_space(9).name, "GO")

    def test_get_brown_properties(self):
        brown = self.board.get_properties_by_colour("Brown")
        self.assertEqual(len(brown), 2)

    def test_normal_rent(self):
        prop = self.board.get_space(1)
        self.assertEqual(prop.rent(all_owned_by_same=False), prop.price)

    def test_doubled_rent(self):
        prop = self.board.get_space(1)
        self.assertEqual(prop.rent(all_owned_by_same=True), prop.price * 2)


if __name__ == "__main__":
    unittest.main()
