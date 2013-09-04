#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#python systemLog.py 'eMsg' 'eType'
#

import sys, os
from subprocess import call
import time

def shell_cmd(cmd):
	_result = os.popen("su -c \"" + cmd + "\"").read()
	_result = _result.replace("\r","")
	_result = _result.replace("\n","")
	print(_result)
	return(_result)

def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])

def getUptime():
    res = os.popen("cat /proc/uptime | cut -d' ' -f1").readline()
    return(res.replace("\n","").strip())

def test():
	print ("log_rpi test" , _UpTime)
	run_softEther()

def run_softEther():
	shell_cmd("iptables -t nat -A POSTROUTING -s 192.168.7.0/24 -j SNAT --to-source 192.168.0.102")
	call(['/etc/init.d/vpnserver',"restart"])
	call(['/etc/init.d/vpnserver',"stop"])
	time.sleep(3)
	call(['/etc/init.d/dnsmasq',"restart"])
	call(['/etc/init.d/vpnserver',"restart"])
	call(['rpi-log.py',"rpi-bootup.py", "start softEther"])


def run_all():
	print ("run all ")
	call(['rpi-log.py',"rpi-bootup.py", "system bootup"])
	run_softEther()
	#modprobe -r lirc_rpi 
	#modprobe lirc_rpi gpio_in_pin=24 gpio_out_pin=23
	#modprobe -r lirc_rpi1
	#modprobe lirc_rpi1 gpio_in_pin=20 gpio_out_pin=21
	#python3 ~/examples/blink &

#########`#############################################################################
## Main function start here
_UpTime = int (float(getUptime()))

if (len(sys.argv) == 1):
	run_all()
	sys.exit(0)

if 	(sys.argv[1]=="test"):
	test()
	sys.exit(0)
