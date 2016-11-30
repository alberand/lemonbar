#!/usr/bin/env python3

from config import colors, icons

# TODO properties instead of GETs/SETs

class Widget:
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
        # Temp
        self.value = value

        self.bg = colors['c_background']
        self.fg = colors['c_white']
        self.icon = icons['laptop']
        self.gaps = (5, 5)

        self.colors_rules = dict()
        self.action = []
        self.action_buttons = []

    def update(self):
        '''

        TO IMPLEMENT.

        '''
        pass

    def add_action(self, button, cmd):
        '''
        Implement if widget should execute any aciont, commands, programs...
        Args:
            button: int. A number ranging from 1 to 5 which maps to the left,
                middle, right, scroll up and scroll down movements.
            cmd: string. Bash command.
        '''
        if not isinstance(button, int):
            return None

        if not button in range(1, 6):
            return None

        self.action.append(cmd)
        self.action_buttons.append(button)

    def remove_action(self, cmd):
        self.action_buttons.pop(self.action.index(cmd))
        self.action.remove(cmd)

    def set_action(self, string, action, button):
        return '%{{A{1}:{2}:}}{0}%{{A}}'.format(string, button, action)

    def set_bg(self, string):
        return '%{{B{1}}}{0}%{{B{1}}}'.format(string, self.bg)

    def set_fg(self, string):
        return '%{{F{1}}}{0}%{{F{1}}}'.format(string, self.fg)

    def set_gaps(self, string):
        return '%{{O{0}}}{1}%{{O{2}}}'.format(self.gaps[0], string, 
                self.gaps[1])

    def get_action(self, string):
        for cmd, button in zip(self.action, self.action_buttons):
            string = self.set_action(string, cmd, button)

        return string

    def get_output(self):
        '''
        Returns generated string for lemonbar.
        '''
        val = self.update() 
        if val:
            self.value = val

        string = ' {} {} '.format(self.icon, self.value)
        if self.bg:
            string = self.set_bg(string)
            
        if self.fg:
            string = self.set_fg(string)

        if self.gaps:
            string = self.set_gaps(string)

        if len(self.action):
            string = self.get_action(string)

        return string

if __name__ == '__main__':
    # a = Widget('a')
    # a.add_action(3, 'date')
    # a.add_action(1, 'time')
    a = Date()
    b = Internet()

    print(a.get_output())
    print(b.get_output())
