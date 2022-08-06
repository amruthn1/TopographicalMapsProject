from bs4 import BeautifulSoup
import os

def cleanse_svg():
    dir = os.fsencode("./segmentedoutputs")
    for file in os.listdir(dir):
        filepath = os.fsdecode(file)
        filedir = './segmentedoutputs/' + filepath
        bs = BeautifulSoup(open(filedir), 'xml')
        prettified_xml = bs.prettify()
        with open(filedir, 'w') as overwritexml:
            overwritexml.write(prettified_xml)

def process_svg():
    dir = os.fsencode('./temp/img')
    for index, file in enumerate(os.listdir(dir)):
        shouldread = False
        vals = []
        filename = os.fsdecode(file)
        filedir = './temp/img/' + filename
        with open(filedir) as svg:
            data = svg.readlines()
            for line in data: 
                if shouldread:
                    if not '<g id="' in line and not '<g data-name="' in line:
                        vals.append(line)
                        print(line)
                        file = open('./segmentedoutputs/' + str(index) + ".svg", 'a')
                        file.write(line)
                        file.close()
                    else:
                        if 'Contour Features' in line or 'Contour Names' in line:
                            vals.append(line)
                            print(line)
                            file = open('./segmentedoutputs/' + str(index) + ".svg", 'a')
                            file.write(line)
                            file.close()
                        else:
                            shouldread = False    
                else:
                    if 'Contours' in line:
                        vals.append(line)
                        shouldread = True
                        print(line)
                        file = open('./segmentedoutputs/' + str(index) + ".svg", 'a')
                        file.write(line)
                        file.close()
    new_dir = os.fsencode('./segmentedoutputs')
    for i, modfile in enumerate(os.listdir(new_dir)):
        new_file = os.fsdecode(modfile)
        new_filedir = './segmentedoutputs/' + new_file
        with open(new_filedir) as mod_svg:
            mod_data = mod_svg.readlines()
            for line in mod_data:
                #iterate through file and count g tags then make sure theres the same amount of closing tags
                print("todo")
process_svg()