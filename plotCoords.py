import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from datetime import datetime

def plotCoords():
    # Read through generated metadata
    # Plot the data in Matplotlib
    print("Plotting generated metadata")
    dir = os.fsencode('./metadata')
    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        filedir = './metadata/' + filename
        csvData = []
        with open(filedir, 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=' ')
            for csvRow in reader:
                csvData.append(csvRow)
        csvData = np.array(csvData)
        csvData = csvData.astype(float)
        x = csvData[:, 0] * 100
        y = csvData[:, 1] * 100
        z = csvData[:, 2] * 0.001
        fig = plt.figure(figsize=(100, 100))
        ax = fig.add_subplot(111, projection='3d')
        ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 1, 0.1, 1]))
        ax.plot_trisurf(x, y, z, color='green', alpha=0.5, linewidth=0, antialiased=False)
        ax.set(xlabel='x', ylabel='y', zlabel='z')
        plt.show()
        input("Press enter to continue...")
        #plt.savefig(str(datetime.now()).replace(".", "_").replace(" ", "_").replace("-", "_").replace(":", "_") + ".pdf")
if __name__ == "__main__":
    plotCoords()
