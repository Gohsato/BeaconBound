
# Trying to isolate bright spots

import numpy as np
import cv2
from matplotlib import pyplot as plt

print(cv2.__file__)

img = cv2.imread('images/image_1.jpg',1)[:,:,::-1]

img = img[:,:,2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()