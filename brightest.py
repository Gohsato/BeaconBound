
# Trying to isolate bright spots

import numpy as np
import cv2
from matplotlib import pyplot as plt

def deviation(img):
    orig = img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Config
    blur_radius = 41

    # blurring
    # blurred_img = cv2.GaussianBlur(img,(blur_radius,blur_radius),0)
    blurred_img = cv2.medianBlur(img,7)

    cv2.imshow('blurred',blurred_img)

    # Find Brghtest Pixel and circle
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blurred_img)
    image = orig.copy()
    circle_radius = 25
    cv2.circle(image, maxLoc, circle_radius, (255, 0, 0), 2)


    cv2.imshow('brightest',image)

    avg = blurred_img.mean()
    # print(f"Avg: {avg}, Max: {maxVal}")

    dev = num_pix = np.around(maxVal/avg,decimals=3)
    return dev

if __name__ == '__main__':
    img = cv2.imread('images/image_1.jpg')
    deviation(img)
    cv2.waitKey(0)