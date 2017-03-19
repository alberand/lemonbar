#!/usr/bin/env python3

import os
import sys
import subprocess
from widgets.widget import Widget
from widgets.config import colors, icons

class internet(Widget):
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
        self.icon = icons['globe']

    def update(self):
        cmd = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + \
                '/utils/internet'

        comp = subprocess.run(cmd.split(), stdout=subprocess.PIPE)

        if comp.returncode == 0:
            self.fg = colors['c_green_l']
        else:
            self.fg = colors['c_red_l']
