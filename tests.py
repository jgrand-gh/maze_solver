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

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        maze._Maze__break_entrance_and_exit() # type: ignore

        self.assertEqual(
            maze._Maze__cells[0][0].has_top_wall, # type: ignore
            False,
        )
        self.assertEqual(
            maze._Maze__cells[0][0].has_left_wall, # type: ignore
            True,
        )
        self.assertEqual(
            maze._Maze__cells[0][0].has_right_wall, # type: ignore
            True,
        )
        self.assertEqual(
            maze._Maze__cells[0][0].has_bottom_wall, # type: ignore
            True,
        )

        self.assertEqual(
            maze._Maze__cells[num_cols-1][num_rows-1].has_top_wall, # type: ignore
            True,
        )
        self.assertEqual(
            maze._Maze__cells[num_cols-1][num_rows-1].has_left_wall, # type: ignore
            True,
        )
        self.assertEqual(
            maze._Maze__cells[num_cols-1][num_rows-1].has_right_wall, # type: ignore
            True,
        )
        self.assertEqual(
            maze._Maze__cells[num_cols-1][num_rows-1].has_bottom_wall, # type: ignore
            False,
        )

if __name__ == "__main__":
    unittest.main()