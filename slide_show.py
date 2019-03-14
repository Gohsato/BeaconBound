import os
import cv2

from histogram import grey_hist

if __name__ == "__main__":

    directory_names = ["images","negatives"]

    for directory_name in directory_names: 
        directory = os.fsencode(directory_name)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg"):
                file_path = directory_name+"/"+ filename
                img = cv2.imread(file_path)
                print(filename)
                grey_hist(img)
                continue
            else:
                continue
    