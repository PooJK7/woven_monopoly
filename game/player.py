class Player:
    """Represents a player in the game"""

    def __init__(self, name, starting_balance=16):
        self.name = name
        self.balance = starting_balance
        self.position = 0
        self.properties = []

    def move(self, steps, board_size):
        """Move the player by a number of steps, returning True if they passed GO."""
        old_position = self.position
        self.position = (self.position + steps) % board_size

        # Passed GO if the new position is less than the old or if steps carried past the end
        passed_go = (old_position + steps) >= board_size
        return passed_go

    def buy(self, property):
        """Buy a property, deducting the price from the player's balance"""
        self.balance -= property.price
        property.owner = self
        self.properties.append(property)

    def pay_rent(self, amount, owner):
        """Pay rent to another player"""
        self.balance -= amount
        owner.balance += amount

    def is_bankrupt(self):
        return self.balance < 0

    def __repr__(self):
        return f"Player({self.name}, ${self.balance}, position={self.position})"
