import collections
from typing import Optional

from Grid import Grid
from PriorityQueue import PriorityQueue
from Tile import Tile, LavaTile


def distance(p1, p2):
    """Returns the "taxicab" distance between two points"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_shortest_path(grid: Grid) -> dict:
    """Uses A* to calculate the shortest path from player to key.
    Raises AssertionError if no path was found."""
    start = grid.get_tile(grid.player_coord)
    destination = grid.get_tile(grid.key_coord)
    done = collections.deque()  # FIFO queue
    to_do = PriorityQueue()
    to_do.append((0, start))
    previous = dict()

    while len(to_do) > 0:
        item = to_do.pop()
        current: Tile = item[1]
        if current == destination:
            return previous

        coord: [int, int] = current.coord
        next_coords = [
            (coord[0] - 1, coord[1]),
            (coord[0] + 1, coord[1]),
            (coord[0], coord[1] - 1),
            (coord[0], coord[1] + 1)
        ]
        neighbors: list[Optional[Tile]] = [grid.get_tile(c) for c in next_coords]

        for neighbor in neighbors:
            if neighbor is None or type(neighbor) is LavaTile:
                continue

            # Skip already handled tiles
            if done.__contains__(neighbor):
                continue

            # Skip tiles that are already waiting to be handled,
            # if they have a lower associated cost in the "to_do" list
            if to_do.is_in_with_lower_prio((neighbor.heuristic, neighbor)):
                continue

            distance_from_start = current.cost + 1
            # This new path is better
            if distance_from_start < neighbor.cost:
                previous[neighbor] = current
                neighbor.cost = distance_from_start
                neighbor.heuristic = (neighbor.cost
                                      + distance(neighbor.coord, destination.coord))
                to_do.append((neighbor.heuristic, neighbor))

        # Done with the current tile
        done.append(current)

    raise AssertionError("could not find path")
