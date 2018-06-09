from src.cell import Cell


class Table:
    def __init__(self, width, height, interval=500, init_state=None):
        self._width = width
        self._height = height
        self._interval = interval
        self._cells = [[Cell(True) for x in range(width)] for y in range(height)]

    def get_state(self):
        return [[True, True, True], [True, True, True], [True, True, True]]