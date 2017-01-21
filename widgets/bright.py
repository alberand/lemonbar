#!/usr/bin/env python3

import os
import subprocess
from widgets.widget import Widget
from widgets.config import colors, icons

class Bright(Widget):
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

        self.colors_rules = dict()
        self.action = []
        self.action_buttons = []

    def update(self):
        '''

        TO IMPLEMENT.

        '''
        with open('/sys/class/backlight/intel_backlight/brightness') as br:
            brightness = br.readlines()[0].strip()
        with open('/sys/class/backlight/intel_backlight/max_brightness') as mx:
            maximum = mx.readlines()[0].strip()

        br = int(int(brightness)*100/int(maximum))
        self.value = br

    def execute(self, cmd):
        if not cmd:
            return None

        if cmd == 'bright_up':
            cmd = 'xbacklight -inc 10'
            subprocess.call(cmd.split(' '), stdout=subprocess.PIPE)
        elif cmd == 'bright_down':
            cmd = 'xbacklight -dec 10'
            subprocess.call(cmd.split(' '), stdout=subprocess.PIPE)
        else:
            print('Bright: incorrect command.', file=sys.stderr)


if __name__ == '__main__':
    # a = Widget('a')
    # a.add_action(3, 'date')
    # a.add_action(1, 'time')

    a = Widget()

    print(a.get_output())
