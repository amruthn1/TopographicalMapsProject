import os
import csv
import numpy as np
import matplotlib.pyplot as plt


def plotCoords():
    # Read through generated metadata
    # Plot the data in Matplotlib
    print("Plotting generated metadata")
    dir = os.fsencode('./metadata')
    for index, file in enumerate(os.listdir(dir)):
        filename = os.fsdecode(file)
        filedir = './metadata/' + filename
        csvData = []
        with open(filedir, 'r') as csvFile:
            reader = csv.reader(csvFile, delimiter=' ')
            for csvRow in reader:
                csvData.append(csvRow)
        csvData = np.array(csvData)
        csvData = csvData.astype(np.float)
        x = csvData[:, 0] * 100
        y = csvData[:, 1] * 100
        z = csvData[:, 2] * 70
        fig = plt.figure(figsize=(100, 100))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_trisurf(x, y, z, color='white', alpha=0.5,
                        linewidth=0, antialiased=False)
        ax.set(xlabel='x', ylabel='y', zlabel='z')
        ax.scatter(x, y, z, c='green')
        plt.show()


if __name__ == "__main__":
    plotCoords()
