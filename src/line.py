from point import Point
from tkinter import Canvas


class Line:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def draw(self, canvas: Canvas, fillColor: str):
        canvas.create_line(
            *self.a.asTuple(), *self.b.asTuple(), fill=fillColor, width=2
        )

    def __str__(self) -> str:
        return f"a:{self.a} b:{self.b}"


def main():
    line = Line(Point(0, 0), Point(250, 250))

    print()
    print(line)


if __name__ == "__main__":
    main()
