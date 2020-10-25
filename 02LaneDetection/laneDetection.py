'''
https://www.youtube.com/watch?v=aXqoPiMPhDw
Self Driving Car with Lane Detection using Raspberry Pi | OpenCV p.1 (2020)
k
'''

import cv2
import numpy as np
import utlis

def getLaneCurve(img):

    imgCopy = img.copy()

    #Step1
    imgThres = utlis.thresholding(img)

    #Step2
    h,w,c = img.shape
    points = utlis.valTrackbars()
    imgWarp = utlis.warpImg(img,points,w,h)
    imgWarpPoints  = utlis.drawPoints(imgCopy,points)

    cv2.imshow("Thres", imgThres)
    cv2.imshow("Warp", imgWarp)
    cv2.imshow("Warp Points", imgWarpPoints)

    return None


if __name__ == '__main__':
    cap = cv2.VideoCapture('vid1.mp4')
    intialTracbarVals = [110,80,20,214]
    utlis.initializeTrackbars(intialTracbarVals)
    frameCounter = 0
    
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter = 0
            
        success, img = cap.read()
        img = cv2.resize(img,(480,240))
        getLaneCurve(img)

        cv2.imshow('Vid',img)
        cv2.waitKey(1) #wait for one milisecond


        

