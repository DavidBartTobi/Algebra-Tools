from tkinter import *
from utilities import gui_utilities


class Calculator:
    
    def __init__(self, top):

        # General fields

        self.number = None
        self.operator = None

        # Top UI details

        self.top = top
        self.top.title("Calculator")
        self.top.iconbitmap('C:/Users/Owner/Desktop/programming/Calculator.ico')

        # Entry UI details

        self.entry = Entry(self.top, width = 45, borderwidth = 5, bg = "black", fg = "#FD8558")
        self.entry.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5)
        w, h = gui_utilities.Center_Window(self.top)
        self.top.geometry("+%d+%d" % (w, h-230))
        self.top.focus_force()

        # Buttons UI details

        button_1 = Button(self.top, text="1", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(1))
        button_2 = Button(self.top, text="2", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(2))
        button_3 = Button(self.top, text="3", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(3))
        button_4 = Button(self.top, text="4", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(4))
        button_5 = Button(self.top, text="5", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(5))
        button_6 = Button(self.top, text="6", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(6))
        button_7 = Button(self.top, text="7", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(7))
        button_8 = Button(self.top, text="8", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(8))
        button_9 = Button(self.top, text="9", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(9))
        button_0 = Button(self.top, text="0", padx=40, pady=20, bg="#FEBE92", command=lambda: self.button_click(0))

        button_plus = Button(self.top, text="+", padx=39, pady=20, bg="#FEBE92", command=self.button_add)
        button_minus = Button(self.top, text="-", padx=41, pady=20, bg="#FEBE92", command=self.button_subtract)
        button_multiplication = Button(self.top, text="*", padx=41, pady=20, bg="#FEBE92", command=self.button_multiply)
        button_division = Button(self.top, text="/", padx=41, pady=20, bg="#FEBE92", command=self.button_divide)
        button_exponentiation = Button(self.top, text="^", padx=39, pady=20, bg="#FEBE92", command=self.button_power)

        button_clear = Button(self.top, text="Clear", padx=127, pady=20, bg="#FEBE92",
                              command=lambda: self.entry.delete(0, END))
        button_result = Button(self.top, text="=", padx=137, pady=20, bg="#FEAB71", command=self.button_result)

        # Buttons grid details

        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)

        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)

        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)
        button_0.grid(row=4, column=0)

        button_plus.grid(row=4, column=1)
        button_minus.grid(row=4, column=2)
        button_multiplication.grid(row=5, column=2)
        button_division.grid(row=5, column=1)
        button_exponentiation.grid(row=5, column=0)

        button_clear.grid(row=6, column=0, columnspan=3)
        button_result.grid(row=7, column=0, columnspan=3)

    # Operator buttons

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(current) + str(number))
    
    def button_add(self):
        self.operator = "+"
        self.number = self.entry.get()
        self.entry.delete(0, END)
    
    def button_subtract(self):
        self.operator = "-"
        self.number = self.entry.get()
        self.entry.delete(0, END)
    
    def button_multiply(self):
        self.operator = "*"
        self.number = self.entry.get()
        self.entry.delete(0, END)
    
    def button_divide(self):
        self.operator = "/"
        self.number = self.entry.get()
        self.entry.delete(0, END)
    
    def button_power(self):
        self.operator = "**"
        self.number = self.entry.get()
        self.entry.delete(0, END)
    
    def button_result(self):
        second_number = self.entry.get()
        self.entry.delete(0, END)
        if self.operator == "+":
            self.entry.insert(0, float(self.number) + float(second_number))
        elif self.operator == "-":
            self.entry.insert(0, float(self.number) - float(second_number))
        elif self.operator == "*":
            self.entry.insert(0, float(self.number) * float(second_number))
        elif self.operator == "/":
            self.entry.insert(0, float(self.number) / float(second_number))
        elif self.operator == "**":
            self.entry.insert(0, float(self.number) ** float(second_number))



