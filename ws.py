#!/usr/bin/env python3

import sys
import i3ipc
from pprint import pprint

i3 = i3ipc.Connection()

def ws_focused(self, e):
    '''
    Reaction to focused workspace.
    Args:
        self: the connection to the ipc
        e: event object
    '''
    print('Change: {}. Old: {}. Current: {}.'.format(
        e.change, e.old, e.current))
    print('Runned windows on the current workspace:')
    for w in e.current.leaves():
        print(w.name)
        print(dir(w))
    print('Runned windows on the old workspace:')
    for w in e.old.leaves():
        print(w.name)

if __name__ == '__main__':
    i3.on('workspace::focus', ws_focused)

    i3.main()
