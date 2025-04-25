from tkinter import Tk, BOTH, Canvas
from graphics import Line, Point


class Cell:
  def __init__(self, win):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._x2 = None
    self._y1 = None
    self._y2 = None
    self._w = win

  def draw(self, x1, y1, x2, y2):
    if self._w is None:
      return
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2
    if self.has_left_wall:
      line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
      self._w.draw_line(line, "black")
    if self.has_right_wall:
      line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
      self._w.draw_line(line, "black")
    if self.has_top_wall:
      line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
      self._w.draw_line(line, "black")
    if self.has_bottom_wall:
      line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
      self._w.draw_line(line, "black")

  def draw_move(self, to_cell, undo=False):
      half_length = abs(self._x1 - self._x2) // 2
      x_center = half_length + self._x1
      y_center = half_length + self._y1

      half_length2 = abs(to_cell._x1 - to_cell._x2) // 2
      x_center2 = half_length + to_cell._x1
      y_center2 = half_length + to_cell._y1

      fill_color = "red"
      if undo:
          fill_color = "gray"

      line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
      self._w.draw_line(line, fill_color)
        
