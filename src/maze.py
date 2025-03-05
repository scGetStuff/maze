from window import Window
from line import Line
from point import Point
from cell import Cell
import random
import time

# just while building to see cells clearly
GAP = 5


class Maze:
    def __init__(
        self,
        origin: Point,
        rows: int,
        cols: int,
        cellWidth: int,
        cellHeight: int,
        win: Window,
    ):
        self.origin = origin
        self.rows = rows
        self.cols = cols
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.win = win
        self.cells: list[list[Cell]] = []

    def __str__(self) -> str:
        return (
            f"window: {self.win.root.title}\n"
            f"origin: {self.origin}\n"
            f"rows: {self.rows}\n"
            f"cols: {self.cols}\n"
            f"cellWidth: {self.cellWidth}\n"
            f"cellHeight: {self.cellHeight}\n"
        )

    def createCells(self):
        cells: list[list[Cell]] = []

        for r in range(self.rows):
            y = self.origin.y + self.cellHeight * r
            row: list[Cell] = []

            for c in range(self.cols):
                x = self.origin.x + self.cellWidth * c
                start = Point(x + GAP, y + GAP)
                end = Point(self.cellWidth + x, self.cellHeight + y)
                cell = Cell(self.win, start, end)
                row.append(cell)

            cells.append(row)

        self.cells = cells

    # nothing in spec on color
    def drawCells(self, fillColor="black"):
        for row in self.cells:
            for cell in row:
                cell.draw(fillColor)

    def drawCell(self, row: int, col: int, fillColor="black"):
        if not self.cells:
            return
        self.cells[row][col].draw(fillColor)
        self.animate()

    def animate(self):
        self.win.redraw()
        time.sleep(0.5)


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


def randomWalls(cells: list[list[Cell]]):
    for row in cells:
        for cell in row:
            cell.walls.top = random.random() > 0.5
            cell.walls.right = random.random() > 0.5
            cell.walls.bottom = random.random() > 0.5
            cell.walls.left = random.random() > 0.5


def main():

    win = Window(500, 500)
    win.root.title = "Maze test"

    maze = Maze(Point(100, 100), 5, 5, 60, 50, win)
    maze.createCells()
    randomWalls(maze.cells)
    connectCells(maze.cells)
    maze.drawCells()
    maze.drawCell(1, 1, "red")

    print()
    print(maze)
    print(maze.cells)

    win.wait()


if __name__ == "__main__":
    main()
