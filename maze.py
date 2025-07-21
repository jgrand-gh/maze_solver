import time

from cell import Cell
from window import Window

class Maze:
    def __init__(self, x: float, y: float, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, window: Window) -> None:
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = window

        self.__cells = []
        self.__create_cells()

    def __create_cells(self) -> None:
        for c in range(self.__num_cols):
            row = []
            for r in range(self.__num_rows):
                row.append(Cell(self.__win))
                self.__draw_cell(c, r)
            self.__cells.append(row)

    def __draw_cell(self, col: int, row: int) -> None:
        cell = Cell(self.__win)
        cell.draw(
            x1=self.__x + (self.__cell_size_x * col),
            y1=self.__y + (self.__cell_size_y * row),
            x2=self.__x + (self.__cell_size_x * (col + 1)),
            y2=self.__y + (self.__cell_size_y * (row + 1))
        )
        self.__animate()

    def __animate(self) -> None:
        self.__win.redraw()
        time.sleep(0.02)