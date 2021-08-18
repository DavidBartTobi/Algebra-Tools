from tkinter import messagebox


def Instance_Error(instance):
    messagebox.showerror("שגיאה", f"אנא הזינו {instance}")


def Range_Error(min, max):
    messagebox.showerror("שגיאה", f"הטווח המותר הוא: {max} - {min}")

def Empty_Error():

    messagebox.showerror("שגיאה", f"אנא מלאו את כל השדות")
