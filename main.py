from window import Window
from maze import Maze

if __name__ == "__main__":
    win = Window(800, 600)

    maze = Maze(
        x=5, y=5,
        num_cols=10, num_rows=10,
        cell_size_x=40, cell_size_y=40,
        window=win)

    win.wait_for_close()