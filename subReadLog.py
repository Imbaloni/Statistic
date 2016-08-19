#!/usr/bin/python
import subprocess
import sys

f = subprocess.Popen(['tail','-F',"/var/log/syslog.all"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
while True:
    line = f.stdout.readline()
    sys.stdout.write(line)
    