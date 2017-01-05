#!/usr/bin/env python3

import os
import subprocess
from widgets.widget import Widget
from widgets.config import colors, icons

class Internet(Widget):
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

        self.colors_rules = dict()
        self.action = []
        self.action_buttons = []

    def update(self):
        '''

        TO IMPLEMENT.

        '''
        cmd = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + \
                '/utils/internet'

        comp = subprocess.run(cmd.split(), stdout=subprocess.PIPE)

        if comp:
            self.fg = colors['c_green_l']
        else:
            self.fg = colors['c_red_l']

if __name__ == '__main__':
    # a = Widget('a')
    # a.add_action(3, 'date')
    # a.add_action(1, 'time')

    a = Widget()

    print(a.get_output())
