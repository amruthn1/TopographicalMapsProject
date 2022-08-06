import parseCSV
import processSVG

def init():
    parseCSV.parse_csv_file()
    #and then
    processSVG.process_svg()
init()