#!/usr/bin/env python3

import sys
import json
import subprocess

from utils import set_b_color, set_f_color, set_spacing
from widgets.widget import Widget
from widgets.config import colors, icons

class ws(Widget):
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
        self.icon = None
        self.gaps = (0, 0)

        self.colors_rules = dict()
        self.action = []
        self.action_buttons = []

    def update(self):
        # Get information about workspace situations
        cmd = 'i3-msg -t get_workspaces'

        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

        # Parse this infomation
        info = json.loads(output.decode('UTF-8')) 
        info.sort(key=lambda data: data['num'])
        # Generate resulting string
        result = ''
        for ws in info:
            if ws['focused']:
                result += self._chosen_ws(ws['num'])
            else:
                result += self._normal_ws(ws['num'])

        # print('{}.'.format(result), file=sys.stderr)
        self.value = result
            
    def _chosen_ws(self, num):
        num = ' {} '.format(num)
        return set_f_color(
                set_b_color(
                    set_spacing(num, (3, 3)), colors['c_gray']
                ), colors['c_white']
        )
    
    def _normal_ws(self, num):
        num = ' {} '.format(num)
        return set_f_color(set_spacing(num, (3, 3)), colors['c_white'])



if __name__ == '__main__':
    a = Widget()

    print(a.get_output())
