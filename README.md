Lemonbar Python generator
===============================================================================
This application written to simplify string generation for lemonbar.

There is also shell script which create two temporarily FIFO queue to connect
lemonbar output to application input and vice versa. It's run both applications
and connect them. By terminating it all child will be also killed.

Run:
```
./run.sh
```

TODO
===============================================================================
* Integration with google-calendar. When event is coming date widget change its
  color and send notification via notify-send.
* Short-cuts. We are in keyboard-oriented environment.
* Configuration file and parser
