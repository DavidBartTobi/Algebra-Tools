from tkinter import *
from tkinter import ttk
from utilities import gui_utilities, errors
from axis_2d import Axis_2D


class Vector_Visualization_2D:

    def __init__(self, top):

        self.x_vectors = []
        self.y_vectors = []
        self.max_vector = 0

        self.top = top
        gui_utilities.Window_Style(self.top, "2D", "195x150")

        self.background_label = Label(self.top, bg=gui_utilities.Main_Theme_Color(), width=27)
        self.background_label.grid(row=0, column=0, rowspan=4, columnspan=2, sticky=W + N + E + S)

        self.x_label = Label(top, text="X", anchor='center', width=6, bg=gui_utilities.Main_Theme_Color())
        self.x_label.grid(row=1, column=0, pady=20)
        self.y_label = Label(top, text="Y", anchor='center', width=6, bg=gui_utilities.Main_Theme_Color())
        self.y_label.grid(row=2, column=0, pady=(0, 20))

        self.x_entry = ttk.Entry(top, width=6, justify='center')
        self.x_entry.grid(row=1, column=1, pady=20)
        self.y_entry = ttk.Entry(top, width=6, justify='center')
        self.y_entry.grid(row=2, column=1, pady=(0, 20))

        self.add_button = ttk.Button(top, text="הוסף", command=self.Add_Vector, cursor='hand2')
        self.add_button.grid(row=3, column=0, pady=(0, 20))

        self.show_button = ttk.Button(top, text="הצג", command=self.Show_Vector, cursor='hand2')
        self.show_button.grid(row=3, column=1, pady=(0, 20))

        self.top.bind('<Return>', lambda func: self.Add_Vector()) # Binding the 'Enter' key to a button
        self.x_entry.focus_force()


    def Add_Vector(self):

        # Checking if the entries are empty

        if len(self.x_entry.get()) == 0:
            errors.Empty_Error()
            self.top.lift()
            self.x_entry.focus_force()
            return

        if len(self.y_entry.get()) == 0:
            errors.Empty_Error()
            self.top.lift()
            self.y_entry.focus_force()
            return

        try:
            # Checking if the entries are numbers before we enter only 1 of them by mistake
            float(self.x_entry.get())
            float(self.y_entry.get())

            # Checking the biggest vector

            if abs(float(self.x_entry.get())) > self.max_vector:
                self.max_vector = abs(float(self.x_entry.get()))
            if abs(float(self.y_entry.get())) > self.max_vector:
                self.max_vector = abs(float(self.y_entry.get()))

            # Entering the entries and deleting them from the fields
            self.x_vectors.append(float(self.x_entry.get()))
            self.y_vectors.append(float(self.y_entry.get()))
            self.x_entry.delete(0, END)
            self.y_entry.delete(0, END)
            self.x_entry.focus_force()

        except:
            errors.Instance_Error("מספר")
            self.top.lift()
            self.x_entry.focus_force()
            return


    def Show_Vector(self):
        self.top.destroy()
        Axis_2D(self.x_vectors, self.y_vectors, self.max_vector)