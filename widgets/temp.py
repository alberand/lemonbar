#!/usr/bin/env python3

import re
import sys
import datetime
import subprocess

from widgets.widget import Widget
from widgets.config import colors, icons

class temp(Widget):
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
        self.icon = icons['thermometer_half']
        self.gaps = (10, 7)
        self.temp = 0
        self.show_text = False

    def update(self):
        cmd = 'sensors coretemp-isa-0000'

        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

        line = re.findall(r'Physical.*', output.decode('UTF-8'))[0]

        raw_value = line.split()[3]

        self.temp = float(raw_value[1:5])
        if self.temp < 70:
            self.fg = colors['c_white']
            self.icon = icons['thermometer_tquarter']
        elif self.temp < 90:
            self.fg = colors['c_red_l']
            self.icon = icons['thermometer_full']
        else:
            self.fg = colors['c_white']
            self.icon = icons['thermometer_half']

        if self.show_text:
            self.value = self.temp
            self.show_text = False
        else:
            self.value = ''

    def execute(self, cmd):
        if cmd == 'show':
            self.show_text = True
