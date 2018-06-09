# coding: utf-8
import sys
import time

import curses

from src.table import Table

ALIVE_CHAR = '*'
DEAD_CHAR = ' '
table = Table(80, 10)
table.generate_random_state(.5)

def print_table(window, table):
    width, height = table.get_size()
    state = table.get_state()
    for x in range(width):
        for y in range(height):
            window.addstr(y, x, ALIVE_CHAR if state[y][x] else DEAD_CHAR)
            window.refresh()

def draw(window):
    while True:
        print_table(window, table)
        table.next()
        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        farg = list(filter(lambda arg: arg.startswith('--fname='), sys.argv[1:]))
        fname = farg[0][8:] if farg else None
        if fname:
            with open(fname, 'r') as f:
                lines = f.readlines()
            init_state = [[c == '*' for c in line.strip()] for line in lines]
            table = Table(len(lines[0].strip()), len(lines), init_state)
    curses.wrapper(draw)
