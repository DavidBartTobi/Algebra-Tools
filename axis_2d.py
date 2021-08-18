import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np

class Axis_2D:

    def __init__(self, x_vectors, y_vectors, max_vector):

        X = x_vectors
        Y = y_vectors

        # Creating the subplots and projecting the vectors

        fig, ax = plt.subplots()

        colors = cycle('grbcmy')
        for i in range(len(x_vectors)):
            current = next(colors)
            ax.quiver([0], [0], X[i], Y[i], units='xy', scale=1, color=current)
            if X[i].is_integer():
                X[i] = int(X[i])
            if Y[i].is_integer():
                Y[i] = int(Y[i])
            ax.text(X[i], Y[i], f'({X[i]},{Y[i]})', color=current)

        # Modifying the distance shown between the ticks\lines depending on the vector sizes

        major_ticks = np.arange(-10, 11, 1)
        minor_ticks = np.arange(-10, 11, 1)

        if max_vector>10 and max_vector <=100:
            major_ticks = np.arange(-100, 101, 10)
            minor_ticks = np.arange(-100, 101, 10)

        if max_vector>100 and max_vector <=1000:
            major_ticks = np.arange(-1000, 1001, 200)
            minor_ticks = np.arange(-1000, 1001, 200)

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)

        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.2)
        ax.grid(which='major', alpha=0.2)

        # UI details
        plt.grid()                      # grid lines
        ax.set_aspect('equal')          # Spaces of boxes
        ax.axhline(y=0, color='k')      # coloring origin Axis
        ax.axvline(x=0, color='k')
        fig.set_size_inches(6, 6)       # Setting figure size

        # Naming the Axis
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

        plt.show()
