#!/usr/bin/env python
import time
import os
import eeml
import sys
import syslog
import json
import sqlite3 as sqlite

def sql_cmd(db_con, sql):
	with db_con:
		cur = db_con.cursor()    
		cur.execute(sql)
		rows = cur.fetchall()
	return (rows)	

API_KEY = 'OdAlic0xBILV5k9HpTR825jwRqmNvMEXhVlR2ixf7SjDKHLU'
FEED = 1277480511
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)

file_path = os.path.dirname(sys.argv[0])
file_db=file_path+"/rpi-event.db"
con = sqlite.connect(file_db)

sql = "select eMsg, eType, eEnter from tb_rpiEvent where eType='sensor_update' ORDER BY eID DESC limit 1;"
result = sql_cmd(con,sql)
for row in result:
	print row
    
CPU_TEMP = 46
CPU_DISK_FREE  = "4G"
CPU_DISK_USE  = "3G"
CPU_RAM_FREE = "1000"
CPU_RAM_USE = "2000"
CPU_UPTIME = "1000"

if (0):
    # open up your feed
    pac = eeml.Pachube(API_URL, API_KEY)

    #compile data
    pac.update([eeml.Data("CPU_TEMP", CPU_TEMP, unit=eeml.Celsius())])
    pac.update([eeml.Data("CPU_DISK_FREE", CPU_DISK_FREE, unit=eeml.Celsius())])
    pac.update([eeml.Data("CPU_DISK_USE", CPU_DISK_USE, unit=eeml.Celsius())])
    pac.update([eeml.Data("CPU_RAM_FREE", CPU_RAM_FREE, unit=eeml.Celsius())])
    pac.update([eeml.Data("CPU_RAM_USE", CPU_RAM_USE, unit=eeml.Celsius())])
    pac.update([eeml.Data("CPU_UPTIME", CPU_UPTIME, unit=eeml.Celsius())])

    # send data to cosm
    pac.put()
