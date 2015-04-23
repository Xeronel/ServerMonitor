__author__ = 'ripster'

import threading
from collections import deque
import time
import psutil


class Network():
    def __init__(self, interface: str='eth0'):
        # Create the ul/dl thread and a deque of length 1 to hold the ul/dl- values
        self._transfer_rate = deque(maxlen=1)
        t = threading.Thread(target=self._calc_ul_dl, args=(interface, self._transfer_rate))

        # The program will exit if there are only daemonic threads left.
        t.daemon = True
        t.start()

    @property
    def speed(self):
        try:
            return self._transfer_rate[-1]
        except IndexError:
            return 0, 0

    @staticmethod
    def _calc_ul_dl(interface, rate):
        t0 = time.time()
        counter = psutil.net_io_counters(pernic=True)[interface]
        total = (counter.bytes_sent, counter.bytes_recv)
        while True:
            last_tot = total
            time.sleep(1)
            counter = psutil.net_io_counters(pernic=True)[interface]
            t1 = time.time()
            total = (counter.bytes_sent, counter.bytes_recv)
            ul, dl = [(now - last) / (t1 - t0) / 1000000.0
                      for now, last in zip(total, last_tot)]
            rate.append((ul, dl))
            t0 = time.time()