#!/usr/bin/env python3

import time
from widget import Widget

class Bar:
    '''
    Object which represent container for widget (time, date, battery, internet
    etc.). Widgets are subclasses of class Widget.
    '''

    def __init__(self):
        self.widgets = list()
        self.timeout = 10
        self.running = True

    def run(self):
        while self.running:
            print(self.get_output())
            time.sleep(self.timeout)

    def stop(self):
        self.running = False

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
                'position': pos
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

        return pos

    def add_widget(self, widget, align=None, pos=None):
        '''
        Args:
            widget: widget.Widget instance
            pos: position of the widget in the align position. 
            align: order id of the widget. 'l' - left, 'c' - center, 'r' - right
        '''
        if not align:
            align = 'r'

        if pos == None:
            pos = len(self.widgets)
        else:
            pos = self.find_last_position(pos, align)
            print(pos)

        cont = self.gen_widget_container(widget, pos, align)

        self.widgets.insert(pos, cont)

    def remove_widget(self, widget):
        # TODO update widgets order
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
    a_wid = Widget('a')
    b_wid = Widget('b')
    c_wid = Widget('c')
    d_wid = Widget('d')
    e_wid = Widget('e')

    # Add widgets to the bar
    bar.add_widget(a_wid)
    bar.add_widget(b_wid, 'c', 0)
    bar.add_widget(c_wid, 'r', 0)
    bar.add_widget(d_wid, 'l', 0)
    bar.add_widget(e_wid, 'r', 0)

    # Run mainloop
    bar.run()
