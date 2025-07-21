from typing import Optional

from window import Window
from point import Point
from line import Line

class Cell:
    def __init__(self, window: Optional[Window] = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window

        self.visited = False

    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        if self.__win is None:
            return
        
        self.__x1, self.__y1, self.__x2, self.__y2 = x1, y1, x2, y2

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        if self.has_top_wall:
            self.__win.draw_line(Line(top_left, top_right))
        else:
            self.__win.draw_line(Line(top_left, top_right), "white")

        if self.has_left_wall:
            self.__win.draw_line(Line(top_left, bottom_left))
        else:
            self.__win.draw_line(Line(top_left, bottom_left), "white")

        if self.has_right_wall:
            self.__win.draw_line(Line(top_right, bottom_right))
        else:
            self.__win.draw_line(Line(top_right, bottom_right), "white")

        if self.has_bottom_wall:
            self.__win.draw_line(Line(bottom_left, bottom_right))
        else:
            self.__win.draw_line(Line(bottom_left, bottom_right), "white")

    def draw_move(self, to_cell: "Cell", undo: bool=False) -> None:
        fill_color = "red"
        if not undo:
            fill_color = "green"

        source = self.get_center()
        destination = to_cell.get_center()
        
        if self.__win is None:
            return
        self.__win.draw_line(Line(source, destination), fill_color)

    def get_center(self) -> Point:
        center_x = (self.__x1 + self.__x2) / 2
        center_y = (self.__y1 + self.__y2) / 2
        return Point(center_x, center_y)