#!/usr/bin/env python

import sys
from multiprocessing import Pool
from multiprocessing.managers import BaseManager


if __name__ == '__main__':
    if sys.argv[1] == 'server':
        l = [1, 2, 3]
        manager = BaseManager(address=('', 50000), authkey='abc')
        manager.register('get_l', callable=lambda: l)

        server = manager.get_server()
        server.serve_forever()

    elif sys.argv[1] == 'client':
        manager = BaseManager(address=('127.0.0.1', 50000), authkey='abc')
        manager.connect()

        print manager.get_l()
