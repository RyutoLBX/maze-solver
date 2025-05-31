from geometry import Line, Point
from window import Window


class Cell:
  def __init__(self, window: Window):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.__x1 = -1
    self.__x2 = -1
    self.__y1 = -1
    self.__y2 = -1
    self.__win = window

  def draw(self, x1: int, y1: int, x2: int, y2: int):
    self.__x1 = x1
    self.__y1 = y1
    self.__x2 = x2
    self.__y2 = y2

    top_left: Point = Point(self.__x1, self.__y1)
    top_right: Point = Point(self.__x2, self.__y1)
    bottom_left: Point = Point(self.__x1, self.__y2)
    bottom_right: Point = Point(self.__x2, self.__y2)

    if self.has_left_wall:
      left_wall: Line = Line(top_left, bottom_left)
      self.__win.draw_line(left_wall)
    if self.has_right_wall:
      right_wall: Line = Line(top_right, bottom_right)
      self.__win.draw_line(right_wall)
    if self.has_top_wall:
      top_wall: Line = Line(top_left, top_right)
      self.__win.draw_line(top_wall)
    if self.has_bottom_wall:
      bottom_wall: Line = Line(bottom_left, bottom_right)
      self.__win.draw_line(bottom_wall)

  def draw_move(self, to_cell: "Cell", undo: bool = False):
    line_color = "gray" if undo else "red"

    centerpoint_self = Point(
      (self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2
    )
    centerpoint_other = Point(
      (to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2
    )

    mid_line = Line(centerpoint_self, centerpoint_other)
    self.__win.draw_line(mid_line, line_color)
