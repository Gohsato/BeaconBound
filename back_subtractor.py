import numpy as np
import cv2

from matplotlib import pyplot as plt

# cv2.namedWindow('Frame',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('Frame',600,600)
# cv2.namedWindow('mask',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('mask',600,600)
# cv2.namedWindow('res',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('res',600,600)

cap = cv2.VideoCapture('infra-beacon-1.mp4',0)

while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  ret, frame = cap.read()
  ret, frame = cap.read()
  ret, frame = cap.read()
  if ret == True:
 
    frame = cv2.resize(frame, (0,0),None,.4,.4)
    
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # # define range of blue color in HSV
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    # # Threshold the HSV image to get only blue colors
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # # Bitwise-AND mask and original image
    # res = cv2.bitwise_and(frame,frame, mask= mask)


    
    # cframe = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    cv2.imshow("main",frame)

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    keyp = cv2.waitKey(50)
    if keyp & 0xFF == ord('c'):
        cv2.destroyWindow('frame')

    if keyp & 0xFF == ord('s'):
        print("drawing circles")
        # frame = cv2.medianBlur(frame,5)
        ret,frame = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
        # frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        circles = cv2.HoughCircles(frame,cv2.HOUGH_GRADIENT,2,50,param1=50,param2=30,minRadius=0,maxRadius=0)

        # Display the resulting frame
        # circles = np.int16(np.around(circles))
        # for i in circles[0,:]:
        #     # draw the outer circle
        #     cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
        #     # draw the center of the circle
        #     cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

        cv2.imshow('frame',frame)
        while (1):
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    # Press Q on keyboard to  exit
    if keyp & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 


# Closes all the frames
cv2.destroyAllWindows()