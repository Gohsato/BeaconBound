
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

def find_corner_fast(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.medianBlur(img,9)

    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector_create()
    # find and draw the keypoints
    kp = fast.detect(img,None)
    # img2 = cv2.drawMatch(img, kp, None, color=(255,0,0))
    # https://github.com/skvark/opencv-python/issues/168 should use drawkeypoints
    img2 = img.copy()
    for marker in kp:
        img2 = cv2.drawMarker(img2, tuple(int(i) for i in marker.pt), color=(255, 0, 0))
    # Print all default params
    print( "Threshold: {}".format(fast.getThreshold()) )
    print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
    print( "neighborhood: {}".format(fast.getType()) )
    print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
    cv2.imshow('fast_true.png',img2)
    # Disable nonmaxSuppression
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img,None)
    print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
    img3 = img.copy()
    for marker in kp:
        img3 = cv2.drawMarker(img3, tuple(int(i) for i in marker.pt), color=(255, 0, 0))
    cv2.imshow('fast_false.png',img3)


if __name__ == '__main__':
    img = cv2.imread('image_1.jpg')
    find_corner_fast(img)
    cv2.waitKey(0)
        