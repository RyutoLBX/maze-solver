from tkinter import Canvas


class Point:
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def get_coords(self) -> tuple[int, int]:
    return (self.x, self.y)


class Line:
  def __init__(self, p1: Point, p2: Point):
    self.p1 = p1
    self.p2 = p2

  def get_line(self) -> tuple[int, int, int, int]:
    return (self.p1.x, self.p1.y, self.p2.x, self.p2.y)

  def draw(self, canvas: Canvas, fill_color: str = "black"):
    canvas.create_line(self.get_line(), fill=fill_color, width=2)
