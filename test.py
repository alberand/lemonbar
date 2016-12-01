#!/usr/bin/env python3

import sys
import time
import select 
import datetime

from widgets.date import Date
from widgets.internet import Internet

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
    cmd = ''
    while True:
        print("%{A:date:}%{F#FF0000} " + date + "  %{F#FF0000}%{A}", end='')
        print("%{A:date:}%{F#FFFFFF} Click here to reboot " + str(i) + " %{F#FFFFFF}%{A}", end='')
        print("%{A:time:}%{F#FFFFFF} Click here for time " + str(i) + " %{F#FFFFFF}%{A}")
        i += 1
        sys.stdout.flush()
        
        if select.select([sys.stdin,], [], [], 0.0)[0]:
            while True:
                char = sys.stdin.read(1)
                if char == '\n':
                    break
                cmd += char


            sys.stdin.flush()

            if cmd == 'date':
                date = 'Monday'
            if cmd == 'time':
                date = str(datetime.datetime.today())

            cmd = ''

        time.sleep(0.1)
