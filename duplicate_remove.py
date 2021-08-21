import cv2
import os
import glob
import numpy as np
import sys


def check(path):
    image = cv2.imread(path)
    return np.sum(image[:, :, 0])


def remove(dir):
    finder = {}
    for image in glob.glob(dir + "/*jpg"):
        hash = check(image)
        image_name = os.path.split(image)[1]
        if hash not in finder:
            finder[hash] = [image_name]
        else:
            os.remove(image)


if __name__ == "__main__":
    folder = sys.argv[1]
    print(f"Begin to remove duplicate images in folder {folder} :3")
    remove(folder)
    print("Done!!")
