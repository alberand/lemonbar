# Lemonbar Python generator
This application written to simplify string generation for lemonbar. It's python
little program to generate system information report (internet status, battery
charge, brightness of the display etc.). 

By running this program you will see formatted message periodically printed to
the standard output. Connecting it to lemonbar (for example by pipeline | on
unix systems) will result in system status bar. 

There is also shell script which create two temporarily FIFO queue to connect
lemonbar output to application input and vice versa. It's run both applications
and connect them. By terminating it all child will be also killed.

Run:
```
./run.sh
```
# Widgets
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

List of currently available widgets can be found in _widgets_ directory.
Possibly they will need to be change for you system. All those scripts were
written for usage on Arch Linux.

# TODO
* Integration with google-calendar. When event is coming date widget change its
  color and send notification via notify-send.
* Short-cuts. We are in keyboard-oriented environment.
* For i3 implement root password asking dialog to run sudo scripts.

# References
- [Lemonbar Github](https://github.com/LemonBoy/bar)
- [i3 windows manager](https://i3wm.org/)
