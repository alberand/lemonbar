#!/usr/bin/env python3

from config import colors, icons

# TODO properties instead of GETs/SETs

class Widget:
    '''
    Abstrac class for all lemonbar widgets.
    '''

    def __init__(self):
        '''
        Params:
            bg: background color
            fg: foreground color
            icon: icon
            icon_p: position of the icon. 0 to the left of the text, 1 to the
            right of the text.
        '''
        self.bg = colors['c_background']
        self.fg = colors['c_white']
        self.icon = icons['laptop']
        self.icon_p = 0

        self.colors_rules = dict()

    def update(self):
        '''
        Update widget status.
        '''
        pass

    def action(self):
        '''
        Implement if widget should execute any aciont, commands, programs...
        '''
        pass

    def get_output(self):
        '''
        Returns generated string for lemonbar.
        '''
        return ' Widget =) '
