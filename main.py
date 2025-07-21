from window import Window
from maze import Maze

if __name__ == "__main__":
    screen_width = 800
    screen_height = 600
    window = Window(screen_width, screen_height)

    num_rows = 8
    num_cols = 12
    margin = 25
    cell_size_x = (screen_width - (2 * margin)) / num_cols
    cell_size_y = (screen_height - (2 * margin)) / num_rows
    maze = Maze(x=margin, y=margin,
                num_cols=num_cols, num_rows=num_rows,
                cell_size_x=cell_size_x,
                cell_size_y=cell_size_y,
                window=window)

    window.wait_for_close()