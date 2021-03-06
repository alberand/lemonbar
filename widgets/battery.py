#!/usr/bin/env python3

import os
import re
import sys
import datetime
import subprocess

from widgets.widget import Widget
from widgets.config import colors, icons

class battery(Widget):
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
        # 0: Normal. (charge > 30% or Plugged)
        # 1: Unplugged. (charge > 30% and unplugged)
        # 2: 30% limit. (charge < 30% and unplugged)
        # 3: 10% limit. (charge < 10% and unplugged)
        # 4: Charging. (charge < 30% and plugged)
        self.status = 0

    def notify(self, title, message, priority=None):
        '''
        Send system notification. 
        Args:
            title: string
            message: string
            priority: string: low, normal, critical
        '''
        if not priority:
            priority = 'normal'
        subprocess.call(['notify-send', 
            '-u',
            '{}'.format(priority),
            '{}'.format(title),
            '{}'.format(message),
        ])

    def update(self):
        '''
        '''
        cmd = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + \
                '/utils/battery'

        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

        string = output.decode('UTF-8')

        # Set tray icon and color
        self.charge = int(re.match('[0-9]+', string).group(0))
        if len(string) < 7 or string[-3:] == 'CHR':
            self.icon = icons['plug']
            self.fg = colors['c_white']
        elif self.charge == 99 or self.charge == 100:
            self.icon = icons['battery_full']
            self.fg = colors['c_white']
        elif self.charge < 10:
            self.icon = icons['battery_empty']
            self.fg = colors['c_red_l']
        elif self.charge < 26:
            self.icon = icons['battery_quarter']
            self.fg = colors['c_yellow_d']
        elif self.charge < 51:
            self.icon = icons['battery_half']
            self.fg = colors['c_white']
        elif self.charge < 76:
            self.icon = icons['battery_tquarter']
            self.fg = colors['c_white']
        else:
            self.icon = icons['battery_full']
            self.fg = colors['c_white']

        # Change status
        if self.status == 0 and self.charge > 26 and len(string) == 7:
            print("Change status.", file=sys.stderr)
            self.notify("Battery", 
                "Cable unplugged. Charge: {}%.".format(self.charge))
            self.status = 1
        elif self.status == 1 and self.charge < 30:
            self.status = 2
        elif self.status == 3 and self.charge < 10:
            subprocess.call("Battery", 
                    "Low battery: {}%.".format(self.charge),
                    "critical")
            self.status = 4
        elif self.status == 2 and self.charge < 30:
            subprocess.call("Battery",
                "Low battery: {}%.".format(self.charge))
            self.status = 3
        elif self.status == 4 and string[-3:] == 'CHR':
            subprocess.call("Battery",
                "Cable is plugged in. Low battery: {}%.".format(self.charge))
        else:
            pass


        if self.show_text:
            self.value = str(self.charge) + '%'
            self.show_text = False
        else:
            self.value = ''

    def execute(self, cmd):
        if cmd == 'show':
            self.show_text = True
