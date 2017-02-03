#!/usr/bin/env python3

import sys
import datetime

from widgets.widget import Widget
from widgets.config import colors, icons

class date(Widget):
    '''
    Abstrac class for all lemonbar widgets.
    '''

    def __init__(self, value=''):
        '''
        Params:
            bg: background color
            fg: foreground color
            icon: icon
        '''
        Widget.__init__(self)
        self.value = value

        self.bg = None
        self.fg = colors['c_white']
        self.icon = icons['clock']

    def update(self):
        '''

        TO IMPLEMENT.

        '''
        date = datetime.datetime.now()

        self.value = date.strftime('%a %d.%m.%y %H:%M %p')
