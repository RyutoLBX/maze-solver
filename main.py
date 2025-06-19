# from cell import Cell
from constants import CELL_SIZE, MARGIN, WINDOW_HEIGHT, WINDOW_WIDTH
from maze import Maze

# from geometry import Point
from window import Window


def main():
  win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

  num_cols = WINDOW_WIDTH // CELL_SIZE - 1
  num_rows = WINDOW_HEIGHT // CELL_SIZE - 1

  Maze(MARGIN, MARGIN, num_rows, num_cols, CELL_SIZE, CELL_SIZE, win, 1)
  win.wait_for_close()


if __name__ == "__main__":
  main()
