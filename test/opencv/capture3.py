import sys,os,thread,threading,time
import cv2.cv as cv

capture = cv.CaptureFromCAM(-1)
time.sleep(3) 
cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,  640)
cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

img = cv.QueryFrame(capture)

print "Captured "
cv.SaveImage("output.jpg",img)