#!/usr/bin/env python
import time
import os
import eeml
import sys
import syslog
import json


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

API_KEY = 'OdAlic0xBILV5k9HpTR825jwRqmNvMEXhVlR2ixf7SjDKHLU'
FEED = 1277480511
API_URL = '/v2/feeds/{feednum}.xml' .format(feednum = FEED)

CPU_temp = getCPUtemperature()
DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_free  = DISK_stats[1]
DISK_perc  = DISK_stats[3]
RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used  = round(int(RAM_stats[1]) / 1000,1)
RAM_free  = round(int(RAM_stats[2]) / 1000,1)

# open up your feed
pac = eeml.Pachube(API_URL, API_KEY)

#compile data
pac.update([eeml.Data("CPU_Temperature", CPU_temp, unit=eeml.Celsius())])
pac.update([eeml.Data("Disk_free", DISK_free, unit=eeml.Celsius())])
pac.update([eeml.Data("RAM__Used", RAM_used, unit=eeml.Celsius())])
pac.update([eeml.Data("RAM_Free", RAM_free, unit=eeml.Celsius())])

# send data to cosm
pac.put()