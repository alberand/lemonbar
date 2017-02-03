#!/usr/bin/env python3

import re
import sys
import datetime
import subprocess

from widgets.widget import Widget
from widgets.config import colors, icons

class button(Widget):
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
        self.icon = icons['dropbox']
        self.gaps = (10, 7)
        self.show_text = False

    def update(self):
        '''
        '''
        pass

    def execute(self, cmd):
        print('Call command.', file=sys.stderr)
        if cmd == 'show':
            cmd = ['i3-msg', 'workspace 3; exec /usr/bin/terminator']

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            output = process.communicate()[0]

if __name__ == '__main__':
    a = Widget()

    print(a.get_output())
