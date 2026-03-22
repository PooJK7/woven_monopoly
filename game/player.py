class Player:
    def __init__(self, name, starting_balance=16):
        self.name = name
        self.balance = starting_balance
        self.position = 0
        self.properties = []

    def move(self, steps, board_size):
        old_position = self.position
        self.position = (self.position + steps) % board_size
        passed_go = self.position < old_position or (old_position + steps) >= board_size
        return passed_go

    def buy(self, property):
        self.balance -= property.price
        property.owner = self
        self.properties.append(property)

    def pay_rent(self, amount, owner):
        self.balance -= amount
        owner.balance += amount

    def is_bankrupt(self):
        return self.balance < 0

    def __repr__(self):
        return f"Player({self.name}, ${self.balance}, position={self.position})"
