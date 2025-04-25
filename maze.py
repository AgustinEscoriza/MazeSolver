from cell import Cell
import time
import random

class Maze:
  def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
      ):
    if seed != None:
      seed = random.seed(seed) 
    print(f"SEED NUMBER: {seed}")
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._w = win
    self._create_sells()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()
    self.solve()

  def _create_sells(self):
      for i in range(self._num_cols):
        col_cells = []
        for j in range(self._num_rows):
          col_cells.append(Cell(self._w))
        self._cells.append(col_cells)

      for i in range(self._num_cols):
        for j in range(self._num_rows):
          self._draw_cell(i, j)
  
  def _draw_cell(self, i, j):
    if self._w is None:
      return
    x1 = self._x1 + i * self._cell_size_x
    y1 = self._y1 + j * self._cell_size_y
    x2 = x1 + self._cell_size_x
    y2 = y1 + self._cell_size_y
    self._cells[i][j].draw(x1, y1, x2, y2)
    self._animate()

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0, 0)
    self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
    self._draw_cell(self._num_cols - 1, self._num_rows - 1)

  def _animate(self): 
    if self._w is None:
            return
    self._w.redraw()
    time.sleep(0.01)

  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True
    while True:
      to_visit = []
      # left
      if i > 0 and not self._cells[i - 1][j].visited:
          to_visit.append((i - 1, j))
      # right
      if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
          to_visit.append((i + 1, j))
      # up
      if j > 0 and not self._cells[i][j - 1].visited:
          to_visit.append((i, j - 1))
      # down
      if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
          to_visit.append((i, j + 1))

      if len(to_visit) == 0:
        self._draw_cell(i,j)
        return
      
      direction_index = random.randrange(len(to_visit))
      next_index = to_visit[direction_index]

      # right
      if next_index[0] == i + 1:
          self._cells[i][j].has_right_wall = False
          self._cells[i + 1][j].has_left_wall = False
      # left
      if next_index[0] == i - 1:
          self._cells[i][j].has_left_wall = False
          self._cells[i - 1][j].has_right_wall = False
      # down
      if next_index[1] == j + 1:
          self._cells[i][j].has_bottom_wall = False
          self._cells[i][j + 1].has_top_wall = False
      # up
      if next_index[1] == j - 1:
          self._cells[i][j].has_top_wall = False
          self._cells[i][j - 1].has_bottom_wall = False

      self._break_walls_r(next_index[0], next_index[1])

  def _reset_cells_visited(self):
    for col in self._cells:
      for cell in col:
         cell.visited = False

  def solve(self):
    return self._solve_r(0, 0)
  
  def _solve_r(self, i, j):
    self._animate()
    self._cells[i][j].visited = True

    if i == self._num_cols -1 and j == self._num_rows - 1:
      print("good ending")
      return True
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for di, dj in directions:
      next_i = i + di 
      next_j = j + dj

      if 0 <= next_i < self._num_cols and 0 <= next_j < self._num_rows:
        if not self._cells[next_i][next_j].visited:
          if di == 1 and dj == 0 and not self._cells[i][j].has_right_wall:
            
            self._cells[i][j].draw_move(self._cells[next_i][ next_j])
            
            if self._solve_r(next_i, next_j):
                return True
            
            self._cells[next_i][ next_j].draw_move(self._cells[i][j], True)
          
          if di == -1 and dj == 0 and not self._cells[i][j].has_left_wall:
            
            self._cells[i][j].draw_move(self._cells[next_i][ next_j])
            
            if self._solve_r(next_i, next_j):
                return True
            
            self._cells[next_i][ next_j].draw_move(self._cells[i][j], True)

          if di == 0 and dj == 1 and not self._cells[i][j].has_bottom_wall:
            
            self._cells[i][j].draw_move(self._cells[next_i][ next_j])
            
            if self._solve_r(next_i, next_j):
                return True
            
            self._cells[next_i][ next_j].draw_move(self._cells[i][j], True)
          
          if di == 0 and dj == -1 and not self._cells[i][j].has_top_wall:
            
            self._cells[i][j].draw_move(self._cells[next_i][ next_j])
            
            if self._solve_r(next_i, next_j):
                return True
            
            self._cells[next_i][ next_j].draw_move(self._cells[i][j], True)

    return False