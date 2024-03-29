
# A basic 'hello world' to test if your setup works

import numpy as np
import cv2
from matplotlib import pyplot as plt

print(cv2.__file__)

img = cv2.imread('images/image_1.jpg',1)[:,:,::-1]
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()