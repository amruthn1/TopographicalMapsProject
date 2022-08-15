import cv2
import matplotlib.pyplot as plt
import os
import glob

from generateCoords import generateCoords


def cleanse_dir():
    # Clean out directory before performing any new segmentation
    seglocalpath = './segmentedoutputs'
    blurredlocalpath = './blurred'
    if not os.path.isdir(seglocalpath):
        raise Exception("The segmentedoutputs folder does not exist")
    else:
        if os.listdir(seglocalpath):
            print("Deleting old segmented outputs files")
            files = glob.glob(seglocalpath + "/*")
            for i in files:
                os.remove(i)
    if not os.path.isdir(blurredlocalpath):
        raise Exception("The blurred folder does not exist")
    else:
        if os.listdir(blurredlocalpath):
            print("Deleting old blurred files")
            files = glob.glob(blurredlocalpath + "/*")
            for i in files:
                os.remove(i)


def preprocessPNG():
    # Remove any colors that may mess up the mask (Common Ones: Roads, Grid Overlay))
    print("TODO")


def segmentPNG():
    # Mask out unnecessary data from image and then blur the result
    cleanse_dir()
    preprocessPNG()
    dir = os.fsencode('./temp/img')
    for index, file in enumerate(os.listdir(dir)):
        filename = os.fsdecode(file)
        filedir = './temp/img/' + filename
        img = cv2.imread(filedir)
        plt.figure(num=None, dpi=1000)
        hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsvimg, (0, 3, 0), (41, 59, 255))
        blur = cv2.blur(mask, (15, 15))
        cv2.imwrite('./segmentedoutputs/' + str(index) + '.png', mask)
        cv2.imwrite('./blurred/' + str(index) + '.png', blur)
    generateCoords()


if __name__ == "__main__":
    segmentPNG()
