#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import sys, os, argparse
from datetime import datetime 

def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])
    
def shell_cmd(cmd):
    _result = os.popen("su -c \"" + cmd + "\"").read()
    _result = _result.replace("\r","")
    _result = _result.replace("\n","")
#    print (cmd)
    return(_result)

sn = "rpi-"+getSerial()
filename = "/run/"+ sn + "_"+datetime.now().strftime('%y%m%d_%H%M%S') + '.jpg'
shell_cmd("rpi-captureWebcam.py -f '"+filename+"'")
shell_cmd("rpi-uploadGdrive.py -f '"+filename+"'" + " -u rpi.fongming@gmail.com -p Fongshek702 -l '" + sn +"'")
shell_cmd("rm " + filename)