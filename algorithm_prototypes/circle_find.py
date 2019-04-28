
# Trying to isolate bright spots

import numpy as np
import cv2
from matplotlib import pyplot as plt


SWITCH = {
    'blurred':True,
    # 'bright':True,
    'thresh':True,
    'noise':True
}

def find_circle(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.medianBlur(img,7)

    cv2.imshow('blur',img)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,50,
                                param1=30,param2=10 ,minRadius=0,maxRadius=15)

    if(circles is not None):
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def canny(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img,100,200)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    img = cv2.imread('images/image_1.jpg')
    find_circle(img)
    canny(img)
    cv2.waitKey(0)
        