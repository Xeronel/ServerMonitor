import threading
from collections import deque
import time
import psutil


class Network:
    def __init__(self, interface: str='eth0'):
        self.interface = interface

        # Create the ul/dl thread and a deque of length 1 to hold the ul/dl- values
        self.__transfer_rate = deque(maxlen=1)
        self.__t = threading.Thread(target=self.__calc_ul_dl)

        # The program will exit if there are only daemonic threads left.
        self.__t.daemon = True
        self.__t.start()

    @property
    def speed(self):
        try:
            return self.__transfer_rate[-1]
        except IndexError:
            return 0, 0

    def __calc_ul_dl(self):
        t0 = time.time()
        counter = psutil.net_io_counters(pernic=True)[self.interface]
        total = (counter.bytes_sent, counter.bytes_recv)
        while True:
            last_tot = total
            time.sleep(0.5)
            counter = psutil.net_io_counters(pernic=True)[self.interface]
            t1 = time.time()
            total = (counter.bytes_sent, counter.bytes_recv)
            # Convert from bits to mebibits
            ul, dl = [(now - last) / (t1 - t0) / 1049000.0
                      for now, last in zip(total, last_tot)]
            self.__transfer_rate.append((ul, dl))
            t0 = time.time()
