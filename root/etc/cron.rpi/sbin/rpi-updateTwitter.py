#!/usr/bin/env python

import sys,os,thread,threading
import tweepy
import sqlite3 as sqlite

CONSUMER_KEY = 'GvCF4RA5wnB1W25FvOfWvA'
CONSUMER_SECRET = '4NCGsZV6qqIEi0Ux4EI2yY1neTWifnY3pAHANlm5k'
ACCESS_KEY = '1654721785-78Eqt2R5uLvghITw3ux7GarSdtMdNGmG3eOnAWw'
ACCESS_SECRET = 'v6Q1zEpTpLOCbpn5ZJDV8as71yrARitY5m3COxXA'


def shell_cmd(cmd):
	_result = os.popen("su -c \"" + cmd + "\"").read()
	_result = _result.replace("\r","")
	_result = _result.replace("\n","")
#	print(_result)
	return(_result)

def sql_cmd(db_con, sql):
	with db_con:
		cur = db_con.cursor()    
		cur.execute(sql)
		rows = cur.fetchall()
	return (rows)	

def getParameter(words, key):
#    print (key,words)
    res = ""
    res_begin = words.find(key)
    if (res_begin !=-1):
        res_end = words.find(";",res_begin)
        if (res_end == -1):
            res_end = len(words)
        res = words[res_begin:res_end].replace(key,"")
    return (res)

def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])
    
def twitter_update(msg):
    myStatus = _myHost + " > " + msg
    print myStatus
    try:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = tweepy.API(auth)
        api.update_status(myStatus)
        return ("1")
    except:
        return ("0")

def run(sensors):
    ENV_TEMP_1 = "TEMP1=" + getParameter (sensors,"Temp1 = ") + ":"
    ENV_HUM_1 = "HUM1=" + getParameter (sensors,"Hum1 = ")+ ":"
    ENV_TEMP_2 = "TEMP2=" + getParameter (sensors,"Temp2 = ")+ ":"
    ENV_HUM_2 = "HUM2=" + getParameter (sensors,"Hum2 = ")+ ":"
    msg = _myLIP + ":" + _myPIP + ":" + _myUptime + ":" + ENV_TEMP_1 + ENV_HUM_1 + ENV_TEMP_2 + ENV_HUM_2  
    result = twitter_update(msg)

def twitter_bootup():
    BootMsg = "System Boot up " + _myLIP + ":" + _myPIP + ":" + _myUptime
    result = twitter_update(BootMsg)
    print ("result - > " + result)
    if (result=="1"):
        sql_cmd(con,"update tb_rpiStatus set boot_twitter = '1'")    

def test():
    print ("test")
    

file_db=os.popen("rpi-log.py show_db").readline().replace("\n","")
con = sqlite.connect(file_db)
_BOOT_TWITTER = sql_cmd(con,"select boot_twitter from tb_rpiStatus limit 1")[0][0]
_mySensor = sql_cmd(con,"select eMsg, eType, eEnter from tb_rpiEvent where eType='sensor_update' ORDER BY eID DESC limit 1;")[0][0]
#print (_mySensor)
_myLIP = getParameter(_mySensor,"CPU_LIP=")
_myPIP = getParameter(_mySensor,"CPU_PIP=")
_myUptime = getParameter(_mySensor,"CPU_UPTIME=")
_myDate = shell_cmd("date +\"%Y%m%d:%H%M%S\"")
_myHost = "rpi-" + getSerial()
#_myUptime = shell_cmd("uptime")

if (_BOOT_TWITTER == '0'):
    twitter_bootup()        

if (len(sys.argv) == 1):
    run(_mySensor)
    sys.exit(0)

if 	(sys.argv[1]=="test"):
	test()
	sys.exit(0)






