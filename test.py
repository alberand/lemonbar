#!/usr/bin/env python3

import datetime
from widgets.date import Date
from widgets.internet import Internet
from config import colors, icons

if __name__ == '__main__':
    # a = Widget('a')
    # a.add_action(3, 'date')
    # a.add_action(1, 'time')

    a = Date()
    b = Internet()

    print(a.get_output())
    print(b.get_output())
