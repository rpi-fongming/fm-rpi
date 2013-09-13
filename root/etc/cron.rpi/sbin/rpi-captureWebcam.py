#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import sys, os,argparse
from datetime import datetime 

def getSerial():
    res = os.popen("cat /proc/cpuinfo | grep Serial | cut -d':' -f2").readline().replace("\n","").strip()
    return(res[8:])

def get_image(_camera):
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = _camera.read()
    return im

def captureWebCam(port,file):
    # Camera 0 is the integrated web cam on my netbook
    camera_port =port
     
    #Number of frames to throw away while the camera adjusts to light levels
    ramp_frames = 10
     
    # Now we can initialize the camera capture object with the cv2.VideoCapture class.
    # All it needs is the index to a camera port.
    print ("connectting to camera")
    camera = cv2.VideoCapture(camera_port)
    print ("flush initial frame")
    # Captures a single image from the camera and returns it in PIL format
     
    # Ramp the camera - these frames will be discarded and are only used to allow v4l2
    # to adjust light levels, if necessary
    for i in xrange(ramp_frames):
        temp =get_image(camera)
    print("Taking image...")
    # Take the actual image we want to keep
    camera_capture = get_image(camera)
#    file = "capture_"+datetime.now().strftime('%Y%m%d_%H%M%S') + '.jpg'
    # A nice feature of the imwrite method is that it will automatically choose the
    # correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, camera_capture)
     
    # You'll want to release the camera, otherwise you won't be able to create a new
    # capture object until your script exits
    del(camera)

try:
    parser = argparse.ArgumentParser(description='Python script that Capture jpg from Webcam')
    parser.add_argument('-p','--port', default=-1, type=int, help='-p --port Webcam port',required=False)
    parser.add_argument('-f','--filename', help='-f --filename The file name/directory for the captured file.',required=True)
    args = parser.parse_args()

    targetfile = args.filename
    port = args.port
    print (port,targetfile)
    captureWebCam (port,targetfile)
   
except:
    print "Error"

#filename = "/run/rpi-"+getSerial() + "_"+datetime.now().strftime('%y%m%d_%H%M%S') + '.jpg'
#captureWebCam (-1,filename)

