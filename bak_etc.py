#!/usr/bin/env python
#
#
import sys,os,thread,threading

def shell_cmd(cmd):
	_result = os.popen("su -c \"" + cmd + "\"").read()
	_result = _result.replace("\r","")
	_result = _result.replace("\n","")
	return(_result)

_HOSTNAME=shell_cmd("hostname") 
_IP=shell_cmd("hostname -I | cut -d' ' -f1")
print (_HOSTNAME,_IP)
print ("copy /etc ./root/etc")
#shell_cmd("cp /etc ./root/etc -r")

#cp /etc ./root/$_IP/etc -r
#tar -zcvf $_IP.tar.gz /etc
#git add *
#git commit -m "regular backup"
#git push origin master