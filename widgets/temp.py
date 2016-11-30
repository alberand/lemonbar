#!/usr/bin/env python3

import datetime
from widgets.widget import Widget
from config import colors, icons

class Temp(Widget):
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

        self.bg = colors['c_background']
        self.fg = colors['c_white']
        self.icon = icons['clock']
        self.gaps = (10, 7)

        self.colors_rules = dict()
        self.action = []
        self.action_buttons = []

    def update(self):
        '''

        TO IMPLEMENT.

        '''
        cmd = 'sensors coretemp-isa-0000'

        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

        line = re.findall(r'Physical.*', output.decode('UTF-8'))[0]
        return 

        raw_value = line.split()[3]

        temp = float(raw_value[1:5])
        if temp < 70:
            self.fg = colors['c_white'])
        elif temp < 90:
            self.fg = colors['c_red_l'])
        else:
            self.fg = colors['c_white'])

if __name__ == '__main__':
    a = Widget()

    print(a.get_output())
