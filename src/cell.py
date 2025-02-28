from point import Point
from line import Line
from walls import Walls
from window import Window


class Cell:
    def __init__(
        self, window: Window, topLeft: Point, bottomRight: Point, walls: Walls = None
    ):
        self.window = window

        self.topLeft = topLeft
        self.topRight = Point(bottomRight.x, topLeft.y)
        self.bottomRight = bottomRight
        self.bottomLeft = Point(topLeft.x, bottomRight.y)

        self.center = Point(
            topLeft.x + (bottomRight.x - topLeft.x) / 2,
            topLeft.y + (bottomRight.y - topLeft.y) / 2,
        )

        if walls is None:
            walls = Walls()
        self.walls = walls

    def __str__(self):
        return (
            f"window: {self.window.root.title}\n"
            f"center: {self.center}\n"
            f"topLeft: {self.topLeft}\n"
            f"topRight: {self.topRight}\n"
            f"bottomRight: {self.bottomRight}\n"
            f"bottomLeft: {self.bottomLeft}\n"
            f"walls: {self.walls}\n"
        )

    def draw(self, fillColor: str):
        if self.walls.top:
            self.window.drawLine(Line(self.topLeft, self.topRight), fillColor)
        if self.walls.right:
            self.window.drawLine(Line(self.topRight, self.bottomRight), fillColor)
        if self.walls.bottom:
            self.window.drawLine(Line(self.bottomLeft, self.bottomRight), fillColor)
        if self.walls.left:
            self.window.drawLine(Line(self.topLeft, self.bottomLeft), fillColor)


def main():
    win = Window(500, 500)
    win.root.title = "Cell test"
    start = Point(200, 200)
    end = Point(300, 300)
    cell = Cell(win, start, end)

    print()
    print(cell)


if __name__ == "__main__":
    main()
