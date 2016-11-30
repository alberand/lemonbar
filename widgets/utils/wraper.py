#!/usr/bin/env python
# -*- coding: utf-8 -*-
    with open('/sys/class/backlight/intel_backlight/brightness') as br:
        brightness = br.readlines()[0].strip()
    with open('/sys/class/backlight/intel_backlight/max_brightness') as mx:
        maximum = mx.readlines()[0].strip()
    return int(int(brightness)*100/int(maximum))

def get_volume():
    cmd = 'amixer get -c 1 Master'

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

    result = re.search('\[\d*%\]', str(output))
    return result.group()[1:-1]

def get_key_layout():
    cmd = ' xkb-switch'

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

    return output[:-1].decode('utf-8')

def print_line(message):
    """ Non-buffered printing to stdout. """
    sys.stdout.write(message + '\n')
    sys.stdout.flush()

def read_line():
    """ Interrupted respecting reader for stdin. """
    # try reading a line, removing any extra whitespace
    try:
        line = sys.stdin.readline().strip()
        # i3status sends EOF, or an empty line
        if not line:
            sys.exit(3)
        return line
    # exit on ctrl-c
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    # Skip the first line which contains the version header.
    print_line(read_line())

    # The second line contains the start of the infinite array.
    print_line(read_line())

    while True:
        line, prefix = read_line(), ''
        # ignore comma at start of lines
        if line.startswith(','):
            line, prefix = line[1:], ','

        j = json.loads(line)
        # insert information into the start of the json, but could be anywhere
        # display brightness as a percentage
        j.insert(0, {'full_text' : '%s' % get_key_layout(), 'name' : 'layout'})
        j.insert(0, {'full_text' : ' %s%%' % get_brightness(), 'name' : 'bright'})
        j.insert(0, {'full_text' : ' %s' % get_volume(), 'name' : 'volume'})
        # kernel version
        #j.insert(0, {'full_text' : ' %s' % get_kernel(), 'name' : 'kernel'})
        # and echo back new encoded json
        print_line(prefix+json.dumps(j))
