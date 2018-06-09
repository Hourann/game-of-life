from src.cell import Cell


class Table:
    def __init__(self, width, height, interval=500, init_state=None):
        self._width = width
        self._height = height
        self._interval = interval
        self._cells = [[Cell(True) for x in range(width)] for y in range(height)]

    def set_state(self, state):
        if not isinstance(state, list):
            raise TypeError()
        elif len(state) != self._height and any(len(row) != self._width for row in state):
            raise ValueError()
        self._cells = [[Cell(st) for st in row] for row in state]

    def get_state(self):
        return [[cell.state for cell in row] for row in self._cells]

