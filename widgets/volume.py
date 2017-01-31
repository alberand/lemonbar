#!/usr/bin/env python3

import os
import re
import subprocess
from widgets.widget import Widget
from widgets.config import colors, icons

class volume(Widget):
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
        self.icon = icons['vol']

        self.colors_rules = dict()
        self.action = []
        self.action_buttons = []

    def update(self):
        '''

        TO IMPLEMENT.

        '''
        cmd = 'amixer get -c 1 Master'

        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

        result = re.search('\[\d*%\]', str(output))
        self.value = result.group()[1:-1]

    def execute(self, cmd):
        if not cmd:
            return None

        if cmd == 'scrl_up':
            cmd = 'amixer -c 1 set Master 5%+'
            subprocess.call(cmd.split(' '), stdout=subprocess.PIPE)
        elif cmd == 'scrl_down':
            cmd = 'amixer -c 1 set Master 5%-'
            subprocess.call(cmd.split(' '), stdout=subprocess.PIPE)
        else:
            print('Volume: incorrect command.', file=sys.stderr)


if __name__ == '__main__':
    # a = Widget('a')
    # a.add_action(3, 'date')
    # a.add_action(1, 'time')

    a = Widget()

    print(a.get_output())
