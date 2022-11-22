import matplotlib.pyplot as plt
import numpy as np


def buildPlot(xMin, xMax):
    x = np.linspace(xMin * np.pi, xMax * np.pi, 10000)
    plt.plot(x, np.tanh(x))
    plt.show()


def buildDoubleAxesOnFigure(x, x2):
    plt.figure(figsize=(10, 5))
    plt.hist(x, bins=30, density=True)
    plt.ylabel('Probability')
    plt.xlabel('Data')
    plt.imshow(x2, cmap="Greens")
    plt.gca().invert_yaxis()
    plt.show()
