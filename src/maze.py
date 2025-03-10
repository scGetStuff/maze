from window import Window
from line import Line
from point import Point
from cell import Cell
import random
import time

# just while building to see all the walls
GAP = 5


class Maze:
    def __init__(
        self,
        origin: Point,
        rows: int,
        cols: int,
        cellWidth: int,
        cellHeight: int,
        win: Window = None,
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
            f"window: {self.win.root.title if self.win else "None"}\n"
            f"origin: {self.origin}\n"
            f"rows: {self.rows}\n"
            f"cols: {self.cols}\n"
            f"cellWidth: {self.cellWidth}\n"
            f"cellHeight: {self.cellHeight}\n"
        )

    # spec has this private and called by constructor, I'm not doing that
    # I want it separate so I can recreate cells if dimentions change
    def createCells(self):
        self.cells: list[list[Cell]] = []

        for r in range(self.rows):
            y = self.origin.y + self.cellHeight * r
            self.cells.append([])

            for c in range(self.cols):
                x = self.origin.x + self.cellWidth * c
                start = Point(x + GAP, y + GAP)
                end = Point(self.cellWidth + x, self.cellHeight + y)
                self.cells[r].append(Cell(self.win, start, end))

                self._drawCell(r, c)

        self._openMaze()

    def _drawCell(self, row: int, col: int, fillColor: str = "black"):
        if not self.win:
            return
        self.cells[row][col].draw(fillColor)
        self._animate()

    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(0.1)

    def _openMaze(self):
        self.cells[0][0].walls.left = False
        self._drawCell(0, 0)

        self.cells[self.rows - 1][self.cols - 1].walls.right = False
        self._drawCell(self.rows - 1, self.cols - 1)

    # TODO: L10 - follow algorithm in the lesson
    def breakRandomWalls(self):
        random.seed(0)

        for r in range(len(self.cells)):
            for c in range(len(self.cells[r])):
                self.cells[r][c].walls.top = random.random() > 0.5
                self.cells[r][c].walls.right = random.random() > 0.5
                self.cells[r][c].walls.bottom = random.random() > 0.5
                self.cells[r][c].walls.left = random.random() > 0.5

                self._drawCell(r, c)


def connectCells(cells: list[list[Cell]]):
    for row in cells:
        # look ahead 1 cell and match wall state
        for c in range(len(row) - 1):
            cell = row[c]
            next = row[c + 1]
            cell.walls.right = next.walls.left
            if not cell.walls.right:
                cell.drawMove(next)


def main():

    win = Window(500, 500)
    win.root.title = "Maze test"

    maze = Maze(Point(100, 100), 5, 5, 60, 50, win)
    maze.createCells()
    maze.breakRandomWalls()

    maze._drawCell(1, 1, "red")

    print()
    print(maze)
    print(maze.cells)

    win.wait()


if __name__ == "__main__":
    main()
