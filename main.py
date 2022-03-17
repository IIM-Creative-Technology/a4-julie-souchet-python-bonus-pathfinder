from Grid import Grid
from path_finding import get_shortest_path

if __name__ == '__main__':
    grid = Grid(4)
    print("\nProblem:")
    print(grid)

    try:
        path = get_shortest_path(grid)
        grid.draw_path(path)
        print("Solution:")
        print(grid)

    except AssertionError:
        print("Could not find a path!!")

