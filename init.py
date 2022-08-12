from plotCoords import plotCoords
from generateCoords import generateCoords
from parseCSV import parse_csv_file
from segmentPNG import segmentPNG

def init():
    parse_csv_file()
    segmentPNG()
    generateCoords()
    plotCoords()
init()