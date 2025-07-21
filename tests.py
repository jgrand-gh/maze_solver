import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(maze._Maze__cells[0]), # type: ignore
            num_rows,
        )

    def test_maze_small_dimensions(self):
        num_cols = 5
        num_rows = 5
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(maze._Maze__cells[0]), # type: ignore
            num_rows,
        )

    def test_maze_large_dimensions(self):
        num_cols = 30
        num_rows = 25
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze._Maze__cells), # type: ignore
            num_cols,
        )
        self.assertEqual(
            len(maze._Maze__cells[0]), # type: ignore
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()