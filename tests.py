import unittest

from constants import CELL_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH
from maze import Maze


class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = WINDOW_WIDTH // CELL_SIZE - 1
    num_rows = WINDOW_HEIGHT // CELL_SIZE - 1
    m1 = Maze(10, 10, num_rows, num_cols, CELL_SIZE, CELL_SIZE)
    m1_cells = m1.get_cells()
    self.assertEqual(
      len(m1_cells),
      num_cols,
    )
    self.assertEqual(
      len(m1_cells[0]),
      num_rows,
    )

  def test_maze_create_cells_invalid(self):
    num_cols = -1
    num_rows = -1
    m1 = Maze(0, 0, num_rows, num_cols, CELL_SIZE, CELL_SIZE)
    m1_cells = m1.get_cells()
    self.assertEqual(m1_cells, [])

  def test_maze_break_entrance_and_exit(self):
    num_cols = WINDOW_WIDTH // CELL_SIZE - 1
    num_rows = WINDOW_HEIGHT // CELL_SIZE - 1
    m1 = Maze(10, 10, num_rows, num_cols, CELL_SIZE, CELL_SIZE)
    m1_cells = m1.get_cells()
    self.assertFalse(m1_cells[0][0].has_top_wall)
    self.assertFalse(m1_cells[num_cols - 1][num_rows - 1].has_bottom_wall)

  def test_maze_visited_is_reset(self):
    num_cols = WINDOW_WIDTH // CELL_SIZE - 1
    num_rows = WINDOW_HEIGHT // CELL_SIZE - 1
    m1 = Maze(10, 10, num_rows, num_cols, CELL_SIZE, CELL_SIZE)
    m1_cells = m1.get_cells()
    for i in range(num_cols):
      for j in range(num_rows):
        self.assertFalse(m1_cells[i][j].visited)


if __name__ == "__main__":
  unittest.main()
