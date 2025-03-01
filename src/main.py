from window import Window
from line import Line
from point import Point
from cell import Cell
import random

# TODO: make this scale to the grid
WIN_SIZE = (1024, 768)
# need spec
CELL_SIZE = 50
# just while building to see cells clearly
GAP = 5


def main():
    print("Build a Maze Solver")

    maze = Window(*WIN_SIZE)

    # doLineStuff(maze)

    # TODO: this stuff will be Maze class later
    cells = makeCells(maze)
    randomWalls(cells)
    connectCells(cells)
    drawCells(cells)
    cells[7][7].drawMove(cells[9][2], True)

    maze.wait()


def doLineStuff(maze: Window):
    line1 = Line(Point(0, 0), Point(200, 200))
    line2 = Line(Point(500, 500), Point(400, 400))
    line3 = Line(Point(150, 250), Point(350, 250))
    maze.drawLine(line1, "red")
    maze.drawLine(line2, "blue")
    maze.drawLine(line3, "black")


def makeCells(maze: Window) -> list[list[Cell]]:
    rows = maze.height // CELL_SIZE
    cols = maze.width // CELL_SIZE
    # print(f"ROWS: {rows}\nCOLS: {cols}")
    cells: list[list[Cell]] = []

    for r in range(rows):
        y = CELL_SIZE * r
        row: list[Cell] = []

        for c in range(cols):
            x = CELL_SIZE * c
            start = Point(x + GAP, y + GAP)
            end = Point(CELL_SIZE + x, CELL_SIZE + y)
            cell = Cell(maze, start, end)
            row.append(cell)

        cells.append(row)

    return cells


def connectCells(cells: list[list[Cell]]):
    for row in cells:
        # print(f"\n{row}")
        # look ahead 1 cell and match wall state
        for c in range(len(row) - 1):
            cell = row[c]
            next = row[c + 1]
            cell.walls.right = next.walls.left
            if not cell.walls.right:
                cell.drawMove(next)


def drawCells(cells: list[list[Cell]]):
    for row in cells:
        for cell in row:
            cell.draw("black")


def randomWalls(cells: list[list[Cell]]):
    for row in cells:
        for cell in row:
            cell.walls.top = random.random() > 0.5
            cell.walls.right = random.random() > 0.5
            cell.walls.bottom = random.random() > 0.5
            cell.walls.left = random.random() > 0.5


if __name__ == "__main__":
    main()
