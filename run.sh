#!/bin/bash

[[ -r p_to_lb ]] || mkfifo p_to_lb
[[ -r lb_to_p ]] || mkfifo lb_to_p
python ./bar.py > p_to_lb < lb_to_p &
lemonbar -p -f "Droid Sans-9" -f "FontAwesome-11" -g1366x22 eDP1 < p_to_lb > lb_to_p

trap 'kill $(jobs -p)' EXIT
