#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import subprocess

cmd = 'amixer get -c 1 Master'

process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
output = process.communicate()[0]

result = re.search('\[\d*%\]', str(output))
print(result.group()[1:-1])
