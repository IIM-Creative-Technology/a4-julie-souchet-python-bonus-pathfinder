import sys


class Tile:
    def __init__(self, coord=(0, 0), category="", symbol=""):
        self.coord = coord
        self.category = category
        self.cost = sys.maxsize
        self.heuristic = 0
        self.symbol = symbol

    def __str__(self):
        return self.symbol


class FloorTile(Tile):
    def __init__(self, coord):
        super().__init__(coord, "floor", "⚪")


class LavaTile(Tile):
    def __init__(self, coord):
        super().__init__(coord, "lava", "🔥")


class KeyTile(Tile):
    def __init__(self, coord):
        super().__init__(coord, "key", "🔑")


class PlayerTile(Tile):
    def __init__(self, coord):
        super().__init__(coord, "player", "🧝‍")
        self.cost = 0

    def move(self, coord):
        self.coord = coord
