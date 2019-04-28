import os

from BeaconFinder import BeaconFinder

if __name__ == "__main__":

    finder = BeaconFinder(1.5)

    directory_names = [
        "images",
        "negatives",
        "positives",
        "images\march18",
        "images\march24"
    ]

    count = 0

    for directory_name in directory_names: 
        directory = os.fsencode(directory_name)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg"):
                file_path = directory_name+"/"+ filename
                result = finder.search_image(file_path)
                count += 1
                continue
            else:
                continue
    print(f"{count}")