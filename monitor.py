__author__ = 'ripster'

from servmon.sysstats import Network
import time
import curses


net = Network()
screen = curses.initscr()
curses.halfdelay(5)
curses.noecho()
quit = False
while not quit:
    screen.clear()
    screen.addstr(12, 25, 'UL: {0:.2f} Mbps - DL: {1:.2f} Mbps'.format(*net.speed))
    screen.refresh()

    if screen.getch() == 3:
        curses.endwin()
        quit = True

