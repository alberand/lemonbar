#!/usr/bin/env python3

import sys
import time
import select 
import threading 

import i3ipc

from widgets.widget import Widget
from widgets.date import Date
from widgets.temp import Temp
from widgets.internet import Internet
from widgets.ws import Workspaces

class Bar:
    '''
    Object which represent container for widget (time, date, battery, internet
    etc.). Widgets are subclasses of class Widget.
    '''

    def __init__(self):
        self.widgets = list()
        self.timeout = 10
        self.running = True
        self.i3 = i3ipc.Connection()

        # self.i3.on('workspace::focus', lambda i3, event: self.update())
        self.i3.on('workspace::focus', lambda i3, event: print(
            self.get_output(), file=sys.stdout))

        self.i3_loop = threading.Thread(target=self.i3.main)
        self.i3_loop.start()

        self.position_offsets = [0, 0]

    def run(self):
        try:
            while self.running:
                self.update()

                time.sleep(0.1)
        except KeyboardInterrupt:
            print('Exiting')

    def update(self):
        print('Updating.', file=sys.stderr)
        print(self.get_output())
        sys.stdout.flush()

        # cmd = self.read_cmd()
        if cmd:
            self.process_cmd(cmd)

        sys.stdin.flush()

    def stop(self):
        self.running = False

    def process_cmd(self, cmd):
        if not len(cmd):
            return False

        widget_id = cmd[0:2]

        # Find widget.
        for cont in self.widgets:
            if cont['id'] == int(widget_id):
                cont['widget'].execute(cmd[3:])
        # print('cmd "{}" executed'.format(cmd), file=sys.stderr)

    def read_cmd(self):
        '''
        Check if there is something in the sys.stdin buffer. If yes read it.
        '''
        cmd = ''
        if select.select([sys.stdin,], [], [], self.timeout)[0]:
            while True:
                char = sys.stdin.read(1)
                if char == '\n':
                    break
                cmd += char

            sys.stdin.flush()

        return cmd

    # Bar configuration
    def set_timeout(self, timeout):
        '''
        Set update time for the bar. Even that bar is event driven, timeout can
        be set to update bar every n-seconds. By default bar is updated every 10
        seconds.
        Args:
            timeout: integer. If set to '-1' than bar will not periodically
            updated.
        '''
        if timeout == -1:
            self.timeout = None
        else:
            self.timeout = timeout


    # Widgets processing
    def gen_widget_container(self, widget, pos, order=None):
        container = {
                'widget': widget,
                'align': order,
                'position': pos,
                'id': widget.id
        }

        return container

    def find_last_order(self, pos=None):
        '''
        Find last order number with specified position.
        Args:
            pos: position of the widget. 0 - left, 1 - center, 2 - right
        Returns:
            Last order for the given position. If position is not specified than
            max order.
        '''
        if len(self.widgets) == 0:
            return 0

        if not pos:
            return max([container['order'] for container in self.widgets])
        elif pos in range(0, 3):
            return max([cont['order'] if cont['position'] == pos else -1 
                    for cont in self.widgets])
        else:
            print('Position is incorrect. Should be in range 0 - 2.')
            return None

    def find_last_position(self, pos, align):
        if not align in ['l', 'c', 'r']:
            return None

        for cont in self.widgets:
            if cont['align'] != align:
                continue
            else:
                return cont['position'] + pos

        return self.position_offsets[0] if align == 'c' else self.position_offsets[1]

    def add_widget(self, widget, align=None, pos=None):
        '''
        Args:
            widget: widget.Widget instance
            pos: position of the widget in the align position. 
            align: order id of the widget. 'l' - left, 'c' - center, 'r' - right
        '''
        # Check align
        if not align or not align in ['l', 'c', 'r']:
            align = 'r'

        # Check position
        if pos == None:
            pos = len(self.widgets)
        elif pos > len(self.widgets) or not isinstance(pos, int):
            return None
        else:
            pos = self.find_last_position(pos, align)

        self.position_offsets[0 if align == 'c' else 1] += 1

        cont = self.gen_widget_container(widget, pos, align)
        self.widgets.insert(pos, cont)

    def remove_widget(self, widget):
        # TODO update widgets order
        self.position_offsets[0 if align == 'c' else 1] -= 1

        self.widgets.remove(widget)

    # External communications
    def set_stdout(self, stdout):
        pass

    def get_output(self):
        container = '%{{l}}{0} %{{c}}{1} %{{r}}{2}'
        arranged_items = {
                'l': [],
                'c': [],
                'r': []
        }

        for cont in self.widgets:
            arranged_items[cont['align']].append(cont['widget'].get_output())

        result = container.format(
                ''.join(arranged_items['l']), 
                ''.join(arranged_items['c']),
                ''.join(arranged_items['r']))

        return result

if __name__ == '__main__':
    # Init the bar
    bar = Bar()
    bar.set_timeout(2)

    # Create widgets
    a_wid = Internet()
    b_wid = Date()
    c_wid = Temp()
    d_wid = Workspaces()
    e_wid = Widget('e')

    c_wid.add_action(1, 'temp')

    # Add widgets to the bar
    bar.add_widget(a_wid, 'r', 0)
    bar.add_widget(c_wid, 'r', 1)
    bar.add_widget(e_wid, 'r', 2)
    bar.add_widget(b_wid, 'c', 0)
    bar.add_widget(d_wid, 'l', 0)

    # Run mainloop
    bar.run()
