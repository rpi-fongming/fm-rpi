#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import sys, os
from subprocess import call

def add_link(target,symbolic):
	if (os.path.exists(symbolic)):
		call(['rm', symbolic])
		print ("rm " + symbolic)
	os.popen("ln -s " + target + " " + symbolic)
	print ("create ln " + target + " " +symbolic)

file_path = os.getcwd()

#ln -s {target-filename} {symbolic-filename}

add_link(file_path +"/rpi-log.py","/usr/local/sbin/rpi-log.py")
add_link(file_path +"/rpi-event.db","/usr/local/sbin/rpi-event.db")
add_link(file_path +"/rpi-eventScript","/usr/local/sbin/rpi-eventScript")
add_link(file_path +"/rpi-sensor.py","/usr/local/sbin/rpi-sensor.py")

print os.popen("ls -l /usr/local/sbin/rpi_*").read()

