from window import Window
from maze import Maze

if __name__ == "__main__":
    screen_width = 800
    screen_height = 600
    window = Window(screen_width, screen_height)

    num_rows = 12
    num_cols = 10
    margin = 25
    cell_size_x = (screen_width - (2 * margin)) / num_cols
    cell_size_y = (screen_height - (2 * margin)) / num_rows
    
    maze = Maze(x=margin, y=margin,
                num_cols=num_cols, num_rows=num_rows,
                cell_size_x=cell_size_x,
                cell_size_y=cell_size_y,
                window=window)
    
    if maze.solve():
        print("yay we did it - 2ez")
    else:
        print("game over - NEVER solveable")

    window.wait_for_close()