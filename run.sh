#!/bin/bash

mkfifo fifo0 fifo1
python ./test.py > fifo0 < fifo1 &
lemonbar -p -f "Droid Sans-9" -f "FontAwesome-11" -g1366x22 eDP1 < fifo0 > fifo1