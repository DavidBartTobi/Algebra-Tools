from tkinter import ttk
from tkinter import *

from utilities import gui_utilities, coordinateEntry, errors
from inverse_Matrix import InverseMatrix
import inverse_Entry


class InverseCoordinateEntry:


    def __init__(self, top, dimension):

        self.top = top
        self.dimension = dimension
        self.entries = [[],[],[],[],[],[]]

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

        coordinateEntry.Coordinate_Entry(self.top, self.entries, self.dimension_status3, self.dimension_status4,
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
                    vectors[i].append(int(self.entries[i][j].get()))

                except:
                    errors.Instance_Error("מספר")
                    self.top.lift()
                    self.entries[i][j].focus_force()
                    return

        inverse_top = Toplevel()
        self.top.destroy()
        InverseMatrix(inverse_top, self.dimension, vectors)

    def Clear_Entries(self):

        for row in self.entries:
            for entry in row:
                entry.delete(0, END)

        self.entries[0][0].focus_force()

    def Change_Dimension(self):

        top = Toplevel()
        inverse_Entry.InverseEntry(top)
        self.top.destroy()
