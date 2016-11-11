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
    def gen_widget_container(self, wid, pos, order=None):
        container = dict()

        container['wid'] = widget
        container['order'] = order
        container['position'] = pos

        return container

    def add_widget(self, widget, pos, order=None):
        '''
        Args:
            widget: widget.Widget instance
            pos: position of the widget. 0 - left, 1 - center, 2 - right
            order: order id of the widget
        '''
        # TODO add widgets in correct order
        self.widgets.insert(order, widget)

    def remove_widget(self, widget):
        # TODO update widgets order
        self.widgets.remove(widget)

    # External communications
    def set_stdout(self, stdout):
        pass

    def get_output(self):
        delimeter = ''

        result = delimeter.join([wid.get_output() for wid in self.widgets])

        return result

if __name__ == '__main__':
    # Init the bar
    bar = Bar()
    bar.set_timeout(2)

    # Create widgets
    a_wid = Widget()
    b_wid = Widget()
    c_wid = Widget()

    # Configure widgets
    for i, wid in enumerate([a_wid, b_wid, c_wid]):
        if not wid.is_order_set():
            wid.order = i

    # Add widgets to the bar
    bar.add_widget(a_wid)
    bar.add_widget(b_wid)
    bar.add_widget(c_wid)

    # Run mainloop
    bar.run()
