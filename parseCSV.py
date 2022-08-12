import csv
from itertools import islice
import wget
import fitz
import os
import glob

from segmentPNG import segmentPNG

def clean_dir():
    pdflocalpath = './temp/pdf'
    imglocalpath = './temp/img'    
    if not os.path.isdir(pdflocalpath):
        raise Exception("The pdf directory in the temp folder does not exist")
    else:
        if os.listdir(pdflocalpath):
            print("Deleting old PDF files")
            files = glob.glob(pdflocalpath + "/*")
            for i in files:
                os.remove(i)
    if not os.path.isdir(imglocalpath):
        raise Exception("The img directory in the temp folder does not exist")
    else:
        if os.listdir(imglocalpath):
            print("Deleting old image files")
            files = glob.glob(imglocalpath + "/*")
            for i in files:
                os.remove(i)
def parse_csv_file():
    clean_dir()
    filedir = './input/ustopo_historical.csv' 
    filepatharr = []
    pdfpatharr = []
    numoffiles = input("How many files should be processed? ")
    with open(filedir, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in islice(reader, int(numoffiles)):
            if (row[29] == "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/USTopo/PDF/AL/AL_Abbeville_East_20180410_TM_geo.pdf"):
                print("skip")
            else:
                filepatharr.append(row[29])
    print(filepatharr)
    for index, file in enumerate(filepatharr):
        path = "./temp/pdf/" + str(index) + ".pdf"
        response = wget.download(file, path)
        print(response)
        pdfpatharr.append(path)
    print("Converting PDF files to SVG files")
    for filenameindex, pdfpath in enumerate(pdfpatharr):
        pdf = fitz.open(pdfpath)
        page = pdf.load_page(0)
        #For SVG
        #img = page.get_svg_image(text_as_path = True)
        #file = open('./temp/img/' + str(filenameindex) + ".svg", 'x')
        #file.write(img)
        #print("Converted PDF #" + str(filenameindex + 1) + " to an SVG file")
        #file.close()
        #For PNG
        img = page.get_pixmap()
        img.save('./temp/img/' + str(filenameindex) + ".png")
        print("Converted PDF #" + str(filenameindex + 1) + " to a PNG file")
    segmentPNG()
if __name__ == "__main__":
    parse_csv_file()