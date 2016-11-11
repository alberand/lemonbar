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
                'order': order,
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


    def add_widget(self, widget, pos=None, order=None):
        '''
        Args:
            widget: widget.Widget instance
            pos: position of the widget. 0 - left, 1 - center, 2 - right
            order: order id of the widget
        '''
        if not order:
            order = self.find_last_order(pos) + 1

        cont = self.gen_widget_container(widget, pos, order)
        self.widgets.insert(order, cont)

    def remove_widget(self, widget):
        # TODO update widgets order
        self.widgets.remove(widget)

    # External communications
    def set_stdout(self, stdout):
        pass

    def get_output(self):
        container = '%{{l}}{0} %{{c}}{1} %{{r}}{2}'
        pos_items = {
                'left': [],
                'center': [],
                'right': []
        }

        for cont in self.widgets:
            cont['widget']

        result = container.format(
            pos_items
        )
        result = delimeter.join(
                [wid['widget'].get_output() for wid in self.widgets])

        return result

if __name__ == '__main__':
    # Init the bar
    bar = Bar()
    bar.set_timeout(2)

    # Create widgets
    a_wid = Widget('alpha')
    b_wid = Widget('beta')
    c_wid = Widget('gamma')
    d_wid = Widget('theta')

    # Add widgets to the bar
    bar.add_widget(a_wid)
    bar.add_widget(c_wid)
    bar.add_widget(b_wid)

    # Run mainloop
    bar.run()
