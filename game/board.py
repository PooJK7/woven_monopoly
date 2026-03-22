from game.utils import load_json


class Space:
    def __init__(self, data):
        self.name = data["name"]
        self.type = data["type"]

    def __repr__(self):
        return f"Space({self.name})"


class Property(Space):
    def __init__(self, data):
        super().__init__(data)
        self.price = data["price"]
        self.colour = data["colour"]
        self.owner = None

    def rent(self, all_owned_by_same):
        if all_owned_by_same:
            return self.price * 2
        return self.price

    def __repr__(self):
        return f"Property({self.name}, ${self.price}, {self.colour})"


class Board:
    def __init__(self, path="board.json"):
        self.spaces = self._load(path)

    def _load(self, path):
        data = load_json(path)
        spaces = []
        for item in data:
            if item["type"] == "property":
                spaces.append(Property(item))
            else:
                spaces.append(Space(item))
        return spaces

    def size(self):
        return len(self.spaces)

    def get_space(self, position):
        return self.spaces[position % self.size()]

    def get_properties_by_colour(self, colour):
        return [s for s in self.spaces if isinstance(s, Property) and s.colour == colour]
