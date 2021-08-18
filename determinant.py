from tkinter import ttk
from tkinter import *
import numpy as np
from numpy.linalg import inv

from utilities import gui_utilities, coordinate_Entry, errors
import determinant_Entry


class Determinant:

    def __init__(self, top, dimension):

        self.top = top
        self.dimension = dimension
        self.entries = [[],[],[],[],[],[]]

        gui_utilities.Window_Style(self.top, "חישוב דטרמיננטה", "285x371")

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
        self.background_label.grid(row=1, column=0, rowspan=9, columnspan=6, sticky=W + N + E + S)

        coordinate_Entry.Coordinate_Entry(self.top, self.entries, self.dimension_status3, self.dimension_status4,
                                          self.dimension_status5, self.dimension_status6)

        self.confirm_button = ttk.Button(self.top, text="אישור", command=self.Get_Determinant, width=5,
                                         cursor='hand2')
        self.confirm_button.grid(row=7, column=0, pady=(20, 10), padx=(53, 0), columnspan=3)

        self.clear_button = ttk.Button(self.top, text="  נקה", command=self.Clear_Entries, width=5,
                                       cursor='hand2')
        self.clear_button.grid(row=7, column=3, pady=(20, 10), padx=(0, 53), columnspan=3)

        self.dimension_button = ttk.Button(self.top, text="     שנה גודל מטריצה", command=self.Change_Dimension,
                                           cursor='hand2', width=20)
        self.dimension_button.grid(row=8, column=0, pady=(10, 15), columnspan=6)

        self.det_frame = LabelFrame(self.top, bg=gui_utilities.Main_Theme_Color())
        self.det_frame.grid(row=9, column=0, columnspan=6, pady=(0,20))
        self.det_label = Label(self.det_frame, font='Helvetica', text="תוצאה", bg='#F9EFDA')
        self.det_label.grid(row=9, column=0, columnspan=6)

        self.top.bind('<Return>', lambda func: self.Get_Determinant())
        self.entries[0][0].focus_force()


    def Get_Determinant(self):

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


        # Getting the determinant
        np_vectors = np.array(vectors)
        det = np.linalg.det(np_vectors)

        # Checking if the determinant provided by numpy is a number that needs to be rounded
        # (for example, numpy returns -3.00000000000004 instead of -3 for the matrix [123, 132, 111])

        count_zeroes = 0
        count_nines = 0
        if '.' in str(det):
            index = str(det).index('.')
            for i in range(index+1, len(str(det))):
                if str(det)[i] == '0':
                    count_zeroes += 1
                elif str(det)[i] == '9':
                    count_nines += 1
                else:
                    break

            if count_zeroes >= 7 or count_nines >= 7:
                final_det = int(det)
                self.det_label.configure(text=str(final_det))
                self.entries[0][0].focus_force()

            else:
                self.det_label.configure(text=det)
                self.entries[0][0].focus_force()

        else:
            self.det_label.configure(text=det)
            self.entries[0][0].focus_force()

        self.Clear_Entries()


    def Clear_Entries(self):

        for row in self.entries:
            for entry in row:
                entry.delete(0, END)

        self.entries[0][0].focus_force()


    def Change_Dimension(self):

        top = Toplevel()
        determinant_Entry.DeterminantEntry(top)
        self.top.destroy()
