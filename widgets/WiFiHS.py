#!/usr/bin/env python3

import os
import re
import sys
import datetime
import subprocess

from widgets.widget import Widget
from widgets.config import colors, icons

class WiFiHS(Widget):
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
        self.fg = colors['c_gray_l']
        self.icon = icons['ssid']
        self.gaps = (10, 7)
        self.show_text = False

    def update(self):
        cmd = ['pidof', 'hostapd']

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        output = process.communicate()[0]

        if output:
            self.fg = None
        else:
            self.fg = colors['c_gray_l']

    def execute(self, cmd):
        if cmd == 'show':
            cmd = ['/'.join(os.path.realpath(__file__).split('/')[:-1]) + \
                '/utils/floating_term.sh',
                '/home/andrew/.scripts/wifi_hotspot.sh']

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            output = process.communicate()[0]
