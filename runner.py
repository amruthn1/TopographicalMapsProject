from parseCSV import parse_csv_file
from segmentPNG import segmentPNG
from generateCoords import generateCoords
from plotCoords import plotCoords


def run():
    # Run initial method
    parse_csv_file()
    segmentPNG()
    generateCoords()
    plotCoords()

if __name__ == "__main__":
    run()
