
# Trying to isolate bright spots

import numpy as np
import cv2
from matplotlib import pyplot as plt

while(True):
    print(cv2.__file__)

    img = cv2.imread('images/image_faulty.jpg',0)

    print(img.shape)

    orig = img

    # blurring
    blur_radius = 51
    blurred_img = cv2.GaussianBlur(img,(blur_radius,blur_radius),0)

    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.show()

    # Find Brghtest Pixel and circle
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blurred_img)
    image = orig.copy()
    circle_radius = 25
    cv2.circle(image, maxLoc, circle_radius, (255, 0, 0), 2)

    plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
    plt.show()

    # Thresolding
    block_size = 5
    substraction_constant = 0

    thres_image = cv2.adaptiveThreshold(blurred_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,block_size,substraction_constant)

    plt.imshow(thres_image, cmap = 'gray', interpolation = 'bicubic')
    plt.show()