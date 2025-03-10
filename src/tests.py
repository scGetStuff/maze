import unittest
from maze import Maze
from point import Point


createCellsTests = [
    {
        "maze": Maze(Point(0, 0), rows=10, cols=12, cellWidth=10, cellHeight=10),
        "rows": 10,
        "cols": 12,
    },
    {
        "maze": Maze(Point(0, 0), rows=20, cols=3, cellWidth=50, cellHeight=40),
        "rows": 20,
        "cols": 3,
    },
]

mazeTests = [
    {
        "maze": Maze(Point(1, 2), rows=3, cols=4, cellWidth=5, cellHeight=6),
        "expected": (
            "window: None\n"
            "origin: (x:1, y:2)\n"
            "rows: 3\n"
            "cols: 4\n"
            "cellWidth: 5\n"
            "cellHeight: 6\n"
        ),
    },
]


class Tests(unittest.TestCase):

    def test_maze(self):
        for test in mazeTests:
            maze: Maze = test["maze"]
            self.assertEqual(f"{maze}", test["expected"])

    def test_createCells(self):
        for test in createCellsTests:
            maze: Maze = test["maze"]
            maze.createCells()
            self.assertEqual(len(maze.cells), test["rows"])
            self.assertEqual(len(maze.cells[0]), test["cols"])


if __name__ == "__main__":
    unittest.main()
