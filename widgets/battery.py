#!/usr/bin/env python3

import os
import re
import sys
import datetime
import subprocess

from widgets.widget import Widget
from widgets.config import colors, icons

class Battery(Widget):
    '''
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
        self.icon = icons['battery_full']
        self.gaps = (10, 7)
        self.charge = 0
        self.show_text = False

        self.colors_rules = dict()
        self.action = []
        self.action_buttons = []

    def update(self):
        '''

        TO IMPLEMENT.

        '''
        cmd = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + \
                '/utils/battery'

        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

        string = output.decode('UTF-8')

        self.charge = int(re.match('[0-9]+', string).group(0))
        if len(string) < 7 or string[-3:] == 'CHR':
            self.icon = icons['plug']
            self.fg = colors['c_white']
        elif self.charge == 99 or self.charge == 100:
            self.icon = icons['battery_full']
            self.fg = colors['c_white']
        elif self.charge < 76:
            self.icon = icons['battery_tquarter']
            self.fg = colors['c_white']
        elif self.charge < 51:
            self.icon = icons['battery_half']
            self.fg = colors['c_white']
        elif self.charge < 26:
            self.icon = icons['battery_quarter']
            self.fg = colors['c_yellow_d']
        elif self.charge < 10:
            self.icon = icons['battery_empty']
            self.fg = colors['c_red_l']
        else:
            self.icon = icons['battery_full']
            self.fg = colors['c_white']

        if self.show_text:
            self.value = str(self.charge) + '%'
            self.show_text = False
        else:
            self.value = ''

    def execute(self, cmd):
        if cmd == 'batt':
            self.show_text = True

if __name__ == '__main__':
    a = Widget()

    print(a.get_output())
