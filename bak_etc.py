#!/usr/bin/env python
#
#
import sys,os,thread,threading

def shell_cmd(cmd):
	_result = os.popen("su -c \"" + cmd + "\"").read()
	_result = _result.replace("\r","")
	_result = _result.replace("\n","")
	return(_result)

def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])

#_HOSTNAME=shell_cmd("hostname") 
#_IP=shell_cmd("hostname -I | cut -d' ' -f1")
#print (_HOSTNAME,_IP)
print ("copy /etc /home/pi/fm-rpi/root")
shell_cmd("cp /etc ./root -r")

#tar -zcvf $_IP.tar.gz /etc
shell_cmd ("git add *")
shell_cmd ("git commit -m \"regular backup from " + getSerial() + "\"")
shell_cmd ("git push origin master")
