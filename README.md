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
Widgets
===============================================================================
Bar is delivered with a few basics widgets such as workspaces, date and time,
internet, power, processor temperature, brightness and volume. You can add
custom widgets by creating widget class in **widgets** catalog. 

**IMPORTANT**: Your class name should be the same as file name and have only 
lower case letters.

Widgets have two basic functions __update__ and __execute__. First one is used
to get widget value which will be latter formatted and sent to lemonbar. Second
function is responsible for action which change widget behavior. Look at the 
example widgets to better understand how to write you own.

After creating widget you need to add it into configuration file, by default it
is **config.ini**.

TODO
===============================================================================
* Integration with google-calendar. When event is coming date widget change its
  color and send notification via notify-send.
* Short-cuts. We are in keyboard-oriented environment.
* Configuration file and parser
