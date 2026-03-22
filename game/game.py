from game.board import Board, Property
from game.player import Player
from game.utils import load_json


class Game:
    def __init__(self, board_path="board.json"):
        self.board = Board(board_path)
        # Players take turns in this order
        self.players = [
            Player("Peter"),
            Player("Billy"),
            Player("Charlotte"),
            Player("Sweedal"),
        ]

    def get_rent(self, property):
        colour_properties = self.board.get_properties_by_colour(property.colour)
        all_owned_by_same = all(p.owner == property.owner for p in colour_properties)
        return property.rent(all_owned_by_same)

    def take_turn(self, player, roll):
        passed_go = player.move(roll, self.board.size())

        # Award $1 for passing GO
        if passed_go:
            player.balance += 1
            print(f"{player.name} passed GO, collected $1")

        space = self.board.get_space(player.position)
        print(f"{player.name} rolled {roll} and landed on {space.name}")

        if isinstance(space, Property):
            if space.owner is None:
                # Property is unowned, player must buy it
                player.buy(space)
                print(f"{player.name} bought {space.name} for ${space.price}")
            elif space.owner != player:
                # if property is owned by another player, pay rent
                rent = self.get_rent(space)
                player.pay_rent(rent, space.owner)
                print(f"{player.name} paid ${rent} rent to {space.owner.name}")

    def is_game_over(self):
        for player in self.players:
            if player.is_bankrupt():
                return player
        return None

    def play(self, rolls_path):
        rolls = load_json(rolls_path)
        roll_index = 0

        while roll_index < len(rolls):
            for player in self.players:
                if roll_index >= len(rolls):
                    break

                roll = rolls[roll_index]
                roll_index += 1

                self.take_turn(player, roll)

                # Check for bankrupt players after each turn
                bankrupt_player = self.is_game_over()
                if bankrupt_player:
                    print(f"\n{bankrupt_player.name} is bankrupt!")
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
