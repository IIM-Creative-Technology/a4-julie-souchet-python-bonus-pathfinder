import random
from typing import Optional, Dict

from Tile import Tile, LavaTile, PlayerTile, KeyTile, FloorTile


class Grid:
    def __init__(self, size=6):
        self.size = size
        self.tiles: list[list[Tile]] = []
        # Generate random grid
        for x in range(size):
            line = []
            for y in range(size):
                rand = random.randint(0, 3)
                if rand == 0:
                    tile = LavaTile((x, y))
                else:
                    tile = FloorTile((x, y))

                line.append(tile)
            self.tiles.append(line)

        # Add player at random position
        is_free = False
        rand = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        while not is_free:
            rand = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            is_free = self.is_free(rand)
        self.set_tile(rand, PlayerTile(rand))
        self.player_coord = rand
        print(f"{self.get_tile(rand)}: {rand}")

        # Add key at random position
        is_free = False
        rand = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
        while not is_free:
            rand = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            is_free = self.is_free(rand)
        self.set_tile(rand, KeyTile(rand))
        self.key_coord = rand
        print(f"{self.get_tile(rand)}: {rand}")

    def __str__(self):
        separator = "\n"
        for n in range(self.size):
            separator += "-----"
        separator += "\n"

        string = separator
        for line in range(self.size):
            string += " "
            for column in range(self.size):
                game_object = self.tiles[column][line]
                string += game_object.__str__() + " | "
            string += separator
        return string

    def get_tile(self, coord) -> Optional[Tile]:
        if not (0 <= coord[0] < self.size
                and 0 <= coord[1] < self.size):
            return None
        return self.tiles[coord[0]][coord[1]]

    def set_tile(self, coord: [int, int], tile: Tile):
        self.tiles[coord[0]][coord[1]] = tile

    def is_free(self, coord: [int, int]):
        tile = self.get_tile(coord)
        return tile is not None and type(tile) is FloorTile

    def draw_path(self, path: Dict):
        player = self.get_tile(self.player_coord)
        prev = self.get_tile(self.key_coord)
        while prev != player:
            current = path.get(prev)
            # Get movement direction
            if prev.coord[0] == current.coord[0] - 1:
                direction = "⬅"
            elif prev.coord[0] == current.coord[0] + 1:
                direction = "➡"
            elif prev.coord[1] == current.coord[1] - 1:
                direction = "⬆"
            else:
                direction = "⬇"
            # Write the direction on the grid
            self.get_tile(current.coord).symbol = direction
            # print(f"{prev.coord}{direction}{current.coord}")
            # Go forward
            prev = current
        # Restore player symbol
        player.symbol = "🧝‍"+player.symbol
