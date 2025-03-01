# clockwise, css order
class Walls:
    def __init__(
        self,
        top: bool = True,
        right: bool = True,
        bottom: bool = True,
        left: bool = True,
    ):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def __str__(self) -> str:
        return f"Walls({self.top}, {self.right}, {self.bottom}, {self.left})"


def main():
    walls = Walls()

    print()
    print(walls)


if __name__ == "__main__":
    main()
