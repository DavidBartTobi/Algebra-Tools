from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np

class Axis_3D:

    def __init__(self, x_vectors, y_vectors, z_vectors, max_vector):

        X = x_vectors
        Y = y_vectors
        Z = z_vectors

        # Creating the subplots and the axis

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Modifying the distance shown between the ticks\lines depending on the vector sizes

        major_ticks = np.arange(-10, 11, 2)
        minor_ticks = np.arange(-10, 11, 2)

        axis_tick_modifier = 10

        if max_vector>10 and max_vector <=100:
            axis_tick_modifier*=10
            major_ticks = np.arange(-100, 101, 20)
            minor_ticks = np.arange(-100, 101, 20)

        if max_vector>100 and max_vector <=1000:
            axis_tick_modifier*=100
            major_ticks = np.arange(-1000, 1001, 200)
            minor_ticks = np.arange(-1000, 1001, 200)

        x, y, z = np.array([[-axis_tick_modifier, 0, 0], [0, -axis_tick_modifier, 0], [0, 0, -axis_tick_modifier]])
        u, v, w = np.array([[2*axis_tick_modifier, 0, 0], [0, 2*axis_tick_modifier, 0], [0, 0, 2*axis_tick_modifier]])

        ax.set_xticks(major_ticks)
        ax.set_xticks(minor_ticks, minor=True)
        ax.set_yticks(major_ticks)
        ax.set_yticks(minor_ticks, minor=True)
        ax.set_zticks(major_ticks)
        ax.set_zticks(minor_ticks, minor=True)

        ax.grid(which='both')
        ax.grid(which='minor', alpha=0.5)
        ax.grid(which='major', alpha=0.5)

        # Setting the origin axis vectors and the size of the figure
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_zlim(-10, 10)
        fig.set_size_inches(7, 6)

        # Make a 3D quiver plot
        ax.quiver(x, y, z, u, v, w, arrow_length_ratio=0.1, color="black")

        # Naming the axis
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Projecting the vectors while rotating their colors
        colors = cycle('grbcmy')
        for i in range(len(x_vectors)):
            current = next(colors)
            ax.quiver([0], [0], [0], X[i], Y[i], Z[i], color=current)
            if X[i].is_integer():
                X[i] = int(X[i])
            if Y[i].is_integer():
                Y[i] = int(Y[i])
            if Z[i].is_integer():
                Z[i] = int(Z[i])
            ax.text(X[i], Y[i], Z[i], f'({X[i]},{Y[i]},{Z[i]})', color=current)

        plt.show()
