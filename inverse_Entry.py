from tkinter import ttk
from tkinter import *

from utilities import gui_utilities, errors
from inverse_Matrix import InverseMatrix


class InverseEntry:

    def __init__(self, top):

        self.top = top
        gui_utilities.Window_Style(self.top, "מטריצה הפכית", "332x150")

        self.background_label = Label(self.top, width=47, bg=gui_utilities.Main_Theme_Color())
        self.background_label.grid(row=1, column=0, rowspan=4, sticky=W + N + E + S)

        self.label = Label(self.top, text='הזינו את גודל המטריצה הריבועית (2 - 6):', width=20, height=3,
                           bg=gui_utilities.Main_Theme_Color())
        self.label.grid(row=0, column=0, sticky=W + N + E + S)

        self.entry = ttk.Entry(self.top, width=10, justify='center')
        self.entry.grid(row=2, column=0, pady=5, padx=50)

        self.button = ttk.Button(self.top, text="אישור", command=self.Coordinate_Entry, cursor='hand2')
        self.button.grid(row=3, column=0, pady=(15, 25))

        self.top.bind('<Return>', lambda func: self.Coordinate_Entry())
        self.entry.focus_force()


    def Coordinate_Entry(self):

        if len(self.entry.get()) == 0:
            errors.Empty_Error()
            self.top.lift()
            self.entry.focus_force()
            return

        try:
            if int(self.entry.get()) < 2 or int(self.entry.get()) > 6:
                errors.Range_Error('2', '6')
                self.top.lift()
                self.entry.focus_force()
                return

        except:
            errors.Instance_Error("מספר")
            self.top.lift()
            self.entry.focus_force()
            return

        dimension = int(self.entry.get())
        coordinate_top = Toplevel()
        self.top.destroy()
        InverseMatrix(coordinate_top, dimension)
