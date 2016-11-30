#!/usr/bin/env python
# -*- coding: utf-8 -*-

#==============================================================================
# As arguments this scripts receive string and some style appereance. This data
# is used to generate string for lemonbar.
# 
# So, it is used to add icons, background and foreground color for some text.
#==============================================================================
import sys
import argparse
from utils import *
from config import colors, icons

# Create parser
parser = argparse.ArgumentParser(description=
        '''Generates string for lemonbar, with some styel appearence, such 
        as icon, foreground, background colors.''')

# Add sting
parser.add_argument(
        '-t', '--text', type=str, help='Text message.', required=True,
        metavar='"text"'
)

# Add color arguments
parser.add_argument(
        '-f', '--foreground', type=str, help='''Foreground color in hex format.
        Without # sign.''',
        metavar=('XXXXXX',)
)

parser.add_argument(
        '-b', '--background', type=str, help='''Background color in hex format.
        Without # sign.''',
        metavar=('XXXXXX',)
)

# Add icon argument
parser.add_argument(
        '-i', '--icon', type=str, choices=list(icons.keys()), metavar='name',
        help='''Icon. List of all icons can be found in config.py file. 
        Icons to choose: {0}'''.format(list(icons.keys()))
)

parser.add_argument(
        '-p', '--position', type=str, help='''Icon position. Using this argument
        you need to specify icon argument. Otherwise this will not affect
        output.''', 
        choices={'left': 0, 'right': 1}
)

# Add spacing argument
parser.add_argument(
        '-s', '--spacing', nargs=2, type=int, metavar=('int', 'int'),
        help='Spacing on the left and right sides.', 
)



args = parser.parse_args()
result = args.text

if args.icon and not args.position:
    result = set_icon(result, args.icon)
elif args.icon and args.position:
    result = set_icon(result, args.icon, args.position)

if args.spacing:
    result = set_spacing(result, args.spacing)

if args.foreground:
    result = set_f_color(result, '#' + args.foreground)

if args.background:
    result = set_b_color(result, '#' + args.background)

print(result)
