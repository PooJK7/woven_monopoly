from game.board import Board, Property
from game.player import Player


class Game:
    def __init__(self, board_path="board.json"):
        self.board = Board(board_path)
        self.players = [
            Player("Peter"),
            Player("Billy"),
            Player("Charlotte"),
            Player("Sweedal"),
        ]

    def load_rolls(self, rolls_path):
        import json
        with open(rolls_path) as f:
            return json.load(f)

    def get_rent(self, property):
        colour_properties = self.board.get_properties_by_colour(property.colour)
        all_owned_by_same = all(p.owner == property.owner for p in colour_properties)
        if all_owned_by_same:
            return property.price * 2
        return property.price

    def play(self, rolls_path):
        rolls = self.load_rolls(rolls_path)
        roll_index = 0

        while roll_index < len(rolls):
            for player in self.players:
                if roll_index >= len(rolls):
                    break

                roll = rolls[roll_index]
                roll_index += 1

                passed_go = player.move(roll, self.board.size())
                if passed_go:
                    player.balance += 1
                    print(f"{player.name} passed GO, collected $1")

                space = self.board.get_space(player.position)
                print(f"{player.name} rolled {roll} and landed on {space.name}")

                if isinstance(space, Property):
                    if space.owner is None:
                        player.buy(space)
                        print(f"{player.name} bought {space.name} for ${space.price}")
                    elif space.owner != player:
                        rent = self.get_rent(space)
                        player.pay_rent(rent, space.owner)
                        print(f"{player.name} paid ${rent} rent to {space.owner.name}")

                        if player.is_bankrupt():
                            print(f"\n{player.name} is bankrupt!")
                            self.print_results()
                            return

        self.print_results()

    def print_results(self):
        print("\n--- Final Results ---")
        for player in self.players:
            space = self.board.get_space(player.position)
            print(f"{player.name}: ${player.balance} on {space.name}")

        winner = max(self.players, key=lambda p: p.balance)
        print(f"\nWinner: {winner.name} with ${winner.balance}")
