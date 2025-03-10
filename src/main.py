from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze


# TODO: make this scale to the grid
WIN_SIZE = (1024, 768)
CELL_SIZE = 50


def main():
    print("Build a Maze Solver")

    win = Window(*WIN_SIZE)

    # doLineStuff(maze)

    maze = Maze(Point(0, 0), 4, 8, CELL_SIZE, CELL_SIZE, win)
    maze.createCells()
    maze.breakRandomWalls()

    win.wait()


def doLineStuff(win: Window):
    line1 = Line(Point(0, 0), Point(200, 200))
    line2 = Line(Point(500, 500), Point(400, 400))
    line3 = Line(Point(150, 250), Point(350, 250))
    win.drawLine(line1, "red")
    win.drawLine(line2, "blue")
    win.drawLine(line3, "black")


if __name__ == "__main__":
    main()
