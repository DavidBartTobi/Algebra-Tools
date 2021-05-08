from tkinter import messagebox
from tkinter import *
import numpy as np
from numpy.linalg import inv
from utilities import gui_utilities


class InverseMatrix:

    def __init__(self, top, dimension, vectors):

        self.top = top
        self.dimension = dimension
        gui_utilities.Window_Style(self.top, "מטריצה הפכית", "200x200")
        self.top.focus_force()

        np_vectors = np.array(vectors)

        try:
            inverse = inv(np_vectors)
            inverse = inverse.round(dimension)
            self.background_label = Label(self.top, text=inverse, width=30, height=20,
                                          bg=gui_utilities.Main_Theme_Color())
            self.background_label.grid(row=0, column=0, sticky=W + N + E + S)

        except:
            messagebox.showerror("Error", f"The matrix is NOT invertible.")
            self.top.destroy()

