from tkinter import *
from utilities import gui_utilities
from PIL import ImageTk, Image
from ttkthemes import ThemedStyle
from tkinter import ttk
from calculator import Calculator
from vector_Visualization_2d import Vector_Visualization_2D
from vector_Visualization_3d import Vector_Visualization_3D
from inverse_Entry import InverseEntry
from determinantEntry import DeterminantEntry
from matrix_Multiplication_Entry import Matrix_Multiplication_Entry


main_root = Tk()
gui_utilities.Window_Style(main_root, "University Tools", "1003x589")

image = Image.open('images/main_img4.jpg')
resized_image = ImageTk.PhotoImage(image)
img_label = Label(main_root, image=resized_image, bg=gui_utilities.Main_Theme_Color())
img_label.grid(row=0, column=0, rowspan=5, columnspan=4)

# lbl = Label(main_root, bg=gui_utilities.Main_Theme_Color())
# lbl.grid(row=1, column=0, rowspan=4, columnspan=4, sticky=W+N+E+S)

# lbl = Label(main_root, bg=gui_utilities.Main_Theme_Color(), height=6)
# lbl.grid(row=4, column=0, columnspan=4, sticky=W+N+E+S)


def Calculator_Tab():
    calculator_top = Toplevel()
    Calculator(calculator_top)


def Vector_Visualization_2D_Tab():
    vector_top = Toplevel()
    Vector_Visualization_2D(vector_top)


def Vector_Visualization_3D_Tab():
    vector_top = Toplevel()
    Vector_Visualization_3D(vector_top)


def Inverse_Matrix_Tab():
    inverse_top = Toplevel()
    InverseEntry(inverse_top)


def Determinant_Tab():
    det_top = Toplevel()
    DeterminantEntry(det_top)


def Matrix_Multiplication_Tab():
    matmul_top = Toplevel()
    Matrix_Multiplication_Entry(matmul_top)


calculator_button = ttk.Button(main_root, text="              מחשבון", command=Calculator_Tab, width=21,
                               cursor='hand2')
calculator_button.grid(row=0, column=0, pady=(25, 0))

vector_2d_button = ttk.Button(main_root, text="         וקטור דו-מימדי", command=Vector_Visualization_2D_Tab, width=21,
                              cursor='hand2')
vector_2d_button.grid(row=1, column=0, pady=25)

vector_3d_button = ttk.Button(main_root, text="      וקטור תלת-מימדי", command=Vector_Visualization_3D_Tab, width=21,
                              cursor='hand2')
vector_3d_button.grid(row=2, column=0)

Inverse_Matrix_button = ttk.Button(main_root, text="        מטריצה הפכית", command=Inverse_Matrix_Tab, width=21,
                                   cursor='hand2')
Inverse_Matrix_button.grid(row=0, column=1, pady=(25, 0))

determinant_button = ttk.Button(main_root, text="            דטרמיננטה", command=Determinant_Tab, width=21,
                                cursor='hand2')
determinant_button.grid(row=1, column=1, pady=25)

matrix_multiplication_button = ttk.Button(main_root, text="          כפל מטריצות", command=Matrix_Multiplication_Tab, width=21,
                               cursor='hand2')
matrix_multiplication_button.grid(row=2, column=1)

# salary_button = ttk.Button(main_root, text="         Modify Salary", command=Salary_Tab, width=21)
# salary_button.grid(row=1,column=1, pady=(40,0))
#
# bonus_button = ttk.Button(main_root, text="        Check Bonuses", command=Bonus_Tab, width=21)
# bonus_button.grid(row=2,column=1, pady=40)
#
# hiring_button = ttk.Button(main_root, text="   Hiring Requirements", command=Hiring_Tab, width=21)
# hiring_button.grid(row=3,column=1)
#
# acknowledgement_button = ttk.Button(main_root, text="Add Acknowledgement", command=Acknowledgement_Tab, width=21)
# acknowledgement_button.grid(row=1,column=2, pady=(40,0))
#
# employee_list_button = ttk.Button(main_root, text="         Employee List", command=Employee_List_Tab, width=21)
# employee_list_button.grid(row=1,column=3, pady=(40,0))
#
# birthday_list_button = ttk.Button(main_root, text="          Birthday List", command=Birthday_List_Tab, width=21)
# birthday_list_button.grid(row=2,column=3, pady=40)
#
# status_label = Label(main_root, text = "By David Bart  ", bd=1, relief=SUNKEN, anchor=E, bg='#1e397e')
# status_label.grid(row=5, column=0, columnspan = 4, sticky=W+E)

# utilities.Create_Database()

main_root.mainloop()