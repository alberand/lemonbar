#!/bin/bash

# Script which create floaging terminal in i3 windows manager. Than ask user 
# for root password and run script thrown as first argument with root 
# privileges.

if [[ "$#" -lt "1" ]]; then
    echo "Need callback function to call with root privilages."
    exit 1
fi

DISPLAY=:0 i3-msg `exec terminator --geometry 683x2+341+34 -e "sudo nohup $1"`
sleep 0.1
DISPLAY=:0 i3-msg 'floating enable'
