from window import Window
from line import Line
from point import Point
from cell import Cell
import random


def main():
    print("Build a Maze Solver")

    maze = Window(500, 500)

    # lineStuff(maze)
    cellStuff(maze)

    maze.wait()


def lineStuff(maze: Window):
    line1 = Line(Point(0, 0), Point(200, 200))
    line2 = Line(Point(500, 500), Point(400, 400))
    line3 = Line(Point(150, 250), Point(350, 250))
    maze.drawLine(line1, "red")
    maze.drawLine(line2, "blue")
    maze.drawLine(line3, "black")


def cellStuff(maze: Window):

    CELL_SIZE = 40
    GAP = 5
    rows = maze.height // (CELL_SIZE)
    cols = maze.width // (CELL_SIZE)
    # print(f"ROWS: {rows}\nCOLS: {cols}")

    for r in range(rows):
        y = CELL_SIZE * r

        for c in range(cols):
            x = CELL_SIZE * c

            start = Point(x + GAP, y + GAP)
            end = Point(CELL_SIZE + x, CELL_SIZE + y)
            cell = Cell(maze, start, end)
            randomWall(cell)
            cell.draw("black")


def randomWall(cell: Cell):
    cell.walls.top = random.random() > 0.5
    cell.walls.right = random.random() > 0.5
    cell.walls.bottom = random.random() > 0.5
    cell.walls.left = random.random() > 0.5


if __name__ == "__main__":
    main()
