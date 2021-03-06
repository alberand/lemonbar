#!/bin/bash

#==============================================================================
# Runs python script which generate string output sent to the lemonbar via FIFO
# file. STDOUT of lemonbar is also connected to python script to generate
# responses for the mouse commands.
#==============================================================================
DIRECTORY="$( cd "$( dirname "$0" )" && pwd )"

# Create FIFO files to communicate between processes
[[ -r /tmp/p_to_lb ]] || mkfifo /tmp/p_to_lb
[[ -r /tmp/lb_to_p ]] || mkfifo /tmp/lb_to_p

trap 'kill -TERM $python_pid' TERM INT
# Run python script
python $DIRECTORY/bar.py > /tmp/p_to_lb < /tmp/lb_to_p &
python_pid=$!

echo "PID of python process: $python_pid"

# Run lemonbar
lemonbar -p -f "Droid Sans-9" -f "FontAwesome-11" -g1366x22 eDP1 < /tmp/p_to_lb > /tmp/lb_to_p

# Kill all when exiting
# Lemonbar will automaticly terminates when lost input connection
echo -e "\rExiting."
wait $python_pid
trap - TERM INT
wait $python_pid
EXIT_STATUS=$?

rm  /tmp/p_to_lb /tmp/lb_to_p
