
# Trying to isolate bright spots

import numpy as np
import cv2
from matplotlib import pyplot as plt

print(cv2.__file__)

img = cv2.imread('images/image_1.jpg',0)

print(img.shape)
# img = cv2.GaussianBlur(img,(5,5),0)


block_size = 35

substraction_constant = 2

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,block_size,substraction_constant)


img = th3
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()