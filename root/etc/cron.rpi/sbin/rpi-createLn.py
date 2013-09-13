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

def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])

file_path = os.getcwd()
cpu_sn = getSerial();
#file_path = os.path.dirname(sys.argv[0])
file_db=file_path+"/rpi-"+cpu_sn+".log.db"
print (file_path, os.path.dirname(sys.argv[0]))
#ln -s {target-filename} {symbolic-filename}

#sys.exit(0)

add_link(file_path +"/rpi-log.py","/usr/local/sbin/rpi-log.py")
add_link(file_path +"/rpi-eventScript","/usr/local/sbin/rpi-eventScript")
add_link(file_path +"/rpi-sensor.py","/usr/local/sbin/rpi-sensor.py")
add_link(file_path +"/rpi-"+cpu_sn+".log.db","/usr/local/sbin/rpi-log.db")
add_link(file_path +"/rpi-bootup.py","/usr/local/sbin/rpi-bootup.py")
add_link(file_path +"/rpi-updateXively.py","/usr/local/sbin/rpi-updateXively.py")
add_link(file_path +"/rpi-updateTwitter.py","/usr/local/sbin/rpi-updateTwitter.py")

print os.popen("ls -l /usr/local/sbin/rpi*").read()

