import time
import random

from typing import Optional

from window import Window
from cell import Cell

ANIMATION_SPEED = 0.02

class Maze:
    def __init__(self,
                 x: float, y: float,
                 num_rows: int, num_cols: int,
                 cell_size_x: float, cell_size_y: float,
                 window: Optional[Window] = None,
                 seed: Optional[int] = None
    ) -> None:
        self.__x = x
        self.__y = y
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = window

        if seed:
            random.seed(seed)

        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(col=0, row=0)

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
        time.sleep(ANIMATION_SPEED)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(col=0, row=0)
        
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(col=self.__num_cols - 1, row=self.__num_rows - 1)

    def __break_walls_r(self, col: int, row: int) -> None:
        self.__cells[col][row].visited = True
        while True:
            nodes_to_visit = self.check_valid_directions(col, row)

            if len(nodes_to_visit) == 0:
                self.__draw_cell(col=col, row=row)
                return
            
            go_direction = random.choice(list(nodes_to_visit.keys()))

            if go_direction == "west":
                self.__cells[col][row].has_left_wall = False
                self.__cells[col-1][row].has_right_wall = False
                self.__break_walls_r(col=col-1, row=row)
            elif go_direction == "north":
                self.__cells[col][row].has_top_wall = False
                self.__cells[col][row-1].has_bottom_wall = False
                self.__break_walls_r(col=col, row=row-1)
            elif go_direction == "south":
                self.__cells[col][row].has_bottom_wall = False
                self.__cells[col][row+1].has_top_wall = False
                self.__break_walls_r(col=col, row=row+1)
            elif go_direction == "east":
                self.__cells[col][row].has_right_wall = False
                self.__cells[col+1][row].has_left_wall = False
                self.__break_walls_r(col=col+1, row=row)
            else:
                print("Something went drastically wrong")
                return

    def check_valid_directions(self, col: int, row: int) -> dict:
        direction_deltas = {
            "west": (-1, 0),
            "north": (0, -1),
            "south": (0, 1),
            "east": (1, 0)
        }
        valid_moves = {}

        for direction, (delta_col, delta_row) in direction_deltas.items():
            next_col = col + delta_col
            next_row = row + delta_row

            if 0 <= next_col < self.__num_cols and 0 <= next_row < self.__num_rows:
                cell = self.__cells[next_col][next_row]
                if cell and not cell.visited:
                    valid_moves[direction] = (next_col, next_row)
        return valid_moves
            