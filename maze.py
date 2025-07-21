import time

from window import Window
from cell import Cell

from typing import Optional

class Maze:
    def __init__(self,
                 x: float, y: float,
                 num_rows: int, num_cols: int,
                 cell_size_x: float, cell_size_y: float,
                 window: Optional[Window] = None
    ) -> None:
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = window

        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self) -> None:        
        for c in range(self.__num_cols):
            row = []
            for r in range(self.__num_rows):
                row.append(Cell(self.__win))
            self.__cells.append(row)

        for c in range(self.__num_cols):
            for r in range(self.__num_rows):
                self.__draw_cell(c, r)

    def __draw_cell(self, col: int, row: int) -> None:
        if self.__win is None:
            return
        self.__cells[col][row].draw(
            x1=self.__x + (self.__cell_size_x * col),
            y1=self.__y + (self.__cell_size_y * row),
            x2=self.__x + (self.__cell_size_x * (col + 1)),
            y2=self.__y + (self.__cell_size_y * (row + 1))
        )
        self.__animate()

    def __animate(self) -> None:
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.02)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(col=0, row=0)
        
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(col=self.__num_cols - 1, row=self.__num_rows - 1)