# coding: utf-8
import time
import curses
from src.table import Table
ALIVE_CHAR = '*'
DEAD_CHAR = ' '
STATE1 = [[False, True, False], [False, True, False], [False, True, False]]
table = Table(3, 3)
table.set_state(STATE1)

def answer():
    return 42


def print_state(window, state):
    height = len(state)
    width = len(state[0])
    for x in range(width):
        for y in range(height):
            window.addstr(x, y, ALIVE_CHAR if state[y][x] else DEAD_CHAR)
            window.refresh()

def game_of_life(window):
    state = table.get_state()
    print_state(window, state)
    table.next()
    time.sleep(0.5)
    game_of_life(window)

curses.wrapper(game_of_life)