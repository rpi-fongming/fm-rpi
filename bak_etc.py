#!/usr/bin/env python
#
#
import sys,os,thread,threading
from subprocess import call

def shell_cmd(cmd):
	_result = os.popen("su -c \"" + cmd + "\"").read()
	_result = _result.replace("\r","")
	_result = _result.replace("\n","")
	return(_result)

def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])

#_HOSTNAME=shell_cmd("hostname") 
myDate = shell_cmd ("date")


print ("remove /home/pi/fm-rpi/root/etc")
print ("copy /etc /home/pi/fm-rpi/root")
#shell_cmd("rm -r /home/pi/fm-rpi/root/etc")
#shell_cmd("cp /etc ./root -r")

#tar -zcvf $_IP.tar.gz /etc
call(["git --git-dir '/home/pi/fm-rpi'", 'add *'])

#shell_cmd ("git add *")
#shell_cmd ("git commit -m 'regular backup from " + getSerial() + myDate + "'")
#shell_cmd ("git push origin master")
