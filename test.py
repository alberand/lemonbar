#!/usr/bin/env python3

import datetime
from widgets.date import Date
from widgets.internet import Internet
import time
import sys

if __name__ == '__main__':
    # a = Widget('a')
    # a.add_action(3, 'date')
    # a.add_action(1, 'time')

    a = Date()
    b = Internet()

    # print(a.get_output())
    # print(b.get_output())
    i = 0
    date = 'Sunday'
    while True:
        print("%{A:date:}%{F#FFFFFF} " + date + " Click here to reboot " + str(i) + " %{F#FFFFFF}%{A}")
        i += 1
        # print("%{O5}%{F#ffb8bb26}%{B#ff282828}  %{B#ff282828}%{F#ffb8bb26}%{O5}")
        sys.stdout.flush()

        # if sys.stdin.read() == 'date':
            # print('Fuck off. Today is monday.')
            # date = 'Monday'
        print(input())

        time.sleep(1)
