from window import Window
from cell import Cell


if __name__ == "__main__":
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.has_left_wall = False
    cell1.draw(50, 50,
              100, 100)

    cell2 = Cell(win)
    cell2.has_bottom_wall = False
    cell2.draw(150, 150,
              200, 200)
    
    cell1.draw_move(cell2)

    win.wait_for_close()