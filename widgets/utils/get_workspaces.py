#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import subprocess
from utils import *
from config import colors, icons

#==============================================================================
# This script is used to generate string for lemonbar to display workspaces.
# Returns '%{F#FFFFFF}%{B#000000}1%{F-}%{B-}%{F#555555}%{#000000}2%{F-}%{B-}'
#==============================================================================

# Functions to generate coresponding output
def choosen_workspace(num):
    num = ' ' + str(num) + ' '
    return set_f_color(
            set_b_color(
                set_spacing(num, (3, 3)), colors['c_background']
            ), colors['c_foreground']
    )

def normal_workspace(num):
    num = ' ' + str(num) + ' '
    return set_f_color(
            set_b_color(
                set_spacing(num, (3, 3)), colors['c_black_l']
            ), colors['c_foreground']
    )

# Get information about workspace situations
cmd = 'i3-msg -t get_workspaces'

process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

# Parse this infomation
info = json.loads(output.decode('UTF-8')) 
info.sort(key=lambda data: data['num'])
# If you want to look uncomment this line. There a lot of interesting
# infomation.
# import pprint
# pprint.pprint(info)

# Generate resulting string
result = ''
for ws in info:
    if ws['focused']:
        result += choosen_workspace(ws['num'])
    else:
        result += normal_workspace(ws['num'])

# Send it to output. If you want to run this scripts straings with lemonbar you
# need to add while loop. Because this sctipt will end.
print(result)
