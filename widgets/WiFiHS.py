#!/usr/bin/env python3

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
        self.fg = None
        self.icon = icons['ssid']
        self.gaps = (10, 7)
        self.show_text = False

    def execute(self, cmd):
        if cmd == 'show':
            cmd = ['/home/andrew/.scripts/wifi_hotspot.sh']

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            output = process.communicate()[0]
