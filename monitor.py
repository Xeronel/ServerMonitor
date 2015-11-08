__author__ = 'ripster'

from servmon.sysstats import Network
import time
import os


net = Network()
os.system('clear')
os.system('setterm -cursor off')
while True:
    print('UL: {0:.2f} MB/s - DL: {1:.2f} MB/s'.format(*net.speed), end='\r')
