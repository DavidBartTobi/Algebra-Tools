from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from utilities import gui_utilities, coordinate_Entry, errors
import inverse_Entry
import numpy as np
from numpy.linalg import inv
from itertools import cycle

class InverseMatrix:

    def __init__(self, top, dimension):

        self.top = top
        self.dimension = dimension
        self.entries = [[],[],[],[],[],[]]
        self.colors = cycle(["#add8e6", '#ffcccb', '#90ee90'])

        gui_utilities.Window_Style(self.top, "מטריצה הפכית", "285x328")

        self.dimension_status6 = 'normal'
        self.dimension_status5 = 'normal'
        self.dimension_status4 = 'normal'
        self.dimension_status3 = 'normal'

        if dimension<6:
            self.dimension_status6 = 'disabled'
            if dimension<5:
                self.dimension_status5 = 'disabled'
                if dimension<4:
                    self.dimension_status4 = 'disabled'
                    if dimension<3:
                        self.dimension_status3 = 'disabled'

        self.background_label = Label(self.top, width=40, height=20, bg=gui_utilities.Main_Theme_Color())
        self.background_label.grid(row=1, column=0, rowspan=8, columnspan=6, sticky=W + N + E + S)

        coordinate_Entry.Coordinate_Entry(self.top, self.entries, self.dimension_status3, self.dimension_status4,
                                          self.dimension_status5, self.dimension_status6)

        self.confirm_button = ttk.Button(self.top, text="אישור", command=self.Get_Inverse, width=5,
                                         cursor='hand2')
        self.confirm_button.grid(row=7, column=0, pady=(20, 10), padx=(53, 0), columnspan=3)

        self.clear_button = ttk.Button(self.top, text="  נקה", command=self.Clear_Entries, width=5,
                                       cursor='hand2')
        self.clear_button.grid(row=7, column=3, pady=(20, 10), padx=(0, 53), columnspan=3)

        self.dimension_button = ttk.Button(self.top, text="     שנה גודל מטריצה", command=self.Change_Dimension,
                                           cursor='hand2', width=20)
        self.dimension_button.grid(row=8, column=0, pady=(10, 20), columnspan=6)

        self.top.bind('<Return>', lambda func: self.Get_Inverse())
        self.entries[0][0].focus_force()


    def Get_Inverse(self):

        vectors = []

        for i in range(self.dimension):
            vectors.append([])

            for j in range(self.dimension):

                if len(self.entries[i][j].get()) == 0:
                    errors.Empty_Error()
                    self.top.lift()
                    self.entries[i][j].focus_force()
                    return

                try:
                    vectors[i].append(float(self.entries[i][j].get()))

                except:
                    errors.Instance_Error("מספר")
                    self.top.lift()
                    self.entries[i][j].focus_force()
                    return

        self.Clear_Entries()

        np_vectors = np.array(vectors)

        try:
            inverse = inv(np_vectors)
            inverse = inverse.round(self.dimension)
            color = next(self.colors)
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if float(inverse[i][j]).is_integer():
                        self.entries[i][j].insert(0, int(float(inverse[i][j])))
                    else:
                        self.entries[i][j].insert(0, float(inverse[i][j]))
                    self.entries[i][j].configure(bg=color)

            for i in range(len(vectors)):
                for j in range(len(vectors)):
                    if float(vectors[i][j]).is_integer():
                        vectors[i][j] = int(float(inverse[i][j]))
                    else:
                        vectors[i][j] = float(inverse[i][j])

        except:
            messagebox.showerror("Error", f"The matrix is NOT invertible.")
            self.top.destroy()


    def Clear_Entries(self):

        for row in self.entries:
            for entry in row:
                entry.delete(0, END)

        self.entries[0][0].focus_force()

    def Change_Dimension(self):

        top = Toplevel()
        inverse_Entry.InverseEntry(top)
        self.top.destroy()
