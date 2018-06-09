# coding: utf-8
import time
import curses
from src.table import Table
ALIVE_CHAR = '*'
DEAD_CHAR = ' '
STATE1 = [[False, True, False], [False, True, False], [False, True, False]]
table = Table(10, 80)
table.generate_random_state()
# table.set_state(STATE1)


def print_table(window, table):
    width, height = table.get_size()
    state = table.get_state()
    for x in range(width):
        for y in range(height):
            window.addstr(x, y, ALIVE_CHAR if state[y][x] else DEAD_CHAR)
            window.refresh()

def draw(window):
    while True:
        print_table(window, table)
        table.next()
        time.sleep(1)


if __name__ == '__main__':
    curses.wrapper(draw)
