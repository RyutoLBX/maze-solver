import random
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
    win: Window | None = None,
    seed: int | None = None,
  ):
    self.x1 = x1
    self.y1 = y1
    self.num_rows = num_rows
    self.num_cols = num_cols
    self.cell_size_x = cell_size_x
    self.cell_size_y = cell_size_y
    self.__win = win
    if seed:
      random.seed(seed)

    self.__cells: list[list[Cell]] = []
    self.__create_cells()

    if self.__cells == []:
      return
    self.__break_entrance_and_exit()
    self.__break_walls_r(0, 0)
    self.__reset_cells_visited()

  def __create_cells(self):
    if self.num_cols <= 0 or self.num_rows <= 0:
      return

    for i in range(self.num_cols):
      cols: list[Cell] = []
      for j in range(self.num_rows):
        cols.append(Cell(self.__win))
      self.__cells.append(cols)

    for i in range(self.num_cols):
      for j in range(self.num_rows):
        self.__draw_cell(i, j)

  def __draw_cell(self, i: int, j: int):
    x1 = self.x1 + self.cell_size_x * i
    y1 = self.x1 + self.cell_size_x * j
    x2 = x1 + self.cell_size_x
    y2 = y1 + self.cell_size_y
    self.__cells[i][j].draw(x1, y1, x2, y2)
    self._animate()

  def _animate(self):
    if self.__win is not None:
      self.__win.redraw()
      time.sleep(0.001)

  def __break_entrance_and_exit(self):
    if not self.__cells:
      return
    max_col_index = self.num_cols - 1
    max_row_index = self.num_rows - 1
    self.__cells[0][0].has_top_wall = False
    self.__cells[max_col_index][max_row_index].has_bottom_wall = False

    self.__draw_cell(0, 0)
    self.__draw_cell(max_col_index, max_row_index)

  def __break_walls_r(self, i: int, j: int):
    self.__cells[i][j].visited = True
    while True:
      next_indexes: list[tuple[int, int]] = []
      if self.can_be_visited(i, j, 0):
        next_indexes.append((i - 1, j))
      if self.can_be_visited(i, j, 1):
        next_indexes.append((i + 1, j))
      if self.can_be_visited(i, j, 2):
        next_indexes.append((i, j - 1))
      if self.can_be_visited(i, j, 3):
        next_indexes.append((i, j + 1))

      if len(next_indexes) == 0:
        print("returning to previous cell")
        self.__draw_cell(i, j)
        return

      dir = random.randrange(len(next_indexes))
      next_index = next_indexes[dir]

      if next_index[0] == i - 1:
        print(f"going down: ({(i, j)}) -> ({next_index})")
        self.__cells[i][j].has_left_wall = False
        self.__cells[i - 1][j].has_right_wall = False
      if next_index[0] == i + 1:
        print(f"going down: ({(i, j)}) -> ({next_index})")
        self.__cells[i][j].has_right_wall = False
        self.__cells[i + 1][j].has_left_wall = False
      if next_index[1] == j - 1:
        print(f"going down: ({(i, j)}) -> ({next_index})")
        self.__cells[i][j].has_top_wall = False
        self.__cells[i - 1][j].has_bottom_wall = False
      if next_index[1] == j + 1:
        print(f"going down: ({(i, j)}) -> ({next_index})")
        self.__cells[i][j].has_bottom_wall = False
        self.__cells[i - 1][j].has_top_wall = False

      self.__break_walls_r(next_index[0], next_index[1])

  def can_be_visited(self, i: int, j: int, dir: int) -> bool:
    match dir:
      # LEFT
      case 0:
        return i > 0 and not self.__cells[i - 1][j].visited
      # RIGHT
      case 1:
        return i < self.num_cols - 1 and not self.__cells[i + 1][j].visited
      # UP
      case 2:
        return j > 0 and not self.__cells[i][j - 1].visited
      # DOWN
      case 3:
        return j < self.num_rows - 1 and not self.__cells[i][j + 1].visited
      case _:
        return False
      
  def __reset_cells_visited(self):
    for i in range(self.num_cols):
      for j in range(self.num_rows):
        self.__cells[i][j].visited = False
    return

  def get_cells(self):
    return self.__cells
