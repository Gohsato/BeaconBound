
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

def show_img(name,img):
    if(name in SWITCH):
        cv2.imshow(name,img)

def highlight(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    orig = img

    # Config
    blur_radius = 41
    thresh_block_size = 3

    # blurring
    blurred_img = cv2.GaussianBlur(img,(blur_radius,blur_radius),0)

    show_img('blurred',blurred_img)

    # Find Brghtest Pixel and circle
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blurred_img)
    image = orig.copy()
    circle_radius = 25
    cv2.circle(image, maxLoc, circle_radius, (255, 0, 0), 2)

    show_img('bright', image)

    # Thresolding
    substraction_constant = 0
    thresh_image = cv2.adaptiveThreshold(blurred_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY,thresh_block_size,substraction_constant)

    show_img('thresh', thresh_image)

    # Remove noise
    noiseless_image = thresh_image
    noiseless_image = cv2.dilate(noiseless_image, None, iterations=1)
    noiseless_image = cv2.erode(noiseless_image, None, iterations=3)
    noiseless_image = cv2.dilate(noiseless_image, None, iterations=2)
    # noiseless_image = cv2.erode(noiseless_image, None, iterations=3)

    show_img('noise', noiseless_image)

    # Count nonzero
    num_pix = cv2.countNonZero(noiseless_image)
    print(f"Number of ligh pix: {num_pix} ", end=" ")

if __name__ == '__main__':
    img = cv2.imread('images/image_faulty.jpg')
    highlight(imgage)
    cv2.waitKey(0)
        