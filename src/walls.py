class Walls:
    # clockwise, css order
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
        return f"({self.top}, {self.right}, {self.bottom}, {self.left})"


def main():
    walls = Walls(True, True, True, True)

    print()
    print(walls)


if __name__ == "__main__":
    main()
