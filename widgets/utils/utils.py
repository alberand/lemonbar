#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.config import icons

#==============================================================================
# Files with some useful function for generating output for lemonbar.
#==============================================================================

def set_f_color(string, color):
    '''
    Set foreground color for string.
    Args:
        string: str
        color: color in hex representation, should be with '#' sign. 
               For example: #FFFFFF
    Returns:
        string
    '''
    return '%{{F{0}}}{1}%{{F-}}'.format(color, string)

def set_b_color(string, color):
    '''
    Set background color for string.
    Args:
        string: str
        color: color in hex representation, should be with '#' sign. 
            For example: #FFFFFF
    Returns:
        string
    '''
    return '%{{B{0}}}{1}%{{B-}}'.format(color, string)

def set_spacing(string, spacing=(0, 0)):
    '''
    Set spacing for string.
    Args:
        string: str
        spacing: tuple with left and right spacing in pixels
    Returns:
        string
    '''
    return '%{{O{0}}}{1}%{{O{2}}}'.format(spacing[0], string, spacing[1])

def set_icon(string, icon, position=0):
    '''
    Add icon to the string.
    Args:
        string: str
        icon: string which contins unicode code of needed icon. For example for
            the font Awesome for a clock icon icon='\uf017'.
        position: position of the icon. If 0 left, if 1 right.
    Returns:
        string
    '''
    if position:
        return '{string} {icon}'.format(icon=icons[icon], string=string)
    else:
        return '{icon} {string}'.format(icon=icons[icon], string=string)
