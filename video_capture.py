import cv2
import numpy as np
import imutils
from skimage import measure

cap = cv2.VideoCapture('infra-beacon-2.mp4',0)

while(True):
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    if(not ret):
        break
    frame = cv2.resize(frame, (0,0),None,.4,.4)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blurred = cv2.GaussianBlur(hsv, (11, 11), 0)
    # b,g,r = cv2.split(blurred)

    # cv2.imshow('h',b)
    # cv2.imshow('s',g)
    # cv2.imshow('v',r)
    lower_red = np.array([150,0,200])
    upper_red = np.array([360,30,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    res = cv2.cvtColor(res,cv2.COLOR_HSV2RGB)
    res = cv2.cvtColor(res,cv2.COLOR_RGB2GRAY)
    cv2.imshow('res',res)

    circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=10,minRadius=3,maxRadius=15)
    if(circles is not None):
        circles = np.int16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('detected circles',frame)
    cv2.imshow('frame',frame)

    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)

    k =cv2.waitKey(1)
       

    if k & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()