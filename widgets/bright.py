#!/usr/bin/env python3

import os
import subprocess
from widgets.widget import Widget
from widgets.config import colors, icons

class bright(Widget):
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
        self.icon = icons['bright']

    def update(self):
        with open('/sys/class/backlight/intel_backlight/brightness') as br:
            brightness = br.readlines()[0].strip()
        with open('/sys/class/backlight/intel_backlight/max_brightness') as mx:
            maximum = mx.readlines()[0].strip()

        br = int(int(brightness)*100/int(maximum))
        self.value = br

    def execute(self, cmd):
        if not cmd:
            return None

        if cmd == 'scrl_up':
            cmd = 'xbacklight -inc 10'
            subprocess.call(cmd.split(' '), stdout=subprocess.PIPE)
        elif cmd == 'scrl_down':
            cmd = 'xbacklight -dec 10'
            subprocess.call(cmd.split(' '), stdout=subprocess.PIPE)
        else:
            print('Bright: incorrect command.', file=sys.stderr)
