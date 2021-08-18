from tkinter import *
from utilities import gui_utilities
from PIL import ImageTk, Image
from tkinter import ttk
from vector_Entry_2d import Vector_Visualization_2D
from vector_Entry_3d import Vector_Visualization_3D
from inverse_Entry import InverseEntry
from determinant_Entry import DeterminantEntry


main_root = Tk()
gui_utilities.Window_Style(main_root, "  University Tools", "1003x589")

image = Image.open('images/main_img4.jpg')
resized_image = ImageTk.PhotoImage(image)
img_label = Label(main_root, image=resized_image, bg=gui_utilities.Main_Theme_Color())
img_label.grid(row=0, column=0, rowspan=5, columnspan=2)

main_root.iconbitmap('images/matrix.ico')


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



vector_2d_button = ttk.Button(main_root, text="    הצגת וקטור דו-מימדי", command=Vector_Visualization_2D_Tab, width=21,
                              cursor='hand2')
vector_2d_button.grid(row=0, column=0, pady=100, padx=(150,0))

vector_3d_button = ttk.Button(main_root, text=" הצגת וקטור תלת-מימדי", command=Vector_Visualization_3D_Tab, width=21,
                              cursor='hand2')
vector_3d_button.grid(row=1, column=0, padx=(150,0))

Inverse_Matrix_button = ttk.Button(main_root, text="  חישוב מטריצה הפכית", command=Inverse_Matrix_Tab, width=21,
                                   cursor='hand2')
Inverse_Matrix_button.grid(row=0, column=1, pady=100, padx=(0,150))

determinant_button = ttk.Button(main_root, text="      חישוב דטרמיננטה", command=Determinant_Tab, width=21,
                                cursor='hand2')
determinant_button.grid(row=1, column=1, pady=25, padx=(0,150))


main_root.mainloop()