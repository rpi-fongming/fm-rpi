import time, cv 
from datetime import datetime 


debug = 0 

def captureImage(): 
     snapped = cv.QueryFrame(capture) 
     cv.SaveImage(datetime.now().strftime('%Y%m%d_%H%M%S') + '.jpg', snapped) 

if __name__ == '__main__': 
	capture = cv.CaptureFromCAM(-1) 
	cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 320)
	cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)


	try: 
		frame = cv.QueryFrame(capture) 
		captureImage() 
		capture = None   
		cv.DestroyAllWindows() 
		
	except KeyboardInterrupt: 
		cv.DestroyAllWindows() 
