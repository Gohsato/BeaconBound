import os
import cv2
import numpy as np

from histogram import grey_hist
from highlighter import highlight
from brightest import deviation
from corner import find_corner_fast

if __name__ == "__main__":

    directory_names = [
        # "images",
        # "negatives",
        # "positives",
        # "images\march18",
        "images\march24"
    ]

    for directory_name in directory_names: 
        directory = os.fsencode(directory_name)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg"):
                file_path = directory_name+"/"+ filename
                img = cv2.imread(file_path)

                print(f"{filename}", end=" ")
                cv2.imshow("original", img)
                grey_hist(np.copy(img))
                bright_pixels = highlight(np.copy(img))
                dev = deviation(np.copy(img))
                # find_corner_fast(img)
                print(f"pix: {bright_pixels}, dev: {dev}")
                print()
                cv2.waitKey(0)
                continue
            else:
                continue
    