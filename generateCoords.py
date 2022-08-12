import cv2
import numpy as np
import image_slicer
import os
import glob

#img = cv2.imread('./test.png')
#average_color_row = np.average(img, axis=0)
#avg_color = np.average(average_color_row, axis=0)
#print(avg_color)
def cleanMetadata():
    metadatalocalpath = './metadata'
    if not os.path.isdir(metadatalocalpath):
        raise Exception("The metadata folder does not exist")
    else:
        if os.listdir(metadatalocalpath):
            print("Deleting old metadata")
            files = glob.glob(metadatalocalpath + "/*")
            for i in files:
                os.remove(i)
def cleanDir():
    slicedlocalpath = './sliced'
    if not os.path.isdir(slicedlocalpath):
        raise Exception("The sliced folder does not exist")
    else:
        if os.listdir(slicedlocalpath):
            print("Deleting old sliced outputs")
            files = glob.glob(slicedlocalpath + "/*")
            for i in files:
                os.remove(i)
def generateCoords():
    cleanMetadata()
    dir = os.fsencode('./blurred')
    for index, file in enumerate(os.listdir(dir)):
        print("Cleaning old files")
        cleanDir()
        filename = os.fsdecode(file)
        filedir = './blurred/' + filename
        tiles = image_slicer.slice(filedir, 9801, save=False)
        image_slicer.save_tiles(tiles, directory='./sliced', prefix='slice', format='png')
        for slicedfile in os.listdir('./sliced'):
            print("Processing slice")
            slicedfilename = os.fsdecode(slicedfile)
            slicedfiledir = './sliced/' + slicedfilename
            img = cv2.imread(slicedfiledir)
            avg_color_row = np.average(img, axis=0)
            avg_color = np.average(avg_color_row, axis=0)
            file = open('./metadata/' + str(index) + ".csv", 'a')
            file.write(slicedfilename.split("_")[1])
            file.write(" ")
            file.write(slicedfilename.split("_")[2].split(".")[0])
            file.write(" ")
            file.write(str(avg_color[0]))
            file.write('\n')
            file.close()            
generateCoords()
