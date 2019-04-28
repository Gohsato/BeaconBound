
# Trying to isolate bright spots

import numpy as np
import cv2
from matplotlib import pyplot as plt

def change_color(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv[:,:,0] = 0
    hsv[:,:,1] = 0


    bg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    average = img.mean(axis=0).mean(axis=0)
    print(average)

    # b,g,r = cv2.split(img)

    # hue = np.zeros(img.shape, dtype=np.uint8)
    # im = cv2.mixChannels([b], [hue], [0,0])

    # print(im)
    hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('valence', hsv)
    cv2.imshow('blackwith', bg)


if __name__ == '__main__':
    img = cv2.imread('image_1.jpg')
    change_color(img)
    cv2.waitKey(0)
