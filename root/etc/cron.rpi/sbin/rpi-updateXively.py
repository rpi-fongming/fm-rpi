#!/usr/bin/env python
import time, os, sys
import eeml
import syslog
import json
import sqlite3 as sqlite

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

def test(mySensor):
    print ("rpi-updateXively test")
    _sensors = mySensor[0]
    print (_sensors)
    CPU_TEMP = getParameter (_sensors,"CPU_TEMP=")
    CPU_DISK_FREE  = getParameter (_sensors,"CPU_DISK_FREE=")
    CPU_DISK_USE  = getParameter (_sensors,"CPU_DISK_USE=")
    CPU_RAM_FREE = getParameter (_sensors,"CPU_RAM_FREE=")
    CPU_RAM_USE = getParameter (_sensors,"CPU_RAM_USE=")
    CPU_UPTIME = getParameter (_sensors,"CPU_UPTIME=")
    
    print (CPU_TEMP,CPU_DISK_FREE,CPU_DISK_USE,CPU_RAM_FREE,CPU_RAM_USE,CPU_UPTIME)
    #print (_sensors)

def Xively_update(mySensor):
    _sensors = mySensor[0]

    CPU_TEMP = getParameter (_sensors,"CPU_TEMP=")
    CPU_DISK_FREE  = getParameter (_sensors,"CPU_DISK_FREE=")
    CPU_DISK_USE  = getParameter (_sensors,"CPU_DISK_USE=")
    CPU_RAM_FREE = getParameter (_sensors,"CPU_RAM_FREE=")
    CPU_RAM_USE = getParameter (_sensors,"CPU_RAM_USE=")
    CPU_UPTIME = getParameter (_sensors,"CPU_UPTIME=")

    # open up your feed
    pac = eeml.Pachube(API_URL, API_KEY)

    #compile data
    pac.update([eeml.Data("CPU_TEMP", CPU_TEMP, unit=eeml.Celsius())])
    pac.update([eeml.Data("CPU_DISK_FREE", CPU_DISK_FREE)])
    pac.update([eeml.Data("CPU_DISK_USE", CPU_DISK_USE)])
    pac.update([eeml.Data("CPU_RAM_FREE", CPU_RAM_FREE)])
    pac.update([eeml.Data("CPU_RAM_USE", CPU_RAM_USE)])
    pac.update([eeml.Data("CPU_UPTIME", CPU_UPTIME)])

    # send data to cosm
    pac.put()    

API_KEY = 'W135Mxs0z9wMXkiiLgIn6WlknYNItIBmHBJYlFhG0N8rKmxJ'
FEED = 723631640
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)

file_db=os.popen("rpi-log.py show_db").readline().replace("\n","")
#print (file_db)
con = sqlite.connect(file_db)

sql = "select eMsg, eType, eEnter from tb_rpiEvent where eType='sensor_update' ORDER BY eID DESC limit 1;"
result = sql_cmd(con,sql)
#print (result[0])
#print (eeml.Celsius())
_SENSOR = result[0]

if (len(sys.argv) == 1):
	Xively_update(_SENSOR)
	sys.exit(0)

if 	(sys.argv[1]=="test"):
	test(_SENSOR)
	sys.exit(0)
    