#!/usr/bin/env python
#
#
import sys,os,thread,threading
import time
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
   try: 
   	conn = httplib.HTTPConnection(url)
   	conn.request("GET", "/")
  	response = conn.getresponse()
   	message = response.status, response.reason
   	message = str(message) 
   	#print message #print http responce for debugging
   	ip = response.read()
   	ip = ip.replace("\n","") #get rid of new line character (may not be necessary)
   	return ip
   except:
	return ("0.0.0.0")	
	
def getDTH11(pin):
	cmd = "dth11 11 " + str(pin) + "  | grep Temp"
#	print (cmd)
	res = os.popen(cmd).readline().replace("\n","").strip()
#	print (res)
	if (res.find("Temp")==-1):
		res = os.popen('dth11 11 " + pin + "  | grep Temp').readline().replace("\n","").strip()
	if (res.find("Temp")==-1):
		res = os.popen('dth11 11 " + pin + "  | grep Temp').readline().replace("\n","").strip()
	return(res.replace(",",";"))


def getDTH11ex(pin):
    cmd = "dth11 11 " + str(pin) + "  | grep Temp"
    count = 0
    res = os.popen(cmd).readline().replace("\n","").strip()
    #	print (res)
    while ((res.find("Temp")==-1) & (count <= 5)):
        res = os.popen(cmd).read()
        time.sleep(1)
        count =count +1
#        print (count, res)
    
#    print (res)
    return(res.replace(",",";").replace("\n","").strip())


def run():
	mySensor = "CPU_TEMP="+CPU_TEMP+";"
	mySensor += "CPU_UPTIME="+CPU_UPTIME+";"
	mySensor += "CPU_DISK_USE="+CPU_DISK_USE+";"
	mySensor += "CPU_DISK_FREE="+CPU_DISK_FREE+";"
	mySensor += "CPU_RAM_USE="+CPU_RAM_USE+";"
	mySensor += "CPU_RAM_FREE="+CPU_RAM_FREE+";"
	mySensor += "CPU_LIP="+CPU_LIP+";"
	mySensor += "CPU_PIP="+CPU_PIP+";"
	mySensor += "CPU_GATEWAY=" + CPU_GATEWAY + ";"	
	mySensor += TEMPHUM1 +";"
	mySensor += TEMPHUM2 +";"
	eMsg = mySensor
	eType = "sensor_update"
	call(['rpi-log.py', eType, eMsg])


def test():
#	print getpubip()
    print (getDTH11ex(4))
    print (getDTH11ex(25))
#    network_reconnect()


CPU_TEMP=getCPUtemperature()
CPU_UPTIME=getUptime()
CPU_SERIAL=getSerial()
CPU_DISK_USE=getDiskSpace()[0]
CPU_DISK_FREE=getDiskSpace()[1]
CPU_RAM_USE=getRAMinfo()[1]
CPU_RAM_FREE=getRAMinfo()[2]
CPU_LIP=getIP()
CPU_PIP=getpubip()
CPU_GATEWAY=getGateway()
TEMPHUM1 = getDTH11ex(4).replace(",",";").replace("Temp","Temp1").replace("Hum","Hum1")
TEMPHUM2 = getDTH11ex(25).replace(",",";").replace("Temp","Temp2").replace("Hum","Hum2") 

if (len(sys.argv) == 1):
	run()
	sys.exit(0)
	

if 	(sys.argv[1]=="test"):
	test()
	sys.exit(0)


