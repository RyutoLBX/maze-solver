import random
import time
from enum import Enum

from cell import Cell
from window import Window

Direction = Enum("Direction", ["LEFT", "RIGHT", "UP", "DOWN"])


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
    self.__num_rows = num_rows
    self.__num_cols = num_cols
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
    if self.__num_cols <= 0 or self.__num_rows <= 0:
      return

    for i in range(self.__num_cols):
      cols: list[Cell] = []
      for j in range(self.__num_rows):
        cols.append(Cell(self.__win))
      self.__cells.append(cols)

    for i in range(self.__num_cols):
      for j in range(self.__num_rows):
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
      time.sleep(0.03)

  def __break_entrance_and_exit(self):
    if not self.__cells:
      return
    max_col_index = self.__num_cols - 1
    max_row_index = self.__num_rows - 1
    self.__cells[0][0].has_top_wall = False
    self.__cells[max_col_index][max_row_index].has_bottom_wall = False

    self.__draw_cell(0, 0)
    self.__draw_cell(max_col_index, max_row_index)

  def __break_walls_r(self, i: int, j: int):
    self.__cells[i][j].visited = True
    while True:
      next_indexes: list[tuple[int, int]] = []
      if self.__can_be_visited(i, j, Direction.LEFT):
        next_indexes.append((i - 1, j))
      if self.__can_be_visited(i, j, Direction.RIGHT):
        next_indexes.append((i + 1, j))
      if self.__can_be_visited(i, j, Direction.UP):
        next_indexes.append((i, j - 1))
      if self.__can_be_visited(i, j, Direction.DOWN):
        next_indexes.append((i, j + 1))

      if len(next_indexes) == 0:
        self.__draw_cell(i, j)
        return

      dir = random.randrange(len(next_indexes))
      next_index = next_indexes[dir]

      if next_index[0] == i - 1:
        # print(f"going left: ({(i, j)}) -> ({next_index})")
        self.__cells[i][j].has_left_wall = False
        self.__cells[i - 1][j].has_right_wall = False
      if next_index[0] == i + 1:
        # print(f"going right: ({(i, j)}) -> ({next_index})")
        self.__cells[i][j].has_right_wall = False
        self.__cells[i + 1][j].has_left_wall = False
      if next_index[1] == j - 1:
        # print(f"going up: ({(i, j)}) -> ({next_index})")
        self.__cells[i][j].has_top_wall = False
        self.__cells[i][j - 1].has_bottom_wall = False
      if next_index[1] == j + 1:
        # print(f"going down: ({(i, j)}) -> ({next_index})")
        self.__cells[i][j].has_bottom_wall = False
        self.__cells[i][j + 1].has_top_wall = False

      self.__break_walls_r(next_index[0], next_index[1])

  # Function to see if a certain direction is visitable, no wall considerations
  def __can_be_visited(self, i: int, j: int, dir: Direction) -> bool:
    match dir:
      case Direction.LEFT:
        return i > 0 and not self.__cells[i - 1][j].visited
      case Direction.RIGHT:
        return i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited
      case Direction.UP:
        return j > 0 and not self.__cells[i][j - 1].visited
      case Direction.DOWN:
        return j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited
      case _:
        return False

  # Function to see if a certain direction is visitable, includng wall considerations
  def __can_be_visited_walls(self, i: int, j: int, dir: Direction) -> bool:
    match dir:
      # LEFT
      case Direction.LEFT:
        return (
          self.__can_be_visited(i, j, dir)
          and not self.__cells[i][j].has_left_wall
          and not self.__cells[i - 1][j].has_right_wall
        )
      # RIGHT
      case Direction.RIGHT:
        return (
          self.__can_be_visited(i, j, dir)
          and not self.__cells[i][j].has_right_wall
          and not self.__cells[i + 1][j].has_left_wall
        )
      # UP
      case Direction.UP:
        return (
          self.__can_be_visited(i, j, dir)
          and not self.__cells[i][j].has_top_wall
          and not self.__cells[i][j - 1].has_bottom_wall
        )
      # DOWN
      case Direction.DOWN:
        return (
          self.__can_be_visited(i, j, dir)
          and not self.__cells[i][j].has_bottom_wall
          and not self.__cells[i][j + 1].has_top_wall
        )
      case _:
        return False

  def __reset_cells_visited(self):
    for i in range(self.__num_cols):
      for j in range(self.__num_rows):
        self.__cells[i][j].visited = False
    return

  def solve(self) -> bool:
    return self._solve_r(0, 0)

  def _solve_r(self, i: int, j: int) -> bool:
    self._animate()
    self.__cells[i][j].visited = True

    # If method reaches end cell then return True
    if i == self.__num_cols - 1 and j == self.__num_rows - 1:
      return True

    result: bool = False
    for dir in Direction:
      if self.__can_be_visited_walls(i, j, dir):
        match dir:
          case Direction.LEFT:
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            result = self._solve_r(i - 1, j)
            if result:
              return True
            else:
              self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)
          case Direction.RIGHT:
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            result = self._solve_r(i + 1, j)
            if result:
              return True
            else:
              self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)
          case Direction.UP:
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            result = self._solve_r(i, j - 1)
            if result:
              return True
            else:
              self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)
          case Direction.DOWN:
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            result = self._solve_r(i, j + 1)
            if result:
              return True
            else:
              self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)
          case _:
            return False
    return False

  def get_cells(self):
    return self.__cells
