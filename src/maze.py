import time

from cell import Cell
from window import Window


class Maze:
  def __init__(
    self,
    x1: int,
    y1: int,
    num_rows: int,
    num_cols: int,
    cell_size_x: int,
    cell_size_y: int,
    win: Window,
  ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.win = win
    self.__cells: list[list[Cell]] = []
    self.__create_cells()

  def __create_cells(self):
    for i in range(self.num_cols):
      print(f"making column {i}")
      cols: list[Cell] = []
      for j in range(self.num_rows):
        print(f"making cell ({i}, {j})")
        cols.append(Cell(self.win))
      self.__cells.append(cols)

    for i in range(self.num_cols):
      for j in range(self.num_rows):
        self.__draw_cell(i, j)

  def __draw_cell(self, i: int, j: int):
    x2 = self.x1 + self.cell_size_x * (i + 1)
    y2 = self.x1 + self.cell_size_x * (j + 1)
    self.__cells[i][j].draw(self.x1, self.y1, x2, y2)
    self._animate()

  def _animate(self):
    self.win.redraw()
    time.sleep(0.001)
