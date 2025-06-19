# from cell import Cell
from constants import (
  CELL_SIZE,
  HORIZONTAL_MARGIN,
  VERTICAL_MARGIN,
  WINDOW_HEIGHT,
  WINDOW_WIDTH,
)
from maze import Maze

# from geometry import Point
from window import Window


def main():
  win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

  num_cols = (WINDOW_WIDTH - HORIZONTAL_MARGIN) // CELL_SIZE
  num_rows = (WINDOW_HEIGHT - VERTICAL_MARGIN) // CELL_SIZE

  m = Maze(
    HORIZONTAL_MARGIN,
    VERTICAL_MARGIN,
    num_rows,
    num_cols,
    CELL_SIZE,
    CELL_SIZE,
    win,
  )
  m.solve()
  win.wait_for_close()


if __name__ == "__main__":
  main()
