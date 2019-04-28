import numpy as np
import cv2
from matplotlib import pyplot as plt


class BeaconFinder():
    
    def __init__(self, brightest_to_mean_ratio_thresh):
        print("init BeaconFinder")
        self.params = {
            "B2M_thresh":brightest_to_mean_ratio_thresh
        }

    def search_image(self, file_path):
        img = cv2.imread(file_path)
        brightest_to_mean_ratio = self.get_brightest_to_mean_ratio(img)
        if(brightest_to_mean_ratio > self.params["B2M_thresh"]):
            return True
        return False

    
    def get_brightest_to_mean_ratio(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Config
        kSize = 7
        blurred_img = cv2.medianBlur(img,kSize)

        # Find Brghtest Pixel and circle
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(blurred_img)

        avg = blurred_img.mean()

        return np.around(maxVal/avg,decimals=3)

