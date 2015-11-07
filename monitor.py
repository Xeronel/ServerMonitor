__author__ = 'ripster'

from servmon.sysstats import Network
import time


net = Network()

while True:
    print('UL: {0:.2f} MB/s - DL: {1:.2f} MB/s'.format(*net.speed))
    print('--------------------------------')