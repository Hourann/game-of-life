from src.cell import Cell
from random import random

class Table:
    def __init__(self, width, height, init_state=None):
        self._width = width
        self._height = height
        self._cells = [[Cell(True) for x in range(width)] for y in range(height)]
        self._time = 0

    def set_state(self, state):
        if not isinstance(state, list):
            raise TypeError()
        elif len(state) != self._height and any(len(row) != self._width for row in state):
            raise ValueError()
        self._cells = [[Cell(st) for st in row] for row in state]

    def get_state(self):
        return [[cell.state for cell in row] for row in self._cells]

    def num_of_alive_neighbor(self, x, y):
        x_range = list(range(max(0, x-1), min(x+2, self._width)))
        y_range = list(range(max(0, y-1), min(y+2, self._height)))
        neighbors_locations = {(_x, _y) for _x in x_range for _y in y_range} - {(x,y)}
        neighbors = {self._cells[_y][_x] for _x, _y in neighbors_locations}

        return sum(neighbor.state for neighbor in neighbors)

    def _get_cell(self, x, y):
        return self._cells[y][x]

    def get_size(self):
        return self._width, self._height

    def next(self):
        self._time += 1
        num_of_alive_neighbor_table = [[0] * self._width for _ in range(self._height)]
        for x in range(self._width):
            for y in range(self._height):
                num_of_alive_neighbor_table[y][x] = self.num_of_alive_neighbor(x, y)
        for x in range(self._width):
            for y in range(self._height):
                self._get_cell(x, y).next(num_of_alive_neighbor_table[y][x])

    def generate_random_state(self, ratio_of_alive=.5):
        for row in self._cells:
            for cell in row:
                cell.state = True if random() < ratio_of_alive else False
