__author__ = 'ripster'

from servmon.sysstats import Network
import time
import curses
import os
import sys


net = Network()
screen = curses.initscr()
curses.halfdelay(5)
curses.noecho()
curses.curs_set(0)

quit = False
while not quit:
    screen.clear()
    screen.addstr(0, 0, 'UL: {0:.2f} Mbps - DL: {1:.2f} Mbps'.format(*net.speed))
    screen.refresh()

    if screen.getch() == 3:
        quit = True

curses.endwin()

