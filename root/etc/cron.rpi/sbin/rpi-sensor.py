#!/usr/bin/env python
#
#
import sys,os,thread,threading
from subprocess import call

def shell_cmd(cmd):
	_result = os.popen("su -c \"" + cmd + "\"").read()
	_result = _result.replace("\r","")
	_result = _result.replace("\n","")
#	print(_result)
	return(_result)

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def getDiskSpace():
    p = os.popen("df | grep /dev/root").readline()
    return (p.split()[2:4])
	 
def getRAMinfo():
    p = os.popen('free | grep Mem:').readline()
    return (p.split()[1:4])

def getUptime():
    res = os.popen("cat /proc/uptime | cut -d' ' -f1").readline()
    return(res.replace("\n","").strip())
		
def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])

def getIP():
    res = os.popen("hostname -I").readline().replace("\n","").strip()
    return(res)

def getGateway():
	res = os.popen("route -n | grep UG | awk '{print $2 \":\" $8}'").readline().replace("\n","").strip()
	return(res)

def getpubip(): #Gets the public IP by doing a get of the webpage below
   url = "myip.xname.org:80"
   import httplib, urllib
   headers = {"Content-type": "HTML"}
   params = ''
   conn = httplib.HTTPConnection(url)
   conn.request("GET", "/")
   response = conn.getresponse()
   message = response.status, response.reason
   message = str(message) 
   #print message #print http responce for debugging
   ip = response.read()
   ip = ip.replace("\n","") #get rid of new line character (may not be necessary)
   return ip

def getTempHum():
	res = os.popen('dth11 11 4 | grep Temp').readline().replace("\n","").strip()
	if (res.find("Temp")==-1):
		res = os.popen('dth11 11 4 | grep Temp').readline().replace("\n","").strip()
	if (res.find("Temp")==-1):
		res = os.popen('dth11 11 4 | grep Temp').readline().replace("\n","").strip()
	return(res.replace(",",";").replace("Temp","Temp1").replace("Hum","Hum1"))

def run():
	mySensor = "CPU_TEMP="+getCPUtemperature()+";"
	mySensor += "CPU_UPTIME="+getUptime()+";"
	mySensor += "CPU_SERIAL="+getSerial()+";"
	mySensor += "CPU_DISK_USE="+getDiskSpace()[0]+";"
	mySensor += "CPU_DISK_FREE="+getDiskSpace()[1]+";"
	mySensor += "CPU_RAM_USE="+getRAMinfo()[1]+";"
	mySensor += "CPU_RAM_FREE="+getRAMinfo()[2]+";"
	mySensor += "CPU_LIP="+getIP()+";"
	mySensor += "CPU_PIP="+getpubip()+";"
	mySensor += "CPU_GATEWAY=" + getGateway() + ";"	
	mySensor += getTempHum().replace(",",";") +";"
	eMsg = mySensor
	eType = "sensor_update"
	call(['rpi-log.py', eType, eMsg])

def test():
	myTempHum = getTempHum().replace(",",";")
	print myTempHum
	
	

if (len(sys.argv) == 1):
	run()
	sys.exit(0)
	

if 	(sys.argv[1]=="test"):
	test()
	sys.exit(0)


