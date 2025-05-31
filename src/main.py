# from cell import Cell
from constants import CELL_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH
from maze import Maze

# from geometry import Point
from window import Window


def main():
  win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

  num_cells_hori = WINDOW_WIDTH // CELL_SIZE - 1
  num_cells_vert = WINDOW_HEIGHT // CELL_SIZE - 1

  maze: Maze = Maze(
    10, 10, num_cells_vert, num_cells_hori, CELL_SIZE, CELL_SIZE, win
  )

  win.wait_for_close()


if __name__ == "__main__":
  main()
